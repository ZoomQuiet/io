---
title: "Issue 406"
summary: ""
date: "2020-02-05T10:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> 值得收藏的22个最常用 Python 模块
原文: [PyCoder's Weekly - Issue #406](https://pycoders.com/issues/406)
![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200205 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200205 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------

- [如何下架 Python 2 从而提升开发人员幸福感](https://pycoders.com/link/3512/web)
  - BARRY WARSAW
"Now that LinkedIn engineering has fully embraced Python 3, we no longer have to worry about supporting Python 2 and have seen our support loads decrease. We can now depend on the latest open source libraries and tools, and free ourselves from the constrictions of having to write bilingual Python."
(`是也乎:`
LinkedIn 的故事教导我们...
)
- [Python " != " 不是 " is not ": 对象对比在 Python](https://pycoders.com/link/3509/web)
  - REAL PYTHON
In this quick and practical tutorial, you'll learn when to use the Python is, is not, == and != operators. You'll see what these comparison operators do under the hood, dive into some quirks of object identity and interning, and define a custom class.
(`是也乎:`
![Comparing](http://ydlj.zoomquiet.top/ipic/2020-02-05-ScreenShot%202020-02-05%2010.38.18.jpg)
好可爱的插图, 油号不匹配真的会出大事儿的
)
- [适用 Python 的简洁代码概念](https://pycoders.com/link/3510/web)
  - RIGEL DI SCALA
"Software engineering principles, from Robert C. Martin's book Clean Code, adapted for Python. This is not a style guide. It's a guide to producing readable, reusable, and refactorable software in Python."
- [世界上 22 个最常用的Python软件包](https://pycoders.com/link/3496/web)
  - ERIK-JAN VAN BAAREN
"As a starting point, I took a list of the most downloaded Python packages on PyPI over the past 365 days. Let's dive in and find out what they do, how they're related, and why they rank so high!"
(`是也乎:`
最具价值的模块, 多数没收录在内建中:
Urllib3;
Six(2->3 自动兼容);
botocore, boto3, s3transfer, awscli (云厂商专用模块);
Pip;Python-dateutil;Requests;
S3transfer;Certifi(SSL 支持模块我);
Idna(民族文化);
PyYAML(越来越常用的);
Pyasn1;Docutils;Chardet;
RSA;
Jmespath(叕一个 JSON 支持);
Setuptools;Pytz;Futures;
Colorama;Simplejson;
都是百万级别的下载量...
)
- [2020 我将如何测试](https://pycoders.com/link/3500/web)
  - JAMES BENNETT
"Everything I'm currently doing for testing my personal [Python] projects, and the reasoning for why I do things the way I do." Interesting read if you're looking to optimize your testing setup.
(`是也乎:`
私人项目才玩的起高科技哪,
越是大项目, 越应该选择无聊的技术桟.
)
- [Django 安全笑柄发布: 3.0.3, 2.2.10, and 1.11.28](https://pycoders.com/link/3499/web)
  - DJANGOPROJECT.COM
Fixes CVE-2020-7471: Potential SQL injection via StringAgg(delimiter)
(`是也乎:`
Django 现在分裂为几个大产品线,是否正确, 还有待市场检验.
)
- [Pandas 1.0.0 新特性 (稳定版)](https://pycoders.com/link/3504/web)
  - PYDATA.ORG
(`是也乎:`
等了10多年的 1.0 版本
)

## 讨论
>
> Discussions

- [要求推迟对Python 3.10进行一些Python 3.9不兼容的更改](https://pycoders.com/link/3487/web)
  - PYTHON.ORG
(`是也乎:`
对历史兼容何时变的不是第一要求了?
)

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [Alpine Linux 能构建更大更慢的 Python Docker](https://pycoders.com/link/3515/web)
  - ITAMAR TURNER-TRAURING
"When you're choosing a base image for your Docker image, Alpine Linux is often recommended. [... ] But if you're using Python, Alpine Linux will quite often: Make your builds much slower. Make your images bigger. Waste your time." Related discussion on Hacker News.
(`是也乎:`
等等,这是 Alpine 的特性嘛? 只针对 Python?
)
- [Sets 在 Python](https://pycoders.com/link/3490/web)
  - REAL PYTHON
  - video
Learn how to work with Python's set data type. You'll see how to define set objects in Python and discover the operations that they support. By the end of this course, you'll have a good feel for when a set is an appropriate choice in your own programs.
(`是也乎:`
真蟒, 在有了流量后, 开始大力积累收费内容了...
)
- [用 Flask 蓝图设计应用程序](https://pycoders.com/link/3488/web)
  - REAL PYTHON
In this tutorial, you'll learn how to use a Flask Blueprint to help you structure your application by grouping its functionality into reusable components. You'll learn what Blueprints are, how they work, and how you can use them to organize your code.
(`是也乎:`
![Blueprint](http://ydlj.zoomquiet.top/ipic/2020-02-05-ScreenShot%202020-02-05%2010.29.47.jpg)
兰图是 Flask 对应用工程的思考成果,
可惜, 整个儿 Flask 的生产力被依赖的上游模块拖乱了,
导致 Django 赢得了一切.
)
- [Python 中的类型化函数依赖注入](https://pycoders.com/link/3489/web)
  - SOBOLEVN.ME
  - • Shared by Nikita Sobolev
"Dependency injection is a controversial topic. There are known problems, hacks, and even whole methodologies on how to work with DI frameworks. It is not the case when using a functional approach."
- [配置 uWSGI以 进行生产部署](https://pycoders.com/link/3513/web)
  - PETER SPERL
  - & BEN GREEN
  - (BLOOMBERG)
Tips about avoiding known gotchas when configuring uWSGI to host services at scale — while still providing a base level of defensiveness and high reliability.
(`是也乎:`
uWSGI 不错, 因为不可安装在 windows 中
)
- [用随机搜索算法在僵尸末日中生存](https://pycoders.com/link/3484/web)
  - OLEG ŻERO
"Pure python implementation of the random search optimization algorithm as an alternative to the standard gradient descent, given a very silly example."
(`是也乎:`
在 世界重启 那书中, 广泛的讨论了人类技术的可靠延续 ;-)
)
- [某位 Pythonista 对 Haskell 的评论](https://pycoders.com/link/3493/web)
  - YING WANG
(`是也乎:`
不是 王珢, 是另外一位在校学生, 之前推荐过这篇文章.
)
- [PyPy 简介](https://pycoders.com/link/3511/web)
  - ANDREW ODENDAAL
(`是也乎:`
很久没见 PyPy 相关的文章了...
)
- [用 Docker 构建 Python 数据科学 容器](https://pycoders.com/link/3508/web)
  - FAIZAN BASHIR
(`是也乎:`
其实, Anaconda 已经作的很好了
)
- [解决 Python,kdb+ 和 BigQuery 中的"最佳大小"问题](https://pycoders.com/link/3492/web)
  - FERENC BODON
  - • Shared by Ferenc Bodon

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [pytracking: 基于PyTorch的视觉跟踪库](https://pycoders.com/link/3485/web)
  - GITHUB.COM/VISIONML
(`是也乎:`
![atom_overview](https://github.com/visionml/pytracking/raw/master/pytracking/.figs/atom_overview.png)
叕一个追踪库, 只是基于 PyTorch, 不知道实时性如何
)
- [minibatch: 适用人类的 Python 流处理](https://pycoders.com/link/3502/web)
  - GITHUB.COM/OMEGAML
(`是也乎:`
for humans 是个好目标, 只是作到的非常少
)
- [inlinec: 用自定义编解码器在 Python 中编写内联 C 函数](https://pycoders.com/link/3516/web)
  - GITHUB.COM/GEORGEK42
(`是也乎:`
叕一种嵌入 C 代码的形式
)
- [express-your-self: 编写没有任何声明的Python](https://pycoders.com/link/3506/web)
  - GITHUB.COM/CHRISTIANSCOTT
(`是也乎:`
超越推导
)
- [hpy: 设计一个更好的 API 来扩展 C语言中给 Python](https://pycoders.com/link/3486/web)
  - GITHUB.COM/PYHANDLE
(`是也乎:`
H 就是 handle,
为 C 提供更好的 Python 接口,
这个思路很靠谱哪.
)
- [pandas-vet: 用以检验 Pandas 代码的 Flake8 插件](https://pycoders.com/link/3514/web)
  - GITHUB.COM/DEPPEN8
  - • Shared by Python Bytes FM
(`是也乎:`
Flake8 终于开始关注 Pandas 了
)
- [mquest: 乘法和除法问题生成器](https://pycoders.com/link/3507/web)
  - GITHUB.COM/JONATHANWILLITTS
  - • Shared by Jonathan Willitts
(`是也乎:`
经过400多期, 9年的积累, 现在 pycoders 周刊,越来越多主动分享的消息了
)
- [gif: 建立 Matplotlib Gif 动画的更好方法](https://pycoders.com/link/3491/web)
  - GITHUB.COM/MAXHUMBER
  - • Shared by Max Humber
(`是也乎:`
![gif](http://ydlj.zoomquiet.top/ipic/2020-02-05-ScreenShot%202020-02-05%2009.51.11.jpg)
叕一个 gif 动画制造工具, 嗯哼, 这 logo 非常亲切了
![tornado](https://raw.githubusercontent.com/maxhumber/gif/master/examples/tornado.gif)
使用也非常简单:
    import gif
    from matplotlib import pyplot as plt
    @gif.frame
    def plot(x, y):
        plt.figure(figsize=(5, 3), dpi=100)
        plt.scatter(x, y)
        plt.xlim((0, 100))
        plt.ylim((0, 100))
正常定义好一帧 plt 图片, 然后指定范围自动化生成就好, 比如:
    from random import randint
    frames = []
    for _in range(50):
        x = [randint(0, 100) for_ in range(10)]
        y = [randint(0, 100) for _ in range(10)]
        frame = plot(x, y)
        frames.append(frame)
)
- [pystencils: 加快您 NumPy 模板计算速度](https://pycoders.com/link/3503/web)
  - GITHUB.COM/MABAU
  - • Shared by Martin Bauer
(`是也乎:`
基于  sympy
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Python Miami](https://pycoders.com/link/3480/web)
  - February 8 to February 9, 2020
  - USA
- [⋅ DFW Pythoneers Teaching Meeting](https://pycoders.com/link/3472/web)
  - February 8, 2020
  - TX,USA
(`是也乎:`
Pythonner 才是正式的 Python 开发者族群名哪.
)
- [⋅ PyCascades 2020](https://pycoders.com/link/3471/web)
  - February 8 to February 10, 2020
  - 波兰
- [⋅ Edmonton Python User Group](https://pycoders.com/link/3474/web)
  - February 10, 2020
  - Canada
- [⋅ PiterPy Meetup](https://pycoders.com/link/3476/web)
  - February 11, 2020
  - ??
- [⋅ Leipzig Python User Group Meeting](https://pycoders.com/link/3473/web)
  - February 11, 2020
  - 德国
- [⋅ IndyPy Mixer](https://pycoders.com/link/3478/web)
  - February 11, 2020
  - IN,USA

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- **[蟒营 Python 入门班](https://py.101.camp/)**
  - 5py
  - 报名
(`(￣▽￣)`:
第五期已经开始报名:
    20.2.20 报名截止
    20.3.1  正式开课
    20.4.12 按时结束
)
- [2020 援助武汉](https://github.com/wuhan2020)
  - github.com/wuhan2020
(`是也乎:`
高速完成构建/发布/传播, 以及社区联合的开源项目,
数据不公开, 那就由人来采集再公开.
)

# 是也乎
>
> NN 3914

- 首发: [Issue 406 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-406.html)
- 修订: [issue-406.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-406.md)
