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

echo "==> 注入最小 front matter (日期/特殊 URL)"
python3 - <<'PY'
import pathlib, re, datetime
root = pathlib.Path('content')
forced_urls = {
    'Pythonic/20230209-dict-dispatch-pattern-in-python .md': '/Pythonic/20230209-dict-dispatch-pattern-in-python /',
}
date_pat = re.compile(r'^(?:(\d{4})(\d{2})(\d{2})|(\d{2})(\d{2})(\d{2}))-')
for md in root.rglob('*.md'):
    rel = md.relative_to(root).as_posix()
    text = md.read_text(encoding='utf-8', errors='replace')
    fm = {}
    body = text
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            for line in parts[1].splitlines():
                if ':' in line:
                    k, v = line.split(':', 1)
                    fm[k.strip()] = v.strip()
            body = parts[2]
            if body.startswith('\n'):
                body = body[1:]
    m = date_pat.match(md.name)
    if m and 'date' not in fm:
        if m.group(1):
            y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        else:
            y, mo, d = int(m.group(4)) + 2000, int(m.group(5)), int(m.group(6))
        try:
            fm['date'] = datetime.date(y, mo, d).isoformat()
        except ValueError:
            pass
    if rel in forced_urls:
        fm['url'] = forced_urls[rel]
    if fm:
        yaml = '---\n' + ''.join(f'{k}: {v}\n' for k, v in fm.items()) + '---\n\n'
        md.write_text(yaml + body, encoding='utf-8')
PY

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