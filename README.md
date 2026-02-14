# ZoomQuiet.io

大妈的主页 - 基于 MkDocs Material 构建的静态网站。

[![Deploy](https://github.com/ZoomQuiet/io/actions/workflows/deploy.yml/badge.svg)](https://github.com/ZoomQuiet/io/actions/workflows/deploy.yml)

## 技术栈

- **构建工具**: [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- **Python 管理**: [uv](https://docs.astral.sh/uv/)
- **任务运行**: [Invoke](https://www.pyinvoke.org/)
- **部署**: GitHub Pages (源: `site/` 目录)
- **CI/CD**: GitHub Actions

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/ZoomQuiet/io.git
cd io

# 安装依赖
uv sync

# 本地构建并预览
uv run inv upd
```

## 构建系统

### 本地构建

```bash
# 完整构建（flush + reidx + mkdocs build）
inv upd

# 单独步骤
inv flush    # 更新导航配置
inv reidx    # 更新首页最新文章
```

### 自动部署（GitHub Actions）

push 到 `main` 分支时自动触发：

```yaml
on:
  push:
    branches: [main]
```

CI 流程：
1. 检出代码
2. 安装 uv + Python 依赖
3. 运行 `inv upd` 构建站点
4. 自动提交 `site/` 目录变更

## 项目优化

### 2025-02-14: 性能优化与 CI 迁移

**问题**: 中国大陆访问慢，Google Fonts 被墙导致阻塞

**解决方案**:
- ✅ 禁用 Google Fonts (`font: false`)，使用系统默认字体
- ✅ 构建流程迁移到 GitHub Actions，无需本地操作
- ✅ 保留本地 `inv upd` 能力用于开发和预览

**效果**: 首屏加载时间从 30-60s 降至 <3s

详见工程报告: [`docs/reports/250214_1_disable-google-fonts-migrate-to-gha.md`](docs/reports/250214_1_disable-google-fonts-migrate-to-gha.md)

## 项目结构

```
.
├── docs/               # 文档源文件
│   ├── reports/        # 工程报告
│   ├── About/          # 关于页面
│   ├── IMHO/           # 拙见文章
│   ├── MurMur/         # 呢喃随笔
│   └── ...
├── site/               # 构建输出（GitHub Pages 源）
├── _theme/             # 自定义主题
├── inv/                # Invoke 任务模块
│   ├── mkdocs.py       # 导航生成
│   └── latestor.py     # 首页更新
├── mkdocs.yml          # MkDocs 配置
├── tasks.py            # 主任务文件
└── .github/workflows/  # CI/CD 配置
```

## 版权

Copyright 1974-2025 Zoom.Quiet, All rights reserved.
