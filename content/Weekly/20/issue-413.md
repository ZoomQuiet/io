---
title: "Issue 413"
summary: ""
date: "2020-03-25T14:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> 匹兹堡的 PyCon US 2020 被取消
原文: [PyCoder's Weekly - Issue #413](https://pycoders.com/issues/413)
![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200325 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200325 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------

- [宾夕法尼亚州/匹兹堡的 PyCon US 2020 被取消](https://pycoders.com/link/3794/web)
  - PYCON BLOG
“Recently, the United States and the State of Pennsylvania have asked that large gatherings be postponed or cancelled until further notice. With that in mind, the PSF has worked to reduce financial exposure and develop a plan to provide content remotely.”
(`是也乎:`
![COVID-19](http://ydlj.zoomquiet.top/ipic/2020-03-25-%E6%9C%AA%E5%91%BD%E5%90%8D%E6%96%87%E4%BB%B6.jpg?imageView2/2/w/360)
注视之下, 终于还是怂了..
)
- [今年将推出新 pip 解析器](https://pycoders.com/link/3796/web)
  - PSF BLOG
“The developers of pip are in the process of developing a new resolver for pip (as we announced on the PSF blog last year). We aim to roll it out later this year. As part of that work, there will be some major changes to how pip determines what to install, based on package requirements.”
- [改进 Python 的 Pretty-Printing](https://pycoders.com/link/3804/web)
  - JAKE EDGE
Some changes are being proposed to add more customization to the pprint module in Python 3.10 or later, and while a PEP hasn’t been created yet, there are some internal discussions going on debating whether or not such a change is worthwhile and what the API might look like.
- [The Real Python Podcast 上线](https://pycoders.com/link/3814/web)
  - REAL PYTHON
  - podcast
A weekly Python podcast hosted by Christopher Bailey with interviews, coding tips, and conversation with guests from the Python community. The show covers a wide range of topics including Python programming best practices, career tips, and related software development topics.
(`是也乎:`
![Podcast](http://ydlj.zoomquiet.top/ipic/2020-03-25-ScreenShot%202020-03-25%2010.47.15.jpg)
也来了哪...
俺们的也有了哪:
[fm.101.camp 蟒营™电台 钩陈各种值得探讨](https://fm.101.camp/)
)
- [Python Scope & the LEGB Rule: 在代码中解析名称](https://pycoders.com/link/3809/web)
  - REAL PYTHON
In this step-by-step tutorial, you’ll learn what scopes are, how they work, and how to use them effectively to avoid name collisions in your code. Additionally, you’ll learn how to take advantage of a Python scope to write more maintainable and less buggy code.
(`是也乎:`
![LEGB](http://ydlj.zoomquiet.top/ipic/2020-03-25-ScreenShot%202020-03-25%2010.42.53.jpg)
LEGB 法则真的是无上真理,
但是, 官方并没约定一个固定的形式,
所以, 导致大家都在摸索自己的...
)
- [CPython 3.9.0a5 现在可用于测试](https://pycoders.com/link/3811/web)
  - PYTHON.ORG
- [DjangoCon Europe 2020 推迟到9月](https://pycoders.com/link/3805/web)
  - DJANGOPROJECT.COM

## 讨论
>
> Discussions

- [链式比较很屌!](https://pycoders.com/link/3792/web)
  - RAYMOND HETTINGER
Chained comparisons, like 0 < x < 5, are shorter, cleaner, and often faster than their more complex counterparts, such as (0 < x) and (x < 5).
- [数独益智盒包含平方数](https://pycoders.com/link/3807/web)
  - STACK OVERFLOW
How do you solve a Sudoku puzzle in Python? And if the puzzle has a solution, how can you tell if the solution is unique? In this Stack Overflow question, see how the z3 SMT solver can be used to answer both of these questions.
(`是也乎:`
Z3 SMT 求解器...魔幻工具..
)

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [从零开始 K-Nearest Neighbors](https://pycoders.com/link/3798/web)
  - PHILIPP MUENS
The k-Nearest Neighbors (k-NN) algorithm is a popular machine learning algorithm for classifying data. It has several neat features, including the fact that it doesn’t require a traditional training phase. While libraries like scikit-learn offer highly optimized black box implementations of k-NN, there’s no better way to understand how something works than to build it yourself. Learn how to do just that in this article from Philipp Muens.
(`是也乎:`

> From Scratch
和 Hand First/Awesome/... 类似, 也变成了一种流行风格了...
)

- [用 Pandas 和 SQLite 搞掂大型数据集的快速子集](https://pycoders.com/link/3800/web)
  - ITAMAR TURNER-TRAURING
“Let’s say you have a large amount of data, too large to fit in memory, and you want to load part of it into Pandas. If you’re only going to load one specific subset a single time, you can use chunking. But what if you need to load different subsets of the data at different times? Loading the whole file each time will be slow. What you need is a searchable index, and one easy (and fast!) way to do that is with SQLite.”
(`是也乎:`
SQLite 果断是 SQL 数据库中最快的...
)
- [在 Python 中实现 Levenshtein 距离](https://pycoders.com/link/3802/web)
  - AHMED FAWZY GAD
The Levenshtein distance is a metric for measuring the “distance” between two words in terms of the number of single-character edits required to transform one word into another. In this article, you’ll learn how to implement the Levenshtein distance in Python using a dynamic programming approach.
- [有关 Python math 模块: 您需要知道的一切](https://pycoders.com/link/3813/web)
  - REAL PYTHON
In this step-by-step tutorial, you’ll learn all about Python’s math module for higher-level mathematical functions. Whether you’re working on a scientific project, a financial application, or any other type of programming endeavor, you just can’t escape the need for math!
(`是也乎:`
![math](http://ydlj.zoomquiet.top/ipic/2020-03-25-ScreenShot%202020-03-25%2010.40.49.jpg)
)
- [Python 解释数学符号](https://pycoders.com/link/3815/web)
  - AMIT CHAUDHARY
You don’t need to know a lot of math to be a successful programmer, but there are times when a little bit of math knowledge can go a long way. In this article, author Amit Chaudhary shows you how to translate various mathematical symbols into Python code.
(`是也乎:`
数学符号实在是当年数学家很的私人狂欢,
行为艺术...
搞到现在给印刷和计算机留下多少坑哪...
)
- [如何用 Pandas read_html() 从 HTML 表格中提取数据](https://pycoders.com/link/3797/web)
  - ERIK MARSJA
In this article, Erik Marsja shows you how to scrape HTML tables using Pandas read_html(). You’ll first see how read_html() works by reading a simple table from an HTML string. Then you’ll take it up a notch and scrape some data from Wikipedia.
(`是也乎:`
其实...还是用专业模块吧, Pandas 作更加擅长的...
)
- [Twisted Matrix 实验室: Twisted 下架 Python 2.7 支持](https://pycoders.com/link/3822/web)
  - TWISTEDMATRIX.COM
“With the open-source Python community at large dropping Python 2.7 support in their projects, Twisted has decided to do the same. Twisted 20.3.0, the most recently released version, is the final release to offer Python 2.7 support.”
(`是也乎:`
类似这种就没办法了...
Py 2 的远去, 还是得全宇宙大力夯实才可能真正落实的...
)
- [重写 Dropbox 同步引擎核心](https://pycoders.com/link/3801/web)
  - DROPBOX.TECH
The Dropbox engineering team shares some reflections on what it took to rewrite the Dropbox sync engine (a 4+ year project!) and how they ultimately decided to scrap their Python code and rewrite the system in Rust.
(`是也乎:`
嗯哼? 现在用 Rust 来重构是政治正确了?
)
- [有关 Django 服务层更多信息](https://pycoders.com/link/3812/web)
  - JAMES BENNETT
Follow-up to last week’s post where James discussed the drawbacks of using a service layer architecture for building Django apps.
- [有效地使用 NumPy 的 np.arange()](https://pycoders.com/link/3806/web)
  - REAL PYTHON
  - video
Learn how to use the NumPy arange() function, which is one of the routines for array creation based on numerical ranges. np.arange() returns arrays with evenly spaced values
(`是也乎:`
![NumPy](http://ydlj.zoomquiet.top/ipic/2020-03-25-ScreenShot%202020-03-25%2009.54.11.jpg)
NumPy 是好东西, 但是, 直接用, 还是有点儿囧的...
)

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [superstring.py: 快速且内存优化的字符串库/用于重文本操作](https://pycoders.com/link/3793/web)
  - GITHUB.COM/BTWAEL
- [whynot: 用于动态决策的Python沙箱](https://pycoders.com/link/3820/web)
  - GITHUB.COM/ZYKLS
(`是也乎:`
项目名本身就是项目的意义...
)
- [MonkeyType: 通过收集运行时类型生成静态类型注释](https://pycoders.com/link/3821/web)
  - GITHUB.COM/INSTAGRAM
(`是也乎:`
这个, 有点象先吃好, 看着给点儿的意思...
)
- [z3: Z3定理证明](https://pycoders.com/link/3816/web)
  - GITHUB.COM/Z3PROVER
(`是也乎:`
![Z3Overall](https://github.com/Z3Prover/doc/raw/master/programmingz3/images/Z3Overall.jpg)
哦哦,支持多种语言的 定理推导 语言.
M$ 研究院还是隐藏着很多神仙想法的...
)
- [python-proxy-server: AWS Lambda 上的 Python 代理服务器](https://pycoders.com/link/3818/web)
  - IAN WHITESTONE
(`是也乎:`
![Lambda](https://ianwhitestone.work/images/free-proxy-server/architecture.png)
对 Lambda 的增强支持
)
- [stable-fluids: Jos Stam’s Stable Fluids 适用以 Python 3](https://pycoders.com/link/3799/web)
  - GITHUB.COM/GREGTJ
(`是也乎:`
![fluids](https://github.com/GregTJ/stable-fluids/raw/master/test.gif)
屌的..
)
- [itomate: 自动进行 iTerm 布局和会话设置](https://pycoders.com/link/3808/web)
  - GITHUB.COM/KAMRANAHMEDSE
(`是也乎:`
![itomate](https://github.com/kamranahmedse/itomate/raw/master/.github/assets/illustration.png)
挺美的...只是 tmux/screen 之后,
这种针对 iterm 的增强, 有什么使用场景?
)
- [PySimpleGUI-COVID19: 帮助分析 COVID-19 病毒传播的工具](https://pycoders.com/link/3795/web)
  - GITHUB.COM/PYSIMPLEGUI
  - • Shared by PythonistaCafe
(`是也乎:`
![PySimpleGUI](https://user-images.githubusercontent.com/46163555/76657707-dc855e00-6548-11ea-89cd-7c9f6b28978a.jpg)
GUI 框架都来蹭热点了...
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyWeek Games Programming Contest (Online)](https://pycoders.com/link/3810/web)
  - March 22 to March 30, 2020
- [TF Dev Summit viewing party 回看趴 \| Meetup](https://www.meetup.com/TensorFlow-User-Group-Zhuhai/events/269476226/)
  - 14:00~16:00
  - online

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [Academic-nCoV/2019-nCoV Wiki](https://github.com/Academic-nCoV/2019-nCoV/wiki)
  - github
(`是也乎:`
![nCoV 最新海外信息](http://ydlj.zoomquiet.top/ipic/2020-03-11-ScreenShot%202020-03-11%2019.32.08.jpg)
文科生的战斗, 虽然没办法象 wuhan2020 们那样快速组织工程师,
先于国家完成各种实用系统;
但是, 文科生通过大量海外报道的浏览/对比/翻译/报道/...
可以帮助人们通过真实世界的反应, 来更好的理解当前状态.
而且, 一个完全没有技术基础的文科团队, 自然通过 github 完成所有协同,
实在..感动 -> github 太好用了.
)

# PS

- 首发: [Issue 413 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-413.html)
- 修订: [issue-413.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-413.md)

-------------
>> NN 3963
好文笔,感叹号年度配额: **1/3**
-------------
ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**
就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):

```python
私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开课程: 蟒营 (订阅号: Mainium)
历史吐糟: Chaos42 (订阅号 PythoniCamp)
as 核心组织者:
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        TFUG珠海 (订阅号: ZH_TFUG)
```

-------------
