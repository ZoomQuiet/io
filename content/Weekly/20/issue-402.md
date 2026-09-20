---
title: "Issue 402"
summary: ""
date: "2020-01-08T12:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> Ubuntu 20.04 LTS 果断禁断 Python 2
原文: [PyCoder's Weekly - Issue #402](https://pycoders.com/issues/402)
![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200108 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200108 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------

- [最后的 Python 2.7 维护版本计划2020四月发布](https://pycoders.com/link/3235/web)
  - PYTHON.ORG
Python 2.7 is retired and became EOL on Jan 1, 2020. The last 2.7 release will be in April 2020.
- [Ubuntu 20.04 LTS 明确移除其 Python 2 依赖](https://pycoders.com/link/3230/web)
  - MICHAEL LARABEL
"With Python 2 having reached end-of-life at the start of 2020, Ubuntu and Debian developers continue their work on removing Python 2 at least from the base OS. Work continues on transitioning packages to Python 3 or otherwise ultimately dropping unmaintained packages."
(`是也乎:`
第一个重量级正式呼应.
)
- [Python *args 和 **kwargs 神秘化](https://pycoders.com/link/3246/web)
  - REAL PYTHON
  - video
Learn how to use args and kwargs in Python to add more flexibility to your functions. You'll also take a closer look at the single and double-asterisk unpacking operators, which you can use to unpack any iterable object in Python.
(`是也乎:`
![kwargs](http://ydlj.zoomquiet.top/ipic/2020-01-08-ScreenShot%202020-01-08%2015.00.53.jpg)
这么复杂的东西, 只能投降了...
)
- [俺对异步压力无感](https://pycoders.com/link/3244/web)
  - ARMIN RONACHER
"So for you developers of async libraries here is a new year's resolution for you: give back pressure and flow control the importance they deserve in documentation and API."
- [思考 Python 目标受众 \[2017\]](https://pycoders.com/link/3243/web)
  - NICK COGHLAN
Who is Python being designed for? CPython core dev Nick Coghlan discusses Python's and PyPI's target audience and design philosophy. Recommended reading.
- [DjangoCon 欧洲2020年发布](https://pycoders.com/link/3234/web)
  - DJANGOPROJECT.COM
DjangoCon Europe 2020 will take place in Porto, Portugal from May 27–31, 2020.
(`是也乎:`
今年是 葡萄牙...
)

## 讨论
>
> Discussions

- [您认为哪个鲜为人知的Python工具不可或缺?](https://pycoders.com/link/3237/web)
  - RAYMOND HETTINGER
ast.literal_eval() vs functools.lru_cache() vs pdb.pm() vs reprlib.recursive_repr() – Which one is your favorite?
(`是也乎:`
必不可缺又无人知晓的 Python 工具...
)

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [Python 包颂歌](https://pycoders.com/link/3239/web)
  - JAMES BENNETT
"Quite often, I see people being wrong on the internet about Python packaging. But the way in which they're wrong is subtle, and often passes unnoticed. The issue with much of the discussion is in conflating multiple different things under the term 'packaging', and failing to be clear exactly which of them is being discussed or criticized."
(`是也乎:`
Python 包的三合一圣讼精神
)
- [用 Pandas 和 Python 探索您的数据集](https://pycoders.com/link/3224/web)
  - REAL PYTHON
In this step-by-step tutorial, you'll learn how to start exploring a dataset with Pandas and Python. You'll learn how to access specific rows and columns to answer questions about your data. You'll also see how to handle missing values and prepare to visualize your dataset in a Jupyter notebook.
(`是也乎:`
![Pandas](http://ydlj.zoomquiet.top/ipic/2020-01-08-ScreenShot%202020-01-08%2014.55.58.jpg)
萌即正义..
)
- [Counting Queries: Django 中的基本性能测试](https://pycoders.com/link/3245/web)
  - FILIPE XIMENES
  - • Shared by Filipe Ximenes
"Testing application performance is hard and time consuming, but there's a type of test that is both easy to do and has a great impact in performance. In this blog post we will show how to unit test the number of queries to the database your application is making."
- [探索 NumPy 的 linspace() 函式](https://pycoders.com/link/3216/web)
  - AHMED GAD
NumPy supports different ways of generating arrays, and this tutorial is going to explore one way of do so, using the np.linspace() function. It returns evenly-spaced numbers and can generate arrays of any dimensionality.
- [测试生涯中需要的 pytest 功能](https://pycoders.com/link/3218/web)
  - MARTIN HEINZ
Tips that make your testing experience more enjoyable and more efficient, like filtering warnings, testing stdout/stderr, and parametrization.
(`是也乎:`
pytest 终于坐稳 TDD.py 首选了..
)
- [自动评分手写数学答题卡](https://pycoders.com/link/3222/web)
  - DIVYAPRABHA M
  - • Shared by Divyaprabha M
This article is about building a computer vision model to automatically grade handwritten mathematical worksheets using Python.
- [令 Python 程序 Blazingly Fast](https://pycoders.com/link/3249/web)
  - MARTIN HEINZ
"First rule of optimization is to not do it. But, if you really have to, then I hope these few tips help you with that."
- [对 单一服务 进行零停机部署](https://pycoders.com/link/3220/web)
  - ALEX BECKER
  - • Shared by Alex Becker
How PyDist achieves zero-downtime deploys without a typical load balancer and blue/green server infrastructure.
(`是也乎:`
所谓兰绿机制的部署管理..
)
- [如何用 Pyramid 和 Cornice 编写 Python Web API](https://pycoders.com/link/3217/web)
  - MOSHE ZADKA
Using Pyramid and Cornice to build and document scalable RESTful web services.
(`是也乎:`
好久没见 Pyramid 相关文章了...又复活了?
)
- [Guido van Rossum 访谈](https://pycoders.com/link/3228/web)
  - THE OXFORD UNION SOCIETY
  - video
(`是也乎:`
退休后, 老爹反而忙起来的样子...
)
- [2019年 StackOverflow 上 20 个最受好评的 Python 问题](https://pycoders.com/link/3225/web)
  - PYTHON-WEEKLY.BLOGSPOT.COM
(`是也乎:`
俺来看看前10都是什么
    0: 为毛 Python 无穷散列数字中有个 π? - [236/3]
    1: 有没有更优雅的表达方式(((x == a and y == b) 和 (x == b and y == a))?
    2: 为毛在 for 循环中可以用列表索引作为索引变量? -[92/6]
    3: 为毛 (inf + 0j)*1 等于 inf + nanj? - [93/4]
    4: 为毛带 f字符串的 f'{{{74}}}' 与 f'{{74}}'相同? -[88/1]
    5: 为毛 b 为列表时 b+=(4,) 可以, 而 b = b + (4,) 不行? - [75/7]
    6: 为毛 Python 从末尾索引列表时是从 -1(而不是0)开始? -[79/7]
    7: 为什么 TensorFlow 2 比 TensorFlow 1 慢得多? -[104/2]
    8: Python 的随机性 -[70/4]
    9: 为毛 Python允许序列使用超出范围的切片索引? -[72/2]
    ...
都很毛...
)
- [如何使用 Python 读取文件/写入并追加到文件](https://pycoders.com/link/3232/web)
  - ERIK MARSJA
- [Python 中的原子无锁计数器](https://pycoders.com/link/3240/web)
  - JULIEN DANJOU
(`是也乎:`
这个可以有
)

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [cachew: 持久性缓存/序列化 Powered by Type Hints](https://pycoders.com/link/3223/web)
  - GITHUB.COM/KARLICOSS
- [tmtoolkit: 文本挖掘和主题建模工具包](https://pycoders.com/link/3221/web)
  - GITHUB.COM/WZBSOCIALSCIENCECENTER
  - • Shared by Markus Konrad
- [vidgear: 适用于 Python 的视频处理框架](https://pycoders.com/link/3233/web)
  - GITHUB.COM/ABHITRONIX
(`是也乎:`
![vidgear](https://camo.githubusercontent.com/7eb66b31e45072cd99ee988690242b93388705db/68747470733a2f2f6162686974726f6e69782e6769746875622e696f2f696d672f766964676561722f766964676561725f66756e6374696f6e322d30312e737667)
组合解决各种场景/平台中视频常用处理流水的框架...
所图乃大哪...
)
- [sheetfu: 与 Google Sheets V4 API 交互的 Python 库](https://pycoders.com/link/3226/web)
  - GITHUB.COM/SOCIALPOINT-LABS
(`是也乎:`
叕一个 docs.google 次生态作品, 当然, 对于我们不存在的...
)
- [karateclub: 图形数据结构的无监督学习](https://pycoders.com/link/3242/web)
  - GITHUB.COM/BENEDEKROZEMBERCZKI
- [ElasticBatch: Easy Elasticsearch Inserts for Data Processing Workflows](https://pycoders.com/link/3231/web)
  - GITHUB.COM/DKASLOVSKY
  - • Shared by Daniel Kaslovsky
- [switchenv: Python-Based 工具, 用于管理Bash环境](https://pycoders.com/link/3241/web)
  - GITHUB.COM/ROBDMC
  - • Shared by Rob deCarvalho
(`是也乎:`
将 Pyenv 的技巧, 单纯抽象为管理系统环境变量,
自动化批量切换不同运行场景时的一组环境变量..
)
- [codetiming: 灵活, 可定制的 Timer for Your Python Code](https://pycoders.com/link/3248/web)
  - PYPI.ORG
(`是也乎:`
叕一个计时器, 不过,这个项目使用了 真蟒 插图, 也不知道是否授权...

> from codetiming import Timer
As a class:
    t = Timer(name="class")
    t.start()
    # Do something
    t.stop()
As a context manager:
    with Timer(name="context manager"):
        # Do something
As a decorator:
    @Timer(name="decorator")
    def stuff():
        # Do something
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Heidelberg Python Meetup](https://pycoders.com/link/3206/web)
  - January 8, 2020
  - 德国
- [⋅ Python North East](https://pycoders.com/link/3207/web)
  - January 8, 2020
  - 大英
- [⋅ PyStaDa](https://pycoders.com/link/3213/web)
  - January 8, 2020
  - Darmstadt
  - 德国
- [⋅ pyCologne User Group Treffen](https://pycoders.com/link/3208/web)
  - January 8, 2020
  - 404
- [⋅ Santa Cruz Python Meetup](https://pycoders.com/link/3212/web)
  - January 8, 2020
  - USA
- [⋅ PyMNTos](https://pycoders.com/link/3209/web)
  - January 9, 2020
  - USA
- [⋅ Python Atlanta](https://pycoders.com/link/3205/web)
  - January 9, 2020
  - USA
- [⋅ Yola Python Club 2020](https://pycoders.com/link/3204/web)
  - January 11 to January 12, 2020
  - 尼日利亚
- [⋅ Python Miami](https://pycoders.com/link/3211/web)
  - January 11 to January 12, 2020
  - USA

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- **[蟒营 Python 入门班](https://py.101.camp/)**
  - 5py ;-)
(`(￣▽￣)`:
第4期马上结业:
    200112 按时结束
年后第5期就来:
    20.2.3 可以上线
    20.3.1 正式开课
)
- [从1965年到2019年,最受欢迎的编程语言 (动画)](https://pycoders.com/link/3100/web)
  - TWITTER.COM/MARCUSBORBA
(`是也乎:`
网红小视频也出现了...
最后3秒, Python 疯狂反转一切.
)

# 是也乎
>
> NN 3886

- 首发: [Issue 402 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-402.html)
- 修订: [issue-402.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-402.md)
