#!/usr/bin/env bash
# Hugo 正式编译 + Cloudflare Pages 发布脚本
# 用法:
#   bash _scm/deploy/hugo-deploy.sh [--dry-run]
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

DRY_RUN=0
if [ "${1:-}" = "--dry-run" ]; then
    DRY_RUN=1
fi

# 优先使用官方/较新 Hugo (PaperMod 要求 >= 0.146.0)
if [ -x "$HOME/go/bin/hugo" ]; then
    HUGO="$HOME/go/bin/hugo"
else
    HUGO="$(command -v hugo)"
fi
echo "==> Hugo: $($HUGO version)"

echo "==> 清理并构建"
rm -rf public resources
"$HUGO" --gc --minify

echo "==> 构建产物: $(find public -type f | wc -l) files, $(du -sh public | cut -f1)"

if [ "$DRY_RUN" = "1" ]; then
    echo "==> dry-run, 不执行发布"
    exit 0
fi

# 从本地 wrangler.toml 读取 Cloudflare 凭据 (该文件不入库)
if [ -f wrangler.toml ]; then
    CLOUDFLARE_API_TOKEN="${CLOUDFLARE_API_TOKEN:-$(sed -n 's/^CLOUDFLARE_API_TOKEN[[:space:]]*=[[:space:]]*"\(.*\)"/\1/p' wrangler.toml | head -1)}"
    CLOUDFLARE_ACCOUNT_ID="${CLOUDFLARE_ACCOUNT_ID:-$(sed -n 's/^CLOUDFLARE_ACCOUNT_ID[[:space:]]*=[[:space:]]*"\(.*\)"/\1/p' wrangler.toml | head -1)}"
fi
: "${CLOUDFLARE_API_TOKEN:?缺少 CLOUDFLARE_API_TOKEN}"
: "${CLOUDFLARE_ACCOUNT_ID:?缺少 CLOUDFLARE_ACCOUNT_ID}"

echo "==> 发布到 Cloudflare Pages (project=io, branch=main)"
export CLOUDFLARE_API_TOKEN
export CLOUDFLARE_ACCOUNT_ID
npx --yes wrangler@4 pages deploy public --project-name=io --branch=main

echo "==> 完成"