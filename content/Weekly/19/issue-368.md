---
title: "Issue 368"
summary: ""
date: "2019-05-15T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

原文: [PyCoder's Weekly - Issue #368](https://pycoders.com/issues/368)
![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)
------

- [CPython 3.8.0a4 已可测试](https://pycoders.com/link/1604/web)
  - PYTHON.ORG
Among the new major new features and changes so far: Assignment expressions (PEP 572), Positional-only arguments (PEP 570), multiprocessing can now use shared memory to avoid pickling, typed_ast is back.
- [用 Python 播放和录制声音](https://pycoders.com/link/1593/web)
  - REAL PYTHON
In this tutorial, you'll learn about libraries that can be used for playing and recording sound in Python, such as PyAudio and python-sounddevice. You'll also see code snippets for playing and recording sound files and arrays, as well as for converting between different sound file formats.
(`是也乎:`
![Sound](https://files.realpython.com/media/Playing-and-Recording-Sound-in-Python_Watermarked.e9aac7628df3.jpg)
总之有太多模块可以使用,
但是, 没有完美解决所有问题的...
所以, 要组合来嗯哼...
推荐外部专用软件来嗯哼, python 就进行管理就好.
)
- [Dropbox 客户端如何用 Python](https://pycoders.com/link/1615/web)
  - ANVILVENTURES.COM
"This blog post talks about reverse engineering the Dropbox client, breaking its obfuscation mechanisms, de-compiling it to Python code as well as modifying the client in order to use debug features which are normally hidden from view."
(`是也乎:`
![litb_tracing](https://anvilventures.com/blog/images/litb_tracing.png)
终于有人站出来分析靠谱的 py 客户端技巧了...
![litb_debugging](https://anvilventures.com/blog/images/litb_debugging.png)
虽然有麻烦, 但是, 都能嗯哼掉
)
- [Python GIL 是否已 Slain?](https://pycoders.com/link/1606/web)
  - ANTHONY SHAW
A discussion of PEP554 (subinterpreters) and how it relates to the global interpreter lock (GIL) in CPython.
(`是也乎:`
有关 PEP 的讨论越来越公开了...
毕竟, BDLF 退位了, 大家终于能愉快的吵架了...
)
- [PEP 554 将终结 GIL 嘛?](https://pycoders.com/link/1607/web)
  - PYTHON BYTES podcast
Another discussion of subinterpreters (PEP 554) and how they will allow true in-process parallelism.
- [可能不会在 Python 3 中使用的, 但, 应该](https://pycoders.com/link/1592/web)
  - VINKO KODŽOMAN
(`是也乎:`
叕一则鼓动使用 py3 新特性的文章...
问题是, 用 py2 的经验来写 py3 并无太大不同哪...
)

## 讨论
>
> Discussions

- [Epic Medieval Painting of GvR](https://pycoders.com/link/1619/web)
  - IMGUR.COM
It was auctioned off at PyCon 2019.
- ["Controversial Random Thought on OOP in Python"](https://pycoders.com/link/1616/web)
  - RAYMOND HETTINGER
Inheritance vs Composition
(`是也乎:`
OOP 早已证明不是银弹, 为毛一直在讨论?
嗯哼, JAVA 在努力续命...
)

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [Python 应用的最佳 Docker 基础映像](https://pycoders.com/link/1600/web)
  - ITAMAR TURNER-TRAURING
Which Docker image should you use for your Python app? There are many choices, and it may not be obvious which is the best for your situation. This article gives you a good overview of the current options available.
(`是也乎:`
    嫑用 Alpine Linux
    嫑用 Alpine Linux
    嫑用 Alpine Linux
)
- [用 PyLint 编写更干净的 Python 代码](https://pycoders.com/link/1622/web)
  - REAL PYTHON video
In this video series you'll see how to install and set up the PyLint code linter tool. You'll learn why you should use code linters like PyLint, Flake8, PyFlakes, or other static analysis tools—and how they can help you write cleaner and more Pythonic code.
(`是也乎:`
![PyLint](https://files.realpython.com/media/Intermediate_Watermarked.9f8c0a24bde7.jpg)
嗯哼, 这次插图就不搭调了...
)
- [用 Python 查找最便宜的多程旅行航班](https://pycoders.com/link/1590/web)
  - NVBN.GITHUB.IO
"I was able to find the cheapest flights with the minimal duration and the resulting prices were almost the same as on Google Flights."
- [Python 3.8 中的 F字符串调试](https://pycoders.com/link/1621/web)
  - TIRKARTHI.GITHUB.IO
F-Strings will get a = format specifier that expands like a macro into <variable_name> = <value_of_variable> to serve as a debugging aid.
- [让 Google 知道您 Django 网站中的其他语言](https://pycoders.com/link/1603/web)
  - HAKI BENITA
If you have a public facing Django site in multiple languages, you probably want to let Google and other search engines know about it. This article shows you the minimal setup necessary to support this use case.
- [Pandas 输出风格化](https://pycoders.com/link/1620/web)
  - CHRIS MOFFITT
Pandas has a relatively new API for styling output. This article shows examples of using the style API.
- [Django 搜索教程](https://pycoders.com/link/1614/web)
  - WILLIAM VINCENT
How to add basic search functionality to any Django website.
- [Python Dicts 和内存使用](https://pycoders.com/link/1610/web)
  - REUVEN LERNER
- [在 Python 中用 Altair 进行大部分可视化的原因](https://pycoders.com/link/1602/web)
  - FERNANDO IRARRÁZAVAL
(`是也乎:`
叕一个声明式数据可视化库,
但是, 和 Bokeh 相比, 都少了一个 HTML 输出能力
)

## 好物
>
> Interesting Projects, Tools and Libraries

- [Pint: 定义,操作和操纵物理量](https://pycoders.com/link/1591/web)
  - PINT.READTHEDOCS.IO
(`是也乎:`
专注各种物理量之间的转化...
嗯哼, 反正时间是最麻烦的...
)
- [plotnine: Python 图形语法,基于ggplot2](https://pycoders.com/link/1613/web)
  - GITHUB.COM/HAS2K1
- [machine-learning-course: 用 Python 进行 Machine Learning 课程](https://pycoders.com/link/1611/web)
  - GITHUB.COM/MACHINELEARNINGMINDSET
(`是也乎:`
![supervised](https://github.com/machinelearningmindset/machine-learning-course/raw/master/_img/supervised.gif)
叕一系列开源 AI 课程,
)
- [cloudmarker: 云监控工具和框架](https://pycoders.com/link/1618/web)
  - GITHUB.COM/CLOUDMARKER
- [pishot: 用 Raspberry Pi 相机捕获高速频闪图像](https://pycoders.com/link/1599/web)
  - GITHUB.COM/REVALO
(`是也乎:`
所以, pi 开始的项目, 都不念 `屁` -> 应该是 `派`
)
- [open-spelling-bee: Terminal-Based Python Clone of New York Times' Puzzle Game "Spelling Bee"](https://pycoders.com/link/1601/web)
  - GITHUB.COM/PHILSHEM
(`是也乎:`
    Type !help or !h for help
    Playing puzzle index: 1
    Your letters are:
                _____
               /     \
              /       \
        ,----(    N    )----.
       /      \       /      \
      /        \_____/        \
      \   H    /     \    U   /
       \      /       \      /
        )----(    R'   )----(
       /      \       /      \
      /        \_____/        \
      \   G    /     \    D   /
       \      /       \      /
        `----(    O    )----'
              \       /
               \_____/
    Max score: 88
    Total words: 37
    Your guess: GROUND
非常经典的拼写游戏了...
RMS 在 emcase 中经常玩...
)
- [django-restql: Dynamically Select Only a Subset of Fields Per DRF Resource](https://pycoders.com/link/1595/web)
  - GITHUB.COM/YEZYILOMO
  - • Shared by Yezy Ilomo

## 📆🐍 活动/大会
>
> Events

- [⋅ PyCon Africa Still Accepting Talk Proposals](https://pycoders.com/link/1597/web)
  - 非洲
- [⋅ EuroPython 2019 Early-Bird Ticket Sales Open](https://pycoders.com/link/1605/web)
  - July 8 – 14 in Basel,
  - Switzerland
- [⋅ Python Northwest](https://pycoders.com/link/1609/web)
  - May 16, 2019
  - UK 西北偏北
- [⋅ Karlsruhe Python User Group (KaPy)](https://pycoders.com/link/1596/web)
  - 德国
  - May 17, 2019

## DAMA
>
> ❤️ Happy Pythonic!
(`大妈私人无责任播报`)

- [I'm desperately searching a good \(and equivalent feature\-wise\) for COLT, anyone have found one ? : firefox](https://www.reddit.com/r/firefox/comments/6sw9t1/im_desperately_searching_a_good_and_equivalent/)
  - FireFox
  - 57+
(`是也乎:`
FF 自己作死, 闷杀了以往杀出重围的利器 -> 扩展生态
参考: [嫑升级 FireFox 到 56 以上](https://du.101.camp/2017-11/ff-no-upgrade/)
前几天又故意关闭了扩展认证...以至老版本 FF 中可用 扩展 也全部失效...
依赖的一系列精选生产力扩展无法使用, 只能全部迁移到 WaterFox 中;
这才恢复 ScrapBook 的的所有体验;
CoLT 也有一半功能失常, 今天又根据分享, 用 FormatLink 完成替代...
[Legacy Firefox extensions - index](https://legacycollector.org/firefox-addons/)
是收集过往传奇扩展并支持下载的非官方网站...
现在就差 [docwhat/itsalltext: It's All Text\! \- Edit textareas in your browser with your favorite editor\!](https://github.com/docwhat/itsalltext)
的完美替代了...
)
- [蟒营 Python 入门班](https://py.101.camp/)
  - 已开班, 进入 ch05
  - 下期可能 7月中

### Jobs
>
> ...

- 北京文因互动诚招 Pythonner:
    +

# 是也乎

- 190515 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190515 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
