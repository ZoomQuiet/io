#!/usr/bin/env python3
"""发布后自动补写仓库根目录 CHANGELOG.md 的部署条目。

由 _scm/deploy/hugo-deploy.sh 在 wrangler 部署成功后调用，也可单独运行:

    python3 _scm/deploy/changelog.py --head "$(git rev-parse --short HEAD)"

条目插入到 CHANGELOG.md 第一个 "## " 章节之前 (最新在最上)。

基线推算: 取上次条目里的 "发布时 HEAD" (记为 H_prev), 再取 H_prev 的第一个后代
提交 (git rev-list --ancestry-path --reverse H_prev..HEAD 首项) 作为变更基线。
正常流程里该提交正是上次发布上线的内容提交, 如此本次变更列表不会重复计入
上次已上线的文章。若 H_prev 之后没有新提交, 则基线退回 H_prev。
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHANGELOG = ROOT / "CHANGELOG.md"
TZ = "Asia/Shanghai"
MAX_ITEMS = 40

SKELETON = """# Changelog

本文件记录 ZoomQuiet.io 站点的**内容发布与部署**记录，按时间倒序。

发布方式：`bash _scm/deploy/hugo-deploy.sh`（`hugo --gc --minify` 编译 + `wrangler pages deploy public --project-name=io --branch=main` 直传 Cloudflare Pages）。

自 2026-11-22 起，部署脚本会在发布成功后自动追加本文件条目。

