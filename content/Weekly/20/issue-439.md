---
title: "Issue 439"
summary: ""
date: "2020-09-23T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> 如何死都不用 Lambda ?
原文: [PyCoder's Weekly - Issue #439](https://pycoders.com/issues/439)
![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)

- 200923 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200923 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------

- [Git 内在: 通过构建 git 来理解](https://pycoders.com/link/4917/web)
  - NIKITA LESHENKO
Master the basics of git by building your own version in Python using this creative and interactive tutorial.
(`是也乎:`
注意 Master 已经不合适继续提及了...
)
- [Python 练习问题: 面试准备](https://pycoders.com/link/4922/web)
  - REAL PYTHON
In this tutorial, you’ll prepare for future interviews by working through a set of Python practice problems that commonly appear in coding tests. You’ll work through the problems yourself and then compare your results with solutions developed by the Real Python team.
(`是也乎:`
![Interview](http://ydlj.zoomquiet.top/ipic/2020-09-23-ScreenShot%202020-09-23%2011.26.10.jpg)
面试已经成为一门显学,
无论面试时考查的东西和实际工作中有无关系,
面试难度, 已经成为一家企业的 face 了.
)
- [用 NumPy 进行数组编程](https://pycoders.com/link/4907/web)
  - CHARLES R. HARRIS ET AL
In this review published in Nature and co-authored by NumPy creator Travis Oliphant, the authors explore how NumPy increasingly acts as an interoperability layer between array computation libraries like PyTorch and Tensorflow.
(`是也乎:`
除非象 PyTorch 要用细致的矩阵控制,
否则, 还是通过 Pandas 来用 NumPy 来的自然.
)
- [例外当控制流程](https://pycoders.com/link/4898/web)
  - GEORGE opinion
Using exceptions as control flow is a practice typically discouraged, and for some good reasons. But is there any time when this approach makes sense?
(`是也乎:`
简单说, 别轻易拿意外当控制用.
)
- [CircuitPython 6.0.0 Beta 0 发布!](https://pycoders.com/link/4918/web)
  - ADAFRUIT.COM
(`是也乎:`
![CircuitPython](http://ydlj.zoomquiet.top/ipic/2020-09-23-ScreenShot%202020-09-23%2011.19.15.jpg)
兼容 Mu, 基于MicroPython,
但是, 进行了更多发展, 支持更多硬件,
专注用 Python 进行智能硬件学习.
值得一试.
)

## 探讨/吐糟
>
> Discussions

- [在哪里运行可以自动执行任务的脚本?](https://pycoders.com/link/4914/web)
  - REDDIT
It’s gotta run somewhere…
(`是也乎:`
这问题扎心了;
俺的习惯是看任务稳定性要求,
从低到高是:
本地桌面编程;
内网主机;
远程外网主机;
远程 VPS;
远程 PaaS;
远程 FaaS...
)

## 文章/教程/嗯哼
>
> Articles, Tutorials and Talks

- [在 Python 中用链表](https://pycoders.com/link/4906/web)
  - REAL PYTHON
  - course
In this course, you’ll learn what linked lists are and when to use them, such as when you want to implement queues, stacks, or graphs. You’ll also learn how to use collections.deque to improve the performance of your linked lists and how to implement linked lists in your own projects.
(`是也乎:`
![Linked](http://ydlj.zoomquiet.top/ipic/2020-09-23-ScreenShot%202020-09-23%2011.15.01.jpg)
链表哪... 好怀念的东西 ,
只是, 工作这么多年, 愣是没相会耍上一次.
)
- [如何从不使用Lambda: Python 3版](https://pycoders.com/link/4915/web)
  - MINEROBBER9000
Ever see something so ugly and hideous that you can’t help but stare at it? Here’s a whole collection of Python lambda functions that will have you pulling your hair out while you’re unable to look away.
(`是也乎:`
老爹的观音兵来了....
感觉 Lambda 就象围棋中的 `手筋` 不到特殊场景中,
根本用不上.
)
- [一元算术运算分解](https://pycoders.com/link/4913/web)
  - BRETT CANNON
Take a look at how unary operators work under the hood in Python.
- [The mmap() Copy-On-Write 技巧: 减少数组副本的内存使用量](https://pycoders.com/link/4919/web)
  - ITAMAR TURNER-TRAURING
Memory usage usually scales with the number of copies: if your original array was 1GB of RAM, each copy will take 1GB of RAM. But often, you’re just changing a small part of the array. Ideally, the memory cost would only be the parts of the copies that you changed. Learn how to do this using mmap() copy-on-write with NumPy.
(`是也乎:`
map -> mmap -> mmmap 这个模式俺是认同的...
)
- [Python 中的数字](https://pycoders.com/link/4899/web)
  - REAL PYTHON
In this tutorial, you’ll learn about numbers and basic math in Python. You’ll explore integer, floating-point numbers, and complex numbers and see how perform calculations using Python’s arithmetic operators, math functions, and number methods.
(`是也乎:`
可记得: [为什么 0.1 + 0.2 = 0.300000004](https://mp.weixin.qq.com/s/M2m3haos2OebXyXFzTc_6A)
![Numbers](http://ydlj.zoomquiet.top/ipic/2020-09-23-ScreenShot%202020-09-23%2011.12.20.jpg)
)
- [初学者的 Python 代码清理](https://pycoders.com/link/4904/web)
  - ROMAN IMANKULOV
Here are twelve actionable steps you can use to clean-up your Python code to make it look more professional and increase readability.
(`是也乎:`
可怜的 Python 本身整洁天性足够的,
但是, 老爹心大, 又内置了多范式支持,
所以, 在 Python 中大家可以任性写出 C/C++/JAVA/Shell/... 各种风格代码来,
人为制造各种高端整洁问题.
再来解决.
)
- [Python 中的字典视图对象](https://pycoders.com/link/4903/web)
  - JOHN LEKBERG
Learn how to create read-only dictionary-like objects using the MappingProxyType in Python’s types package.
(`是也乎:`
嗯哼?
![JOHN](http://ydlj.zoomquiet.top/ipic/2020-09-23-ScreenShot%202020-09-23%2011.09.31.jpg)
这种风格的 blog 太友好了...
)
- [用 FastAPI 和 MongoDB 构建 CRUD 应用](https://pycoders.com/link/4897/web)
  - ABDULAZEEZ ABDULAZEEZ ADESHINA
  - • Shared by
  - Abdulazeez Abdulazeez Adeshina
Learn how to develop an an asynchronous REST API with FastAPI and the Motor package with MongoDB.
(`是也乎:`
FastAPI 是好的,
MongoDB 是什么肥四.
直接上 ZODB 也不差吧.
)

## 好物/妙品/
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [kb: 最小可用 知识库管理器](https://pycoders.com/link/4916/web)
  - GITHUB.COM/GNEBBIA
(`是也乎:`
这个工程名儿起的够屌.
![kb logo](http://ydlj.zoomquiet.top/ipic/2020-09-23-ScreenShot%202020-09-23%2011.04.45.jpg)
)
- [cadquery: Python 参数化 CAD 脚本框架](https://pycoders.com/link/4920/web)
  - GITHUB.COM/CADQUERY
(`是也乎:`
隔壁那谁说的, 对机械设计工程师来说, Py 无用?
)
- [jazzit: 用音乐丰富您的 Python 脚本](https://pycoders.com/link/4900/web)
  - GITHUB.COM/SANGARSHANAN
(`是也乎:`
吓人, 对听力障碍程序猿不友好.
)
- [git-cu: 保持本地 Git 存储库井井有条](https://pycoders.com/link/4908/web)
  - GITLAB.COM/3POINT2
(`是也乎:`
等等, 竟然是 gitlab 的仓库?
看来, github 大逃亡的后期效果终于展现了.
这个小工具, 简直就是 go fetch 的通用化.
简单说, 自动将你 clone 的仓库, 按照 url 进行合理子目录树化.
)
- [scriv: Changelog 管理工具](https://pycoders.com/link/4905/web)
  - GITHUB.COM/NEDBAT
(`是也乎:`
嗯哼, 虽然每次 Changelog 可以夹点儿吐糟,
但是, 长期来, 还是自动化比较好.
嘦坚持一个固定的 commit log 格式.
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyCon Turkey (Virtual) September 26 to September 27, 2020](https://pycoders.com/link/4902/web)
  - September 26 to September 27, 2020
  - 土尔其?

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)
101camp13py 即将提价...
参考 => [蟒营®编程思维提高班 Python版/ 第12期](https://py.101.camp/)

# PS

- 首发: [Issue 439 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-439.html)
- 修订: [issue-439.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-439.md)

-------------

好文笔,感叹号年度配额: **1/3**
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
>> NN 4145
![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/439)
