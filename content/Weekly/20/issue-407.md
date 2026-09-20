Title: Issue 407
Slug: issue-407
Date: 2020-02-12 10:42
Tags: Weekly,Python,pycoders,ZH

> Guido 老爹义劝快乐的为 Python 提贡献吧



原文: [PyCoder's Weekly - Issue #407](https://pycoders.com/issues/407)

![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200205 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200205 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------



- [通过比较流行的项目模板了解 Python 工具的最佳实践](https://pycoders.com/link/3535/web)
    + JONAS KEMPER

"Use Flake8, pytest, and Sphinx in your current Python project. Also evaluate pre-commit, black, and Pylint. For your next project, consider adding poetry and Dependabot."


(`是也乎:`

老爹对结果呛声指点更加实在的...

> @gvanrossum

You missed mypy. Simpler docs use markdown, not ReST (Sphinx). Black is overrated unless your team argues over style a lot. You don't need Pylint if you're using flake8. Never heard of poetry or dependabot. And you should use a CI solution, e.g. Travis-CI, to run your tests.

)


- [用 Python 播放和录制声音](https://pycoders.com/link/3534/web)
    + REAL PYTHON 
    + video

Learn about libraries that can be used for playing and recording sound in Python, such as PyAudio and python-sounddevice. You'll also see code snippets for playing and recording sound files and arrays, as well as for converting between different sound file formats.


(`是也乎:`

![Sound](http://ydlj.zoomquiet.top/ipic/2020-02-12-ScreenShot%202020-02-12%2010.28.58.jpg)

其实吧, 通过 shell 调用专业工具来完成实际工作就好.

)

- [由 SQL 理解 Django 中的 GROUP BY](https://pycoders.com/link/3527/web)
    + HAKI BENITA

Understand GROUP BY in Django ORM by comparing QuerySets and SQL side by side. If SQL is where you are most comfortable, this is the Django GROUP BY tutorial for you.

- [用 Python 对自定义着色器的电视背光补偿](https://pycoders.com/link/3548/web)
    + PEKKA VÄÄNÄNEN

Extending a broken TV's lifetime with Python code and some custom shaders. Impressive!

- [将Mypy应用于实际项目](https://pycoders.com/link/3553/web)
    + CAL PATERSON

Hints and tips for getting started with Mypy and introducing it to existing projects.

- [Virtualenv 20.0 发布](https://pycoders.com/link/3526/web)
    + PYPA.IO




## 讨论
> Discussions

- [用 NSA 来学习 Python](https://pycoders.com/link/3540/web)
    + TWITTER.COM/CHRIS_SWENSON

"I put in a FOIA request to the NSA for their Python training materials and got back a 400-page printout of their COMP 3321 training course. So, I scanned and OCR'd it. Here is a PDF (warning: 118 MB)"

(`是也乎:`

神人, 直接搞到了 国安内部的 Python 学习资料并 OCR 共享了出来;

然后万能的网友们友好的指出,早已在 github 发布出来了

github.com/NationalSecurityAgency/ghidra

)


- [开始为 CPython 做贡献](https://pycoders.com/link/3524/web)
    + GUIDO VAN ROSSUM

(`是也乎:`

老爹终于忍不住了, 用 Dropbox 的只读文档形式发布指导:

想为 CPython 贡献很简单,没那么多传说的技能要求:

要懂 C 语言 (错误,你并不用懂 C 语言. 大多标准库都是用 Python 写的. 而且我们也需要人帮忙完善文档)

要懂 Git 和 GitHub (不完全正确. 虽然有一些概念要理解,但入门还是很容易的)

要有10多年的 Python 经验 (不正确. 有个几年 Python 经验,不只局限于numpy和pandas这两个库就可以了)

现在有 7000+ 提案, 选择一个适合自己的开始, 然后, 才可能有然后.

标准协同流程就是 github 的 pull-request 流程, 得用对, 否则, 只会难为到自己.

老爹自己应该工件在 mac 中, 所以, 给出的编译过程就是用 XCode 进行的,
只是, 吐糟-> 一定有各种意外,
比如 openssl 在 macOS 中并不是默认配置.

以及, 千万别用 虚拟环境来编译, 都是坑.

有队友增补了 VSCode 中调试技巧,

最后, 老爹推荐了几个 C代码调试工具:

首先当然是简单的 `printf()`;

然后是GDB (Linux)/lldb (Mac), Windows 中就蒙了...


> 可以说, 对 Python 这种不小的综合工程, 想进入核心开发, 所要求的技术储备看起来并不多,
> 也就2页纸的样子;
> 但是, 其实, 每一项都得经过艰苦/长期的努力, 才可能自如的;
> 但是, 想想当年, 老爹可真的就是单枪匹马, 独自撸出来的, 
> 现在, 有这么多现成工具/资料/社区可依赖了, 当然也可以哈.

)


## 文章,教程和嗯哼 
> Articles, Tutorials and Talks

- [用 Python 构建 macOS 状态栏应用 (蕃茄钟)](https://pycoders.com/link/3522/web)
    + CAMILLO VISINI 
    + • Shared by Camillo Visini

"On my Mac, I use the menu bar countless times per day. In this post we will go through the process of creating a custom macOS menu bar app using Python."

(`是也乎:`

macOS 环境, 总是能吸引各种精巧的实现形式,
关键内置的自动化项目, 可以不依赖任何第三方开发库, 就能完成各种事务,
问题是:

为什么是 Apple 公司一直在力图营造对程序猿友好的环境?

用 [jaredks/rumps](https://github.com/jaredks/rumps) 构造状态栏工具;
用 [py2app](https://py2app.readthedocs.io/en/latest/) 来自动基于 Python 脚本生成 mac 应用;

)


- [在 Python 中实现接口](https://pycoders.com/link/3543/web)
    + REAL PYTHON

In this tutorial, you'll explore how to use a Python interface. You'll come to understand why interfaces are so useful and learn how to implement formal and informal interfaces in Python. You'll also examine the differences between Python interfaces and those in other programming languages.


(`是也乎:`

![Interface](http://ydlj.zoomquiet.top/ipic/2020-02-12-ScreenShot%202020-02-12%2009.56.19.jpg)

给自身以及其它语言构建友好的界面.
类的狂欢.


)

- [SciPy 1.0: Python 中科学计算的基本算法](https://pycoders.com/link/3549/web)
    + NATURE.COM

"In this work, we provide an overview of the capabilities and development practices of SciPy 1.0 and highlight some recent technical developments."

- [用赋值表达式防止重复](https://pycoders.com/link/3551/web)
    + BRETT SLATKIN

An assignment expression—also known as the walrus operator—is a new syntax introduced in Python 3.8 to solve a long-standing problem with the language that can cause code duplication.

- [Python 命令行参数解](https://pycoders.com/link/3542/web)
    + REAL PYTHON

Python command line arguments are the key to converting your programs into useful and enticing tools that are ready to be used in the terminal of your operating system. In this step-by-step tutorial, you'll learn their origins, standards, and basics, and how to implement them in your program.

(`是也乎:`

![REALpy](http://ydlj.zoomquiet.top/ipic/2020-02-12-ScreenShot%202020-02-12%2009.45.57.jpg)

其实, CLI 指令这么复杂, 并不能解决易用性问题:

![Arguments](https://files.realpython.com/media/python_blue.37b9170f4345.png)

所以, RESTful 思路也是一个可选择项哪.


)


- [并行蓝调: 当代码变慢时](https://pycoders.com/link/3545/web)
    + ITAMAR TURNER-TRAURING

"As it turns out, for certain operations NumPy will parallelize operations transparently. And if you're not careful, this can actually slow down your code."


(`是也乎:`

Blues 音乐本质就是哀伤...
代码变慢慢的本质也是...

)



- [sys.getsizeof 不是您想要的](https://pycoders.com/link/3525/web)
    + NED BATCHELDER

"sys.getsizeof is almost never what you want, for two reasons: it doesn't count all the bytes, and it counts the wrong bytes."

(`是也乎:`

所以, 编程自古以来最大的难题, 也可能是无解的难题就是:

    如何起个好名字?

也许只有 `七枝桶` 文字,才能真正承载永远正确的命名.

)



- [Python asyncio and await -ing 多种功能](https://pycoders.com/link/3539/web)
    + ERIC URBAN

How to call await on multiple functions in Python using the asyncio package.

- [在 Kaggle 竞赛中作弊 (A Post-Mortem)](https://pycoders.com/link/3523/web)
    + KAGGLE.COM 
    + • Shared by Python Bytes FM

(`是也乎:`

Kaggle 也是个奇迹,
以纯粹的竞赛组织,只是附加上了开源共同体的气质,
就变成了全球 AI 代码黑洞,
所有先进思想/模块, 都首先在此展示/传播/学习...

> 赛末点

)


- [用 YAPF 自动格式化 Python 代码](https://pycoders.com/link/3555/web)
    + LEI MAO

- [如何用 Python 检查文件是否为有效图像](https://pycoders.com/link/3529/web)
    + MIKE DRISCOLL

(`是也乎:`

`鼠与蟒` 这个网站一直非常有爱,
撰写的一系列小书更加有爱,
再次推荐.

)


## 好物
> Interesting Projects, Tools and Libraries, Projects & Code


- [hydra: 用于配置复杂应用程序的框架](https://pycoders.com/link/3537/web)
    + GITHUB.COM/FACEBOOKRESEARCH

(`是也乎:`

叕见 `海德拉` 好名儿太难得,
但是,也不能反复用哪

)


- [cookiecutter-data-science: 执行/共享数据科学工作的项目模板](https://pycoders.com/link/3532/web)
    + GITHUB.COM/DRIVENDATA

- [pytorch3d: 用于3D数据的深度学习的可重用组件](https://pycoders.com/link/3541/web)
    + GITHUB.COM/FACEBOOKRESEARCH

(`是也乎:`

3D 模型本身就是数学生成的,
对这种空间意义进行深度学习,
那不就是对 3D 网络游戏可以进一步理解和控制->自动生成?

)

- [Diagrams: 用 Python 代码生成系统架构图](https://pycoders.com/link/3544/web)
    + GITHUB.COM/MINGRAMMER


(`是也乎:`

    from diagrams import Diagram
    from diagrams.aws.compute import EC2
    from diagrams.aws.database import RDS
    from diagrams.aws.network import ELB

    with Diagram("Web Service", show=False):
        ELB("lb") >> EC2("web") >> RDS("userdb")

即可生成:

![Diagrams](https://diagrams.mingrammer.com/img/web_service_diagram.png)


基于 [Graphviz](https://www.graphviz.org/) ,
但是, 用 Py 脚本形式, 快速生成漂亮的示意图,
果断粉上;


)



- [opnieuw: 通用重试库](https://pycoders.com/link/3554/web)
    + GITHUB.COM/CHANNABLE

(`是也乎:`

简洁的重试机制支持, 
来提高系统可靠性...

嗯哼? 系统可能性就这么简单可以提高了?


)


- [Celery Director:用 Celery 管理任务和构建工作流](https://pycoders.com/link/3550/web)
    + GITHUB.COM/OVH 
    + • Shared by Nicolas Crocfer

(`是也乎:`

又见芹菜馅儿的好物

)


- [donkeycar: 小型自动驾驶汽车平台](https://pycoders.com/link/3531/web)
    + GITHUB.COM/AUTOROPE

(`是也乎:`

![donkeycar](https://github.com/autorope/donkeycar/raw/dev/docs/assets/build_hardware/donkey2.png)

包含硬件的全套自动驾驶系统.

纯Python 完成.

)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyCon Namibia 2020](https://pycoders.com/link/3533/web)
    + February 18 to February 21, 2020
    + 纳米比亚

- [⋅ Open Source Festival Africa](https://pycoders.com/link/3538/web)
    + February 20 to February 23, 2020
    + 非洲

- [⋅ PyCon Belarus 2020](https://pycoders.com/link/3521/web)
    + February 21 to February 23, 2020
    + 白俄罗斯




## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- **[蟒营 Python 入门班](https://py.101.camp/)**
    + 5py 
    + 报名

(`(￣▽￣)`:

第五期已经开始报名:

    20.2.24 报名截止
    20.3.1  正式开课
    20.4.12 按时结束

)


- [2020新冠肺炎记忆](https://github.com/2019ncovmemory/nCovMemory)
    + github.com/2019ncovmemory/nCovMemory

报道,非虚构与个人叙述(持续更新) Memory of 2020 nCov: Media Coverage, Non-fiction Writings, and Individual Narratives (Continuously updating)

(`是也乎:`

可能是最考验 M$ 政府关系能力的项目,
这个开源新闻实录项目,
综合使用现有工具, 快速将 NCP 历史, 用普遍人的目光固化在版本历史海洋中,
但是,万一呢? 期望大家及时, 自觉分散 clone 到全球每一个硬盘中,
42年后, 我们才可能有真实的 snap 来回顾.

项目结构

    ├─archive                          文章的存档,目前提供jpg格式
    │  └─jpg
    │    ├─1.jpg
    │    └─...
    ├─data                             csv格式的文章数据
    │  └─data.csv
    ├─docs                             一个用于展示README的 Github Page
    ├─gh-page
    ├─template                         README模板
    │  └─README.handlebars
    ├─utils                            构建README的工具
    │  ├─generateReadmeFromCsv.js
    │  └─...
    └─README.md                        主文档


)


# 是也乎
> NN 3921

- 首发: [Issue 407 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-407.html)
- 修订: [issue-407.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-407.md)




