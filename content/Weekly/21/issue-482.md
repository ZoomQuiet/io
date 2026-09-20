Title: Issue 482
Slug: issue-482
Date: 2021-07-21 16:42
Tags: Weekly,Python,pycoders,ZH


> Python 3.11 新功能


原文: [PyCoder's Weekly - Issue #482](https://pycoders.com/issues/482)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210721 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210721 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [用Fastapi构建Python Web APIs](https://pycoders.com/link/6705/web)
    + REAL PYTHON

In this guide, written by FastAPI creator Sebastián Ramírez, you’ll learn the main concepts of FastAPI and how to use it to quickly create web APIs that implement best practices by default. By the end of it, you will be able to start creating production-ready web APIs.


(`是也乎:`

![FastAPI](http://ydlj.zoomquiet.top/ipic/2021-07-21-ScreenShot%202021-07-21%2016.56.12.jpg)

)


- [幕后/ Python导入系统的工作原理](https://pycoders.com/link/6723/web)
    + VICTOR SKVORTSOV

Importing a Python module is probably one of the most used language features. But Python’s import system remains a mystery to many Python developers, even folks with years of experience. This in-depth article explores how the import system works from the top down. You’ll learn everything from the difference is between absolute and relative imports to how Python searches for modules and packages and resolves naming conflicts.



- [全职 CPYTHON 开发商周报](https://pycoders.com/link/6722/web)
    + ŁUKASZ LANGA

After years of fundraising efforts, the Python Software Foundation finally hired their first CPython Developer-In-Residence. Łukasz Langa reports on what he accomplished during his first week on the job, how he’s finding a balance between the various tasks required of him, and what his plans are for next week. He’s included a full detailed log of everything accomplished with links to GitHub issues and pull requests.


(`是也乎:`

`Ł` <- 怎么念? 7 ?


)


- [Python 3.11 新功能](https://pycoders.com/link/6707/web)
    + PYTHON.ORG

Python 3.10 is still in beta, but work on Python 3.11 has already begun. Big changes include some major improvements to tracebacks as well as a new cube root function in the math module.

(`是也乎:`

嗯哼, 先用 Py3.11 重写 PyPI ?

)



- [Coverage 6.0 Beta 1 发布](https://pycoders.com/link/6720/web)
    + NED BATCHELDER

-----------------------------------------
## 探讨/吐糟
> Discussions


- [NumPyic 方法对 NDARRAY 进行顺时针排序](https://pycoders.com/link/6717/web)
    + STACK OVERFLOW

There might not be too many applications for this, but the accepted solution to this Stack Overflow question is pretty slick and features a NumPy array method that you might have glossed over: .rot90().


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [用 python 进行语音识别](https://pycoders.com/link/6710/web)
    + REAL PYTHON 
    + course

In this course, you’ll cover the fundamentals of speech recognition with Python. You’ll learn which speech recognition library gives the best results and build a full-featured “Guess The Word” game with it.


(`是也乎:`


![Recognition](http://ydlj.zoomquiet.top/ipic/2021-07-21-ScreenShot%202021-07-21%2016.36.11.jpg)



)


- [地图与Django/ Geodjango，Postgis和传单](https://pycoders.com/link/6715/web)
    + PAULO MELCHIORRE

This quickstart guide shows you how to create a web map using Django’s GeoDjango module. Data for the map is stored in a PostgreSQL database using the PostGIS extension, and Leaflet, a lightweight JavaScript library for interactive maps, is used on the front-end. You’ll not only learn how to set up the Django application and display the map but also add markers to the map and automatically center the map on the application user’s location.



- [Python 语言峰会上规划未来必须更快](https://pycoders.com/link/6724/web)
    + REAL PYTHON 
    + podcast

Do you wonder what the future may hold for the Python language? Are there speed improvements coming soon? What if you could be in the room while the core developers discuss Python’s future? This week on the podcast, we have Joanna Jablonski, who was invited to the Python Language Summit 2021 as a journalist to summarize and document the event.


(`是也乎:`

![Faster](http://ydlj.zoomquiet.top/ipic/2021-07-21-ScreenShot%202021-07-21%2016.33.52.jpg)


)


- [了解django/弄清楚 Settings](https://pycoders.com/link/6721/web)
    + MATT LAYMAN 
    + • Shared by Matt Layman

All Django apps need to be configured in order to run properly. This article walks you through how the Django settings file works and how it is organized. You’ll learn about environment variables and how to use them in your settings. You’ll also see some patterns for dealing with settings in different environments, such as development, testing, and production, as well as some tools for monitoring and managing Django settings.


(`是也乎:`

Settings 虽好,
不可贪杯...

)



- [Python 社区采访/ Dustin Ingram](https://pycoders.com/link/6729/web)   
    + REAL PYTHON
Dustin Ingram is a developer advocate at Google, a director of the PSF, and a maintainer of PyPI. In this interview, Dustin talks about how Google’s use of Python might differ from your own, maintaining PyPI, his love of PyCons and cooking, and more.


(`是也乎:`

![Community](http://ydlj.zoomquiet.top/ipic/2021-07-21-ScreenShot%202021-07-21%2016.33.10.jpg)

)


- [无服务器 django apis 与 aws lambda 和 zappa](https://pycoders.com/link/6709/web)
    + JEKAYINOLUWA OLABEMIWO 
    + • Shared by Robertino

Hosting serverless apps on AWS can be a lot of work if you set everything up manually. The Zappa project makes configuring and deploying a serverless app on AWS Lambda a cinch! This tutorial walks you through creating a Django REST API and deploying it to AWS Lambda with Zappa step-by-step. You’ll even learn how to set up authentication using Auth0!


(`是也乎:`

叕见 Zappa,
这真心是个良心服务, 等于是接口的接口...
将各种流行服务都封装为 IFTTT 的触发器,
可以堆叠,
当然, 受到 Yahoo 已死的 pipline 启发.

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code

- [manim: 社区维护的Python框架，用于创建数学动画](https://pycoders.com/link/6714/web)
    + GITHUB.COM/MANIMCOMMUNITY

(`是也乎:`

Mathematical 制作动画是专业的...

)


- [auto-all: 在Python模块中自动管理 __all__ 变量](https://pycoders.com/link/6711/web)
    + GITHUB.COM/JONGRACECOX

(`是也乎:`

类似自动化感知并编排刷新模块依赖的模块越来越多...
其实, 不如学习 rust/golang 在编译时自动指出.

)


- [pdfme: 轻松制作 PDF](https://pycoders.com/link/6708/web)
    + GITHUB.COM/AFELIPESP




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6728/web)
    + July 21, 2021

- [⋅ EuroPython 2021 (Virtual)](https://pycoders.com/link/6184/web)
    + July 26 – August 1, 2021

- [⋅ PyCon India 2021](https://pycoders.com/link/6052/web)
    + September 17 – 20, 2021



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


- [gruns/icecream: 🍦 Never use print() to debug again.](https://github.com/gruns/icecream)
    + github

(`是也乎:`

独创 logging + debug 模块

)


- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)

- [如何持证 \(SSL\) 开车 — 蟒营™ 怂怼录](https://blog.101.camp/ts/190130-jump-into-ssl/)
    + UPYUN

(`是也乎:`

私人初体验,
现在 http/https 资源混用浏览器越来越傲娇了,
最好有工具可以统一迁移...

)

-----------------------------------------
# PS:

- 首发: [Issue 482 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-482.html)
- 修订: [issue-482.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-482.md)


-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):



```python

私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开课程: 蟒营 (订阅号: Mainium)
历史吐糟: Chaos42 (订阅号 PythoniCamp)

as 创始组织者:
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        TFUG珠海 (订阅号: ZH_TFUG)
```

-------------





