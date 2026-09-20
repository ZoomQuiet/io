Title: Issue 480
Slug: issue-480
Date: 2021-07-07 11:42
Tags: Weekly,Python,pycoders,ZH


> 如何在 Python 中处理 JWT


原文: [PyCoder's Weekly - Issue #480](https://pycoders.com/issues/480)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210707 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210707 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [Python 的类型类](https://pycoders.com/link/6650/web)
    + NIKITA SOBOLEV 
    + • Shared by Nikita Sobolev

Sometimes you need to change the behavior of a function based on the type of argument passed to it. This is a classic example of polymorphism in programming. In this article, you’ll learn how this is typically done in Python, compare that to polymorphism in other languages, and see how the new classes library can make the whole process easier.

- [Django REST 框架中/自定义权限类](https://pycoders.com/link/6649/web)
    + TESTDRIVEN.IO 
    + • Shared by Špela Giacomelli 
    + (aka GirlLovesToCode)

One of the great things about Django REST Framework (DRF) is how easy it is to be productive with the built-in API views and permission classes. But sometimes you need a bit more control than the built-in objects allow. This article walks you through how to create and use custom permission classes in DRF so that you can have complete control over how permissions work in your REST API.


(`是也乎:`

这种想绕过框架的尝试,
多数都没能坚持多久...

)


- [Monitor Your Python Applications’ Performance in Real Time with Datadog APM](https://pycoders.com/link/6633/web)
    + DATADOG
    + sponsor

Pinpoint hard-to-reproduce problems in your production code without affecting your app’s performance with Datadog’s Continuous Profiler. Locate which functions (or lines of code) consume the most resources, such as CPU and memory and optimize for a better app experience. [Try Datadog APM free →](https://pycoders.com/link/6633/web)

- [Python 计数器: Pythonic 方式计数对象 ](https://pycoders.com/link/6657/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn how to use Python’s Counter to count several repeated objects at once. You’ll also learn how to use Counter objects to enhance other computations that you do in Python.


- [Django Security 发布: 3.2.5 and 3.1.13](https://pycoders.com/link/6663/web)
    + DJANGO SOFTWARE FOUNDATION



-----------------------------------------
## 探讨/吐糟
> Discussions



- [为毛 is a, b = b, a 并不总是等价于 b, a = a, b ?](https://pycoders.com/link/6658/web)
    + STACK OVERFLOW

In Python you can swap the values of two variables without creating a temporary variable. So, if you have two variables a = 1 and b = 2, you can swap their values using a, b = b, a. Now a has the value 2 and b has the value 1. So shouldn’t b, a = a, b do the same thing? In most cases, it will, but one user on Stack Overflow found an instance where they don’t, and the explanation gets into the nitty-gritty about how assignments are evaluated.

(`是也乎:`


因为...所以...

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [用 SQLAlchemy 贯通 Python 和 PostgreSQL 枚举](https://pycoders.com/link/6643/web)
    + BRENDAN LE

An Enumlets you restrict variables to a set of constants. You can use them to map values that would typically be strings to integer constants, which helps reduce human error due to misspellings. SQLAlchemy also supports enums for use with your database layer. This article shows you how to generate an SQLAlchemy enum from a Python Enum instance so that your data can live in a single place and be shared between the Python and database layers of your application.


(`是也乎:`

反正连 DB 用 SQLAlchemy 没问题

)


- [用 Papermill 参数化和自动化 Jupyter Notebook](https://pycoders.com/link/6639/web)
    + MATT WRIGHT

Jupyter Notebooks are a great way to create reproducible experiments and data analysis, but sometimes you want to alter parameters used in the notebook to see how the results change. One way to do that is with the papermill package. Using papermill, you can execute a notebook with new parameters straight from the command line.



- [用 Dustin Ingram 保护您的 Python 软件供应链](https://pycoders.com/link/6652/web)
    + REAL PYTHON 
    + podcast

How well do you know your software supply chain? When you PIP install a package, what steps can you take to minimize the risk of installing something malicious? This week on the Real Python Podcast, we have Dustin Ingram, a director of the Python Software Foundation (PSF) and a maintainer of the Python Package Index (PyPI).


(`是也乎:`


![Securing](http://ydlj.zoomquiet.top/ipic/2021-07-07-ScreenShot%202021-07-07%2010.57.52.jpg)
)


- [如何在 Python 中处理 JWT](https://pycoders.com/link/6644/web)
    + JESSICA TEMPORAL 
    + • Shared by Robertino

JavaScript Web Tokens (JWTs) are used to store information about web users. They are compact and can be used to authorize users in APIs. In this article and how to create and verify them in Python using the PyJWT package.



- [定义和调用 Python 函式](https://pycoders.com/link/6665/web)
    + REAL PYTHON 
    + course

In this course, you’ll learn how to define and call your own Python function. You’ll also learn about passing data to your function and returning data from your function back to its calling environment.

(`是也乎:`

唉嘛, 这个忒基础了,
也最不容易说清楚...

![Defining](http://ydlj.zoomquiet.top/ipic/2021-07-07-ScreenShot%202021-07-07%2010.55.55.jpg)

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [calibre: Calibre 电子书管理器/官方源代码库](https://pycoders.com/link/6662/web)
    + GITHUB.COM/KOVIDGOYAL

(`是也乎:`

来了, 来了,
官方库咯...

)


- [luigi: 帮助您构建批处理作业/复杂管道的 Python 模块](https://pycoders.com/link/6642/web)
    + GITHUB.COM/SPOTIFY




- [interactive-coding-challenges: 120 多个使用 Anki 抽认卡的交互式 Python 编码面试挑战](https://pycoders.com/link/6653/web)
    + GITHUB.COM/DONNEMARTIN

(`是也乎:`

叕一个面试题库...
讲真, 面试时最想看出来的不是技术实力,
而是: 是否能长期共事.

)



- [saleor: 模块化/高性能/无头 电子商务平台](https://pycoders.com/link/6647/web)
    + GITHUB.COM/MIRUMEE


(`是也乎:`

![saleor](http://ydlj.zoomquiet.top/ipic/2021-07-07-ScreenShot%202021-07-07%2011.20.05.jpg)

GraphQL 为先.
支持一键上 Heroku;

![saleor](http://ydlj.zoomquiet.top/ipic/2021-07-07-ScreenShot%202021-07-07%2011.21.10.jpg)

)


- [plotext: 在终端中绘制图表](https://pycoders.com/link/6660/web)
    + GITHUB.COM/PICCOLOMO


(`是也乎:`

CLI 其实是非常通用友好的界面,
也叫 CUI,
本质是 `TUI`/文本用户界面

![plotext](http://ydlj.zoomquiet.top/ipic/2021-07-07-ScreenShot%202021-07-07%2010.49.59.jpg)

可以在终端中直接输出图表,
也就意味着可以输出到 markdown 中;
直接.

)


- [pyjwt: Python 中的 JSON Web 令牌实现](https://pycoders.com/link/6648/web)
    + GITHUB.COM/JPADILLA

(`是也乎:`

JWT 非常流行的一种安全接口约定,
看名字还以为是 JAVA 世界溢出的,
其实只是 JSON 为主体而已

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6661/web)
    + July 6, 2021

- [⋅ PyHEP 2021](https://pycoders.com/link/6627/web)
    + July 5 – 10, 2021

- [⋅ PyBirras 2021 (Virtual)](https://pycoders.com/link/6587/web)
    + July 8, 2021

- [⋅ SciPy 2021 (Virtual)](https://pycoders.com/link/6656/web)
    + July 12 to July 19, 2021

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

- 首发: [Issue 480 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-480.html)
- 修订: [issue-480.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-480.md)


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





