# 工程报告：禁用 Google Fonts 并迁移构建到 GitHub Actions

## 基本信息

| 项目 | 内容 |
|------|------|
| 日期 | 2025-02-14 |
| Issue | [#1](https://github.com/ZoomQuiet/io/issues/1) |
| 主题 | 中国大陆访问慢问题分析与解决方案 |
| 执行人 | Kimi Code CLI |

## 决策确认

根据 Issue #1 的讨论，确认以下决策：

1. **字体策略**: 方案 A - 禁用 Google Fonts，使用系统字体，**不使用字体镜像**
2. **部署策略**: 保留 GitHub Pages，但构建流程迁移到 GitHub Actions
3. **触发条件**: Push 到 main 分支时自动触发 (Q1-A)
4. **输出目录**: 保持 `site/` 目录，gh-pages 继续指向此处 (Q2)
5. **本地能力**: 保留 `inv upd` 本地构建能力 (Q3)

## 实施内容

### 1. 禁用 Google Fonts

**修改文件**: `mkdocs.yml`

```yaml
theme:
  name: material
  language: zh
  custom_dir: _theme/material
  font: false  # ← 新增：禁用 Google Fonts，解决中国大陆访问慢问题
```

**效果**: 
- 移除所有 HTML 中的 `fonts.googleapis.com` 和 `fonts.gstatic.com` 引用
- 使用浏览器系统默认字体栈
- 中国大陆访问不再有字体加载阻塞

### 2. 创建 GitHub Actions Workflow

**新建文件**: `.github/workflows/deploy.yml`

**功能**:
- 触发条件：push 到 main 分支（site/ 目录变更除外，避免无限循环）
- 构建流程：
  1. 检出代码（完整历史，支持 git-authors 插件）
  2. 设置 Python 3.13
  3. 安装 uv 和依赖
  4. 运行 `inv upd` 构建站点
  5. 如有变更，自动提交 site/ 目录并推送
- 手动触发：保留 `workflow_dispatch` 能力

### 3. 保留本地构建能力

本地开发工作流保持不变：

```bash
# 本地预览
inv upd

# 手动提交（如需）
git add site/
git commit -m "manual update"
git push
```

## 技术细节

### 为什么使用 `font: false`

根据 [MkDocs Material 官方文档](https://squidfunk.github.io/mkdocs-material/setup/changing-the-fonts/?h=font#disabling-font-loading)，`font: false` 会：

1. 禁用从 Google Fonts CDN 加载字体
2. 使用系统字体栈作为 fallback
3. 移除 `<link rel="preconnect" href="https://fonts.gstatic.com">` 预连接

### GitHub Actions 防循环机制

```yaml
paths-ignore:
  - 'site/**'      # site/ 变更不会触发 workflow
```

当 workflow 提交 site/ 目录时，由于 commit message 包含 `[skip ci]` 且路径被忽略，不会触发新的构建。

### 依赖管理

使用 `uv sync --frozen` 确保依赖版本锁定，与本地开发环境一致。

## 预期效果

| 指标 | 优化前 | 优化后 |
|------|--------|--------|
| 首屏加载时间 (中国大陆) | 30-60s (字体超时) | <3s |
| 外部网络依赖 | Google Fonts (被墙) | 无 |
| 构建自动化 | 本地手动 | CI 自动 + 本地手动 |
| 字体显示 | Roboto | 系统默认字体 |

## 验证步骤

1. 本地构建测试：
   ```bash
   inv upd
   grep -r "googleapis\|gstatic" site/  # 应无结果
   ```

2. 推送到 main 分支后，检查 GitHub Actions 运行状态

3. 访问 https://zoomquiet.io 验证：
   - 页面加载速度
   - DevTools Network 面板无 Google Fonts 请求

## 后续优化建议

1. **短期**: 观察 CI 构建是否正常工作，确认 site/ 目录自动更新
2. **中期**: 考虑添加构建缓存加速 CI
3. **长期**: 如仍有访问问题，考虑方案 C (CDN 迁移)

## 变更文件清单

- [x] `mkdocs.yml` - 添加 `font: false`
- [x] `.github/workflows/deploy.yml` - 新建 CI 配置
- [x] `docs/reports/250214_1_disable-google-fonts-migrate-to-gha.md` - 本报告

---

**状态**: ✅ 已完成，等待验证
