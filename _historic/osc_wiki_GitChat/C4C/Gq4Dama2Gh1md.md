# GQ:1: md 在 github

[TOC]

## GFM !-)

> github 其实是伪装成 git 仓库的 md 编辑平台

gh 对 md 是狂热的

从发布之初就宣称: [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/)

并将这种狂热传染给了全球开发者, 以致到后来所有 md 编辑器,都得有 github 风格的渲染支持.
这种狂热甚至于高于对 git 的支持,

这也是为什么要将 gh 对 md 的支持, 放在 git 的支持之前来强调


## 为毛?

- 只是, md 之前同类的简化标记文档规范有很多哪,
    + 为什么 gh 忠情 md?
- 可能,事儿是相反的, 正因为 gh 选择了 md, 从而引发了 md 的极大爆发
    + 是的, 俺说是的 gh-pages
    + 这个古怪的分支, 由 gh 发明出来
    + 不仅仅令大家用起来了 `--orphan` 参数
    + 同时带来了几个后果:
        * 提升了 .io 域名的含金量
        * 推动了 Jekyll 框架的爆款
        * 使 md 成为发展最快速的私人建站首选内容格式
- 当然, 从技术角度看, 也许原因非常朴素:
    + RoR 创建之初, 类似的 文本解析器, ruby 支持的最小的就是 md
    + 同时又想扩展出很多独有的功能
    + 当然选择最简单的那个
    + 所以, md 从一开始就成为 gh 的基因
    + 而且是弥散最深最自在的一个
- 不过, 从程序猿心理角度, 俺可以很坚定的认为:
    + 就是因为创始人们懒
    + 没心情发明一个自己已经熟悉的 md 格式
    + 就直接拿来用先
    + 没想到一用就丢不下了...


## 出没.md

在 gh 中最常见的输入场景中都支持 md 的解析:

- 仓库中的 .md 直接编译为对应 html 来展示
- issue 的正文/回复 都默认支持 md
    + 而且包含了很多方便功能
    + 比如说, 最受欢迎的 chk-box
    + 而且自动识别, 并展示为 issue 标题旁的进展条
    + ...
- wiki 不用说也是
- 版本的 commit comment 也支持 md
- 甚至于, 从远程 git 仓库 push 时的 commit log 也支持 md
    + 而且是 GFM ~ 扩展的 md 格式
    + `#12` 这种将自动转换为相同编号的 issue 链接
    + `ec0b06a` 这种 commit hash, 将自动指向对应的 commit diff 页面
    + 还能指向用户仓库的具体 comiit 
    + ...


## 配合的工具

md 再简洁, 也无法在网页上快速的激烈的进行大规模的编辑,
最简单的全局查找和替换文字就无法简单的在网页上完成,
所以, 除了能通过 git 远程编辑仓库和wiki 中的 md 文本之外,
有什么工具, 可以帮助我们高速进行在线 md 文本的编辑?!

- Sublime Text 3 等等现代编辑器, 都有非常优秀的 md 编辑支持
- 智能缩进/自动关闭语法/颜色提醒/...
- 如何将网页输入和本地编辑器软件结合起来?
    + 当然, 通过 git 仓库可以解决部分输入问题
    + 但是, 更多的场景是 issue/commit comments ~ 并没有对应仓库可以 clone
- 所以, 很久之前用的是笨办法:
    + Ctrl+A, Ctrl+c, Ctrl+v
    + 对的, 将网页 textarea 中的文本全选粘到本地编辑器中
    + 编辑好了, 再全选粘回去...
    + 可用, 但是,每次可能都丢失当前的编辑位置
    + 而且, 傻....
- 幸好, 后来 FireFox 的插件解决了这个问题
    + 哪个插件?
    + 你猜...

## 问题->mail
~ 唯一的 md 支持不一致场景

- gh 其实也支持 mailling-list 的
- 只是不是内置的服务
- 而是通过 整合服务(Integrations & Services) 接入
    + 当初只有几个服务
    + 现在已经扩充为上百个了...
- 所以,和 googlegroup 自然的关联起来起来后
    + 大家就能不上 gh 网站
    + 从 gmail 邮箱中自然的接受到所有 仓库/issue 相关变化了
    + 神奇的是, 用邮件回复 issue
    + 将自动的发布为对应 issue 的回复
    + 只是, 这时, 邮件中的文本, 就不被解析为 md 了

问题是, 项目托管服务在 gh 之前, 从未有哪个服务,有这种邮件的双向渠道支持,
一般都是单向的, 并在邮件标题中强调:

    不得回复


所以, gh 的创始者们,一定非常懒, 连自己网站都懒得上,
才创造出这种通过邮件也能完成协同的功能,

    太爽了!


## gh-pages

- web 1.0 时代, 大家怎么发布个人网站的?
    + 租主机/空间, 自行构建 LAMPs 体系
- web 2.0 时代, 大家又都是怎么发布个人网站的?
    + 免费通过 blogger 等等服务发布
- gh 之后呢?
    + 当然首先是用 github.io 来发布静态网站
    + 然后简单的通过 `CNAME` 的配置完成私人域名的绑定 

甚至于, 由于 gh 选择了 md 以及免费发布了 gh-pages 服务,
依托 gh-pages 发布了:

- blogging
- CMS
- wiki
- PKM 
- ...
- 各种工具, 来帮助人们快速完成各种信息的发布...


> 功德无量


笔者和小伙伴甚至于用 gh-pages 快速发布过技术大会的官网...

gh-pages 还能作什么?是否能结合前端技术, 直接变成可用的 SPA ?

- 答案是肯定的, 而且早已有社区这么作了
- 最常用(之于中国程序猿)的应就是: [ziahamza/webui-aria2: The aim for this project is to create the worlds best and hottest interface to interact with aria2. Very simple to use, just download and open index.html in any web browser.](https://github.com/ziahamza/webui-aria2)



## ipynb?
> 木星笔记本

从 IPython notebook 进化为 Jupyter Notebook 后,
ipynb 文件,其实已经支持包含 Java/php/ruby 等其它语言了.

但是, 狂热的将相关模块加载在后台, 直接支持在仓库页面解析 .ipynb 文件的项目托管服务,
gh 是第一家,

当然, 肯定不会是最后一家, 毕竟在数据科学时代,
可运行的文档这种形式是基础形式了.

问题是:

- gh 是否能足够好的解决依赖模块的自动化安装?
- 以及 gh 是否原意支撑大家在 gh 页面上进行 ipynb 的创作和交流?
- 如果实现的话, 可能应用的发布/部署形式又多了一个...


## 提问
~ 是的, GitQ 不是单向灌输, 双向交流才真诚

- markdown 同类结构化文本还有什么?
- 什么是 WYTIWYG ? 比 WYSIWYG 好还是挫?
- gh 中还有哪儿不支持 md ? 


## 是也乎

- 170911 init.

