---
title: "Issue 395"
summary: ""
date: "2019-11-13T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> 激萌模块->用表情符编写Python程序
原文: [PyCoder's Weekly - Issue #395](https://pycoders.com/issues/395)
![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 191120 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 191120 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------

- [Python 中咯线程](https://pycoders.com/link/2932/web)
  - REAL PYTHON
  - video
Learn how to use threading in your Python programs. You'll see how to create threads, how to coordinate and synchronize them, and how to handle common problems that arise in threading.
(`是也乎:`
![Threading](http://ydlj.zoomquiet.top/ipic/2019-11-20-ScreenShot%202019-11-20%2010.41.42.jpg)
基础而又不简单的嗯哼...
)
- [加载较少数据来减少 Pandas 内存用量](https://pycoders.com/link/2926/web)
  - ITAMAR TURNER-TRAURING
How to reduce the memory your DataFrame uses at the time it is initially loaded: by dropping columns, lower-range numerical dtypes, and categoricals.
- [Python 字典"加法"的回归](https://pycoders.com/link/2943/web)
  - JAKE EDGE
An interesting summary of discussions around PEP 584 ("Add + and += operators to the built-in dict class").
- [为什么向 Python 3 迁移需要这么长时间?](https://pycoders.com/link/2939/web)
  - VICKI BOYKIS
(`是也乎:`
因为, 多数项目没法儿迁移...
)
[Related discussion on Hacker News.](https://pycoders.com/link/2949/web)
- [Django 3.0 RC 1 可用矣](https://pycoders.com/link/2933/web)
  - DJANGOPROJECT.COM
- [PyCon 2020 Tutorial 提案截止日期临近](https://pycoders.com/link/2948/web)
  - PYCON.BLOGSPOT.COM

## 讨论
>
> Discussions

- [嫑将 property() 用于计算密集型任务](https://pycoders.com/link/2927/web)
  - RAYMOND HETTINGER
"To a user, attribute-style access is implicitly assumed to be fast. In contrast, a well-named method can communicate workload: raymondh.family_members vs raymondh.scan_entire_social_graph()"
- [正要学习Django, 应该等待 3.0 发布的教程吗?](https://pycoders.com/link/2936/web)
  - REDDIT
(`是也乎:`
简单说: 没必要
)
- [工作中的自动化任务...  Boss Found Out](https://pycoders.com/link/2946/web)
  - REDDIT

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [Python IDLE 入门](https://pycoders.com/link/2934/web)
  - REAL PYTHON
See how to use the development environment included with your Python installation. Python IDLE is a small program that packs a big punch! You'll learn how to use Python IDLE to interact with Python directly, work with Python files, and improve your development workflow.
(`是也乎:`
![IDLE](http://ydlj.zoomquiet.top/ipic/2019-11-20-ScreenShot%202019-11-20%2009.44.46.jpg)
IDLE 虽好, 可嫑贪杯哪...
这都21世纪了, 为什么要用 IDLE 呢? 有什么想不开的说出来大家开心一下嘛...

> Integrated Development and Learning Environment
人家是用来学习的, 开发真心囧的...
)

- [当您的数据不适合内存时: 基本技术](https://pycoders.com/link/2938/web)
  - ITAMAR TURNER-TRAURING
  - • Shared by ITAMAR TURNER-TRAURING
Python techniques for processing "bigger than RAM" data on a single computer, with minimal setup, and as much as possible using the same libraries you're already using.
- [用 SSH 的非常规安全和异步 RESTful API](https://pycoders.com/link/2940/web)
  - TRYEXCEPTPASS.ORG
  - • Shared by Cristian Medina
How to build secure asynchronous APIs in Python using Korv and AsyncSSH that listen on TCP sockets over SSH sessions.
- [Pandas GroupBy: Python 数据分组指南](https://pycoders.com/link/2923/web)
  - REAL PYTHON
Learn how to work adeptly with the Pandas GroupBy facility while mastering ways to manipulate, transform, and summarize data. You'll work with real-world datasets and chain GroupBy methods together to get data in an output that suits your purpose.
(`是也乎:`
![Pandas GroupBy](http://ydlj.zoomquiet.top/ipic/2019-11-20-ScreenShot%202019-11-20%2010.36.00.jpg)
这也是神器之一...
)
- [Jupyter 上手机 (或哪儿都行)](https://pycoders.com/link/2937/web)
  - UMAR KHAN
How to host Jupyter notebooks on your own server so you can access them anywhere, even with your mobile phone.
(`是也乎:`
其实, 官方文档都有曰...只是, 还是太重了...
Azure 们提供了预嗯哼好的...
)
- [如何将 awk 脚本移植到 Python](https://pycoders.com/link/2950/web)
  - MOSHE ZADKA
(`是也乎:`
为什么这么想不开?
)
- [用 DTrace 和 cProfile 对 Django 进行性能分析](https://pycoders.com/link/2929/web)
  - SEBASTIAN WIEDENROTH
(`是也乎:`
DTrace ~ Solaris 贡献的神器...
)
- [PyCon Africa 2019 (回顾)](https://pycoders.com/link/2945/web)
  - REAL PYTHON
(`是也乎:`
![Recap](http://ydlj.zoomquiet.top/ipic/2019-11-20-ScreenShot%202019-11-20%2010.30.03.jpg)
真蟒 率先嗯哼非洲去了...
)
- ["int" 去除空格字符串](https://pycoders.com/link/2941/web)
  - REUVEN LERNER
(`是也乎:`
guido 老爹太皮了, 将一个不起眼的 `int()` 转换函式嗯哼的这么强大...
)

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [modin: Pandas 工作流加速](https://pycoders.com/link/2944/web)
  - GITHUB.COM/MODIN-PROJECT
(`是也乎:`
![modin_architecture](https://github.com/modin-project/modin/raw/master/docs/img/modin_architecture.png)
等等,好象这事儿是 Jupyter 之前要作的事儿哪...

> 一行完美加速 Pandas 们的计算....
    import modin.pandas as pd
)

- [viewflow: 用于 Django 的可重用工作流库](https://pycoders.com/link/2947/web)
  - GITHUB.COM/VIEWFLOW
(`是也乎:`
等等, 工作流扎堆发布是想抢 oDoo 的生意?
)
- [django-fsm: 适用Django 的易用 有限状态机](https://pycoders.com/link/2951/web)
  - GITHUB.COM/VIEWFLOW
- [django-river: Django 工作流程库](https://pycoders.com/link/2930/web)
  - GITHUB.COM/JAVRASYA
(`是也乎:`
这项目名起的好哪...
)
- [BrachioGraph: 最便宜/最简单的笔式绘图仪](https://pycoders.com/link/2922/web)
  - BRACHIOGRAPH.ART
- [adtk: 时间序列中的无监督异常检测](https://pycoders.com/link/2928/web)
  - GITHUB.COM/ARUNDO
(`是也乎:`
![adtk](https://arundo-adtk.readthedocs-hosted.com/en/latest/_images/quickstart2.png)
)
- [slim4py: Ruby Slim 当 Python 模板引擎](https://pycoders.com/link/2931/web)
  - GITHUB.COM/MULTIVERSECODER
(`是也乎:`
等等... Rubista 叛变来的?
)
- [Makefile.venv: 用 Makefile 管理 Python 虚拟环境](https://pycoders.com/link/2942/web)
  - GITHUB.COM/SIO
(`是也乎:`
嗯哼? 这个非常正义哪, 沈游侠曰过:
    每个程序猿
    一生
    终将完成自己那个 makefile
make 作为一个通用工具, 已经达到了完美级别,
只是, 很少有大规模宣传而已,
但是, 要论通用/兼容, 真的没什么工具能比过1976年4月,​43年前发布的:
[GNU make](https://www.gnu.org/software/make/manual/make.html)
)
- [jenkinsapi: 用于 Jenkins CI 的 Python API](https://pycoders.com/link/2925/web)
  - PYPI.ORG
(`是也乎:`
JAVA 的地盘总归会吞入 Python 腹中
)
- [pythonji: 使用表情符号编写Python](https://pycoders.com/link/2924/web)
  - GITHUB.COM/GAHJELLE
(`是也乎:`
    import pandas as 🐼
    from numpy import random as 🔀

  # Define a dataframe and print it to the console

    📋 = 🐼.DataFrame(
        {
            "😀": ["🐼", "🐍", "🦁"],
            "🏷️": ["Panda", "Python", "Lion"],
            "💯": 🔀.randint(2, 5, size=3),
        },
    ).set_index("😀")
    print(📋)

  # Do some arithmetic with the dataframe

    🔤 = f" Pythonji {' '.join(📋.index)}"
    🔢 = 📋.loc["🐍", "💯"] + 📋.loc["🐼", "💯"]
    print(🔤 * 🔢)
萌是萌...问题是如何输入哪...
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyData Bristol Meetup](https://pycoders.com/link/2913/web)
  - November 21, 2019
  - UK
- [⋅ Python Northwest](https://pycoders.com/link/2914/web)
  - November 21, 2019
  - UK
- [⋅ PyLadies Dublin](https://pycoders.com/link/2915/web)
  - November 21, 2019
  - 德国
- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/2916/web)
  - November 23, 2019
  - 印度

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- **[蟒营 Python 入门班](https://py.101.camp/)**
  - 第4期
  - 101camp4py
第4期已上线, 为期6周;
    191124 报名结束
    191201 正式开课
    200112 按时结束
- [JohnCoates/Aerial: Apple TV Aerial Screensaver for Mac](https://github.com/JohnCoates/Aerial)
  - macOS
  - 屏保
(`是也乎:`
网友 𝙰𝚣𝚎𝚛𝚒𝚕 推荐, 为了心灵...
)

# 是也乎
>
> NN 3837

- 首发: [Issue 395 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-395.html)
- 改进: [issue-395.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-395.md)
