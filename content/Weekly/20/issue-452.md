---
title: "Issue 452"
summary: ""
date: "2020-12-23T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> Python 3.10a3 发布
原文: [PyCoder's Weekly - Issue #452](https://pycoders.com/issues/452)
![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)

- 201223 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 201223 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------

- [Python 软件基金会 2020 募捐](https://pycoders.com/link/5408/web)
  - PYTHON.ORG
“COVID-19 has changed all aspects of our lives and is reshaping our future. Nonprofits like the PSF are having to rebuild. With PyCon 2020 and 2021 happening virtually, the PSF is faced with potentially losing $1.2 million USD of expected revenue for those two years. This fundraiser is critically important and the money raised will help the PSF support the tools and initiatives that Pythonistas use everyday.”
(`是也乎:`
Pythonistas 年度咨文,
值得动员日本分部漫画化.
将今年损失的 120万$ 找回来.
)
- [建立自己的国际象棋引擎](https://pycoders.com/link/5383/web)
  - ANDREW HEALEY
Writing your own chess engine is a great way to explore computational complexity and combinatorial aspects of programming. Not to mention it’s pretty fun! Follow along with this reflection on how one coder created his own Chess engine from scratch.
(`是也乎:`
反正, 没人折腾 go 的.
)
- [用 Python pickle 模块序列化对象](https://pycoders.com/link/5406/web)
  - REAL PYTHON
  - course
Learn how you can use the Python pickle module to convert your objects into a stream of bytes that can be saved to a disk or sent over a network. You’ll also learn the security implications of using this process on objects from an untrusted source.
(`是也乎:`
![Serializing](http://ydlj.zoomquiet.top/ipic/2020-12-23-ScreenShot%202020-12-23%2010.06.27.jpg)
等等, 官方已经不推荐用 pickle 了哪..
)
- [Python 真的是瓶颈吗?](https://pycoders.com/link/5394/web)
  - ANNA ANISIENIA
Python is slow. From one perspective, that is. But what are the true bottlenecks in the data engineering/data processing space, and how does Python compare to other technologies when those factors are considered?
(`是也乎:`
工具的瓶颈并不是工程的,
人思想的瓶颈才一直是.
)
- [用 PyQt 的 QThread 防止 GUI 冻结](https://pycoders.com/link/5382/web)
  - REAL PYTHON
In this step-by-step tutorial, you’ll learn how to prevent freezing GUIs by offloading long-running tasks to worker QThreads in PyQt.
(`是也乎:`
![QThread](http://ydlj.zoomquiet.top/ipic/2020-12-23-ScreenShot%202020-12-23%2010.00.55.jpg)
其实, 就是 Qt 不得不接管系统的各种职责在完成自我控制.
)
- [Python 3.10a3 发布](https://pycoders.com/link/5393/web)
  - PYTHON.ORG
See what changes Python 3.10 will bring
- [新指导委员会选出ed](https://pycoders.com/link/5396/web)
  - TWITTER.COM/PYBLOGSAL

## 探讨/吐糟
>
> Discussions
NONE

## 文章/教程/嗯哼
>
> Articles, Tutorials and Talks

- [如何用 np.linspace 管理内存和创建数组](https://pycoders.com/link/5385/web)
  - REAL PYTHON
  - podcast
Have you wondered how Python manages memory? How are your variables stored in memory, and when do they get deleted? This week on the show, David Amos is here, and he has brought another batch of PyCoder’s Weekly articles and projects. Along with the Real Python article on Python memory management, we also talk about another article about creating even and non-even spaced arrays in Python with np.linspace.
(`是也乎:`
等等, 上周也说了这事儿? 是系列?
![podcast](http://ydlj.zoomquiet.top/ipic/2020-12-23-ScreenShot%202020-12-23%2009.56.35.jpg)
)
- [用 Python 和 Scikit-Learn 进行 OPTICS 聚类](https://pycoders.com/link/5387/web)
  - CHRISTIAN VERSLOOT
Clustering is a big part of unsupervised machine learning. Since no labels are available, data point must be grouped, or clustered, based on some similarity measure. OPTICS is a clustering algorithm, and in this article you’lol learn how to use it with the Scikit-Learn library.
- [pass 语句: 如何在Python中无所事事](https://pycoders.com/link/5388/web)
  - REAL PYTHON
In this tutorial, you’ll learn about the Python pass statement, which tells the interpreter to do nothing. Even though pass has no effect on program execution, it can be useful. You’ll see several use cases for pass as well as some alternative ways to do nothing in your code.
(`是也乎:`

>> 无为而治
![pass](http://ydlj.zoomquiet.top/ipic/2020-12-23-ScreenShot%202020-12-23%2009.56.07.jpg)
)

- [用 Python 可视化 Mandelbrot 集](https://pycoders.com/link/5402/web)
  - BLAKE SANIE
The Mandelbrot set is fractal and infinitely self-similar. Fortunately, you can write a finite Python program to visualize it! Have some fun creating beautiful pictures with this tutorial.
(`是也乎:`
![Mandelbrot](http://ydlj.zoomquiet.top/ipic/2020-12-23-ScreenShot%202020-12-23%2010.13.26.jpg)
用不到50行代码,
就可实现无限分形的绘制...
只引用了:
    from PIL import Image
    import colorsys
    import math
    import os
核心就是 math 标准计算.
)
- [用 Python 生成 STL 模型](https://pycoders.com/link/5389/web)
  - CARLO SUPINA
Learn how to use the numpy-stl library to create STL files that can be loaded into CAD software and used to create 3D printed shapes.
- [基于Django 会话的 Auth 用以单页应用程序](https://pycoders.com/link/5401/web)
  - NIK TOMAZIC
  - • Shared by Michael Herman
Learn how to add session-based authentication to a Single-Page Application powered by Django and React.
(`是也乎:`
所以, Django 也开始 Liveshow, 向 Phoenix 学习?
)
- [佛罗里达的 Python 嗅探犬开始成功追踪入侵物种](https://pycoders.com/link/5403/web)
  - ANN SCHMIDT
Watch out pythons! These dogs are on your trail.

## 好物/妙品/
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [hiplot: HiPlot 令理解高维数据变得容易](https://pycoders.com/link/5392/web)
  - GITHUB.COM/FACEBOOKRESEARCH
(`是也乎:`
高维数据原本就是人类创造出来的数学工具,
理解这种纯粹理论概念, 可视化可能并不是最好...
)
- [numpy-stl: 用于处理 STL 文件和 3D 对象的库](https://pycoders.com/link/5380/web)
  - GITHUB.COM/WOLPH
(`是也乎:`
等等, 3D对象原先都不是标准 NumPy 矩阵对象?
)
- [PsychRNN: 针对认知任务训练递归神经网络模型的包](https://pycoders.com/link/5390/web)
  - GITHUB.COM/MURRAYLAB
- [PETAL: 深度生物途径分析工具](https://pycoders.com/link/5384/web)
  - GITHUB.COM/PEX2892
(`是也乎:`
生物技术原本就是 Python 基本盘
)
- [A Day in Code: Python, 用代码编写的图画书 by Shari Eskenas](https://pycoders.com/link/5391/web)
  - KICKSTARTER.COM
(`是也乎:`
![KICKSTARTER](http://ydlj.zoomquiet.top/ipic/2020-12-23-ScreenShot%202020-12-23%2009.48.05.jpg)
电子书众筹
)
- [questionary: 构建漂亮的命令行用户提示](https://pycoders.com/link/5381/web)
  - GITHUB.COM/TMBO
(`是也乎:`
![questionary](http://ydlj.zoomquiet.top/ipic/2020-12-23-ScreenShot%202020-12-23%2010.19.21.jpg)
在 CLI 中实现菜单以及多选项...
前提是有在一个现代终端中,
cmd 就别想了...
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/5404/web)
  - December 23, 2020
- [⋅ Python Pizza New Year’s Party (Virtual)](https://pycoders.com/link/5395/web)
  - December 31 to January 1, 2021
(`是也乎:`
在国外来个 Pizza 就是过年了
)
- [⋅ BelPy](https://pycoders.com/link/5398/web)
  - January 30 – 31, 2021
- [⋅ PyCascades 2021 (Virtual)](https://pycoders.com/link/5400/web)
  - February 19 – 21, 2021
- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5386/web)
  - May 12 – 18, 2021
(`是也乎:`
嗯哼?明年的已经定档了?
PyCon中国何时能成功提档到上半年, 证明成熟?
)
![PyCon2020中国](http://ydlj.zoomquiet.top/ipic/2020-11-04-ScreenShot%202020-11-04%2008.51.39.jpg)
- [PyCon2020中国, 明年见](https://mp.weixin.qq.com/s/9u4NP0CAzZMqy96C9y-OHg)
  - 11.28~29
  - 在线
(`是也乎:`
[PyCon20深圳 大妈 暖场小单口](https://mp.weixin.qq.com/s/OrHA4vimeHUYDROQ9G75GA)
并实锤可用神器:
[NixOS - NixOS Linux](https://nixos.org/)
nix 可以跨语言非Docker 将开发和运行时环境精确锁定.
以及 PyCon19广州 的坑终于填上了:
- [欢迎使用 lightning](https://gitmen.gitee.io/lightning-doc/)
  - [GitHub](https://github.com/git-men/lightning)
  - [OSC](https://gitee.com/gitmen/lightning)
基于Django的无代码Admin + 低代码开发框架
)

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)
None

# PS

- 首发: [Issue 452 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-452.html)
- 修订: [issue-452.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-452.md)

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
>> NN 4236
![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/452)
