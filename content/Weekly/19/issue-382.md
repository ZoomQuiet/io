---
title: "Issue 382"
summary: ""
date: "2019-08-21T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

原文: [PyCoder's Weekly - Issue #382](https://pycoders.com/issues/382)
![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)
------

- [有效的 Python 环境: 构造自己的家](https://pycoders.com/link/2315/web)
  - REAL PYTHON
This guide will walk you through the decisions you need to make when customizing your development environment for working with Python: shells, terminal emulators, version management (pyenv), virtual environments & pipenv, package management, and more.
(`是也乎:`
![pyenv](https://ipic.zoomquiet.top/2019-08-21-ScreenShot%202019-08-21%2011.57.00.jpg)
pyenv 是正确的开始.
)
- [规模 Python 静态分析: Instagram 版本](https://pycoders.com/link/2293/web)
  - BENJAMIN WOODRUFF
  - (INSTAGRAM)
Instagram's back-end is a massive Django app with several million lines of code. This post is about how they've used linting and automated refactoring to help manage the scale of their Python codebase.
(`是也乎:`
这之前 google 已经完成更加大规模静态自动化分析...
只是, 故事主人没怎么说...
)
- [为 Python 编写自定义 profilers](https://pycoders.com/link/2323/web)
  - ITAMAR TURNER-TRAURING
In this article you'll learn how to write custom profilers, and in particular profilers that will help you pinpoint the places in your code where it just sits there waiting.
- [Python Web 框架概述](https://pycoders.com/link/2300/web)
  - STXNEXT.COM
Django, Flask, Pyramid, and many, many others—get an overview of what's available so you can choose the right Python framework for your web development project.
- [设计持续构建系统: 用 Sanic 处理 Webhooks](https://pycoders.com/link/2291/web)
  - CHRISTIAN MEDINA
  - • Shared by Cristian Medina
How to use Python and Sanic to handle webhook events from GitHub in continuous build systems.
- [PyCon US 2020 网站已上线](https://pycoders.com/link/2308/web)
  - PYCON.ORG
PyCon 2020 takes place April 15–23, 2020 in Pittsburgh, PA.
(`是也乎:`
加油  PyCon2020China , 目测咱们的 11月能上线就是巨大的进步...
以往都是下半年了,才上线当年的...
)

## 讨论
>
> Discussions

- [PyPI 拥有接近 200,000 包](https://pycoders.com/link/2320/web)
  - RAYMOND HETTINGER
(`是也乎:`
作者预言国庆之后将超过 20万.
)
- [用 Black 格式化 Python 代码不会被 git blame 嗯哼](https://pycoders.com/link/2288/web)
  - TWITTER.COM/LLANGA
- [为毛只有讨论 "Pure Python" 却没人BB "Pure Java", "Pure C", etc?](https://pycoders.com/link/2294/web)
  - REDDIT
(`是也乎:`
好问题哪...
目测因为其它老语言早已形成了坚固的思想框架,以及对应强大的教育和工具体系,
根本写不出非  JAVA/C 味儿的代码;
当然, 也有另外一个解释,
因为其它语言用户基数更大, 无论写成什么味儿都算它们自己的.
而, Python 为了宣传, 只能创造性发明 Python-style 这种嗯哼来嗯哼
)

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [用 Python 和 Pandas 进行数据清理](https://pycoders.com/link/2290/web)
  - ERIK MARSJA
Learn how to do simplify your data preprocessing work using the Pyjanitor package. More specifically, you'll learn how to: Add a column to a Pandas dataframe, remove missing values, remove an empty column, and clean up column names.
- [Python 直方图绘图: NumPy, Matplotlib, Pandas & Seaborn](https://pycoders.com/link/2316/web)
  - REAL PYTHON
  - video
Get equipped to make production-quality, presentation-ready Python histogram plots with a range of choices and features. It's your one-stop shop for constructing and manipulating histograms with Python's scientific stack.
- [Slack <3 Python](https://pycoders.com/link/2274/web)
  - SLACK
  - sponsor
Slack Python SDK v2 is now available to help you build Slack apps faster with less complexity. Built for Python 3, you can now use new features (like type hints and return types) to help you accomplish more while coding less. Looking for a tutorial or migration guide? It all lives here →
(`是也乎:`
亲测是真的...
)
- [用于乐高 EV3 的 Python](https://pycoders.com/link/2312/web)
  - LEGO.COM
  - • Shared by Python Bytes FM
"You can now use your EV3 Brick to unleash the power of Python programming using MicroPython. Simply install the EV3 MicroPython image onto any micro SD card and boot up your EV3 Brick from it to start programming straight away."
(`是也乎:`
LEGO EV3 什么都好, 就是一个受不了 -> 贵
)
- [如何用 Python 构造 Discord Bot](https://pycoders.com/link/2311/web)
  - REAL PYTHON
Learn how to make a Discord bot in Python and interact with several APIs. See how to handle events, accept commands, validate and verify input, and all the basics that can help you create useful and exciting automations!
(`是也乎:`
![Discord](https://ipic.zoomquiet.top/2019-08-21-ScreenShot%202019-08-21%2011.56.43.jpg)
何时能有 qq/wx bot?
)
- [用 PyNode 桥接 Node.js 和 Python 完成房价预测](https://pycoders.com/link/2319/web)
  - ADAM MCQUISTAN
"In this article I demonstrate a novel Node.js package named PyNode used to invoke Python code within a Node.js application and, more importantly, receive Python return types in the calling Node.js application."
(`是也乎:`
在 wasm 之后, 还有 JS 什么事儿嘛?
)
- [Azure Functions 现在支持 Python](https://pycoders.com/link/2303/web)
  - MICROSOFT.COM
Python support for Azure Functions is now generally available and ready to host your production workloads across data science and machine learning, automated resource management, and more.
(`是也乎:`
在 Lambda 支持7年之后?
)
- [基于 Python 的 150+ 商用 Data Science 应用思路](https://pycoders.com/link/2322/web)
  - GITHUB.COM/FIRMAI
A curated list of practical business machine learning (BML) and business data science (BDS) applications for Accounting, Customer, Employee, Legal, Management and Operations.
(`是也乎:`
嚓, 商用 ML 列表, 这简直就是 AI 落地姿势索引表...
)
- [用 Click 实现 Python CLIs 超级简单](https://pycoders.com/link/2296/web)
  - RICHARD BARELLA
How to give your Python scripts a full-featured Command-Line Interface (CLI) using the click library.
(`是也乎:`
pocoo 出品必属佳品...
用过, 只是也得看场景, 有大量本地系统工具使用的话, 还是 fabric 以及后续 invoke 方便...
)
- [用 OpenCV 进行简单场景边界/镜头过渡检测](https://pycoders.com/link/2321/web)
  - ADRIAN ROSEBROCK
Learn how to implement a simple scene boundary and shot transition detector with OpenCV and Python.
- [软件定义网络和 OpenFlow 协议](https://pycoders.com/link/2314/web)
  - REBECA SARAI
Explains a simple implementation of a switching hub using software defined networking with Python.
- [Python 3 在 Mozilla](https://pycoders.com/link/2304/web)
  - ANDREW HALBERSTADT
  - • Shared by Python Bytes FM
How far along has Mozilla come in the Python 3 migration?
(`是也乎:`
Mozilla 工程中有 3500+ Python 脚本,都是 Py2 的...
已经努力很久了, 但是, 目测还得一年才可能安全迁移到 Py3...
)
- [Python 中的非本地语句](https://pycoders.com/link/2289/web)
  - ABHILASH RAJ
  - • Shared by Abhilash Raj
- [什么是一些真正写得很好的开源Python项目?](https://pycoders.com/link/2292/web)
  - REDDIT
(`是也乎:`
好问题哪...
等等, 谁能定义一下什么是:`真的写的好?`
[The Architecture of Open Source Applications](http://aosabook.org/en/)
书中实锤过的好工程列表...
回答中 Django/Flask 直接开始 PK...好象都偏离了问题.
)
- [Scala 的 Case Class 在 Python 中的 Case Matching](https://pycoders.com/link/2310/web)
  - BRANKO BLAGOJEVIC
(`是也乎:`
那什么...
)
- [Qt for Python 的未来](https://pycoders.com/link/2306/web)
  - QT.IO
(`是也乎:`
Flutter/Eletron 外来了,也就没 Qt 什么事儿了.
)

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [dry-python: 用于可插拔业务的逻辑组件](https://pycoders.com/link/2302/web)
  - GITHUB.COM/DRY-PYTHON
- [pytest-mypy: Pytest 的 mypy 静态类型检查器插件](https://pycoders.com/link/2298/web)
  - PYPI.ORG
(`是也乎:`
嗯哼, 首次见 mypy 被这个领域进入哪...
看来, 大家等不了 Py 本番变得安全了...
)
- [flake8-mypy: Flake8 的插件集成 mypy](https://pycoders.com/link/2313/web)
  - PYPI.ORG
(`是也乎:`
嗯哼, 首次见 mypy 进入这种领域哪...
)
- [homer: 使您的文本更清晰,更简单,对读者更有用](https://pycoders.com/link/2307/web)
  - GITHUB.COM/WYOUNAS
- [starlark: 类似 Python 的配置语言](https://pycoders.com/link/2297/web)
  - GITHUB.COM/BAZELBUILD
(`是也乎:`
等等, 那为什么不直接用 Py 代码?
明白了, 又是安全问题...
)
- [sneklang: 用于安全评估的 Python 的实验受限子集](https://pycoders.com/link/2318/web)
  - GITHUB.COM/READEVALPRINT
(`是也乎:`
等等,叒一个安全? 到底大家撞上了什么, 都触发了不安全事件?
)
- [opendrop: Python 编写的 Apple AirDrop实现](https://pycoders.com/link/2309/web)
  - GITHUB.COM/SEEMOO-LAB
(`是也乎:`
NB , 非常需要, 刚需...
)
- [strictyaml: 类型安全的 YAML 解析器和验证器](https://pycoders.com/link/2305/web)
  - GITHUB.COM/CRDOCONNOR
- [memory-profiler: 监视 Python 程序的内存使用情况](https://pycoders.com/link/2324/web)
  - PYPI.ORG

  - • Shared by Mike Driscoll
(`是也乎:`
效果:
    Line #    Mem usage  Increment   Line Contents
    ==============================================

         3                           @profile
         4      5.97 MB    0.00 MB   def my_func():
         5     13.61 MB    7.64 MB       a = [1] *(10 **6)
         6    166.20 MB  152.59 MB       b = [2]* (2 * 10** 7)
         7     13.61 MB -152.59 MB       del b
         8     13.61 MB    0.00 MB       return a

其实...对大型项目没什么用哪...
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Kiwi PyCon X](https://pycoders.com/link/2287/web)
  - August 23 to August 26, 2019
  - NZ
- [⋅ IndyPy Web Conf 2019](https://pycoders.com/link/2284/web)
  - August 23 to August 24, 2019
  - 虚拟
  - 线上
- [⋅ Inland Empire Pyladies (CA, USA)](https://pycoders.com/link/2275/web)
  - August 26, 2019
(`是也乎:`
老爹盛赞过的活动...
)
- [⋅ Python Sheffield](https://pycoders.com/link/2276/web)
  - August 27, 2019
  - 英国
- [⋅ PyCon Latam 2019](https://pycoders.com/link/2282/web)
  - August 29 to September 1, 2019
  - MÉXICO

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [蟒营 Python 入门班](https://py.101.camp/)
  - 第2期
  - 101camp2py
进入 ch4, 下期 190901 左右发布.
本周准备上线 `写作入门班`
- [Chromium\+APISIX GDG珠海 MeetUp \| Meetup](https://www.meetup.com/Zhuhai-GDG/events/263962960/)
  - GDG 珠海
  - 极简汇率
- [What Can I Do With Python? – Real Python](https://realpython.com/what-can-i-do-with-python/)
  - FAQ
(`是也乎:`
![Do With Py](https://ipic.zoomquiet.top/2019-05-25-ScreenShot%202019-05-25%2010.27.25.jpg)
总是永远有人问这个问题...
当然, 这个问题任何一个技术社区都有人在问...
其实, 本质上并不是对应技术是否有什么能力,
而是相反...
)

### Jobs
>
> 必须 Pythonic 相关
...

# 是也乎

- 190821 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190821 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

> NN 3746
