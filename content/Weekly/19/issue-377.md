---
title: "Issue 377"
summary: ""
date: "2019-07-17T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

原文: [PyCoder's Weekly - Issue #377](https://pycoders.com/issues/377)
![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)
------

- [用 Collaborative Filtering 构建推荐引擎](https://pycoders.com/link/2040/web)
  - REAL PYTHON
In this tutorial, you'll learn about collaborative filtering, which is one of the most common approaches for building recommender systems. You'll cover the various types of algorithms that fall under this category and see how to implement them in Python.
(`是也乎:`
![Recommendation](https://ipic.zoomquiet.top/2019-07-17-ScreenShot%202019-07-17%2010.24.38.jpg)
有公式原理分析的教程...
)
- [Python GIL GIL是否已被杀?](https://pycoders.com/link/2023/web)
  - ANTHONY SHAW
Thoughts on upcoming features in Python 3.8 and 3.9, like sub-interpreters, that will make writing high-performance concurrent programs that are CPU-bound more convenient.
(`是也乎:`
GIL 将被谋杀嘛?
)
- [The Python Celery Cookbook: 小工具,巨大的可能性](https://pycoders.com/link/2037/web)
  - VADYM ZAKOVINKO
"Everyone in the Python community has heard about Celery at least once, and maybe even already worked with it. Basically, it's a handy tool that helps run postponed or dedicated code in a separate process or even on a separate computer or server. This saves time and effort on many levels."
(`是也乎:`
又见 芹菜...
)
- [在 Python 3 中将列表转换为集合的速度更快: set() or {*}](https://pycoders.com/link/2034/web)
  - MICHAEL BASSILI
Perhaps surprisingly, there is a performance difference between the two. Read Michael's article to find out why using a {*} set literal is faster.
- [用 Keras 和深度学习进行视频分类](https://pycoders.com/link/2029/web)
  - ADRIAN ROSEBROCK
In this tutorial, you will learn how to perform video classification using Keras, Python, and Deep Learning.
(`是也乎:`
pyimagesearch.com
是位非常厉害的光头程序猿, 一己之立写书/设计课程,完成原创模块,
四处演讲/咨询....
专注 CV
)

## 讨论
>
> Discussions

- [对于抽象基类,注册是继承的替代方法](https://pycoders.com/link/2024/web)
  - RAYMOND HETTINGER
- [Pythonista 用 Tkinter 编写餐厅 POS 系统](https://pycoders.com/link/2039/web)
  - REDDIT
(`是也乎:`
没毛病哪, NASA 都用了那么多年 Tk,
如果对颜值没要求,而是对响应/稳定/简洁有要求,
Tk 才是第一选择了...
)

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [如何写循环才够 Pythonic](https://pycoders.com/link/2042/web)
  - REAL PYTHON
  - video
In this course, you'll see how you can make your loops more Pythonic if you're coming to Python from a C-style language. You'll learn how you can get the most out of using range(), xrange(), and enumerate(). You'll also see how you can avoid having to keep track of loop indexes manually.
- [Black 简介,不妥协的Python代码格式化程序](https://pycoders.com/link/2041/web)
  - MIKE DRISCOLL
Black is a Python code formatter. It will reformat your entire file in place according to the Black code style, which is pretty close to PEP8. This article shows you the basics of working with Black.
(`是也乎:`
虽然想不妥协, 但是, 和 gofmt 不同,
所有 Python 代码格式器,
都难以作到真正的智能联动...
)
- [Python 消耗大量内存或如何减少对象的大小?](https://pycoders.com/link/2035/web)
  - HABR.COM
An overview of some methods for reducing the size of objects, which can significantly reduce the amount of RAM needed for pure Python programs.
- [用 Python 和 Tor 作为代理避免 Webscraping 限制](https://pycoders.com/link/2033/web)
  - JAMES RUSSO
This post describes how to use Python based web scraping tools and Tor to hide yourself when scraping websites for data.
(`是也乎:`
发现 Tor 才是终极爬虫平台...
可惜在中国已经不存在了...
)
- [接口是永恒的](https://pycoders.com/link/2026/web)
  - MOSHE ZADKA
"When publishing interfaces, one must be careful: to a first approximation, they are forever."
(`是也乎:`
永生的 Interfaces
)
- [Python Web Servers 的自适应进程和内存管理](https://pycoders.com/link/2044/web)
  - INSTAGRAM-ENGINEERING.COM
- [Python Is Eating the World](https://pycoders.com/link/2032/web)
  - ZDNET.COM
(`是也乎:`
大蟒在吞食世界...
早年 Python 发展回顾, 现在
帮助Netflix将视频流传输到全球超过1亿个家庭,为照片共享现象Instagram提供动力,并帮助NASA进行太空探索...
但是, 网络中针对无基础学习者提供的 Python 课程,
多数只是针对 Python 本身, 而对 Python 积累的庞大生态视而不见,

> 蟒营
>> 伴你重新享受自学的乐趣
>>
>> **101camp**
>>
报名入口: [蟒营 Python 入门班](https://py.101.camp/)
)

- [Spiking Neural Network (SNN) With PyTorch](https://pycoders.com/link/2025/web)
  - GUILLAUME CHEVALIER
- [The Programmer Mindset: 主调试循环](https://pycoders.com/link/2031/web)
  - DROPBOX.COM

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [grizzly: 跨平台浏览器模糊测试框架](https://pycoders.com/link/2038/web)
  - GITHUB.COM/MOZILLASECURITY
- [sherlock: 在社交网络中查找用户名](https://pycoders.com/link/2043/web)
  - GITHUB.COM/SHERLOCK-PROJECT
(`是也乎:`
华生 都不够用了...
![sherlock](https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png)
)
- [bistring: Python Library for Non-Destructive Text Processing](https://pycoders.com/link/2028/web)
  - GITHUB.COM/MICROSOFT
(`是也乎:`
    >>> from bistring import bistr
    >>> s = bistr('𝕿𝖍𝖊 𝖖𝖚𝖎𝖈𝖐, 𝖇𝖗𝖔𝖜𝖓 🦊 𝖏𝖚𝖒𝖕𝖘 𝖔𝖛𝖊𝖗 𝖙𝖍𝖊 𝖑𝖆𝖟𝖞 🐶')
    >>> s = s.normalize('NFKD')     # Unicode normalization
    >>> s = s.casefold()            # Case-insensitivity
    >>> s = s.replace('🦊', 'fox')  # Replace emoji with text
    >>> s = s.replace('🐶', 'dog')
    >>> s = s.sub(r'[^\w\s]+', '')  # Strip everything but letters and spaces
    >>> s = s[:19]                  # Extract a substring
    >>> s.modified                  # The modified substring, after changes
    'the quick brown fox'
    >>> s.original                  # The original substring, before changes
    '𝕿𝖍𝖊 𝖖𝖚𝖎𝖈𝖐, 𝖇𝖗𝖔𝖜𝖓 🦊'
更加狂野的字串处理模块
)
- [Coinsta: 加密货币的历史和当前数据](https://pycoders.com/link/2036/web)
  - GITHUB.COM/PYDATABLOG
  - • Shared by Bernard Brenyah
- [Pyret: 专为学习而设计的编程语言,受Python启发](https://pycoders.com/link/2030/web)
  - PYRET.ORG
(`是也乎:`
![Pyret](https://camo.githubusercontent.com/d45f1457534ff10c255de8b6dbbfb1946d952800/68747470733a2f2f7261772e6769746875622e636f6d2f62726f776e706c742f70797265742d6c616e672f6d61737465722f696d672f70797265742d62616e6e65722e706e67)
叕一门全新编程语言...
node 实现, .arr 为后缀...
)
- [expressPython: 一个小型 Python 3 编辑器](https://pycoders.com/link/2027/web)
  - GITHUB.COM/JADOGG
(`是也乎:`
![expressPython](https://camo.githubusercontent.com/99b27ef0c06a498f971f7296928a0d46172d6e50/68747470733a2f2f69312e77702e636f6d2f70616e646162756e6e79746563682e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031372f30392f646963745f636f756e745f63686172732e676966)
竞技用编辑器?
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyData Bristol Meetup](https://pycoders.com/link/2012/web)
  - July 18, 2019
  - 英国
- [⋅ PyLadies Dublin](https://pycoders.com/link/2016/web)
  - July 18, 2019
  - Ireland
- [⋅ MadPUG](https://pycoders.com/link/2005/web)
  - July 18, 2019
- [⋅ Karlsruhe Python User Group (KaPy)](https://pycoders.com/link/2011/web)
  - July 19, 2019
  - 德国
- [⋅ Chattanooga Python User Group](https://pycoders.com/link/2006/web)
  - July 19, 2019
  - 查塔努加
  - USA.田纳西州
- [⋅ BangPypers](https://pycoders.com/link/2015/web)
  - July 20, 2019
  - Bangalore
  - 印度

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [蟒营 Python 入门班](https://py.101.camp/)
  - 第2期
  - 101camp2py

> 开始报名,
> 190725截止, 最后7天
>
> 课程: 0728~0908
<a href="https://pyscaffold.org">
    <img src="https://pyscaffold.org/en/latest/_images/logo.png" alt="logo"
 width="200"/>
</a>
~ helps you setup a new Python project

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

- [Wangjunyu/MemectRecruitment: 文因招聘](https://github.com/Wangjunyu/MemectRecruitment)
  - 北京
  - anti-996

# 是也乎

- 190710 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190710 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
