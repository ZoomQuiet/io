# Changelog

本文件记录 ZoomQuiet.io 站点的**内容发布与部署**记录，按时间倒序。

发布方式：`bash _scm/deploy/hugo-deploy.sh`（`hugo --gc --minify` 编译 + `wrangler pages deploy public --project-name=io --branch=main` 直传 Cloudflare Pages）。

自 2026-11-22 起，部署脚本会在发布成功后自动追加本文件条目（`_scm/deploy/changelog.py`）；下列早期条目为手工记录。

---

## 2026-11-22 — 4 篇新文章上线

| 项目 | 内容 |
|------|------|
| 发布时 HEAD | `a0fb0a8e4` |
| 内容 commit | `83ae014ce` |
| CF Pages 部署 | `28d73da5-085f-496b-a65c-400bdc44f580` (Production / main) |
| 预览地址 | https://28d73da5.io-8h2.pages.dev |
| 工具链 | Hugo v0.147.9 (extended) · wrangler 4.127.1 |
| 构建产物 | 1159 pages / 2474 files / 95M |

### 新增文章

- `content/MurMur/26/20261109-loggin4what.md` — 收藏什么最重要?（2026-11-09）
- `content/MurMur/26/20261113-20km4cny20.md` — 确定性僵尸（2026-11-13）
- `content/Weekly/26/20261114-w45.md` — 上周蠎超赞 26w45 #546（2026-11-14）
- `content/Weekly/26/20261122-w46.md` — 上周蠎超赞 26w46 #547（2026-11-21）

### 内容修订

- 为上述 4 篇补齐 Hugo front matter：`title` / `summary` / `date` / `tags`
  - Weekly 篇目日期沿用正文原始 `Date:` 行（`2026-11-14T11:42:00`、`2026-11-21T11:42:00`），与 w37/w42/w44 一致
  - MurMur 篇目日期取自文件名（`2026-11-09`、`2026-11-13`）
- 修复 `20261109-loggin4what.md` 中断行的 x.com 链接（原 URL 内含换行，导致链接失效）

### 验证

- 全量扫描 `content/` 1064 个 `.md`：除章节索引 `_index.md` 外，无其它文章缺 front matter
- 构建后 `public/index.json` 收录 4 篇新文章（标题、permalink 正确）
- 线上 4 个新页面均 HTTP 200，`<title>` 与日期渲染正确，首页列表已出现

---

## 2026-11-19 — 26w44 与「未来十年的生存与进化指南」上线

对应 CF 部署 `0f8e1b8a-b0b3-4be6-b632-b8d7b26c2f05`（Production / main），commit `87145d060`。

## 更早记录

2026-09 ~ 2026-11 的历次发布（多为「批量/逐篇补齐 Hugo front matter」）未逐条登记；
完整历史见 `git log --oneline` 与 Cloudflare Pages 部署列表
（`npx wrangler pages deployment list --project-name=io`）。
