---
title: "Issue 474"
summary: ""
date: "2021-05-26T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> 单女生/硬件公司的工具和技术
原文: [PyCoder's Weekly - Issue #474](https://pycoders.com/issues/474)
![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)

- 210526 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210526 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------

- [用来经营单身硬件公司的工具和技术](https://pycoders.com/link/6362/web)
  - STARGIRL FLOWERS
Winterbloom makes open-source, boutique synthesizers. There’s a lot that goes into running a hardware company. Someone has to design the hardware, code the firmware, write the documentation, not to mention administrate the company. Winterbloom does all of this with just one engineer — Stargirl Flowers. Learn what tools and tech Stargirl uses to run her company, and how Python fits into the big picture in more ways than one.
(`是也乎:`
`One-Woman`
一直是亮点...
)
- [咩是 WSGI? 为毛在 Django 项目需要 Gunicorn 和 Nginx?](https://pycoders.com/link/6384/web)
  - DENIS OREHOVSKY
  - • Shared by Denis
Django is one of the most popular Python web frameworks. But you can’t run a web application with Django alone. You need a host of other tools in place to deploy a Django project, from a server to run your application to a server to handle incoming requests. In this article, you’ll learn about Gunicorn and Nginx and how they work together with Django to deliver a web application to your users.
(`是也乎:`
老梗,
可其实可以用其它协议跑的
)
- [用 Django/Vue 和 GraphQL 建立博客](https://pycoders.com/link/6357/web)
  - REAL PYTHON
In this step-by-step project, you’ll build a blog from the ground up. You’ll turn your Django blog data models into a GraphQL API and consume it in a Vue application for users to read. You’ll end up with an admin site and a user-facing site you can continue to refine for your own use.
(`是也乎:`
还是 Pelican 更加轻便吧,
不占用在线计算资源的才是好 blog 系统
)
- [在6月12日前帮 PSF 筹集 80,000 美元](https://pycoders.com/link/6352/web)
  - TWITTER.COM/THEPSF
- [PyPy v7.3.5: Python 2.7 and 3.7 错误修正版本](https://pycoders.com/link/6388/web)
  - PYPY.ORG
(`是也乎:`
随着老爹的 flag 竖立起来,
以往各种以性能为目标的社区,
立即被打了鳮血...
)

-----------------------------------------

## 探讨/吐糟
>
> Discussions

- [可以动态计算传递给一个函数的位置参数能有多少?](https://pycoders.com/link/6379/web)
  - STACK OVERFLOW
While you might not find yourself with a need to count the number of positional arguments to a function very often, the answers to this Stack Overflow question contain a lot of interesting Python language features that you might not be aware of.
(`是也乎:`
如果不加以控制,
随时可能突破42个...
)
- [Python 必须学习的库有什么?](https://pycoders.com/link/6387/web)
  - REDDIT
Lots of standard library and third-party modules and packages get a shout-out in this Reddit thread. What would you pick as the top libraries a new Pythonista should learn once they’ve got a good grasp on the basics of the language?
(`是也乎:`
其实吧, 内建的都值得学习,
而 os 开头的是必须掌握的
)

-----------------------------------------

## 文章/教程/嗯哼
>
> Articles, Tutorials and Talks

- [了解 Django: 每个会话的每位访问者数据](https://pycoders.com/link/6380/web)
  - MATT LAYMAN
  - • Shared by Matt Layman
How does Django know when a user is logged in?  Where can the framework store data for a visitor on your app?  In the next installment of his Understand Django series, Matt Layman answers those questions and looks at a storage concept in Django called sessions.
- [如何建立 Django 项目](https://pycoders.com/link/6389/web)
  - REAL PYTHON
  - course
In this course, you’ll learn the necessary steps you’ll need to take to set up a new Django project. You’ll learn the basic setup for any new Django project that needs to happen before programming the specific functionality of your project.
(`是也乎:`
![Django](http://ydlj.zoomquiet.top/ipic/2021-05-26-ScreenShot%202021-05-26%2011.18.22.jpg)
官方没及时给出脚手架指令的话,
是根本想象不出用户能有多野的...
)
- [扩展数据科学和像 Netflix 这样的机器学习基础设施](https://pycoders.com/link/6364/web)
  - REAL PYTHON
  - podcast
Would you move your data science project from a laptop to the cloud? Would you also like to have snapshots of your project saved along the way so that you can go back in time or share the state of your project with another team member? This week on the Real Python Podcast, listen to Savin Goyal, the technical lead for machine learning infrastructure at Netflix, talk about Metaflow, an open-source tool to simplify building, managing, and scaling data science projects.
(`是也乎:`
![podcast](http://ydlj.zoomquiet.top/ipic/2021-05-26-ScreenShot%202021-05-26%2011.16.49.jpg)
)
- [为何愁眉苦脸?](https://pycoders.com/link/6394/web)
  - ŁUKASZ LANGA
The [Black](https://black.readthedocs.io/en/stable/) autoformatter adopts some conventions that might surprise you the first time you use it. One of those conventions — the “sadface dedent” — moves closing parentheses in function signatures and other block headers to their own lines. This creates a line containing nothing but ):, which looks like a sad face emoji. Łukasz Langa, Black’s creator, explains why Black does this.
(`是也乎:`
![:(](http://ydlj.zoomquiet.top/ipic/2021-05-26-ScreenShot%202021-05-26%2011.15.39.jpg)
作者的颜文字理由...
)
- [用 Postgres/Gunicorn 和 Traefik 对 Django 进行 Docker 化](https://pycoders.com/link/6363/web)
  - AMAL SHAJI
  - • Shared by Amal Shaji
Learn how to configure Django to run on Docker. You’ll see how to set up Django with a Postgres database, run your application with Gunicorn, and handle incoming requests with Traefik, which is an Nginx alternative for microservices. You’ll also learn how to manage TLS certificates in production using Let’s Encrypt.
(`是也乎:`
无论 Docker 镜像仓库有多少相似的,
还是亲手构建一个来的安心,
谁也不知道公开的 image 中包含了什么东西
)
- [澄清 async 和 await](https://pycoders.com/link/6361/web)
  - BRETT CANNON
In the latest article in his Syntactic Sugar series, Python steering council member Brett Cannon explains how the async and await keywords work and how they evolved from earlier language constructs.
- [用 Python 和 PyQt 构建批量文件重命名工具](https://pycoders.com/link/6378/web)
  - REAL PYTHON
In this step-by-step project, you’ll build a bulk file rename tool using Python and pathlib to manage the file renaming process and PyQt to provide the application’s GUI.
(`是也乎:`
![Qt](http://ydlj.zoomquiet.top/ipic/2021-05-26-ScreenShot%202021-05-26%2011.02.49.jpg)
)

-----------------------------------------

## 好物/妙品/
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [recommenders: 推荐系统的最佳实践](https://pycoders.com/link/6353/web)
  - GITHUB.COM/MICROSOFT
(`是也乎:`
以往中文网站的推荐系统还有点儿特殊性,
现在终于可以国际通用了...
感谢那些一直在进行全球统一用户训练的顶部 app 们;
所以,
这是 microsoft 的开源贡献之一
)
- [dagster: 用于机器学习/分析和 ETL 的数据协调器](https://pycoders.com/link/6354/web)
  - GITHUB.COM/DAGSTER-IO
- [sqlfluff: 适用于人类的 SQL Linter 和自动格式化程序](https://pycoders.com/link/6395/web)
  - GITHUB.COM/SQLFLUFF
(`是也乎:`
原先这都是各种 数据库客户端 内置的,
现在有通用 Python 版本的了
)
- [sh: 适用于Python 2.6/PyPy 和 PyPy3 的完整子进程替换](https://pycoders.com/link/6382/web)
  - GITHUB.COM/AMOFFAT
(`是也乎:`
![sh](http://ydlj.zoomquiet.top/ipic/2021-05-26-ScreenShot%202021-05-26%2010.58.31.jpg)
这个项目名满分哪...
)
- [vim-clutch: 用 Raspberry Pi Zero W 将按键发送到 Vim](https://pycoders.com/link/6393/web)
  - GITHUB.COM/L00SED

-----------------------------------------

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6399/web)
  - April 28, 2020
(`是也乎:`
即便是线上的, 一样收费.
)
- [⋅ Conf42 Python 2021](https://pycoders.com/link/6322/web)
  - May 27 to May 28, 2021
(`是也乎:`
这个大会关心的事儿比较大.
)
- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
  - June 2 – 6, 2021
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

- 首发: [Issue 474 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-474.html)
- 修订: [issue-474.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-474.md)

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
![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/474)
