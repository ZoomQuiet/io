---
title: "Issue 380"
summary: ""
date: "2019-08-07T15:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

原文: [PyCoder's Weekly - Issue #380](https://pycoders.com/issues/380)
![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)
------

- [在 Django Admin 中管理用户应该了解的](https://pycoders.com/link/2182/web)
  - REAL PYTHON
Learn what you need to know to manage users in Django admin. Out of the box, Django admin doesn't enforce special restrictions on the user admin. This can lead to dangerous scenarios that might compromise your system.
(`是也乎:`
当年的时尚, 今天就变成黑魔法了...
)
- [为什么你的 Mock 不起作用](https://pycoders.com/link/2168/web)
  - NED BATCHELDER
"Mocking is a powerful technique for isolating tests from undesired interactions among components. But often people find their mock isn't taking effect, and it's not clear why. Hopefully this explanation will clear things up."
(`是也乎:`
所以, 还是 Docker 中给真东西测试吧
)
- [Django 安全版本发布: 2.2.4, 2.1.11 and 1.11.23](https://pycoders.com/link/2197/web)
  - DJANGOPROJECT.COM
Addresses DoS possibilities in django.utils.text.Truncator, strip_tags(), django.utils.encoding.uri_to_iri(), and a potential SQL injection issue in JSONField/HStoreField.
(`是也乎:`
三连发...可见 Django 基金会是真赚銭的...
)
- [PySpark 大数据处理的第一步](https://pycoders.com/link/2170/web)
  - REAL PYTHON
Take your first steps with Spark, PySpark, and Big Data processing concepts using intermediate Python concepts.
- [用 Fakes 以及 Factories 改进 Django 测试](https://pycoders.com/link/2184/web)
  - MARTIN ANGELOV
This blog post is an introduction into unit testing in Django. It offers an explanation on what are faker and factories and code examples illustrating them.
- [Python 中的内存管理](https://pycoders.com/link/2181/web)
  - ARTEM GOLUBIN
This article describes memory management in CPython 3.6 and how it uses a pool allocator called PyMalloc to speed-up memory operations and reduce fragmentation.
(`是也乎:`
随着 Python 越来越 C++ 化, 内存问题也必然回到程序猿眼前...
)
- [PEP 589 – TypedDict: 带有一组固定键的字典类型提示](https://pycoders.com/link/2195/web)
  - PYTHON.ORG

## 讨论
>
> Discussions

- [你造现在可以用 API 令牌上传 PyPI 包吗?](https://pycoders.com/link/2194/web)
  - TWITTER.COM/NLHKABU
(`是也乎:`
.pypirc 渠道..不过, 不稳定...
)
- [Matlab vs Python](https://pycoders.com/link/2186/web)
  - REDDIT
(`是也乎:`
什么鬼...这怎么 PK 哪...
)

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [用 Matplotlib 和 Python 探索数学](https://pycoders.com/link/2188/web)
  - ANTONIO CANGIANO
"Data Visualization can be a great tool for mathematical exploration and experimentation. In this article, I show you an example using Matplotlib and Python."
(`是也乎:`
对比隔壁的 Seaborn 们就知道 matplotlob 是老了...
)
- [如何用 Seaborn 在 Python 中制作散点图](https://pycoders.com/link/2196/web)
  - ERIK MARSJA
Learn how to make scatter plots, adding trend lines, text, rotating the labels, changing color, and markers, among other things.
- [Python 提示进入正在运行的进程: 用 Manhole 进行调试](https://pycoders.com/link/2198/web)
  - ITAMAR TURNER-TRAURING
"Sometimes your Python process will behave strangely, run slowly, or give you the wrong answers. And while hopefully you have logging, the logging isn't always enough. So how do you debug this process?"
(`是也乎:`
OTP 已经成熟使用20年的小技巧, 当然, LISP 用的时间更加长
)
- [11 种 Python 初学者技巧](https://pycoders.com/link/2163/web)
  - REAL PYTHON
  - video
In this course, you'll see several learning strategies and tips that will help you jumpstart your journey towards becoming a rockstar Python programmer!
(`是也乎:`
学习 Python 11 种最佳开始姿势:
    Code Every Day ~ 每天编程
    Write It Out  ~ 写下来
    Go Interactive  ~ 运行起来
    Take Breaks  ~ 追踪错误
    Become a Bug Bounty Hunter ~ 找到问题
    Surround Yourself With Others Who Are Learning ~ 和其它人交流
    Teach ~ 教导自己
    Pair Program  ~ 结对编程
    Ask GOOD Questions ~ 问好问题
    Build Something, Anything  ~ 构造点什么
    Contribute to Open Source ~ 为开源作贡献
这不就是 Hacker 的养成手册嘛?
)
- [传输学习和 PyTorch 的图像分类](https://pycoders.com/link/2192/web)
  - DAN NELSON
In this article you'll go over the theory behind transfer learning and see how to carry out an example of transfer learning on Convolutional Neural Networks (CNNs) in PyTorch.
(`是也乎:`
![transfer](https://stackabuse.s3.amazonaws.com/media/introduction-to-transfer-learning-3.png)
转移学习?
)
- [使用 QuadTree 算法在 Python 中实现 Photo Stylizer](https://pycoders.com/link/2161/web)
  - RICHARD BARELLA
Learn how to write a Python script to create a quadtree based filter for stylizing photos.
(`是也乎:`
![stylizing](https://raw.githubusercontent.com/ribab/quadart/master/examples/green-apple-quadart.jpg)
风格化图片?
)
- [Softmax 函数的一个简单解释](https://pycoders.com/link/2171/web)
  - VICTOR ZHOU
What Softmax is, how it's used, and how to implement it in Python.
(`是也乎:`
本家? Princeton 学生, 已经分别在 Google/Airbnb/Facebook 实习过了...
Softmax 函式是神经网络计算中一种算法,
不是 Python 自己的新嗯哼...
)
- [Python 基础: Python 3的实用介绍](https://pycoders.com/link/2151/web)
  - REAL PYTHON
  - book
  - sponsor
Make the leap from Beginner to Intermediate in Python with this complete curriculum freshly updated for Python 3.7. Includes exercises, interactive quizzes, and sample projects so you'll always know what to focus on next. Get the book today and save 27% →
(`是也乎:`
嗯哼? 真蟒 作培训果然积累出书了,毕竟国外出版业还比较健康, 有銭赚...
)
- [了解用于分类的决策树 (Python)](https://pycoders.com/link/2203/web)
  - MICHAEL GALARNYK
- [10分钟, 过 Django 上传文件到 S3](https://pycoders.com/link/2183/web)
  - DAVID BRUTON
- [如何使用 Linting,Type-Checking,Testing 等设置 Python 项目](https://pycoders.com/link/2200/web)
  - SOURCERY.AI
- [用 Pairs Plots 在 Python 进行数据可视化](https://pycoders.com/link/2205/web)
  - WILL KOEHRSEN
- [Using Twitter With Python and Tweepy](https://pycoders.com/link/2162/web)
  - MIKE DRISCOLL

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [awesome-asgi: 令人敬畏的 ASGI 服务器,框架,应用程序,库和其他资源的列表](https://pycoders.com/link/2199/web)
  - GITHUB.COM/FLORIMONDMANCA
(`是也乎:`
不得不说, 作为全球最大同性交际网站,
`awesome-*` 实在是开创了一种标签文化.
就象那些综合性论文...帮助很多用心但没什么技术的好人, 获得了足量 star
)
- [Xylene: 从 Reddit Posts, ...  获取天气信息](https://pycoders.com/link/2180/web)
  - GITHUB.COM/XITHRIUS
  - • Shared by Charles Buell
(`是也乎:`
还在早期, 刚刚完成了一个特性的样子...
)
- [py-gui: 像React一样桌面应用库](https://pycoders.com/link/2191/web)  
  - GITHUB.COM/JAKECOXON
(`是也乎:`
嗯哼, 从洪教授的 Ring 开始, 就一直有这个方向的尝试...
![gui](https://github.com/JakeCoxon/py-gui/raw/master/screenshots/Screen%20Shot%202019-03-27%20at%2021.21.00.png)
其实, 图元的嗯哼, 一直不是难事儿,
困难的是包含功能时...
)
- [alive-progress: Python 动画和智能进度条](https://pycoders.com/link/2159/web)
  - GITHUB.COM/RSALMEI
(`是也乎:`
叕一个进度条...
可能这是 CLI 中最无害又最漂亮的小东西了...
)
- [kubetest: Python 中的 Kubernetes 集成测试](https://pycoders.com/link/2204/web)
  - GITHUB.COM/VAPOR-WARE
- [handout: 使用Markdown和数字将Python脚本转换为讲义](https://pycoders.com/link/2202/web)
  - GITHUB.COM/DANIJAR
(`是也乎:`
Jupter 中分解出来的小工具?
将 Py 代码批量改换为标准 md.
)
- [Python Oberon: An Emulator Written for the Project Oberon RISC Processor](https://pycoders.com/link/2193/web)
  - PYTHONOBERON.READTHEDOCS.IO
(`是也乎:`
嗯哼? 印象中首个面向 CPU 的 Py 项目?
)
- [BASIC 解释器在Jupyter笔记本中实现](https://pycoders.com/link/2160/web)
  - GITHUB.COM/NORVIG
(`是也乎:`
Bill 手写的就好了...
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Python Atlanta Meetup](https://pycoders.com/link/2173/web)
  - August 8, 2019
  - USA
- [⋅ Python Miami](https://pycoders.com/link/2179/web)
  - August 10 to August 11, 2019
  - USA
- [⋅ DFW Pythoneers 2nd Saturday Teaching Meeting](https://pycoders.com/link/2189/web)
  - August 10, 2019
  - Plano, TX, USA
(`是也乎:`
Pythoneer 才是 Python 狂热用户的自称
)
- [⋅ Python North East](https://pycoders.com/link/2164/web)
  - August 14, 2019
  - 西北...英国
![logo.png (PNG Image, 400 × 400 pixels)](https://www.pythonnortheast.com/assets/logo.png)
- [⋅ pyCologne User Group Treffen](https://pycoders.com/link/2201/web)
  - August 14, 2019
- [⋅ PyBay](https://pycoders.com/link/2167/web)
  - August 15 to August 19, 2019
  - USA
- [⋅ PyCon Korea 2019](https://pycoders.com/link/2185/web)
    August 15 to August 19, 2019

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [蟒营 Python 入门班](https://py.101.camp/)
  - 第2期
  - 101camp2py
进入 ch2, 下期 190901 左右启动...
- [What Can I Do With Python? – Real Python](https://realpython.com/what-can-i-do-with-python/)
  - FAQ
(`是也乎:`
![Do With Py](https://ipic.zoomquiet.top/2019-05-25-ScreenShot%202019-05-25%2010.27.25.jpg)
总是永远有人问这个问题...
当然, 这个问题任何一个技术社区都有人在问...
其实, 本质上并不是对应技术是否有什么能力,
而是相反...
)

### Jobs
>
> 必须 Pythonic 相关
...

# 是也乎

- 190807 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190807 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

> NN 3732
