# ZoomQuiet.io

大妈的主页（私人官网）— 基于 **Hugo + PaperMod** 构建的静态网站。

- **构建工具**: [Hugo](https://gohugo.io/)（Extended，≥ 0.146）+ [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 主题（已入库）
- **发布**: Cloudflare Pages，**wrangler 直传 `public/`**（无 CI、无 GH Actions、CF 端不构建）
- **评论**: Giscus（`ZoomQuiet/comment` 仓库 Discussions，`mapping=url`）
- **搜索**: PaperMod 内置 Fuse.js（`public/index.json` 预编译）
- **域名**: `zoomquiet.io`（CF Pages 已 active）

## 技术栈

| 组件 | 说明 |
|------|------|
| Hugo | 编译 HTML/RSS/JSON（搜索索引） |
| PaperMod | 主题（`themes/PaperMod/` 入库，离线可构建） |
| wrangler | 直传 `public/` 到 CF Pages 项目 `io` |
| Giscus | 评论区（经 CDN，可选） |
| jieba/fuse | 搜索分词（可选） |

## 仓库结构（关键路径）

```
.
├── content/                  # Hugo 内容源（权威，写稿在此）
├── hugo.toml                 # Hugo/PaperMod 配置（权威）
├── _scm/config/hugo.toml     # 配置副本（与根一致）
├── _scm/migrate/hugo-migrate.sh  # docs/ -> content/ 一次性迁移
├── _scm/deploy/hugo-deploy.sh    # 编译 + wrangler 发布
├── layouts/partials/comments.html # Giscus 注入（字面量声明）
├── themes/PaperMod/          # 主题（入库）
├── wrangler.toml             # 部署凭据（gitignore，绝不上传）
├── docs/                     # 【旧】MkDocs 源码（可删）
├── site/                     # 【旧】MkDocs 构建产物（可删）
├── mkdocs*.yml / inv/ / tasks.py / pyproject.toml / uv.lock
│                            # 【旧】MkDocs/uv 工具链（可删）
├── _historic/                # 【旧】历史导入归档（视需要保留/迁移）
└── public/ resources/        # Hugo 生成（gitignore）
```

---

## 一、本地安装 Hugo 并撰写初稿 / 预览

任何一台本地机器，只要装有 Hugo（≥ 0.146）即可写稿并本地编译预览：

```bash
# 1) 安装 Hugo Extended（macOS 两选一）
#    方式 A: Homebrew
brew install hugo
#    方式 B: 官方二进制（选 hugo_extended_*_darwin-universal2 或 arm64）
#    下载后解压到 $PATH，如 ~/go/bin/hugo
hugo version   # 确认 >= 0.146

# 2) 克隆仓库（含已入库主题，无需 submodule）
git clone https://github.com/ZoomQuiet/io.git
cd io

# 3) 写稿：在 content/<栏目>/<子目录>/ 新建 .md
#    文件名用日期前缀，便于自动注入日期/分页/标签
#    content/MurMur/26/20260819-my-draft.md

# 4) 本地编译并预览（自动监听变更）
hugo server -D --disableFastRender

# 打开 http://localhost:1313 即可实时预览
```

常用命令：

```bash
hugo                # 只编译到 public/
hugo server -D      # 预览（含草稿）
~/go/bin/hugo --gc --minify   # 正式构建
```

---

## 二、远程主机（hk0）LLM 辅助：元数据整理 + 编译发布

远程主机是日常发布入口，LLM/Agent 可全程接管。依赖：Hugo + node/wrangler + git + forgejo-cli。

```bash
# 1) 拉取最新内容
git pull

# 2) （可选）从 docs/ 转换到 content/
#    首次/迁移后一般不需要；仅当新增了旧格式 docs/ 内容
bash _scm/migrate/hugo-migrate.sh

# 3) LLM 辅助整理每个已迁移文件的元数据
#    - 首行 H1 作 title
#    - H1 下首个引用作 summary
#    - 按目录名注入 tags（如 Weekly/26 -> Weekly,26）
#    缺失项由脚本/LLM 补全，保持 URL 不变

# 4) 编译并发布（一条命令）
bash _scm/deploy/hugo-deploy.sh   # = hugo --gc --minify && wrangler pages deploy public --project-name=io --branch=main

# 5) 如需回帖 Issue（如 #148）
fj issue comment 148 -C /opt/src/DAMA --body-file comment.md
```

发布前务必确保本地 `wrangler.toml` 凭据可用、且 `env` 中无旧 token 遮蔽：

```bash
unset CLOUDFLARE_API_TOKEN CLOUDFLARE_ACCOUNT_ID   # 若被旧值占用
bash _scm/deploy/hugo-deploy.sh
```

---

## 三、在新主机部署相同的 wrangler 发布环境

新主机（新的本地机器 / 新的远程服务器）装齐依赖即可接管发布：

```bash
# 1) 装 Hugo（Extended >= 0.146）
#    macOS: brew install hugo
#    Linux/其他: 下载官方 hugo_extended_* 二进制放 $PATH
hugo version

# 2) 装 Node（含 npx/wrangler）
#    macOS: brew install node
node -v

# 3) 克隆仓库
git clone https://github.com/ZoomQuiet/io.git && cd io

# 4) 配置发布凭据 —— 只放本机，绝不入库/上传
cat > wrangler.toml <<'EOF'
name = "io"
account_id = "<你的 CF ACCOUNT_ID>"
[pages]
project_name = "io"
[[pages.advanced]]
build_command = ""
EOF
# 让 deploy 脚本读取凭据（脚本支持从 wrangler.toml 读取 CLOUDFLARE_API_TOKEN / CLOUDFLARE_ACCOUNT_ID）

# 5) 首次编译
unset CLOUDFLARE_API_TOKEN CLOUDFLARE_ACCOUNT_ID
~/go/bin/hugo --gc --minify -d public

# 6) 试发布（生成临时代理 URL，不覆盖生产）
npx --yes wrangler@4 pages deploy public --project-name=io --branch=preview-test

# 7) 正式发布
bash _scm/deploy/hugo-deploy.sh
```

> 新主机发布只需：Hugo + node/wrangler + git + `wrangler.toml`（凭据）。仓库内主题与脚本齐全，不依赖任何外部主题下载。

---

## 发布要点

- CF Pages 项目 `io`：无 GitHub 集成、无构建命令，`destination_dir = public`，仅接受 wrangler 直传。
- 仓库**不包含 `.github/`**，push GitHub 不会触发任何构建。
- 正式发布 = `bash _scm/deploy/hugo-deploy.sh`。

## 版权

Copyright 1974-2026 Zoom.Quiet, All rights reserved.
