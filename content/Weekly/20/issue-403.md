---
title: "Issue 403"
summary: ""
date: "2020-01-15T16:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> 监狱中学 Python 改变人生
原文: [PyCoder's Weekly - Issue #403](https://pycoders.com/issues/403)
![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200115 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200115 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------

- [A coverage.py 调试求助](https://pycoders.com/link/3302/web)
  - NED BATCHELDER
Ned was getting reports for a mysterious disk I/O bug in the latest coverage.py release and asked the community for help. Read the crowd-sourced diagnosis on Hacker News and Ned's follow-up post next. What a journey...
(`是也乎:`
最喜欢这种故事了...总是展现出软件工程的诗意来
)
- [The "No Code" 妄想](https://pycoders.com/link/3303/web)
  - ALEX HUDSON
  - 观点
"2020 is going to be the year of 'no code': the movement that say you can write business logic and even entire applications without having the training of a software developer. I empathise with people doing this, and I think some of the 'no code' tools are great. But I also thing it's wrong at heart."
(`是也乎:`
机械代码->编译代码->高级代码->DSL->低代码->无码科技...
嗯哼,突然 发现 fenng 的前瞻能力哪
)
- [Python 如何实现超长整数?](https://pycoders.com/link/3273/web)
  - ARPIT BHAYANI
"Python must be doing something beautiful internally to support super long integers and today we find out what's under the hood. The article goes in-depth to explain design, storage, and operations on super long integers as implemented by Python."
- [Python GUI 编程学习路径](https://pycoders.com/link/3285/web)
  - REAL PYTHON
Does your Python program need a Graphical User Interface (GUI)? With this free learning path you'll develop your Python GUI programming skills from scratch. Covers Tkinter, PyQt, wxPython, and Kivy.
(`是也乎:`
![gui](http://ydlj.zoomquiet.top/ipic/2020-01-15-ScreenShot%202020-01-15%2015.53.59.jpg)
图形界面开发之路...
)
- [Mercurial's 的 Python 3 之旅和思考](https://pycoders.com/link/3275/web)
  - GREGORY SZORC
Lessons learned from Mercurial's Python 3 porting effort and a more opinionated commentary of the transition to Python 3 and the Python language ecosystem as a whole. A great read about the mechanics of porting a large Python project to Python 3.
(`是也乎:`
hg 真心命不好, 就是因为爹没 Linus 知名,所以, 这么好的 DVCS 工具,
一直被 git 压制.
但是,真正好用, 俺一直在服务端配置 hg 内置 web 服务来配合 hooks,
完成要很多其它工具配合才能完成的自动化并版本化配置同步.
)
- [用 super() 增强 Python OOP 代码](https://pycoders.com/link/3279/web)
  - REAL PYTHON
  - video
How to leverage single and multiple inheritance in your object-oriented Python code using the built-in super() function.
- [在监狱中俺从 Python 学到了什么](https://pycoders.com/link/3296/web)
  - SHADEED WALLACE-STEPTER
How open source programming can offer opportunities after incarceration.
(`是也乎:`
社区, 永远是社区的力量...
)
- [Pandas 1.0.0 新功能](https://pycoders.com/link/3272/web)
  - PANDAS.IO

## 讨论
>
> Discussions

- [学习 Django: 哪些初学错误是可以避免咯...](https://pycoders.com/link/3281/web)
  - REDDIT

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [逻辑回归在 Python](https://pycoders.com/link/3299/web)
  - REAL PYTHON
In this step-by-step tutorial, you'll get started with logistic regression in Python. Classification is one of the most important areas of machine learning, and logistic regression is one of its basic methods. You'll learn how to create, evaluate, and apply a model to make predictions.
(`是也乎:`
![Logistic](http://ydlj.zoomquiet.top/ipic/2020-01-15-ScreenShot%202020-01-15%2015.52.25.jpg)
逻辑回归...真蟒 开始深入非通用知识点了...
)
- [Redis服务器辅助的 Python客户端缓存](https://pycoders.com/link/3287/web)
  - ITAMAR HABER
Server-assisted client-side caching is a new capability added in Redis version 6. It is intended to assist the management of a local cache by having the server send invalidation notifications. The server tracks the keys accessed by a client and notifies the client when these change.
- [用 Python 探索 HTTPS](https://pycoders.com/link/3282/web)
  - REAL PYTHON
In this tutorial, you'll gain a working knowledge of the various factors that combine to keep communications over the Internet safe. You'll see concrete examples of how to keep information secure and use cryptography to build your own Python HTTPS application.
(`是也乎:`
![HTTPS](http://ydlj.zoomquiet.top/ipic/2020-01-15-ScreenShot%202020-01-15%2015.46.06.jpg)
这么解释加密:
![secret](https://files.realpython.com/media/alpha.12689a36982a.png)
)
- [将 Bokeh 嵌入脚本中](https://pycoders.com/link/3276/web)
  - JIM ANDERSON
"I really wanted to have a self-contained script that would launch Bokeh as part of its operation, rather than remembering which command line options I needed to specify."
(`是也乎:`
等等, Bokeh 本身不就是 Py 的模块由脚本执行的?
)
- [用 FastAPI 和 Pytest 开发/测试异步API](https://pycoders.com/link/3271/web)
  - TESTDRIVEN.IO
  - • Shared by Michael Herman
This tutorial looks at how to develop and test an asynchronous API with FastAPI, Postgres, Pytest, and Docker using Test-Driven Development (TDD).
(`是也乎:`
FastAPI/Pytest 强强联手.
)
- [在 Linux 内核中运行 Python](https://pycoders.com/link/3267/web)
  - YONATAN GOLDSCHMIDT
"This article will talk about a cool project I've worked on recently — a full Python interpreter running inside the Linux kernel"
(`是也乎:`
等等, 可是这有什么好处?
让 shell 可以直接使用 Python 内置的所有模块?
)
- [用 MkDocs 和 Netlify 在一天之内发布静态网站](https://pycoders.com/link/3269/web)
  - SEAN STEWART
  - • Shared by Sean Stewart
A Pythonista's (almost) no-code solution to building a website with the Python-based MkDocs static site generator.
(`是也乎:`
in a Day?
10分钟就足够了:
[Home — 蟒营™ 怂怼录](https://blog.101.camp/)
[蟒营™ Python 入门班第5期](https://py.101.camp/)
...
这些都是用 MkDocs 通过 github-pages 发布的
)
- [从 Browser 到 Django](https://pycoders.com/link/3266/web)
  - MATT LAYMAN
  - • Shared by Matt Layman
What happens from when a browser makes a request to how Django receives the request and sends back a response.
- [Python 在 Visual Studio Code – January 2020 发布](https://pycoders.com/link/3301/web)
  - MICROSOFT.COM
- [用 Python 构建并行图像下载器](https://pycoders.com/link/3293/web)
  - AMIT UPRETI
- [在 Dockerfile 中激活 Conda 环境](https://pycoders.com/link/3270/web)
  - ITAMAR TURNER-TRAURING
- [在 Django 中创建透明加密的字段](https://pycoders.com/link/3297/web)
  - KEVIN VERONEAU
- [在 PyQt 中创建密码输入小部件](https://pycoders.com/link/3298/web)
  - KUSHAL DAS

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [codetiming: 灵活,可自定义的 Py 代码运行计时器](https://pycoders.com/link/3286/web)
  - GITHUB.COM/REALPYTHON
- [nfstream: 灵活的网络数据分析框架](https://pycoders.com/link/3278/web)
  - GITHUB.COM/AOUINIZIED
(`是也乎:`
![nfstream](http://ydlj.zoomquiet.top/ipic/2020-01-15-ScreenShot%202020-01-15%2015.38.22.jpg)
很有诚意的项目...
)
- [scalene: 适用于 Python 的高性能,高精度 CPU 和内存分析器](https://pycoders.com/link/3280/web)
  - GITHUB.COM/EMERYBERGER
- [HTTPX: N适用于Python的下一代HTTP客户端](https://pycoders.com/link/3268/web)
  - PYTHON-HTTPX.ORG
(`是也乎:`
每年都有下一个一代的作品出现,
当然, 都是号称, 一切得看历史以及程序猿们的选择.
)
- [CleverCSV: 处理混乱CSV文件的Python包](https://pycoders.com/link/3288/web)
  - GITHUB.COM/ALAN-TURING-INSTITUTE
(`是也乎:`
![CleverCSV](https://raw.githubusercontent.com/alan-turing-institute/CleverCSV/eea72549195e37bd4347d87fd82bc98be2f1383d/.logo.png)
这才是真正需要的东西, 特别是从 Excel 导出的 csv 们...
    USAGE
      clevercsv [-h] [-v] [-V] <command> [<arg1>] ... [<argN>]
    ARGUMENTS
      <command>       The command to execute
      <arg>           The arguments of the command
    GLOBAL OPTIONS
      -h (--help)     Display this help message.
      -v (--verbose)  Enable verbose mode.
      -V (--version)  Display the application version.
    AVAILABLE COMMANDS
      code            Generate Python code for importing the CSV file.
      detect          Detect the dialect of a CSV file
      help            Display the manual of a command
      standardize     Convert a CSV file to one that conforms to RFC-4180.
      view            View the CSV file on the command line using TabView
)
- [mp3splitter: 将有声读物MP3文件拆分为章节](https://pycoders.com/link/3283/web)
  - GITHUB.COM/JIMA80525
- [用 pyproject.toml 作配置文件的 Python 项目](https://pycoders.com/link/3295/web)
  - GITHUB.COM/CARLOSPERATE
  - • Shared by Carlos
(`是也乎:`
叕一个 ML 的后代...
人们总是在寻求又灵魂又兼顾又规整又图灵完备的配置格式.
)
- [pytest-testmon: 可选择受更改文件影响的测试](https://pycoders.com/link/3291/web)
  - TESTMON.ORG
- [GoStyle: Go语法实现在 Python](https://pycoders.com/link/3274/web)
  - GITHUB.COM/LUOYUSANG2007
(`是也乎:`
所以, 早就说过:
    人生苦短
    Python当歌(go)
go 和 py 不分家咯:
    import time
    from gostyle import go
    def test_thread(title:str):
        while True:
            time.sleep(1)
            print(title)

  # Start the thread

    go(test_thread)("Call")
)
- [rq: 适用于Python的简单作业队列](https://pycoders.com/link/3294/web)
  - GITHUB.COM/RQ
(`是也乎:`
没错, 基于 Redis 的, 很老牌了...
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyData Bristol Meetup](https://pycoders.com/link/3257/web)
  - January 16, 2020
  - 英国
- [⋅ Python Northwest](https://pycoders.com/link/3255/web)
  - January 16, 2020
  - 英国
- [⋅ PyLadies Dublin](https://pycoders.com/link/3254/web)
  - January 16, 2020
  - 爱尔兰
- [⋅ MadPUG](https://pycoders.com/link/3253/web)
  - January 16, 2020
  - 404
- [⋅ Karlsruhe Python User Group (KaPy)](https://pycoders.com/link/3258/web)
  - January 17, 2020
  - 德国
- [⋅ Chattanooga Python User Group](https://pycoders.com/link/3256/web)
  - January 17, 2020
  - USA
- [⋅ BangPypers](https://pycoders.com/link/3262/web)
  - January 18, 2020
  - 印度
- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/3260/web)
  - January 18, 2020
  - 印度
- [⋅ Dominican Republic Python User Group](https://pycoders.com/link/3265/web)
  - January 21, 2020
  - 非洲

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- **[蟒营 Python 入门班](https://py.101.camp/)**
  - 5py ;-)
(`(￣▽￣)`:
第4期马上结业:
    200112 按时结束
年后第5期就来:
    20.2.3  可以上线
    20.2.20 报名截止
    20.3.1  正式开课
)
- [从1965年到2019年,最受欢迎的编程语言 (动画)](https://pycoders.com/link/3100/web)
  - TWITTER.COM/MARCUSBORBA
(`是也乎:`
网红小视频也出现了...
最后3秒, Python 疯狂反转一切.
)

# 是也乎
>
> NN 3893

- 首发: [Issue 403 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-403.html)
- 修订: [issue-403.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-403.md)
