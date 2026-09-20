Title: 蠎周刊(PyCoder)599
Slug: issue-599
Date: 2023-10-18 21:42
Tags: Weekly,Python,pycoders,ZH


> 遇见guido老爹时


原文: [PyCoder's Weekly - Issue #599](https://pycoders.com/issues/599)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 231018 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 231018 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------




- [如何在 Python 中按字母顺序对 Unicode 字符串进行排序](https://pycoders.com/link/11642/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to correctly sort Unicode strings in Python while avoiding common pitfalls. You’ll explore powerful third-party libraries implementing the complete Unicode Collation Algorithm (UCA), as well as standard library modules and a few handmade solutions.


(`是也乎:`


![Unicode](https://ipic.zoomquiet.top/2023-10-18-zshot%202023-10-18%2010.45.06.jpg)

)


- [用 functools 模块可以做 6 件很酷的事情](https://pycoders.com/link/11629/web)
    + BOB BELDERBOS

The functools module in the standard library has all sorts of useful bits and pieces. This article talks about six of them: caching, writing fewer dunder methods, freeze functions, generic functions, better decorators, and reduce().

(`是也乎:`

不止, 只是 functools 中的参数顺序都有点儿反直觉要习惯先...


)

- [用 Stripe、Vue.js 和 Flask 接受付款](https://pycoders.com/link/11654/web)
    + MICHAEL HERMAN

If you’re building a site to make money, at some point you have to collect money. This tutorial shows you how to build a Flask application that integrates with Stripe for payment processing through the Vue.js framework.

(`是也乎:`

Stripe 已经变成海外的支付宝,
当然无法接入银联的...

)



- [Python 荣获 NEC C&C 基金会奖](https://pycoders.com/link/11644/web)
    + NEC.COM





-----------------------------------------
## 探讨/吐糟
> Discussions




- [Django 性能的最佳实践？](https://pycoders.com/link/11625/web)
    + DJANGO SOFTWARE FOUNDATION





-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [用Python的 min() 和 max()](https://pycoders.com/link/11653/web)
    + REAL PYTHON 
    + COURSE

In this video course, you’ll learn how to use Python’s built-in min() and max() functions to find the smallest and largest values. You’ll also learn how to modify their standard behavior by providing a suitable key function. Finally, you’ll code a few practical examples of using min() and max().


(`是也乎:`


![COURSE](https://ipic.zoomquiet.top/2023-10-18-zshot%202023-10-18%2010.42.31.jpg)

)


- [Django 用 HTMX 实现你想要的东西](https://pycoders.com/link/11624/web)
    + BITE CODE

HTMX is allowing more dynamic pages to be built with less JavaScript than before. This blog post talks about three techniques you can use to improve your HTMX pages when working with Django: HTTP 303 redirections, the django-htmx library, and using the hx-trigger header.


(`是也乎:`


Django 已经是 Python 宇宙的 PHP 了, 所以, 和任何流行元素结合已经变成了习惯..

)


- [当我遇见吉多·范·罗森时](https://pycoders.com/link/11638/web)
    + ADARSH DIVAKARAN

This personal blog post by Adarsh recounts his conversations with Guido at PyCasades back in the spring. They talked about the how to get better at Python and what it takes to become a core developer.

(`是也乎:`

是的, 大仙其实都很乐于交流的, 嘦是认真的...

)


- [79,306 人讲述数据科学的未来](https://pycoders.com/link/11626/web)
    + MAHA TAQI

Data science is thought of as a growing field, but can you prove it? By using the results of both the 2021 and 2022 Python Developers survey, this article shows how the field is growing and changing.

(`是也乎:`


也就是jetbrains 的调查问卷统计结果...

)


- [为 Django ORM 构建 RisingWave 连接器](https://pycoders.com/link/11622/web)
    + BAS 
    + • Shared by Bas

This articles shows the internals of the Django ORM. We build a prototype for a connector to the RisingWave event streaming database and enable dashboarding capabilities in Django

- [用 JSON 文件配置您的 MicroPython 项目](https://pycoders.com/link/11637/web)
    + BHAVESH KAKWANI

Learn how to get your microcontroller to remember your settings, so you can quickly get it back in working state even if it loses power or reboots!

- [Python 变量：命名空间和变量作用域](https://pycoders.com/link/11628/web)
    + MUHAMMAD RAZA

This post is a comprehensive guide on namespaces and variable scope. Learn about the four different name spaces and how to access each.

- [自动差异拼图](https://pycoders.com/link/11650/web)
    + SASHA RUSH

“This notebook contains a series of self-contained puzzles for learning about derivatives in tensor libraries.”

(`是也乎:`

colab 直接可运行的 Jupyter ...

)

- [PyTimeTK 基础知识](https://pycoders.com/link/11627/web)
    + BUSINESS-SCIENCE.GITHUB.IO

An introduction to the pytimetk library and how you can use it to handle time series analysis.

(`是也乎:`


文档如此完备的社区, 走的远...

)

- [Python 的 yield 和生成器解释](https://pycoders.com/link/11640/web)
    + ERIK O'SHAUGHNESSY 
    + • Shared by Bob

Learn about yield and how generators can make your code more performant.

- [Python 自评分数](https://pycoders.com/link/11647/web)
    + JPGLOMOT.COM 
    + • Shared by Jean-Philippe Glomot

A quick little web site to evaluate your Python basic syntax knowledge







-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code





- [build123d: Python CAD 编程库](https://pycoders.com/link/11651/web)
    + GITHUB.COM/GUMYR


(`是也乎:`

核心组件库不开源, 调用层开源其实没什么帮助的?

)


- [humanhash: 人类可读的摘要](https://pycoders.com/link/11643/web)
    + GITHUB.COM/ZACHARYVOASE


(`是也乎:`

这就得上 LLMs 了?

)


- [logmerger: 具有合并时间线的日志文件的 TUI](https://pycoders.com/link/11620/web)
    + GITHUB.COM/PTMCG

(`是也乎:`


![TUI](https://ipic.zoomquiet.top/2023-10-18-zshot%202023-10-18%2010.33.28.jpg)

TUI 永远有需求...

)


- [pipeless-ai: 开源计算机视觉框架](https://pycoders.com/link/11633/web)
    + GITHUB.COM/PIPELESS-AI 
    + • Shared by Miguel Angel Cabrera

(`是也乎:`

等等, OpenCV 不是一直在这个领域积累的?

)


- [magentic: 将 LLM 无缝集成为 Python 函数](https://pycoders.com/link/11648/web)
    + GITHUB.COM/JACKMPCOLLINS

(`是也乎:`

OpenAI 创始不是曰过:

    凡是作壳的没有前途...

)






-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11639/web)
    + October 18, 2023

- [PyData Bristol Meetup](https://pycoders.com/link/11631/web)
    + October 19, 2023

- [PyLadies Dublin](https://pycoders.com/link/11623/web)
    + October 19, 2023

- [Chattanooga Python User Group](https://pycoders.com/link/11635/web)
    + October 20 to October 21, 2023

- [EduPy 2023](https://pycoders.com/link/11649/web)
    + October 21 to October 22, 2023

- [PyDay Cali 2023](https://pycoders.com/link/11630/web)
    + October 21 to October 22, 2023

- [PackagingCon 2023](https://pycoders.com/link/11641/web)
    + October 26 to October 29, 2023

- [PyCon APAC 2023](https://pycoders.com/link/11632/web)
    + October 27 to October 29, 2023




-----------------------------------------
## 历史上这周


- 2022: [蠎周刊 PyCoder 547](https://weekly.pychina.org/issue/issue-547.html)
- 2021: [蠎周刊 494](https://weekly.pychina.org/issue/issue-494.html)
    + [pythonista-weekly : Pyw 521](https://weekly.pychina.org/python-weekly/pyw-521.html)
- 2020: [蠎周刊 441](https://weekly.pychina.org/issue/issue-441.html)
    + [pythonista-weekly : Pyw 471](https://weekly.pychina.org/python-weekly/pyw-471.html)
- 2019: [蠎周刊 390](https://weekly.pychina.org/issue/issue-390.html)
- 2018: [蠎周刊 339](https://weekly.pychina.org/issue/issue-339.html)
- 2017: [蠎加载 146](https://weekly.pychina.org/importpython/importpython-146.html)
- 2016: [蠎加载 95](https://weekly.pychina.org/importpython/importpython-95.html)
- 2015: [蠎周刊 188](https://weekly.pychina.org/issue/issue-188.html)
    + [蠎加载 54](https://weekly.pychina.org/importpython/importpython-54.html)
- 2014: [Issue 137](https://weekly.pychina.org/issue/issue-137.html)
- 2013: [Issue 88 ~ asyncio](https://weekly.pychina.org/issue/issue-88.html)
- 2012: 空缺


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [大妈的多重宇宙 - YouTube](https://www.youtube.com/@Chaos42DAMA)
    + @Chaos42DAMA
    + 恢复各种嗯哼...
- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅, 包含当前周刊





```
      _~-~∽~_
  \/ /  ◕ ♡  \ (/
    '_   △   _'
    \ '--+--' \

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```



-----------------------------------------
# PS:

- 首发: [Issue 599 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-599.html)
- 修订: [issue-599.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-599.md)

> Happy Pythoning!
>> Copyright © 2023 PyCoder’s Weekly, All rights reserved.
    
## PPS:
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

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF599D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF599D4Q90XdDA7g):



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



