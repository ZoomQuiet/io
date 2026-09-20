---
title: "蠎周刊(PyCoder)589"
summary: ""
date: "2023-08-09T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> “为什么Python很糟糕”
原文: [PyCoder's Weekly - Issue #589](https://pycoders.com/issues/589)
![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)

- 230809 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230809 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------

- [探索 Pandas 2.0 和 Apache Arrow 的目标](https://pycoders.com/link/11255/web)
  - REAL PYTHON
  - PODCAST
What are the new ways to describe your data in pandas 2.0? Will the addition of Apache Arrow to the data back end foster the growth of data interoperability? This week on the show, we talk with pandas core developer Marc Garcia about the release of pandas 2.0.
(`是也乎:`
![Arrow](https://ipic.zoomquiet.top/2023-08-09-zshot%202023-08-09%2011.22.19.jpg)
Arrow 是目标替代 NumPy 的各种数据类型...
参考: [pandas 2\.0 and the Arrow revolution \(part I\)](https://datapythonista.me/blog/pandas-20-and-the-arrow-revolution-part-i)
)
- [Python、外部函数和 Steam](https://pycoders.com/link/11251/web)
  - ARTUR DRYOMOV
  - • Shared by Artur Dryomov
This article shows you how to call foreign C functions from Python. This allows you to call into shared libraries and is similar to how extensions work. The examples use the Steamworks SDK which games use to communicate with Steam.
- [Python 包版本控制的怪癖](https://pycoders.com/link/11253/web)
  - SETH LARSON
Python packaging allows for a wide variety of version styles for your packages. This article shows you what is out there and why you might use each.
- [PSF宣布 2023 年第一季度的资深会员](https://pycoders.com/link/11248/web)
  - PYTHON SOFTWARE FOUNDATION
- [Django 4.2.4 发布](https://pycoders.com/link/11249/web)
  - DJANGO SOFTWARE FOUNDATION
- [Pydantic v2.1 发布](https://pycoders.com/link/11246/web)
  - PYDANTIC.DEV

-----------------------------------------

## 探讨/吐糟
>
> Discussions

- [“为什么Python很糟糕”](https://pycoders.com/link/11244/web)
  - HACKER NEWS
(`是也乎:`
因为没办法像 JAVA 那样合理扩展成上千人团队,
通常10来人, 什么都作出来了...
![HACKER](https://ipic.zoomquiet.top/2023-08-09-zshot%202023-08-09%2011.18.28.jpg)
当然原文作者鼓吹的是 Rust ..
)
- [有人在实际工作中使用 PyPy 吗？](https://pycoders.com/link/11243/web)
  - HACKER NEWS
(`是也乎:`
当然有, 不过, 都没什么名气...
所以, 为什么呢?
CPython 性能其实是足够的;
)

-----------------------------------------

## 文章/教程/嗯哼
>
> Articles, Tutorials and Talks

- [Filtering Iterables With Python
使用 Python 过滤可迭代对象](https://pycoders.com/link/11259/web)
  - REAL PYTHON
  - COURSE
In this video course, you’ll learn how Python’s filter() works and how to use it effectively in your programs. You’ll also learn how to use list comprehension and generator expressions to replace filter() and make your code more Pythonic.
(`是也乎:`
![COURSE](https://ipic.zoomquiet.top/2023-08-09-zshot%202023-08-09%2011.14.27.jpg)
可以是可以, 不过,调试太困难了...
)
- [通过索引提高 Pandas 的效率](https://pycoders.com/link/11260/web)
  - FEDERICO TROTTA
Pandas is the most widely used Python library for data manipulation, and it allows you to access and manipulate data efficiently. Its indexing techniques can significantly improve the speed and efficiency of your queries. Learn how.
(`是也乎:`
所以, 本质上还是 DBA 哪...
)
- [Overloading Arithmetic Operators With Dunder Methods
使用 Dunder 方法重载算术运算符](https://pycoders.com/link/11234/web)
  - RODRIGO GIRÃO SERRÃO
  - • Shared by Rodrigo Girão Serrão
This article shows you how to overload the arithmetic operators in Python with dunder methods. It includes examples for add, radd, and iadd, while also outlining how to deal with error conditions in dunder methods.
- [Django 支持多种语言](https://pycoders.com/link/11250/web)
  - SAMUEL TORIMIRO
  - • Shared by Michael Herman
This step-by-step article shows you how to add multiple language support to your Django projects. It covers the difference between localization and internationalization, and how to use both in the template engine.
- [如何使用 Python 从 URL 下载文件](https://pycoders.com/link/11228/web)
  - REAL PYTHON
In this tutorial, you’ll find the right tools to help you download files from URLs with Python and manage the data retrieval process. You’ll cover data streaming, thread pools, and asynchronous downloads.
(`是也乎:`
![URL](https://ipic.zoomquiet.top/2023-08-09-zshot%202023-08-09%2011.11.26.jpg)
不过, 如果量大了, 还是使用类似 wget 的第三方专业工具来完成..
Py 进行指令生成就好
)
- [用 Python operator 模块](https://pycoders.com/link/11254/web)
  - REAL PYTHON
In this tutorial, you’ll explore the Python operator module and its role in functional programming. You’ll code several examples of using both operator-equivalent and higher-order functions in programs.
(`是也乎:`
![operator](https://ipic.zoomquiet.top/2023-08-09-zshot%202023-08-09%2011.10.43.jpg)
)
- [热门航空客运航线](https://pycoders.com/link/11231/web)
  - MARK LITWINTSCHIK
This article talks about scraping passenger count data from Wikipedia and building visualizations for it. It uses wikitextparser for scraping, DuckDB for data, and rich for the terminal interface.
(`是也乎:`
![MARK](https://ipic.zoomquiet.top/2023-08-09-zshot%202023-08-09%2011.09.32.jpg)
基于duckdb 完成的数据可视化
)
- [用 Python 和 Polylith 进行 Kafka 消息传递](https://pycoders.com/link/11237/web)
  - DAVID VUJIC
  - • Shared by David Vujic
Get started with Apache Kafka to produce & consume messages with Python. All this in a Polylith workspace, for a nice developer experience and to easily re-use existing code.
- [PyFlo: Python 初学者指南](https://pycoders.com/link/11245/web)
  - PYFLO
This is an online course with an interesting flow chart guiding you through lessons, with optional tangents and core concepts. It even includes an instructor’s guide.
(`是也乎:`
![PYFLO](https://ipic.zoomquiet.top/2023-08-09-zshot%202023-08-09%2011.05.52.jpg)
有个清晰的路线图..
和蟒营®当年课程类似...
)
- [构建和运营 S3](https://pycoders.com/link/11252/web)
  - ANDY WARFIELD
This article is a very deep dive into how Amazon S3 Storage was created, and the complexities involved in operating a system at that scale.
(`是也乎:`
呵, 这个先进了...
)

-----------------------------------------

## 好物/妙品/
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [reflex: 纯 Python 的 Web 应用程序](https://pycoders.com/link/11258/web)
  - GITHUB.COM/REFLEX-DEV
(`是也乎:`
国货, 要 node 配套,
不是 htmx 方向..
)
- [lpython: Python 编译器](https://pycoders.com/link/11239/web)
  - GITHUB.COM/LCOMPILERS
- [Django ORM 备忘单](https://pycoders.com/link/11256/web)
  - DJANGOCENTRAL
(`是也乎:`
Django ORM 最大的问题是无法优化吧...
如果没有事先由 DBA 直接在数据库中完成优化,
ORM 迭代出来的数据库结构已经不可控了?
)
- [textual-paint: 艺术：终端中的 MS Paint](https://pycoders.com/link/11225/web)
  - GITHUB.COM/1J01
(`是也乎:`
![textual](https://ipic.zoomquiet.top/2023-08-09-zshot%202023-08-09%2011.00.07.jpg)
8bit 艺术重要工具...
支持输出为多种格式文件, 包含 .svg,.webp...
)
- [Biaslyze: NLP 偏差识别工具包](https://pycoders.com/link/11230/web)
  - GITHUB.COM/BIASLYZE-DEV
  - • Shared by Tobias Sterbak

-----------------------------------------

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11229/web)
  - August 9, 2023
- [Python Atlanta](https://pycoders.com/link/11227/web)
  - August 10 to August 11, 2023
- [PyCon KR](https://pycoders.com/link/11235/web)
  - August 11 to August 14, 2023
- [Django Girls Abuja](https://pycoders.com/link/11236/web)
  - August 11 to August 13, 2023
- [PyDelhi User Group Meetup](https://pycoders.com/link/11233/web)
  - August 12, 2023
- [DFW Pythoneers 2nd Saturday Teaching Meeting](https://pycoders.com/link/11224/web)
  - August 12, 2023
- [EuroSciPy 2023](https://pycoders.com/link/11240/web)
  - August 14 to August 19, 2023
- [DjangoConAU 2023](https://pycoders.com/link/11242/web)
  - August 18 to August 19, 2023
- [PyCon AU 2023](https://pycoders.com/link/11257/web)
  - August 18 to August 23, 2023

-----------------------------------------

## 历史上这周

- 2022: [蠎周刊 PyCoder 537](https://weekly.pychina.org/issue/issue-537.html)
- 2021: [蠎周刊 484](https://weekly.pychina.org/issue/issue-484.html)
  - [pythonista-weekly : Pyw 511](https://weekly.pychina.org/python-weekly/pyw-511.html)
- 2020: [蠎周刊 431](https://weekly.pychina.org/issue/issue-431.html)
  - [pythonista-weekly : Pyw 461](https://weekly.pychina.org/python-weekly/pyw-461.html)
- 2019: [蠎周刊 380](https://weekly.pychina.org/issue/issue-380.html)
- 2018: [蠎周刊 329](https://weekly.pychina.org/issue/issue-329.html)
- 2017: [蠎加载 136](https://weekly.pychina.org/importpython/importpython-136.html)
- 2016: [蠎加载 85](https://weekly.pychina.org/importpython/importpython-85.html)
- 2015: [蠎周刊 178](https://weekly.pychina.org/issue/issue-178.html)
  - [蠎加载 44](https://weekly.pychina.org/importpython/importpython-44.html)
- 2014: [Issue 127](https://weekly.pychina.org/issue/issue-127.html)
- 2013: 空缺
- 2012: [Issue 26: 好奇心](https://weekly.pychina.org/issue/issue-26.html)

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
          _~~+~~_
      () /  → #  \ \/
        '_   ⏡   _'
        \ '--∽--' <
...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```

-----------------------------------------

# PS

- 首发: [Issue 589 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-589.html)
- 修订: [issue-589.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-589.md)

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

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF589D4Q90XdDA7g)**
就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF589D4Q90XdDA7g):

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
