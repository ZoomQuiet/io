---
title: "Issue 446"
summary: ""
date: "2020-11-11T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> Python 正式世界第二
原文: [PyCoder's Weekly - Issue #446](https://pycoders.com/issues/446)
![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)

- 201111 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 201111 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------

- [在 Python 中作 Key-Driver 分析](https://pycoders.com/link/5153/web)
  - BRYCE MACHER
Take a look at how statistical knowledge plays an important role in answering business questions like “What drives the winningness of candy?” Along the way you’ll learn how to do Key-Driver analysis in Python on a problem that can’t be easily solved with a call to a machine learning library.
- [用 Python Defaultdict 类型处理缺少的键](https://pycoders.com/link/5161/web)
  - REAL PYTHON
  - course
In this step-by-step course, you’ll learn how the Python defaultdict type works and how to use it for handling missing keys when you’re working with dictionaries. You’ll also learn how to use a defaultdict to solve problems like grouping or counting the items in a sequence or collection.
(`是也乎:`
![Defaultdict](http://ydlj.zoomquiet.top/ipic/2020-11-11-ScreenShot%202020-11-11%2010.59.25.jpg)
`Defaultdict`
每种新类型, 都需要长久的扫盲.
)
- [机器学习的距离度量](https://pycoders.com/link/5176/web)
  - JAIME ZORNOZA
Many machine learning algorithmns can be summarized as transforming data to n-dimensional vectors and computing similarity between points by means of some distance metric. This article explores four of these metrics—the Euclidean, Manhattan, Minkowski, and Hamming distances—and how to compute them with Python.
- [在 Python 中用 LRU 策略进行缓存](https://pycoders.com/link/5165/web)
  - REAL PYTHON
Caching is an essential optimization technique. In this tutorial, you’ll learn how to use Python’s @lru_cache decorator to cache the results of your functions using the LRU cache strategy. This is a powerful technique you can use to leverage the power of caching in your implementations.
(`是也乎:`
![LRU](http://ydlj.zoomquiet.top/ipic/2020-11-11-ScreenShot%202020-11-11%2010.57.36.jpg)

> Least Recently Used (LRU) strategy
最小最新可用策略?
)

## 探讨/吐糟
>
> Discussions

- [Python 现在正式成为第二流行的编程语言](https://pycoders.com/link/5160/web)
  - REDDIT
(`是也乎:`
这可能意味着 Python 正式进入衰退期?
)
- [复盘数据科学家的第一年](https://pycoders.com/link/5167/web)
  - REDDIT

## 文章/教程/嗯哼
>
> Articles, Tutorials and Talks

- [用 Python 对电影评论进行情绪分类](https://pycoders.com/link/5159/web)
  - REAL PYTHON
In this tutorial, you’ll learn about sentiment analysis and how it works in Python. You’ll then build your own sentiment analysis classifier with spaCy that can predict whether a movie review is positive or negative.
(`是也乎:`
![Sentiment](http://ydlj.zoomquiet.top/ipic/2020-11-11-ScreenShot%202020-11-11%2010.54.17.jpg)
)
- [大数定律和中心极限定理 (用 Python)](https://pycoders.com/link/5178/web)
  - ARTI AGARWAL
Time for a Python-infused math lesson! The Law of Large Numbers and the Central Limit Theorem are fundamental concepts in statistics and machine learning. Learn how these theorems work with illustrative examples in Python.
- [世界需要程序媛](https://pycoders.com/link/5179/web)
  - SEEMA SAHARAN
Author Seema Saharan argues that now is better than ever for women to get started in the tech industry. Learn how she got started with coding, why she enjoys it, and why women should consider learning to code. The article is full of resources to help aspiring women coders get started with Python.
- [The Real Python 播客–第34集: Python 模运算符和用 SQLite 和 SQLAlchemy 管理数据](https://pycoders.com/link/5168/web)
  - REAL PYTHON
  - podcast
Are you ready to move beyond flat files for your data in Python? Maybe you’re not sure where to start with databases and SQL. This week on the show, David Amos returns with another batch of PyCoder’s Weekly articles and projects. We cover a Real Python article about managing data with SQLite and SQLAlchemy.
(`是也乎:`
![podcast](http://ydlj.zoomquiet.top/ipic/2020-11-11-ScreenShot%202020-11-11%2010.53.20.jpg)
)
- [用 10 行代码构建轻量级 Blog CMS](https://pycoders.com/link/5154/web)
  - STEVEN TEY
For small projects, many of the popular content manage systems, such as Wordpress or Medium, are overkill or potentially present significant downsides for authors. In this article, you’ll learn how to build a light-weight CMS in just a few lines of code!
(`是也乎:`

> ..我的朋友 linus ...
Flask-FlatPages 作者的语气很民国.
)

- [Flask 中的CSRF保护](https://pycoders.com/link/5169/web)
  - AMAL SHAJI
Cross-Site Request Forgery (CSRF) is an attack against a web application in which the attacker attempts to trick an authenticated user into performing a malicious action. Learn how to protect against CSRF attacks in Flask projects.
- [学习 Python 测试自动化](https://pycoders.com/link/5174/web)
  - ANDY KNIGHT
Python is a great language for test automation. Here’s a big list of resources to help you get started!
- [荷兰大气涡旋模拟的Python接口](https://pycoders.com/link/5172/web)
  - SCIENCEDIRECT.COM
Python is playing an increasingle large role in research science. This article discusses how one group of researches used Python to create a high-level interface to a popular Fortran simulation library for atmospheric simulation. Although academic, the article is approachable and provides insight into the methodology and frameworks used to make C and Fortran libraries more accessible.
- [Monty Python 和圣杯: 空载燕子的空速](https://pycoders.com/link/5151/web)
  - TREVOR ENGLISH
It’s a question for the ages: “what is the airspeed velocity of an unladen swallow?” Get your Monty Python kicks and do a little math. Can you come up with a Python script that answers the question?
(`是也乎:`
这种探索非常 XKCD.
)

## 好物/妙品/
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [tinygrad: 小型 Autograd Tensory 库](https://pycoders.com/link/5158/web)
  - GITHUB.COM/GEOHOT
You like pytorch? You like micrograd? You love tinygrad! ❤️ - geohot/tinygrad
- [allennlp: 基于 PyTorch 的开源 NLP 研究库](https://pycoders.com/link/5170/web)
  - GITHUB.COM/ALLENAI
- [pifuhd: 单幅图像的高分辨率 3D 数字化人类](https://pycoders.com/link/5175/web)
  - GITHUB.COM/FACEBOOKRESEARCH
- [omuse: 用于多物理和多尺度地球科学仿真的软件包](https://pycoders.com/link/5156/web)
  - GITHUB.COM/OMUSE-GEOSCIENCE
- [PyAnchor: 查找断开的链接,以便用户别点](https://pycoders.com/link/5166/web)
  - GITHUB.COM/ENDLESSTRAX • Shared by Ricky White

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyCon 瑞典 2020](https://pycoders.com/link/5173/web)
  - November 12 to November 14, 2020
- [⋅ PyCon Indonesia 2020 (在线)](https://pycoders.com/link/5157/web)
  - November 14 to November 16, 2020
- [⋅ PyHPC 2020: 9th Workshop ...(在线)](https://pycoders.com/link/5152/web)
  - November 15 to November 16, 2020
关于 Python 的高性能和科学计算第9次讲习班
![PyCon2020中国](http://ydlj.zoomquiet.top/ipic/2020-11-04-ScreenShot%202020-11-04%2008.51.39.jpg)
- PyCon2020中国
  - 11.28~29
  - 在线
- [⋅ Python Brasil 2020](https://pycoders.com/link/5113/web)
  - November 2 to November 9, 2020

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)
![14py](http://ydlj.zoomquiet.top/ipic/2020-10-28-barnner-101camp-wx14py.png)

# PS

- 首发: [Issue 446 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-446.html)
- 修订: [issue-446.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-446.md)

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
>> NN 4194
![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/446)
