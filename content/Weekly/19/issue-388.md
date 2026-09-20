---
title: "Issue 388"
summary: ""
date: "2019-10-06T21:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> NASA实锤对比Py和多种主力数据科学语言
原文: [PyCoder's Weekly - Issue #388](https://pycoders.com/issues/388)
![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 191006 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 191006 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------

- [Python 中如何用 Generators 和 Yield](https://pycoders.com/link/2577/web)
  - REAL PYTHON
Learn about generators and yielding in Python. You'll create generator functions and generator expressions using multiple Python yield statements. You'll also see how to build data pipelines that take advantage of these Pythonic tools.
(`是也乎:`
![Generators](https://ipic.zoomquiet.top/2019-10-07-ScreenShot%202019-10-07%2020.14.24.jpg)
可以说, 真蟒, 一己之力, 将 Python 领域所有值得嗯哼的事儿, 这几年全部重新嗯哼了一遍...
这是为了获得完全自主产权的教材, 来构筑课程池?
)
- [对比 Python, Julia, Matlab, IDL 以及 Java](https://pycoders.com/link/2579/web)
  - NASA.GOV
"We use simple test cases to compare various high level programming languages. We implement the test cases from an angle of a novice programmer who is not familiar with the optimization techniques available in the languages. The goal is to highlight the strengths and weaknesses of each language but not to claim that one language is better than the others."
(`是也乎:`
实锤了....
![NASA](https://ipic.zoomquiet.top/2019-10-07-fig_languages_histo.png)
没有一枝独秀, 只有相对优势.
如果自己用 Python 没毛病, 如果公司来, Java 永远正确.
)
- [正则表达式在 Python 中的性能](https://pycoders.com/link/2572/web)
  - JUN WU
"Working with regex, you have to understand what you are doing: the regex engine for Python, the type of statement you are writing, and alternative tools that are available for your purposes. Yes, there are instances when the re package may not be the best tool to use."
- [PEG 在 Core Developer Sprint](https://pycoders.com/link/2587/web)
  - GUIDO VAN ROSSUM
"Every year for the past four years a bunch of Python core developers get together for a week-long sprint at an exotic location. These sprints are sponsored by the PSF as well as by the company hosting the sprint."
(`是也乎:`
老爹真的开始放飞了, 敢于放权给大家玩内核了...
)
- [Mypy 0.730 发布](https://pycoders.com/link/2588/web)
  - MYPY-LANG.BLOGSPOT.COM
Mypy 0.730 is out, with prettier, colored output and error code support, along with many other fixes and improvements.
(`是也乎:`
兼容 Py2 的生态圈已经正式起航...再次.
)
- [Django Bugfix 发布: 2.2.6, 2.1.13 and 1.11.25](https://pycoders.com/link/2570/web)
  - DJANGOPROJECT.COM

## 讨论
>
> Discussions

- [Python 3.8.0 候选发行版今天到期](https://pycoders.com/link/2583/web)
  - ŁUKASZ LANGA
- [如果有人说"知道Python",内心里希望他们知道什么?](https://pycoders.com/link/2581/web)
  - REDDIT
(`是也乎:`
缩进/历史/黑洞/...
)
- [您需要知道数学才能成为程序员吗?](https://pycoders.com/link/2582/web)
  - REDDIT
(`是也乎:`
Yes and Not,
数学不一定要精通, 但是, 数学依赖的逻辑一定得稳.
)

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [用 Python 防止 SQL 注入攻击](https://pycoders.com/link/2574/web)
  - REAL PYTHON
SQL injection attacks are one of the most common web application security risks. In this step-by-step tutorial, you'll learn how you can prevent Python SQL injection. You'll learn how to compose SQL queries with parameters, as well as how to safely execute those queries in your database.
(`是也乎:`
![注入攻击](https://ipic.zoomquiet.top/2019-10-07-ScreenShot%202019-10-07%2020.04.40.jpg)
注入攻击...只是, 也早已有对应模块可以自动防止绝大多数了...
)
- [用Keras纠正Adam(RAdam)优化器](https://pycoders.com/link/2573/web)
  - ADRIAN ROSEBROCK
Learn how to use Keras and the Rectified Adam optimizer as a drop-in replacement for the standard Adam optimizer, potentially leading to a higher accuracy model (and in fewer epochs).
(`是也乎:`
Keras 可能又是一个 Panda 级别的作品.
)
- [简单介绍 Python 中的 StringIO 和 BytesIO](https://pycoders.com/link/2585/web)
  - DANIEL BEACH
  - • Shared by Daniel Beach
"For some reason IO streams are a totally underused feature that rarely comes up in most code. We all know that memory if faster than disk IO, this is what I use IO streams for."
- [与PostgreSQL相比,Redis在存储JSON Blob方面要快多少?](https://pycoders.com/link/2589/web)
  - PETER BENGTSSON
Also [read the followup here.](https://pycoders.com/link/2571/web).
(`是也乎:`
快也无法替换.
)
- [Python 中的字符串和字符数据](https://pycoders.com/link/2575/web)
  - REAL PYTHON
  - video
Learn how to use Python's rich set of operators, functions, and methods for working with strings. You'll learn how to access and extract portions of strings, and also become familiar with the methods that are available to manipulate and modify string data in Python 3.
(`是也乎:`
![字符串和字符数据](https://ipic.zoomquiet.top/2019-10-07-ScreenShot%202019-10-07%2020.01.56.jpg)
这绝对是基础又重要的嗯哼...只是, 涉及中文, 又得复杂一倍.
)
- [使用iloc 和 loc为 Pandas Dataframes 建立索引和切片](https://pycoders.com/link/2586/web)
  - ERIK MARSJA
Learn how to work with Pandas iloc and loc to slice, index, and subset your dataframes, for example by row and columns.
(`是也乎:`
要不是 `:` 操作符已占用, 否则, 更加直觉
)
- [自定义您的 Pytest 测试套件(第2部分)](https://pycoders.com/link/2584/web)
  - RAPHAEL PIERZINA
- [Python 中的 Multiprocessing vs Threading : 每位数据科学家都需要知道的](https://pycoders.com/link/2578/web)
  - SUMIT GHOSH
(`是也乎:`
数据科学家应知应会的东西, 太多了...
)
- [在Visual Studio Code中设置Flask应用程序](https://pycoders.com/link/2580/web)
  - MIGUEL GRINBERG
(`是也乎:`
得益于 VSCode 设计合理的插件体系, 各大框架都可以快速包装自己专用的插件来.
只是....
)
- [Python Negatypes: ABCs 和 __subclasshook__](https://pycoders.com/link/2576/web)
  - HILLEL WAYNE

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [pire: Python 交互式正则表达式](https://pycoders.com/link/2569/web)
  - GITHUB.COM/JOHANNESTAAS
PIRE is an interactive command-line interface allowing you to edit regexes live and see how your changes match against the input you specify.
(`是也乎:`
这么多年了, 正则表达式 依然没找到合适的辅助表述工具/协议/DSL/...
)
- [pyrrhic: 可编程 Python 构建系统](https://pycoders.com/link/2567/web)
  - GITHUB.COM/TAWESOFT • Shared by Ben Golightly
- [pandas-profiling: 从Pandas DataFrame 对象创建 HTML 分析报告](https://pycoders.com/link/2568/web)
  - GITHUB.COM/PANDAS-PROFILING
- [limeade: 适用 Python 3.4+ 的热重装](https://pycoders.com/link/2566/web)
  - GITHUB.COM/CFSWORKS
(`是也乎:`
![limeade](https://github.com/CFSworks/limeade/raw/master/.github/readme/logo.png?raw=true)
动态加载,也就是热升级前夜技巧?
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyCon Estonia](https://pycoders.com/link/2561/web)
  - October 3 to October 4, 2019
  - 爱沙尼亚
- [⋅ PyCon Balkan 2019](https://pycoders.com/link/2560/web)
  - October 3 to October 6, 2019
  - 巴尔干半
- [⋅ SciPy Latam](https://pycoders.com/link/2558/web)
  - October 8 to October 11, 2019
  - 哥伦比亚
(`是也乎:`
logo 设计很不错, .svg 的
<img src="https://conf.scipyla.org/static/images/logo-menu.svg?h=8aaed2a3" alt="logo menu"
    width="142"/>
)
- [⋅ PyCon ZA 2019](https://pycoders.com/link/2562/web)
  - October 9 to October 14, 2019
  - 南非
- [⋅ PyConDE & PyData Berlin 2019](https://pycoders.com/link/2563/web)
  - October 9 to October 12, 2019
  - 德国
- [⋅ PyTennessee 2020 CFP](https://pycoders.com/link/2565/web)
  - March 7 to March 8, 2020
  - in Nashville, TN
  - 田纳西州

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- __[蟒营 Python 入门班](https://py.101.camp/)__
  - 第3期
  - 101camp3py
第3期已开课, 为期6周;
191103 按时结束, 到时再约 4py ;-)

# 是也乎
>
> NN 3793

- 首发: [Issue 388 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-388.html)
- 改进: [issue-388.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-388.md)
