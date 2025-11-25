# 基于 gitcafe-pages 服务的 markdoc 私人维基发布
[TOC]

## 背景
- 又看到一篇大张旗鼓的忽悠人去 SAE 架 Wordpress 的教程...
- 再对比:
    - [将博客从GitHub迁移到GitCafe - 唐巧的技术博客](http://blog.devtang.com/blog/2014/06/02/use-gitcafe-to-host-blog/)
    - [还没用过 Markdown 吗?那你就 OUT 了!](http://mp.weixin.qq.com/s?__biz=MjM5ODc4MjcyMA==&mid=201705313&idx=1&sn=fbe6d0398e19f640882750a9cc510eab&scene=1&key=2f5eb01238e84f7e8fce9906a94c635c59eca3ac7d725d5f102799e7e32574efc556ae15498ab8d689ec4e46bcf6d33b&ascene=0&uin=MTg1NDU4NTY4MQ%3D%3D&devicetype=iMac+MacBookPro8%2C2+OSX+OSX+10.10.1+build(14B25)&version=11020012&pass_ticket=SUmaaeudmJ%2Bqbo%2BZk4djWsGMbLoRzEpUgYhaQ5%2BKJovW5RKT5QU4bwFffsaV2bJb)
    - [GitCafe Pages 服务启用顶级域名 gitcafe.io!](http://mp.weixin.qq.com/s?__biz=MjM5ODc4MjcyMA==&mid=203433592&idx=1&sn=412f176982328ed629de99540ea1f8ce&scene=1&key=2f5eb01238e84f7e1181289bc7b218c48242f1c6e699bf2fcbf6f20d0692d9c5fab97ab52cd54ead8fb32c97ab3e78da&ascene=0&uin=MTg1NDU4NTY4MQ%3D%3D&devicetype=iMac+MacBookPro8%2C2+OSX+OSX+10.10.1+build(14B25)&version=11020012&pass_ticket=SUmaaeudmJ%2Bqbo%2BZk4djWsGMbLoRzEpUgYhaQ5%2BKJovW5RKT5QU4bwFffsaV2bJb)

- 配合体会: 

![](https://github.com/Dobiasd/articles/raw/master/programming_language_learning_curves/php.png)

~ 来自: [articles/programming_language_learning_curves.md at master · Dobiasd/articles](https://github.com/Dobiasd/articles/blob/master/programming_language_learning_curves.md)


感觉有必要说点什么,于是有了这篇高速入门

## 分析

- 其实:
    - SAE 是个非常可用的国产 PaaS 平台, 几乎免费
    - Wordpress 是世界最好的 blog 系统之一
    - `#PHP是最好的语言`
    - 还有 MySQL ,世界上可能是第一个大规模赢利的开源数据库产品
- 但是,加起来,好象就哪里有不对了
- 我们可能只是想要有一个快速发布自个儿想法/思考/心得 的空间
    + 能用 Markdown
    + 能用自个儿的域名
    + 能任意迁移/发布到任何空间
    + 能自动备份
    + 能轻松的,不用什么帐号,就可以自然的增补/反馈/建议
    + 能在本地也查阅
    + ...
- 当然,可能最直接的一个非功能性要求就是:
    + 不用学习太多技术知识点!
- 所以, `LAMP` 架构思路的 `SAE+PHP+Wordpress+MySQL` ,明显复杂到飞溅了
- 世界是懒人的,早已有很多工具,可以只用一组脚本就达成以上所有心愿的了
- 参考官方文档:[Wiki Pages 相关帮助 · GitCafe/Help - GitCafe](https://gitcafe.com/GitCafe/Help/wiki/Pages-%E7%9B%B8%E5%85%B3%E5%B8%AE%E5%8A%A9#wiki)
    - 当然,这是针对 `gitcafe-pages` 服务的说明
    - 但是,要看到本质!
        + `gitcafe-pages` 本质上是一个可绑定域名的静态网站发布空间!
        + 只不过内置了 `Jekyll` 兼容的静态编译服务
        + **但是!** 没规定一定要使用 Ruby 系的静态网站工具哪!

### 俺的方案

- 使用自个儿喜欢的静态网站工具
    - 将编译出来的 `.html` 网络,单独纳入到合法的 `gitcafe-pages` 发布分支中
    - 通过 `fabric` 来批量化本地的编译/准备/发布 行为
    - 将 `Jekyll` 在服务端作的事儿,在本地作了
    - 从而达到相同的效果 ;-) 但是,更加任性!
- 当然俺是 `Pythoneer` 仅仅在本地安装有 Python 环境,不用数据库不用 web 服务器
    + 仅仅依赖 Python
    + 就可以达成以上所有目标 ;-)


## e.g

- 使用 [Markdoc](http://markdoc.org/)
- 文章仓库: [zhgdg/wiki - master](https://gitcafe.com/zhgdg/wiki)
    - 发布仓库: [zhgdg/wiki - gitcafe-pages](https://gitcafe.com/zhgdg/wiki/tree/gitcafe-pages)
    - 配置好域名
- 本地目录设定:

:

    /path/2/wiki
    ├── .git/
    ├── .gitignore
    ├── .html -> ../七牛同步目录/wiki/
    ├── .python-version # pyenv 声明戳, 可以任意的切换各种 Python 环境来玩
    ├── _static/        # markdoc 资源目录
    ├── _templates/     # markdoc 模板目录
    ├── fabfile.py      # fab 自动化脚本
    ├── markdoc.yaml    # 配置,相比Jekyll 的上百项, markdoc 10行以内就足够好用了
    └── wiki/           # .md 分目录收纳的文章



- 技巧就在 `.html` 是个软链接, 指向另外一个仓库
    + 其实就是当前仓库的 `gitcafe-pages` 分支克隆
- [Fabric](http://www.fabfile.org/) 是一个快速配置管理脚本工具,可以在本地或是远程用脚本描述一系列自动化操作,通过一个标签反复调用

:

    $ fab ?
    ...
    Available commands:
        build
        p2cafe
        pub7niu
        reserve
        serve



- 可以看到, `fabfile.py` 定义的操作有这么些,其中:
    + `pub7niu` 就是,编译,然后跳到对应目录将成果同步到 [七牛云存储](http://developer.qiniu.com/)
    + `p2cafe` 自然就是,编译,跳到对应目录,使用 git 将成果发布到 gitcafe 空间
- 以上,俺平常的写作流程就变成:
    + 到 `wiki` 对应目录中,创建一个 `.md` 文本,用喜爱的编辑器,爽快的书写
    + `fab p2cafe` 完成发布
    + `fab reverve` ,启动本地网站,然后在 http://localhost:8008/ 看看效果
    + `git ci -am "注释"` + `git pu` 将原稿也用 gitcfe 备份上
- 实际上,习惯后,基本就前两步,定期进行第四步就好.
    - 如果是 `fab pub7niu` 则是发布到 [七牛云存储](http://developer.qiniu.com/)
    - **就这么任性!**
- 朋友们,可以:
    + 在嵌入了 [Disqus](https://disqus.com/home/) 评论功能的网页上反馈
    + 也可以直接 `fork->clone->pull rwquest` 俺的文章仓库来反馈
- 就这么任性!



### .nojekyll

今天,通过不断的戳 [gitcafe](https://gitcafe.com/help) 的工程师,才知道一个隐藏技巧:

- 如果不是用 `Jekyll` 兼容的静态网站工具
- 那么
    + 嘦在最终发布仓库根目录中
    + 部署一个空白文件
    + 名为 `.nojekyll`
- `gitcafe-pages` 服务,就知道已经是静态网站, 不再试图找 `Jekyll` 工程配置来编译了.


## 效果

- 基于 [Pelican](http://getpelican.com/)
    + [About |PyChina.org | PyChina.org | 蠎中国社区](http://pychina.org/about.html)
    + [About |蠎周刊 |汇集全球蠎事儿 !-)](http://weekly.pychina.org/about.html)
    + [About | #是也乎# | ZoomQuiet.io](http://blog.zoomquiet.io/pages/about.html)
    + ...
- 基于: [Markdoc](http://markdoc.org/)
    + [华蠎 维基 | PyChina.org Static Wiki](http://wiki.pychina.org/)
    + [珠海GDG 维基 | ZHGDG Static Wiki](http://wiki.zhgdg.org/)
    + [Index | Zoom.Quiet's Personal Static Wiki](http://wiki.zoomquiet.io/)
    + ...

## 进一步的

有小朋友说了:

    骗纸! 
    俺不会 Python 怎么办?! 
    而且,
    俺是大 Windows 
        木有什么 `软链接` !



- 内什么...整体上涉及的工具只有:
    - Python ~ 推荐安装 [ActivePython](http://www.activestate.com/activepython/downloads) 有完备的 M$ 版本
    - [Git](http://www.git-scm.com/downloads) ~ 更加有 
- 相比官方推荐的工具组合:
    - ruby ~ 好象 M$ 版本很错觉...
    - jekyll
    - git
- 再相比更加高端的 `LAMP` 组合,在 M$ 上要折腾:
    + Apache
    + PHP
    + MySQL
    + Wordpress
    + ...
- 怎么看都最简洁了哪...
- 更进一步的, 请 google 或是留言吼俺来增补...


## 是也乎

当然,相同的策略也一样适用在 `github-pages` 服务空间呢...


