---
title: "Issue 476"
summary: ""
date: "2021-06-09T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> WSL变成 Python 开发第一选择?
原文: [PyCoder's Weekly - Issue #476](https://pycoders.com/issues/476)
![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)

- 210609 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210609 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------

- [PEP 654: 例外组和 except*](https://pycoders.com/link/6498/web)
  - JOANNA JABLONSKI
Currently, Python’s exception handling mechanisms only allow you to focus on a single exception at a time. PEP 654, which is still in draft, aims to change that by adding to the Python language the concept of an exception group. Learn about this proposed feature in this article covering the discussion about exception groups from the 2021 Python Language Summit
- [70+ 面向初学者/中级和经验丰富的开发的 Python 项目](https://pycoders.com/link/6510/web)
  - INSANE
We don’t often include listicles in PyCoder’s Weekly, but this was just too good of a resource to pass up. If you’re looking for some Python projects to tackle, whether your a beginner looking to learn some new skills or an advanced developer researching implementation ideas, this list of over 70 Python projects has you covered.
(`是也乎:`
多数都是依赖外部网关键数据集/服务的案例,
对于中国学习者意义不大...
)
- [上下文管理器和 Python 的 with 语句](https://pycoders.com/link/6508/web)
  - REAL PYTHON
Context managers are a must-know Python language feature. In this step-by-step tutorial, you’ll learn what the Python with statement is and how to use it with existing context managers. You’ll also learn how to create your own context managers.
(`是也乎:`
![Context](http://ydlj.zoomquiet.top/ipic/2021-06-09-ScreenShot%202021-06-09%2011.47.33.jpg)
with -> async with
可堆叠的特性哪, 非常赞
)
- [PyCon US 2021 录制完成!](https://pycoders.com/link/6516/web)
  - PYCON.BLOGSPOT.COM
You can now watch all of the PyCon 2021 US videos on YouTube.
(`是也乎:`
![PyCon](http://ydlj.zoomquiet.top/ipic/2021-06-09-ScreenShot%202021-06-09%2012.07.16.jpg)
深夜连续剧, 已经第16季了...
)
- [CircuitPython 6.3.0 发布ed](https://pycoders.com/link/6524/web)
  - ADAFRUIT.COM
The third alpha release of the next major version 7.0.0 is also available.
(`是也乎:`
![CircuitPython](http://ydlj.zoomquiet.top/ipic/2021-06-09-ScreenShot%202021-06-09%2011.45.38.jpg)
比树莓派 还小巧的硬件平台
)
- [PyCharm 2021.2 EAP 已发动](https://pycoders.com/link/6509/web)
  - JETBRAINS.COM
Try out new features and provide feedback on the latest, unreleased version of PyCharm.

-----------------------------------------

## 探讨/吐糟
>
> Discussions

- [TIL 一直在令调试语句比人们需要的更难](https://pycoders.com/link/6519/web)
  - REDDIT
Python 3.8’s new f-string feature is a huge win for teaching and debugging!
(`是也乎:`
新的 f-string 是一次迟到了30年的重大调试体验增强;
革命群众们纷纷喜极而泣...

```
In [1]: example_variable = [1,2,3,4,5,6]
In [2]: print(f"{example_variable=}")
example_variable=[1, 2, 3, 4, 5, 6]
```

简单说 f-string 是一个 Python 版本的 LISP 列表计算展开器
)
-----------------------------------------

## 文章/教程/嗯哼
>
> Articles, Tutorials and Talks

- [Django Rest Framework 中的权限](https://pycoders.com/link/6523/web)
  - ŠPELA GIACOMELLI
  - • Shared by Špela Giacomelli
  - (aka GirlLovesToCode)
Django Rest Framework (DRF) is a powerful framework for creating RESTful APIs in Django. Permissions in DRF allow you to limit access to a resource to a subset of authenticated users. Learn how permissions work in DRF in this in-depth tutorial. You’ll learn about DRF’s built-in permission classes, as well as how to define your own custom permissions.
- [仅用 Anvil 基于 Python 创建 Web 应用程序](https://pycoders.com/link/6506/web)
  - REAL PYTHON
  - podcast
What if you could create an application and deploy it to the web with just Python? Wouldn’t it be nice to skip the additional full-stack development steps of learning three different languages in addition to Python? That’s the idea behind Anvil. This week on the Real Python Podcast, we have Meredydd Luff, co-founder of Anvil.
(`是也乎:`
![podcast](http://ydlj.zoomquiet.top/ipic/2021-06-09-ScreenShot%202021-06-09%2011.12.00.jpg)
刚刚在 PyCOn2021US 上发布的 Anvil;
叕一个 Heroku 或是 glitch
关键看市场反应了...
)
- [如何在 Django 中构建 Webhook 接收器](https://pycoders.com/link/6505/web)
  - ADAM JOHNSON
Webhooks are a common way to receive data in web applications. In this hands-on tutorial, you’ll learn how to build a webhook receiver in Django — with tests!. The article strictly covers receiving data and doesn’t touch on what to do with that data, since that would be application-dependent anyway.
- [Python 社区采访/ Sebastián Ramírez](https://pycoders.com/link/6496/web)
  - REAL PYTHON
Sebastián Ramírez is a software developer at Explosion AI and is the creator of the popular frameworks FastAPI and Typer. In this interview, we discuss typing in Python, his motivations for creating FastAPI and the future of the framework, and much more.
(`是也乎:`
![cc show](http://ydlj.zoomquiet.top/ipic/2021-06-09-ScreenShot%202021-06-09%2011.11.25.jpg)
)
- [2021: Windows 成为一流 Python 开发环境的一年](https://pycoders.com/link/6495/web)
  - CHRIS PATTI
  - opinion
Have you heard that Windows and Python don’t play nice together? Well, it might be time to think again! In this opinion piece, author Chris Patti explains why 2021 is finally the year that Windows offers a top-notch Python development environment.
- [Python 基础: 设置 Python](https://pycoders.com/link/6499/web)
  - REAL PYTHON
  - course
The first step to getting started with Python is to set it up on your machine. In this course, you’ll learn how to download Python for Windows, macOS, and Ubuntu Linux and how to open Python’s Integrated Development and Learning Environment, IDLE.
(`是也乎:`
其实也是最关键以及最难的一步
![Setting](http://ydlj.zoomquiet.top/ipic/2021-06-09-ScreenShot%202021-06-09%2011.09.17.jpg)
)

-----------------------------------------

## 好物/妙品/
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [Tkinter-Designer: 通过拖放创建漂亮的 Tkinter GUI](https://pycoders.com/link/6504/web)
  - GITHUB.COM/PARTHJADHAV
(`是也乎:`
![Designer](http://ydlj.zoomquiet.top/ipic/2021-06-09-ScreenShot%202021-06-09%2011.06.51.jpg)
Tk 也 fashion 起来了?
不过, 看起来就象 electron 的...
)
- [pyRTOS: 纯 Python 编写的 RTOS/专为 CircuitPython 使用而设计](https://pycoders.com/link/6512/web)
  - GITHUB.COM/RYBEC
(`是也乎:`
实时操作系统?
CircuitPython 专用?
)
- [full-stack-fastapi-postgresql: 全栈式现代 Web 应用程序生成器](https://pycoders.com/link/6518/web)
  - GITHUB.COM/TIANGOLO
(`是也乎:`
靠谱, 好用,
推荐过...
FastAPI 这据一组合几乎就替代了 Flask.
)
- [RapidFuzz: 在 Python 中用各种字符串度量快速进行模糊字符串匹配](https://pycoders.com/link/6502/web)
  - GITHUB.COM/MAXBACHMANN
- [fuzzywuzzy: Python 中的模糊字符串匹配](https://pycoders.com/link/6520/web)
  - GITHUB.COM/SEATGEEK
(`是也乎:`
放心, 不支持中文
)

-----------------------------------------

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6522/web)
  - June 9, 2020
(`是也乎:`
即便是线上的, 一样收费.
)
- [⋅ PyCon Namibia 2021](https://pycoders.com/link/6497/web)
  - June 18 to June 20, 2021
  - 非洲
- [⋅ EuroPython 2021 (Virtual)](https://pycoders.com/link/6184/web)
  - July 26 – August 1, 2021
- [⋅ PyCon India 2021](https://pycoders.com/link/6052/web)
  - September 17 – 20, 2021

-----------------------------------------

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [gruns/icecream: 🍦 Never use print() to debug again.](https://github.com/gruns/icecream)
  - github
(`是也乎:`
独创 logging + debug 模块
)
- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
  - 哔哩哔哩
(`是也乎:`
老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:
![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)
)
- [如何持证 \(SSL\) 开车 — 蟒营™ 怂怼录](https://blog.101.camp/ts/190130-jump-into-ssl/)
  - UPYUN
(`是也乎:`
私人初体验,
现在 http/https 资源混用浏览器越来越傲娇了,
最好有工具可以统一迁移...
)

-----------------------------------------

# PS

- 首发: [Issue 476 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-476.html)
- 修订: [issue-476.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-476.md)

-------------

好文笔,感叹号年度配额: **2/3**
投稿/反馈邮箱:
    <askdama@googlegroups.com>
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
>> NN 4390
![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28476fda9228.png?imageView2/2/w/476)
