---
title: "蠎周刊(PyCoder)594"
summary: ""
date: "2023-09-13T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> 为什么更喜欢缩进而不是块标记？
原文: [PyCoder's Weekly - Issue #594](https://pycoders.com/issues/594)
![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)

- 230913 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230913 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------

- [在 Python 中使用遗传算法](https://pycoders.com/link/11421/web)
  - JOSEP RUBIÓ PIQUÉ
A Genetic Algorithm (GA) is an AI technique where random code is mutated and tested for fitness iteratively until a solution is found. This article shows you a couple of problems solved using GAs in Python. Associated HN discussion.
- [用Python生成漂亮的二维码](https://pycoders.com/link/11437/web)
  - REAL PYTHON
In this tutorial, you’ll learn how to use Python to generate QR codes, from your standard black-and-white QR codes to beautiful ones with your favorite colors. You’ll learn how to format QR codes, rotate them, and even replace the static background with moving images.
(`是也乎:`
![QR](https://ipic.zoomquiet.top/2023-09-13-zshot%202023-09-13%2016.21.43.jpg)
能上 gif 动态背景的呢...
)
- [我是 Null 先生。我的名字让计算机看不到我](https://pycoders.com/link/11422/web)
  - CHRISTOHPER NULL
NULL is a magic word in many computer languages. This article is by someone who has Null as a last name, and the consequences that entails. See also this Radiolab Podcast Episode for a similar topic.
(`是也乎:`
真的有人叫这个姓...
)
- [2023 年 Django 开发者调查](https://pycoders.com/link/11407/web)
  - DJANGO SOFTWARE FOUNDATION
- [Python 3.12.0 候选版本 2 可用](https://pycoders.com/link/11410/web)
  - CPYTHON DEV BLOG
- [Pandas 2.1.0 发布](https://pycoders.com/link/11414/web)
  - PYDATA.ORG

-----------------------------------------

## 探讨/吐糟
>
> Discussions

- [为什么更喜欢缩进而不是块标记？](https://pycoders.com/link/11419/web)
  - STACKEXCHANGE.COM
(`是也乎:`
Donald E. Knuth & Peter J. Landin 等大仙们都同意...
)

-----------------------------------------

## 文章/教程/嗯哼
>
> Articles, Tutorials and Talks

- [一行 Python 代码启动 HTTP 服务器](https://pycoders.com/link/11430/web)
  - REAL PYTHON
In this tutorial, you’ll learn how to host files with a single command using an HTTP server built into Python. You’ll also extend it by making a miniature web framework able to serve dynamic content from HTML templates. Along the way, you’ll run CGI scripts and use encryption over HTTPS.
(`是也乎:`
![HTTP](https://ipic.zoomquiet.top/2023-09-13-zshot%202023-09-13%2016.17.35.jpg)
)
- [介绍 flake8-logging](https://pycoders.com/link/11409/web)
  - ADAM JOHNSON
The Python standard library’s logging module is a go-to for adding observability to applications, but there are right and wrong ways to use it. This article is about a new linter that explicitly looks for problems with your logging calls.
(`是也乎:`
logging 内建模块实在是个经典 Pythonic 气质的组件,
易用难精...
)
- [Apple Vision 框架通过 PyObjC 进行文本识别](https://pycoders.com/link/11433/web)
  - YASOOB KHALID
  - • Shared by Yasoob Khalid
Learn how to use PyObjC to interface with the Apple Vision Framework and create a script to detect text in images. Become familiar with how PyObjC works and how it maps functions and methods from Objective C to Python.
- [类概念：Python 中的面向对象编程](https://pycoders.com/link/11402/web)
  - REAL PYTHON
  - COURSE
Python uses object-oriented programming to group data and associated operations together into classes. In this video course, you’ll learn how to write object-oriented code with classes, attributes, and methods.
(`是也乎:`
![OOP](https://ipic.zoomquiet.top/2023-09-13-zshot%202023-09-13%2016.15.30.jpg)
)
- [切换到孵化/Hatch](https://pycoders.com/link/11416/web)
  - OLIVER ANDRICH
Oliver used Poetry for most of his projects, but recently tried out Hatch instead. This blog post covers what it took to get things going and what features he used, including how he ditched tox.
- [Python 字典调度模式](https://pycoders.com/link/11418/web)
  - JAMES GALLAGHER
The dictionary dispatch pattern is when you keep references to functions in a dictionary and change code behavior based on keys. Learn how to use this pattern in practice.
(`是也乎:`
原来这种技巧叫这名儿, 以往都当成普通 hub 来用...
)
- [分析解析PyPI的内容](https://pycoders.com/link/11406/web)
  - TOM FORBES
  - • Shared by Tom Forbes
High-level statistics gathered from PyPI, including how popular language features are, project sizes (tensorflow accounts for 16% of the data on PyPI!) and growth.
(`是也乎:`
将近2成都是 tensorflow 相关业务的流量...
)
- [用 500 行 Python 编写一个 C 编译器](https://pycoders.com/link/11417/web)
  - THEIA VOGEL
This post details how to build a C compiler, step-by-step, using Python. A great intro to compilers. The target source is WASM, so learn a bit about that too.
(`是也乎:`
这个可以有...
![compilers](https://ipic.zoomquiet.top/2023-09-13-zshot%202023-09-13%2016.06.57.jpg)
)
- [Django 中的过滤器： filter(A, B) 与 filter(A).filter(B)](https://pycoders.com/link/11425/web)
  - APIROBOT.ME
  - • Shared by Denis
An advanced dive into the Django ORM, how it handles joins, and what that means for your code.
- [最喜欢的 LeetCode 问题 Python 技巧](https://pycoders.com/link/11429/web)
  - JJ BEHRENS
A collection of intermediate-level Python tricks and tools. Write more Pythonic code!
- [TOML 有什么问题？](https://pycoders.com/link/11405/web)
  - HITCHDEV.COM
Some YAML people talk about why TOML is too limited.
(`是也乎:`
因为不姓赵?
)

-----------------------------------------

## 好物/妙品/
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [StrictYAML: 类型安全的 YAML 受限子集](https://pycoders.com/link/11431/web)
  - HITCHDEV.COM
- [dara: 用纯 Python 创建交互式 Web 应用程序](https://pycoders.com/link/11423/web)
  - GITHUB.COM/CAUSALENS
- [JobSpy: LinkedIn、Indeed 和 ZipRecruiter 的 Scraper](https://pycoders.com/link/11404/web)
  - GITHUB.COM/CULLENWATSON
- [krypton: 静态数据加密和 Python 的 IAM](https://pycoders.com/link/11413/web)
  - GITHUB.COM/KRPTN
- [iommi: 您 Django 强力Chord首选](https://pycoders.com/link/11403/web)
  - GITHUB.COM/IOMMIROCKS
(`是也乎:`
叕一个低代码平台...?
)

-----------------------------------------

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11411/web)
  - September 13, 2023
- [PyData Amsterdam 2023](https://pycoders.com/link/11426/web)
  - September 14 to September 17, 2023
- [Python Atlanta](https://pycoders.com/link/11434/web)
  - September 14 to September 15, 2023
- [Kiwi PyCon 2023](https://pycoders.com/link/11420/web)
  - September 15 to September 18, 2023
- [PyCon CZ 2023](https://pycoders.com/link/11427/web)
  - September 15 to September 18, 2023
- [PyData Seattle: Language Creators Charity Fundraiser](https://pycoders.com/link/11428/web)
  - September 19 to September 20, 2023
- [PyCon Uganda](https://pycoders.com/link/11435/web)
  - September 21 to September 24, 2023
- [PyCon UK 2023](https://pycoders.com/link/11412/web)
  - September 22 to September 26, 2023

-----------------------------------------

## 历史上这周

- 2022: [蠎周刊 PyCoder 542](https://weekly.pychina.org/issue/issue-542.html)
- 2021: [蠎周刊 489](https://weekly.pychina.org/issue/issue-489.html)
  - [pythonista-weekly : Pyw 516](https://weekly.pychina.org/python-weekly/pyw-516.html)
- 2020: [蠎周刊 436](https://weekly.pychina.org/issue/issue-436.html)
  - [pythonista-weekly : Pyw 466](https://weekly.pychina.org/python-weekly/pyw-466.html)
- 2019: [蠎周刊 385](https://weekly.pychina.org/issue/issue-385.html)
- 2018: [蠎周刊 334](https://weekly.pychina.org/issue/issue-334.html)
- 2017: [蠎加载 141](https://weekly.pychina.org/importpython/importpython-141.html)
- 2016: [蠎加载 90](https://weekly.pychina.org/importpython/importpython-90.html)
- 2015: [蠎周刊 183](https://weekly.pychina.org/issue/issue-183.html)
  - [蠎加载 49](https://weekly.pychina.org/importpython/importpython-49.html)
- 2014: [Issue 132](https://weekly.pychina.org/issue/issue-132.html)
- 2013: 空缺
- 2012: 空缺

-----------------------------------------

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [大妈的多重宇宙 - YouTube](https://www.youtube.com/@Chaos42DAMA)
  - @Chaos42DAMA
  - 恢复各种嗯哼...
- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
  - 古早:新闻组式写作
  - 欢迎订阅, 包含当前周刊

```
          _~`|`~_
      \/ /  ◕ ←  \ \/
        '_   ∧   _'
        ( '--∽--' )
...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```

-----------------------------------------

# PS

- 首发: [Issue 594 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-594.html)
- 修订: [issue-594.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-594.md)

> Happy Pythoning!
>> Copyright © 2023 PyCoder’s Weekly, All rights reserved.
>>
## PPS
>
> 不觉中蟒周刊快译已经到了第10+2个年头
开始有小伙伴加入承担 `pythonisa` 周刊的翻译,
从来没提醒过, 可就这么默默坚持下来了...
问为什么:
    [皱眉]每周新闻资讯 怎么能错过
    看看有什么新东西
    当有新的发现时：
        what f**k 还能这样玩？ 还有这东西？
        每周开彩蛋[吃瓜]
`无法同意更多`...
很多社区贡献看起来辛苦,
其实受益最多的,
就是主动承担者也.
所以++> [锈周刊 -> Weekly :: China<Rustaceans>](https://weekly.rs.101.so/2023/index.html)
-------------

好文笔,感叹号年度配额: **2/3**
投稿/反馈邮箱:
    <askdama@googlegroups.com>
(邮件列表地址,
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)
-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF594D4Q90XdDA7g)**
就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF594D4Q90XdDA7g):

```python
全职嗯哼: 大妈的多重宇宙 - https://www.youtube.com/@Chaos42DAMA
私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开社群: 蟒营 (订阅号: Mainium)
as 创始组织者:
    CPyUG (mailling-list: python-cn@googlegroups.com)
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        AIGC珠海 
```

-------------
