---
title: "Issue 397"
summary: ""
date: "2019-12-04T14:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> Guido 退出 Python 指导委员会
原文: [PyCoder's Weekly - Issue #397](https://pycoders.com/issues/397)
![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 191204 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 191204 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------

- [Guido van Rossum 退出 Python 指导委员会](https://pycoders.com/link/2993/web)
  - PYTHON.ORG
"Part of my reason is that in the end, SC duty feels more like a chore to me than fun, and one of the things I'm trying to accomplish in my life post Dropbox retirement is to have more fun. To me, fun includes programming in and contributing to Python, for example the PEG parser project."
(`是也乎:`
放弃争论, 清心编程...
)
- [Python Descriptors: 简介](https://pycoders.com/link/2995/web)
  - REAL PYTHON
Learn what Python descriptors are and how they're used in Python's internals. You'll learn about the descriptor protocol and how the lookup chain works when you access an attribute. You'll also see a few practical examples where Python descriptors can come in handy.
(`是也乎:`
![Descriptors](http://ydlj.zoomquiet.top/ipic/2019-12-04-ScreenShot%202019-12-04%2011.59.54.jpg)
配合装饰器才能发挥作用的描述符:

> ...能在类上拦截对实例属性的访问,由此可以引出很多有趣的用法,和metaclass结合起来更是如此. 对于Python来说"性能"似乎从来不是牺牲"功能"(以及其他各种美德)的理由,这次也不例外.
zhihu 上有人点评...
)

- [PSF 周二筹款活动](https://pycoders.com/link/2994/web)
  - PYTHON.ORG
When you support the Python Software Foundation on Giving Tuesday you'l support organizations like the Cameroon Digital Skills Campaign. The global donatio drive runs for 24 hrs starting December 3.
- [PIP_REQUIRE_VIRTUALENV : 为 Pip 申请活动虚拟环境](https://pycoders.com/link/2996/web)
  - PYTHON-GUIDE.ORG
After setting the PIP_REQUIRE_VIRTUALENV environment variable, Pip will no longer let you accidentally install packages if you are not in a virtual environment.
- [测试已安装的 Python 软件包](https://pycoders.com/link/2992/web)
  - PAUL GANSSLE
How to test Python packages as they will be installed on your users' systems to avoid subtle bugs.
- [平展嵌套循环以提高并行处理速度](https://pycoders.com/link/2997/web)
  - S. LOTT
A functional programming pattern you can use to parallelize the processing of nested loops.
- [Django 3.0 发布](https://pycoders.com/link/2998/web)
  - DJANGOPROJECT.COM
- [PyCharm 2019.3 发布](https://pycoders.com/link/2999/web)
  - JETBRAINS.COM

## 讨论
>
> Discussions
NIL

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [通过有损压缩减少 Pandas 内存用量](https://pycoders.com/link/3025/web)
  - ITAMAR TURNER-TRAURING
"If you want to process a large amount data with Pandas, there are various techniques you can use to reduce memory usage without changing your data. But what if that isn't enough? What if you still need to reduce memory usage? Another technique you can try is lossy compression: drop some of your data in a way that doesn't impact your final results too much."
(`是也乎:`
嗯哼? 意思是精确性可以不要?
)
- [Pandas: 如何读写文件](https://pycoders.com/link/3027/web)
  - REAL PYTHON
In this tutorial, you'll learn about the Pandas IO tools API and how you can use it to read and write files. You'll use the Pandas read_csv() function to work with CSV files. You'll also cover similar methods for efficiently working with Excel, CSV, JSON, HTML, SQL, pickle, and big data files.
(`是也乎:`
![Pandas](http://ydlj.zoomquiet.top/ipic/2019-12-04-ScreenShot%202019-12-04%2011.52.50.jpg)
饥饿的 Pandas 什么都能食
)
- [Python, Boto3, 和 AWS S3: Demystified](https://pycoders.com/link/3023/web)
  - REAL PYTHON
Get started working with Python, Boto3, and AWS S3. Learn how to create objects, upload them to S3, download their contents, and change their attributes directly from your script, all while avoiding common pitfalls.
(`是也乎:`
![Boto3](http://ydlj.zoomquiet.top/ipic/2019-12-04-ScreenShot%202019-12-04%2011.51.59.jpg)
这课一定有赞助
)
- ["Python 已在银行中替换了 Excel"](https://pycoders.com/link/3024/web)
  - SARAH BUTCHER
  - opinion
"You can already walk across the trading floor and see people writing Python code... it will become much more common in the next three to four years."
(`是也乎:`
用了30年...当然日本还得30年
)
- [对 Python 运用 Bag-Of-Words 模型的简单说明](https://pycoders.com/link/3021/web)
  - VICTOR ZHOU
The bag-of-words (BOW) model is a representation that turns arbitrary text into fixed-length vectors by counting how many times each word appears.
(`是也乎:`
周同学的 `简单说明` 系列周刊推荐过,
看来真心一直在折腾事儿..
)
- [基于属性的 Python 科学代码测试](https://pycoders.com/link/3022/web)
  - MARKUS KONRAD
  - • Shared by Markus Konrad
How to write better tests in less time by using property based testing with the hypothesis package.

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [pywonderland: 用 Python 游览数学仙境](https://pycoders.com/link/3016/web)
  - GITHUB.COM/NEOZHAOLIANG
A collection of Python scripts for drawing beautiful figures and animating interesting algorithms in mathematics.
(`是也乎:`
很早就推荐过的...
![Wonderland](https://camo.githubusercontent.com/f327031bbd958e861ebcf62b6f887a120a892103/68747470733a2f2f692e696d6775722e636f6d2f707453716c446c2e676966)
)
- [xarray: N-D标签数组和数据集 in Python](https://pycoders.com/link/3012/web)
  - PYDATA.ORG
  - • Shared by Python Bytes FM
- [pyhttptest: 基于 RESTful API 的 HTTP 测试](https://pycoders.com/link/3019/web)
  - GITHUB.COM/SLAILY
  - • Shared by Python Bytes FM
- [mutpy: 适用于 Python 3 的突变测试](https://pycoders.com/link/3015/web)
  - GITHUB.COM/MUTPY
- [qiskit: 用于量子计算的 Python 框架](https://pycoders.com/link/3011/web)
  - GITHUB.COM/QISKIT
(`是也乎:`
量子计算哪, Python 当然不会缺席
)
- [image-quality-assessment: 预测图像的美学和技术质量](https://pycoders.com/link/3010/web)
  - GITHUB.COM/IDEALO
- [Lightbus: 用于事件和 RPC 的 Python/Redis 消息总线](https://pycoders.com/link/3020/web)
  - LIGHTBUS.ORG
(`是也乎:`
叕一个 PRC 框架, 世界在重新,或是说, 从来没离开过 C/S 结构,
B/S 一直是幻觉哪
)
- [PyOxidizer: 打包和分发 Python 应用程序](https://pycoders.com/link/3017/web)
  - PYOXIDIZER.READTHEDOCS.IO
(`是也乎:`
基于 Rust 技术, 之前试用时,无法简单编译过...
现在...
)
- [emacs-application-framework: 用 Python + PyQt 扩展 Emacs](https://pycoders.com/link/3018/web)
  - GITHUB.COM/MANATEELAZYCAT
(`是也乎:`
等等, Qt ? 看来不是 Emacs 真用户
)
- [squabble: 用于 SQL 查询和迁移的可扩展 Linter](https://pycoders.com/link/3014/web)
  - GITHUB.COM/ERIK
  - • Shared by Erik Price
(`是也乎:`
少见的 SQL 静态代码检验器,
之前,都是各家厂商自己内置的.
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/3006/web)
  - December 7, 2019
  - 印度
- [⋅ Edmonton Python User Group](https://pycoders.com/link/3002/web)
  - December 9, 2019
  - Canada
- [⋅ PiterPy Meetup](https://pycoders.com/link/3004/web)
  - December 10, 2019
- [⋅ Leipzig Python User Group Meeting](https://pycoders.com/link/3008/web)
  - December 10, 2019
  - 德国
- [⋅ Dominican Republic Python User Group](https://pycoders.com/link/3001/web)
  - December 10, 2019
  - 非洲

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- **[蟒营 Python 入门班](https://py.101.camp/)**
  - 4py :-}
  - 5py ;-)
(`(￣▽￣)`:
第4期已开始, 为期6周;
    200112 按时结束
年后第5期就来:
    200203 可以上线
)

# 是也乎
>
> NN 3851

- 首发: [Issue 397 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-397.html)
- 修订: [issue-397.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-397.md)
