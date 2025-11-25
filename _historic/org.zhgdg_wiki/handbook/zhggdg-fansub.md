# 珠海 GDG 字幕组工作流程

[TOC]

## 是什么
珠海 GDG 字幕组是一个专门翻译Google发布的教程的一个字幕组

我们专注于高效地提供有质量的中文字幕

以便于中国的IT爱好者乃至全世界的华人IT爱好者能够以最快的速度观赏到Google的最新动态

## 背景

- [GDG字幕组官方网站](http://www.gfansub.com/)
- [GDG字幕组翻译最佳实践 - Google 文档](https://www.gdgdocs.org/document/d/1ZLp0U-Fm4q2Msbdtx8_0EHQRZiI6qQmvBQ_L0zHbLc0/edit)

## 分析

GDG字幕组翻译流程过长,不能够及时把最新最酷的科技分享到互联网上供中国的开发者们学习. 

作为一个热爱Google技术的GDGer,珠海GDG 决定增强当前字幕组工作流程

于是GDG字幕组的开源项目式协同流程应运而生. 

## 方案

目标: 

- 全程透明 ~ 全部有可接触的服务来公开
- 基本自主 ~ 全部基于 github 协同工作流来主动推进不需要过多的专职人员来管理

资源:

- 仓库: https://github.com/ZHGDG/gfansub
- 列表: zhgdgsubtitle@googlegroups.com
- 片源: [Google Developers](https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw)
- 下载: [youtube-dl-subscriptions](https://github.com/mewfree/youtube-dl-subscriptions)
- 频道: [GDG技术视频珠海字幕组](https://www.youtube.com/channel/UC94WbZP_OkC9ZAjLBK63Oxg)
- 制度: [珠海 GDG 学生贡献奖状获得规章](zhggdg-goa)


流程:


    [[官方片源频道]]
      ^   |
      |   V (复制)
      | [[珠海GDG频道]]
      |   |        ^
      |   |        | 合成发布
      |   V        |
      | ((github)) |
      `--+ ^ |  +--/
           | V
        <Issue>
           ^ |
           | V
          邮件列表


1. 字幕组织
    + 在 Youtube 上,从官方频道中复制 珠海GDG 本地学生有兴趣的节目到 `珠海GDG` 频道中
    + 上传一份视频和字幕到 `珠海GDG` 百度云盘中
    + 同时下载 en 字幕
2. 任务发布
    + 在专用 github 仓库中,分目录追加新节目的原文字幕文件
    + 对应每个节目, 发布一个 Issue 说明内容/工作量
    + 使用 `milestone` 来划分任务状态:
        * inbox     ~ 新任务
        * buffer    ~ 已指派/认领
        * doing     ~ 翻译中的
        * checking  ~ 校对中的
        * done      ~ 已经完成
        * publish   ~ 正式发布的
3. 任务认领
    + 任何有能力的志愿者,都可以注册 github 认领 Issue
    + 主动完成字幕的翻译
        * 通过 git 命令,在本地完成
        * 或是,通过 web 页面,直接在网页上完成
4. 字幕交付
    + 完成翻译后,通过对应 Issue 的  `milestone` 变更来推动协同
    + 社区组织者,将所有 `checking` 状态的字幕,上传到 Youtube `珠海GDG` 频道中对应视频后台
    + 将有字幕的视频链接注释到 Issue 中
        * 任何可以看 Youtube 的志愿者,都可以进行校对
        * 或者下载百度云盘的视频在本地校对
    + 将意见追加到 Issue 评注中
5. 正式发布
    + 经过几轮校对, 在 `珠海GDG` 频道或者在 `Github` 中完成字幕
    + 将复制到专用的正式字幕仓库中, 正式提交给 Google 官方等待统一合并发布



福利:

1.小伙伴们通过翻译得来的知识是天然福利 XD
2.拥有对自己的翻译的署名权,毕竟是劳动成果嘛 :)
3.通过翻译字幕,你们可以认识来自全国各地的小伙伴们,拓展自己的社交圈


## 参考

- [Fork+Pull工作模式-GotGitHub](http://www.worldhello.net/gotgithub/04-work-with-others/010-fork-and-pull.html)



### github 相关关键操作

只需要一些基本的 git 操作:

    # clone frok 的仓库到本地工作目录
    $ git clone https://github.com/yourgithubname/gfansub

    # 添加上游仓库
    $ git remote add upstream https://github.com/ZHGDG/gfansub 

    # 提交本地修改
    $ git add 被修改文件
    $ git commit -m "****"  //***为修改内容注释
    $ git push origin master

    # 同步上游版本
    $ git remote update upstream
    $ git rebase upstream/master
    $ git push origin master

    # pull request
    ... 在自己Github项目仓库下提交pull request到上游仓库


管理员只做一件事情,merge request,merge的时候要判断内容的准确性以及对质量的把控

### 非技术翻译人员工作流程
~ 等待截屏教程

1. 注册Github帐号
2. Fork项目

- 打开要翻译的文档,点击右上角的笔"Edit this file"进行翻译
- 翻译完成之后添加描述,然后点击下方的"Commit changes"进行保存
- 点击文本框右边第二个按钮"Pull requests"进行提交
- 等待管理员确认

## 反馈

- 任何问题,请通过[support@zhgdg.org](mailto:support@zhgdg.org)反馈


## 参考

- 150703 Martin 修改频道信息
- 150614 Martin 测试流程并修改
- 150515 Martin 根据大妈指正 增补下载资源链接
- 150513 Martin 增补FeedBack
- 150512 Martin 增补简介以及非技术人员教程
- 150511 大妈 整理 Martin 草案发布
