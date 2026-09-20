Title: PyCoder 497
Slug: issue-497
Date: 2021-11-03 11:42
Tags: Weekly,Python,pycoders,ZH


>  zipapp 值得认真用卟?


原文: [PyCoder's Weekly - Issue #497](https://pycoders.com/issues/497)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 211103 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成快译
- 211103 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [Python 并发可行性解决方案](https://pycoders.com/link/7343/web)
    + JONATHAN CORBET

“The end result thus appears to be a GIL-removal effort that has a rather better-than-average chance of making it into the CPython interpreter. That would be cause for a lot of rejoicing among Python developers. That said, a change this fundamental is unlikely to be rushed into the CPython mainline; it will take a lot of testing to convince the community that it is ready for production use.”


(`是也乎:`

COOL,
不过, 等等, 为什么一定要可视化?


)


- [Django 模板: 对 Tags and Filters 实施习惯](https://pycoders.com/link/7320/web)
    + REAL PYTHON

Django templates have many built-in tags and filters to render content, but they may not meet all your needs. This tutorial covers how to write Django custom template tags and filters, including simple tags, inclusion tags, block tags, and different types of filters.


(`是也乎:`

![Templates](https://ipic.zoomquiet.top/2021-11-03-ScreenShot%202021-11-03%2011.30.31.jpg)

)



- [Python’s zipapp 模块: 构建可执行的ZIP应用程序](https://pycoders.com/link/7326/web)
    + REAL PYTHON

In this step-by-step tutorial, you’ll learn what Python Zip applications are and how to create them quickly using the zipapp module from the standard library. You’ll also learn some alternative tools you can use to build this kind of application manually.

(`是也乎:`

万千 VB 程序猿 最爱的 Python 模块了

![zipapp](https://ipic.zoomquiet.top/2021-11-03-ScreenShot%202021-11-03%2011.30.04.jpg)

)



- [Infix 运算符 (Python 配方)](https://pycoders.com/link/7339/web)
    + ACTIVESTATE.COM

Python has the in operator and it would be nice to have additional infix operator like this. This recipe shows how (almost) arbitrary infix operators can be defined in vanilla Python: x |op| y or x <<op>> y

(`是也乎:`

ACTIVESTATE 公司免费公开运营几十年的 Recipe
应该是最早最成功的贴吧以及QA 社区了

)



- [PSF 社区服务奖项提名](https://pycoders.com/link/7335/web)
    + PYTHON.ORG

Do you know of a deserving individual who should be considered for a PSF Community Service Award? The PSF is accepting nominations for the Q4 2021 Community Service Award.




-----------------------------------------
## 探讨/吐糟
> Discussions


- [在编码面试中/我如何修改Python字符串](https://pycoders.com/link/7329/web)
    + REDDIT

- [在 OrderedDict and dict 中关键词顺序一样嘛?](https://pycoders.com/link/7347/web)
    + STACK OVERFLOW




- [是否有一种方法可以在 Python≥3.10 中用模式匹配不等式 ?](https://pycoders.com/link/7348/web)
    + STACK OVERFLOW



-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [通过重构更大的函数来理解复杂代码](https://pycoders.com/link/7330/web)
    + TEST & CODE 
    + podcast
“To understand complex code, it can be helpful to remove abstractions, even if it results in larger functions. This episode walks through a process I use to refactor code that I need to debug and fix, but don’t completely understand.”


- [用 FunctionTrace 优化Python代码 ](https://pycoders.com/link/7321/web)
    + MATT BRYANT

“I recently did a quick optimization pass over glyphsLib, using FunctionTrace to improve performance by ~30% in under half an hour. This is writeup of my approach, which should be mostly extensible to optimizing other codebases.”








- [在 Python 中读取输入和写入输出](https://pycoders.com/link/7323/web)
    + REAL PYTHON
    + course

In this introductory Python course, you’ll learn how to take user input from the keyboard with the built-in function input() and how to display output to the console with the built-in function print().

(`是也乎:`

![course](https://ipic.zoomquiet.top/2021-11-03-ScreenShot%202021-11-03%2011.25.28.jpg)

)


- [用 borb 在 python 中创建和操纵 pdf](https://pycoders.com/link/7349/web)
    + REAL PYTHON 
    + podcast

Have you wanted to generate PDFs from your Python project? This week on the show, it’s Joris Schellekens talking about his library for creating and manipulating PDFs named borb.

(`是也乎:`
![podcast](https://ipic.zoomquiet.top/2021-11-03-ScreenShot%202021-11-03%2011.24.51.jpg)

borb 的广告已经嗯哼了两个月

)


- [Pyston Python 实现路线图](https://pycoders.com/link/7332/web)
    + KEVIN MODZELEWSKI

“We’ve spent some time recently thinking about the future of Pyston, our faster implementation of Python, and wanted to share what’s on our mind.”


(`是也乎:`

老爹另启炉灶之后的 Pyston...

)


- [Pants 2.8 支持 PEP 517: 轻松构建 Python 本机扩展](https://pycoders.com/link/7346/web)
    + BENJY WEINBERGER


Pants is a software build system. It orchestrates the various tools and steps that process your source code into deployable software.


(`是也乎:`

新裤子乐队指定代言模块

)


- [PyDev of the Week: Tzu-ping Chung](https://pycoders.com/link/7336/web)
    + MIKE DRISCOLL

Tzu-ping is a member of Python Packaging Authority (PyPA) and a maintainer of pip and pipx.

- [用 Pants and PEX 精简 Docker 构建](https://pycoders.com/link/7325/web)
    + BENJY WEINBERGER


(`是也乎:`


其实还是并行化更加需要2一些?
反正就是越来越快, 最好不要消耗时间.

)


- [在 coverage.py 中进行覆盖承诺](https://pycoders.com/link/7324/web)
    + NED BATCHELDER

(`是也乎:`



覆盖测试工具自身的覆盖要求...

)



-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [detr: 有 Transformers 的 End-to-End 对象检测 ](https://pycoders.com/link/7345/web)
    + GITHUB.COM/FACEBOOKRESEARCH




- [pyhpc-benchmarks: 最受欢迎的 CPU和GPU 基准测试Python libs ](https://pycoders.com/link/7333/web)
    + GITHUB.COM/DIONHAEFNER

(`是也乎:`

强测集

)


- [structlog: Python的结构日志](https://pycoders.com/link/7350/web)
    + STRUCTLOG.ORG

(`是也乎:`

![structlog](https://ipic.zoomquiet.top/2021-11-03-ScreenShot%202021-11-03%2011.19.05.jpg)


足够可爱,
对终端有极高要求, windows 就囧了...

)


- [Dataconf: 具有自动 Dataclasses 解析能力的配置库](https://pycoders.com/link/7319/web)
    + GITHUB.COM/ZIFEO • Shared by Teo

(`是也乎:`

反正能自动化的, 一定会自动化

)


- [epilog: Docker Container Log Aggregation With Elasticsearch, Kibana, and Filebeat](https://pycoders.com/link/7318/web)
    + GITHUB.COM/REDNAFI 
    • Shared by Redowan Delowar

(`是也乎:`

ELK 虽然好, 但是, 还是应该更加简洁些...

)


- [Closember: 当月 Close/Merge  Issues and PR 数量排名](https://pycoders.com/link/7322/web)
    + CLOSEMBER.ORG


(`是也乎:`

![Closember](https://ipic.zoomquiet.top/2021-11-03-ScreenShot%202021-11-03%2011.12.41.jpg)

不以 star 为荣,
而应该以关闭 issue 为耀


)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyCon Chile](https://pycoders.com/link/7338/web)
    + November 5 to November 8, 2021

- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/7351/web)
    + November 6, 2021

- [⋅ Edmonton Python User Group](https://pycoders.com/link/7337/web)
    + November 8, 2021

- [⋅ IndyPy Monthly Meetup](https://pycoders.com/link/7342/web)
    + November 9, 2021

- [⋅ TuPLE (Tucson Python Language Enthusiasts)](https://pycoders.com/link/7340/web)
    + November 9, 2021

- [⋅ deploy by DigitalOcean](https://pycoders.com/link/7356/web)
    + November 16 to November 17, 2021




-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)




- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
    + 哔哩哔哩

(`是也乎:`

老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:

![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)

)



-----------------------------------------
# PS:

- 首发: [Issue 497 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-497.html)
- 修订: [issue-497.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-497.md)


## PPS:
> 不觉中蟒周刊快译已经到了第9个年头

去年开始有小伙伴加入承担 `pythonisa` 周刊的翻译,
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

-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF497D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF497D4Q90XdDA7g):



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