---
"""

# "发布时 HEAD | `abc1234`" —— 取文件中第一次出现 (最新条目在最上)
RE_PREV_HEAD = re.compile(r"发布时 HEAD\s*\|\s*`?([0-9a-f]{7,40})`?")
RE_WHENEVER = re.compile(r"(\d{4}-\d{2}-\d{2})[ T](\d{2}:\d{2})")


def sh(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)


def now_stamp():
    try:
        from zoneinfo import ZoneInfo

        tz = ZoneInfo(TZ)
    except Exception:
        tz = datetime.timezone(datetime.timedelta(hours=8))
    return datetime.datetime.now(tz)


def resolve_deployment(project, branch, deploy_url):
    """从 wrangler 部署列表里取本次部署的完整 ID 与 URL。"""
    info = {"id": "", "url": deploy_url or ""}
    if info["url"]:
        info["id"] = info["url"].split("//", 1)[-1].split(".", 1)[0]
    r = sh(["npx", "--yes", "wrangler@4", "pages", "deployment", "list",
            f"--project-name={project}", "--json"])
    if r.returncode != 0:
        return info
    try:
        items = json.loads(r.stdout)
    except json.JSONDecodeError:
        return info
    for item in items:
        if info["url"] and item.get("Deployment") != info["url"]:
            continue
        if branch and item.get("Branch") != branch:
            continue
        info["id"] = item.get("Id", info["id"])
        info["url"] = item.get("Deployment", info["url"])
        info["environment"] = item.get("Environment", "")
        break
    return info


def collect_changes(base):
    """已提交部分 (base..HEAD) + 工作区未提交部分。"""
    changes = []
    seen = set()

    r = sh(["git", "diff", "--name-status", f"{base}..HEAD"])
    for line in r.stdout.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        path = parts[-1]
        if path == "CHANGELOG.md":
            continue
        if path in seen:
            continue
        seen.add(path)
        changes.append((status, path))

    r = sh(["git", "status", "--porcelain"])
    for line in r.stdout.splitlines():
        if len(line) < 4:
            continue
        status = line[:2].strip() or "M"
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        if path == "CHANGELOG.md" or path in seen:
            continue
        seen.add(path)
        if status.startswith("?"):
            status = "A"
        changes.append((status, path))

    return changes


def build_entry(args, deployment, prev_head, base, changes):
    now = now_stamp()
    title = f"## {now:%Y-%m-%d %H:%M} — 发布记录"
    if changes:
        title += f"（{len(changes)} 项内容变更）"

    rows = [
        "| 项目 | 内容 |",
        "|------|------|",
        f"| 发布时 HEAD | `{args.head}` |",
        f"| 变更基线 | `{base}` |",
    ]
    if prev_head:
        rows.append(f"| 上次发布时 HEAD | `{prev_head}` |")
    if deployment.get("id"):
        env = deployment.get("environment") or "Production"
        rows.append(f"| CF Pages 部署 | `{deployment['id']}` ({env} / {args.branch}) |")
    if deployment.get("url"):
        rows.append(f"| 预览地址 | {deployment['url']} |")
    if args.toolchain:
        rows.append(f"| 工具链 | {args.toolchain} |")
    if args.build_info:
        rows.append(f"| 构建产物 | {args.build_info} |")
    rows.append("| 记录方式 | 自动（`_scm/deploy/changelog.py`） |")

    lines = [title, "", *rows, ""]

    if changes:
        lines.append(f"### 本次内容变更（相对 `{base}`）")
        lines.append("")
        for status, path in changes[:MAX_ITEMS]:
            lines.append(f"- `{status}` `{path}`")
        if len(changes) > MAX_ITEMS:
            lines.append(f"- …另有 {len(changes) - MAX_ITEMS} 项")
        lines.append("")
    else:
        lines.append("### 本次内容变更")
        lines.append("")
        lines.append("- 无内容变更（仅重新构建发布）")
        lines.append("")

    return "\n".join(lines).rstrip("\n") + "\n"


def insert_entry(text, entry):
    lines = text.splitlines(keepends=True)
    idx = next((i for i, line in enumerate(lines) if line.startswith("## ")), len(lines))
    head = "".join(lines[:idx]).rstrip("\n")
    tail = "".join(lines[idx:])
    parts = [head, "", entry]
    if tail:
        parts.append(tail)
    return "\n".join(parts).rstrip("\n") + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--head", default=sh(["git", "rev-parse", "--short", "HEAD"]).stdout.strip())
    ap.add_argument("--branch", default="main")
    ap.add_argument("--project", default="io")
    ap.add_argument("--deploy-url", default="")
    ap.add_argument("--toolchain", default="")
    ap.add_argument("--build-info", default="")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-commit", action="store_true")
    args = ap.parse_args()

    text = CHANGELOG.read_text(encoding="utf-8") if CHANGELOG.exists() else SKELETON

    m = RE_PREV_HEAD.search(text)
    prev_head = m.group(1) if m else ""

    base = ""
    if prev_head:
        r = sh(["git", "rev-list", "--ancestry-path", "--reverse", f"{prev_head}..HEAD"])
        commits = [c for c in r.stdout.split() if c]
        base = commits[0][:7] if commits else prev_head[:7]
    else:
        r = sh(["git", "rev-list", "--max-parents=0", "HEAD"])
        roots = [c for c in r.stdout.split() if c]
        base = roots[0][:7] if roots else ""

    deployment = resolve_deployment(args.project, args.branch, args.deploy_url)
    changes = collect_changes(base)
    entry = build_entry(args, deployment, prev_head, base, changes)

    if args.dry_run:
        print(entry)
        return 0

    new_text = insert_entry(text, entry)
    fd, tmp = tempfile.mkstemp(dir=str(CHANGELOG.parent), prefix=".changelog-")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(new_text)
        os.replace(tmp, CHANGELOG)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

    print(f"==> CHANGELOG.md 已补写条目: {entry.splitlines()[0]}")

    autoc = os.environ.get("CHANGELOG_AUTOCOMMIT", "1") not in ("0", "false", "no")
    if autoc and not args.no_commit:
        r = sh(["git", "add", "CHANGELOG.md"])
        if r.returncode == 0:
            stamp = now_stamp().strftime("%Y-%m-%d %H:%M")
            r = sh(["git", "commit", "-q", "-m", f"docs: changelog for {stamp} deployment"])
            if r.returncode == 0:
                sha = sh(["git", "rev-parse", "--short", "HEAD"]).stdout.strip()
                print(f"==> 已自动提交 changelog: {sha}")
            else:
                print("==> changelog 写入成功, 自动提交跳过 (无暂存变更或不在 git 仓库)")
    else:
        print("==> changelog 写入成功, 未自动提交 (CHANGELOG_AUTOCOMMIT=0)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
