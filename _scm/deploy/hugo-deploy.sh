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

# 发布时 HEAD: 用于 changelog 记录本次发布的仓库基线
DEPLOY_HEAD="$(git rev-parse --short HEAD 2>/dev/null || echo unknown)"
DEPLOY_BRANCH="main"
DEPLOY_PROJECT="io"

echo "==> 清理并构建"
rm -rf public resources
HUGO_OUT="$("$HUGO" --gc --minify 2>&1)" || { echo "$HUGO_OUT"; exit 1; }
echo "$HUGO_OUT"
HUGO_PAGES="$(echo "$HUGO_OUT" | sed -n 's/.*Pages *│ *\([0-9][0-9]*\).*/\1/p' | head -1)"
BUILD_INFO="$(find public -type f | wc -l | tr -d ' ') files, $(du -sh public | cut -f1)"
[ -n "$HUGO_PAGES" ] && BUILD_INFO="$HUGO_PAGES pages / $BUILD_INFO" || true
echo "==> 构建产物: $BUILD_INFO"

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

echo "==> 发布到 Cloudflare Pages (project=$DEPLOY_PROJECT, branch=$DEPLOY_BRANCH)"
export CLOUDFLARE_API_TOKEN
export CLOUDFLARE_ACCOUNT_ID
DEPLOY_LOG="$(mktemp)"
npx --yes wrangler@4 pages deploy public --project-name="$DEPLOY_PROJECT" --branch="$DEPLOY_BRANCH" 2>&1 | tee "$DEPLOY_LOG"
DEPLOY_URL="$(grep -o 'https://[0-9a-z-]*\.[0-9a-z-]*\.pages\.dev' "$DEPLOY_LOG" | tail -1 || true)"
WRANGLER_VER="$(grep -o 'wrangler [0-9][0-9.]*' "$DEPLOY_LOG" | head -1 | awk '{print $2}' || true)"
rm -f "$DEPLOY_LOG"
HUGO_VER="$("$HUGO" version | head -1 | grep -o 'v[0-9][0-9.]*' | head -1 || true)"

# 发布成功后自动补写 CHANGELOG.md (可用 CHANGELOG_AUTOCOMMIT=0 关闭自动提交)
echo "==> 记录 changelog"
python3 "$ROOT/_scm/deploy/changelog.py" \
    --head "$DEPLOY_HEAD" \
    --branch "$DEPLOY_BRANCH" \
    --project "$DEPLOY_PROJECT" \
    --deploy-url "$DEPLOY_URL" \
    --toolchain "Hugo ${HUGO_VER:-$($HUGO version | head -1)} · wrangler ${WRANGLER_VER:-4}" \
    --build-info "$BUILD_INFO"

echo "==> 完成"