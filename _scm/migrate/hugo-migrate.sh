#!/usr/bin/env bash
# Hugo 迁移脚本: docs/ -> content/
# 用法: bash _scm/migrate/hugo-migrate.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

echo "==> 清理旧 Hugo 产物"
rm -rf content public resources
mkdir -p content

echo "==> 复制 docs/ -> content/ (排除 _historic/)"
cp -a docs/. content/
rm -rf content/_historic

echo "==> 转换 section 首页 index.md -> _index.md"
# 目录下只要还有其它内容(子目录或兄弟 md), index.md 就应作为 section 首页
find content -type f -name 'index.md' | while read -r idx; do
    dir=$(dirname "$idx")
    others=$(find "$dir" -mindepth 1 -maxdepth 1 ! -name "$(basename "$idx")" | wc -l)
    if [ "$others" -gt 0 ]; then
        mv "$idx" "$dir/_index.md"
        echo "    renamed: $idx -> _index.md"
    fi
done

echo "==> 转换 6 篇含本地图片文章为 Page Bundle"
bundle() {
    local src="$1"; shift
    local rel="${src#docs/}"
    local stem="${rel%.md}"
    local dir="content/$stem"
    mkdir -p "$dir"
    mv "content/$rel" "$dir/index.md"
    for img in "$@"; do
        # 图片与文章同目录
        mv "content/$(dirname "$rel")/$img" "$dir/$img"
        echo "    bundled: $img"
    done
}

bundle docs/About/20241015-zoomquiet.md dama_alipay.png.webp dama_wxpay.png.webp
bundle docs/IMHO/FLOSS/20250904-aiage-person-band.md 20250904-aiage-person-band.png
bundle docs/MurMur/25/20250903-vibe-anything.md 20250903-vibe-anything-gemini.png
bundle docs/MurMur/25/20250905-vibe101coding.md 20250905-vibe101coding-liuns.jpg
bundle docs/Pythonic/24/20240918-ubnt-cloudflared.md 20240918-ubnt-cloudflared.jpg
bundle docs/Pythonic/25/20250615-claude-code-gh-flow.md 20250615-claude-code-gh-flow-ccusage.jpg 20250615-claude-code-gh-flow-mermaid.jpg

echo "==> 注入 front matter (日期/特殊URL/标题/概要/Tags)"
python3 - <<'PY'
import pathlib, re, datetime, json

root = pathlib.Path('content')
forced_urls = {
    'Pythonic/20230209-dict-dispatch-pattern-in-python .md': '/Pythonic/20230209-dict-dispatch-pattern-in-python /',
}
date_pat = re.compile(r'^(?:(\d{4})(\d{2})(\d{2})|(\d{2})(\d{2})(\d{2}))-')
title_pat = re.compile(r'^\s*#\s+(.+?)\s*$', re.MULTILINE)


def parse(text):
    fm, body = {}, text
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            for line in parts[1].splitlines():
                if ':' in line:
                    k, v = line.split(':', 1)
                    v = re.split(r'\s+#', v, 1)[0].strip()  # 去掉 YAML 行内注释
                    fm[k.strip()] = v
            body = parts[2]
            if body.startswith('\n'):
                body = body[1:]
    return fm, body


def add_date(fm, key, y, mo, d):
    try:
        fm['date'] = datetime.date(y, mo, d).isoformat()
    except ValueError:
        pass


def match_date(s):
    m = date_pat.match(s)
    if not m:
        return None
    if m.group(1):
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return (int(m.group(4)) + 2000, int(m.group(5)), int(m.group(6)))


def extract_title_summary(body):
    title, summary = None, []
    mt = title_pat.search(body)
    if mt:
        title = mt.group(1).strip()
    pre = body.split('\n## ', 1)[0]
    for line in pre.splitlines():
        ls = line.strip()
        if not ls.startswith('>'):
            continue
        s = re.sub(r'^>\s?', '', ls)
        # 跳过纯装饰性引用（如 '..' 分隔线）
        if len(s) < 3 or not any(ch.isalnum() for ch in s):
            continue
        summary.append(s)
    return title, ' '.join(summary)[:300]


for md in root.rglob('*.md'):
    rel = md.relative_to(root).as_posix()
    name = md.name
    if name == '_index.md':
        continue  # 真实 section/主页，非文章
    fm, body = parse(md.read_text(encoding='utf-8', errors='replace'))

    title, summary = extract_title_summary(body)
    if title:
        fm.setdefault('title', title)
    if summary:
        fm.setdefault('summary', summary)
    else:
        fm.setdefault('summary', '')

    if name == 'index.md':
        # Page Bundle：日期/标签从父目录名取
        parent = rel.split('/')[-2] if '/' in rel else ''
        tags = rel.split('/')[:-2]
        d = match_date(parent)
        key_name = parent
    else:
        d = match_date(name)
        tags = rel.split('/')[:-1]
        key_name = name

    if d and 'date' not in fm:
        add_date(fm, 'date', *d)
    if tags and 'tags' not in fm:
        fm['tags'] = tags
    if rel in forced_urls:
        fm['url'] = forced_urls[rel]

    lines = ['---']
    for k, v in fm.items():
        if isinstance(v, list):
            lines.append(f'{k}:')
            for t in v:
                lines.append(f'  - {json.dumps(t, ensure_ascii=False)}')
        else:
            lines.append(f'{k}: {json.dumps(v, ensure_ascii=False)}')
    lines.append('---')
    md.write_text('\n'.join(lines) + '\n\n' + body, encoding='utf-8')
PY

echo "==> 重写内容根 _index.md 为空（首页自述改由 [params.homeInfoParams] 提供）"
cat > content/_index.md <<'EOF'
---
---
EOF

echo "==> 创建 reports 占位（保持原站点 /reports/ 无独立首页）"
mkdir -p content/reports
cat > content/reports/_index.md <<'EOF'
---
build:
  render: false
  list: false
---
EOF

echo "==> 创建 PaperMod 内置页面 (search/archives)"
cat > content/search.md <<'EOF'
---
title: "Search"
layout: "search"
summary: "搜索"
placeholder: "搜索文章…"
---
EOF
cat > content/archives.md <<'EOF'
---
title: "Archive"
layout: "archives"
summary: "文章归档"
---
EOF

echo "==> 完成"
find content -type f | wc -l