Title: Issue 481
Slug: issue-481
Date: 2021-07-14 11:42
Tags: Weekly,Python,pycoders,ZH


> WASM 支持下跑在浏览器中的 Jupyter


原文: [PyCoder's Weekly - Issue #481](https://pycoders.com/issues/481)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210714 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210714 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [数据库事务太多](https://pycoders.com/link/6685/web)
    + HAKI BENITA

Learn how a bug was born — one that resulted in hundreds of users of an application getting a notification that they had been paid when in fact they had not! In this story, Haki Benita shares how a slip-up with Django signals caused him and his team quite a headache. You’ll learn how the application was architected, how the bug occurred, and how they fixed it, along with some other remedies to consider.


(`是也乎:`

这得怪 SQL, 以及框架的隔离...

)


- [在 2021 Python 打包状态](https://pycoders.com/link/6677/web)
    + BASTIAN VENTHUR 
    + opinion

What does Python packaging look like in 2021? What are the best tools to use? In this article, you’ll see one developer’s opinion about the state of Python packaging in 2021, what tools they are using the most often, and some thoughts on how the situation can continue to improve moving forward.

(`是也乎:`

![BASTIAN](http://ydlj.zoomquiet.top/ipic/2021-07-14-ScreenShot%202021-07-14%2012.28.33.jpg)


低产作者...知名作品:
[Creating Beautiful Github Streaks | Bastian Venthur's Blog](https://venthur.de/2020-12-30-streak.html)

)




- [Python 新闻: 2021 年 6 月有什么新变化?](https://pycoders.com/link/6682/web)
    + REAL PYTHON

June 2021 was full of notable events in the Python world! In this article, you’ll get caught up on what’s been happening with Python during this past month, including some changes at the Python Software Foundation and the announcement of a new recipient of the PSF Fiscal Sponsorship Program.

(`是也乎:`


![News](http://ydlj.zoomquiet.top/ipic/2021-07-14-ScreenShot%202021-07-14%2012.26.22.jpg)

)



- [Python 3.10.0b4 可用](https://pycoders.com/link/6692/web)
    + CPYTHON DEV BLOG

This is the last beta release, which means the next release will be the first release candidate.

- [Łukasz Langa -> 首位 CPython 筑地开发人员](https://pycoders.com/link/6673/web)
    + PYTHON SOFTWARE FOUNDATION


-----------------------------------------
## 探讨/吐糟
> Discussions


NULL


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [探索 Python 中 functools 模块和复数](https://pycoders.com/link/6683/web)
    + REAL PYTHON 
    + podcast

Are you ready to expand your Python knowledge into the intermediate to advanced territory? What tools are awaiting your discovery inside Python’s functools module? This week on the Real Python Podcast, David Amos is back, and he’s brought another batch of PyCoder’s Weekly articles and projects.


(`是也乎:`

![functools](http://ydlj.zoomquiet.top/ipic/2021-07-14-ScreenShot%202021-07-14%2012.24.10.jpg)

)


- [Pyflyby: 提高 Jupyter 交互式会话效率](https://pycoders.com/link/6681/web)
    + MATTHIAS BUSSONNIER 
    + AND AARON MEURER

There’s a new tool in town that aims to improve Python developer focus and minimize distractions while coding, especially in Jupyter Notebooks. That new tool is pyflyby, and it can handle tidying up and collecting imports and exports from Python modules. For example, in a Jupyter Notebook, pyflyby can automatically import the right modules and functions from NumPy if you use something in a cell without importing it first.



- [Copilot /用 Python 编写的文本游戏](https://pycoders.com/link/6675/web)
    + SAGINDYK URAZAYEV

GitHub’s new Copilot feature has a lot of people talking. The project’s goal is to be an AI pair programmer — a tool that can suggest entire lines of code or even entire functions! In this amusing article, one developer who gained access to Copilot’s technical preview shares how the AI wrote an entire text-based adventure game that turned out to be the solution to an exercise from a Python instructional book.


(`是也乎:`

TUI/CLI 永远是程序猿致亲,
优先折腾, 没毛病,

![vscode](http://ydlj.zoomquiet.top/ipic/2021-07-14-ScreenShot%202021-07-14%2012.22.03.jpg)

嗯哼, VSCode 出镜率越来越高,

> "workbench.colorTheme": "Solarized Dark"

也是最常见的...

)


- [更友好的 Tracebacks 在 REPLs (包含 Jupyter)](https://pycoders.com/link/6690/web)
    + ANDRÉ ROBERGE

Tracebacks are often the start of any Python debugging journey. But tracebacks can be difficult to read and confusing to beginners. The friendly-traceback project aims to lift the veil of confusion for tracebacks by providing more helpful error messages with lots of context. New updates to the project include better tracebacks in Jupyter Notebooks!


(`是也乎:`

可执行笔记们已经非常友好了,
还要友好化并错误追踪那真的是 IDE 了...


![Friendlier](http://ydlj.zoomquiet.top/ipic/2021-07-14-ScreenShot%202021-07-14%2012.19.03.jpg)

这种功能内巻值得越来越多

)


- [平方根函数在 Python](https://pycoders.com/link/6697/web)
    + REAL PYTHON 
    + course

In this quick and practical course, you’ll learn what a square root is and how to calculate one in Python. You’ll even see how you can use the Python square root function to solve a real-world problem.



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [jupyterlite: 在浏览器中运行由 WASM 驱动的 Jupyter](https://pycoders.com/link/6698/web)
    + GITHUB.COM/JTPIO

(`是也乎:`

浏览器就是 OS, 没跑了,
现在不允许运行浏览器的计算机基本无用...


)


- [pyflyby: 一套 Python 编程生产力工具](https://pycoders.com/link/6689/web)
    + GITHUB.COM/DESHAW

(`是也乎:`

专门支持了 Py2.7,
看来是公司长久使用的包, 现在开源了...
比如说这个 `py` 指令:

```
$ py b64decode aGVsbG8=
[PYFLYBY] from base64 import b64decode
[PYFLYBY] b64decode('aGVsbG8=', altchars=None)
'hello'

$ py log2 sys.maxint
[PYFLYBY] from numpy import log2
[PYFLYBY] import sys
[PYFLYBY] log2(9223372036854775807)
63.0

$ py 'plot(cos(arange(30)))'
[PYFLYBY] from numpy import arange
[PYFLYBY] from numpy import cos
[PYFLYBY] from matplotlib.pyplot import plot
[PYFLYBY] plot(cos(arange(30)))
<plot>

$ py 38497631 / 13951446
2.7594007818257693

$ py foo.py
```

不过, 要将这种超级包应用在生产中, 可就得有心理准备了...

)


- [multipledispatch: 一种在 Python 中进行多次调度/相对合理的方法](https://pycoders.com/link/6684/web)
    + GITHUB.COM/MROCKLIN

- [calcengine: 简单的 Python 计算引擎](https://pycoders.com/link/6686/web)
    + GITHUB.COM/BSDZ


(`是也乎:`
带 Simple 的一般都不简单,
毕竟在 Pythonic: `少是指数级的多`

)


- [tryceratops: 一个用于管理所有 Python 异常和 Try/Except 块的 Linter](https://pycoders.com/link/6691/web)
    + GITHUB.COM/GUILATROVA

(`是也乎:`

TDD 市场一直在发展,
可是...

)


- [django-postgres-extra: 为 Django 带来 PostgreSQL 的所有精彩](https://pycoders.com/link/6695/web)
    + GITHUB.COM/SECTORLABS

(`是也乎:`

至今 Wordpress 还是拒绝这种精彩

)

-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6678/web)
    + July 14, 2021

- [⋅ EuroPython 2021 (Virtual)](https://pycoders.com/link/6184/web)
    + July 26 – August 1, 2021

- [⋅ PyCon India 2021](https://pycoders.com/link/6052/web)
    + September 17 – 20, 2021



-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)


- [gruns/icecream: 🍦 Never use print() to debug again.](https://github.com/gruns/icecream)
    + github

(`是也乎:`

独创 logging + debug 模块

)


- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)

- [如何持证 \(SSL\) 开车 — 蟒营™ 怂怼录](https://blog.101.camp/ts/190130-jump-into-ssl/)
    + UPYUN

(`是也乎:`

私人初体验,
现在 http/https 资源混用浏览器越来越傲娇了,
最好有工具可以统一迁移...

)

-----------------------------------------
# PS:

- 首发: [Issue 481 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-481.html)
- 修订: [issue-481.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-481.md)


-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

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





