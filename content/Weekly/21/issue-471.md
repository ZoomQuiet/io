Title: Issue 471
Slug: issue-471
Date: 2021-05-05 11:42
Tags: Weekly,Python,pycoders,ZH


> C扩展的隐藏性能开销


原文: [PyCoder's Weekly - Issue #471](https://pycoders.com/issues/471)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210505 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210505 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [Python C扩展的隐藏性能开销](https://pycoders.com/link/6235/web)
    + ITAMAR TURNER-TRAURING

It’s no secret that Python is slower than compiled languages like C, C++, and Rust. If you need a performance boost, you can write compiled Python C extensions. But there are some hidden performance costs that you should be aware of if you decide to do this. This article explains two ways that Python C extensions can actually be slower than pure Python and discusses some solutions and work around for them.


(`是也乎:`

是的, Py 内建模块是宝藏, 很少有人都用过的...

)



- [如何用 ipywidgets 令 Jupyter Notebook 能交互式](https://pycoders.com/link/6230/web)
    + MATT WRIGHT

Jupyter Notebooks are great for exploratory data analysis. They’re also a good way to share results and analysis with other people, who can alter the notebook to further explore the data themselves. But there are some limitations to notebook interactivity. That’s where ipywidgets comes in! In this tutorial you’ll learn how to create widgets like check boxes, drop-down menus, sliders, and how to handle events like button clicks.

- [Rapidly Identify Bottlenecks in Your Python Applications with Datadog APM.](https://pycoders.com/link/6204/web)
    + DATADOG
    + sponsor

Datadog’s Continuous Profiler allows you to find the most resource-consuming parts in your production code all the time, at any scale, with minimal overhead. Debug and optimize your code, enhancing application performance before your customers notice. Try Datadog APM today →

- [用 Arcade 在 Python 中构建平面游戏](https://pycoders.com/link/6218/web)
    + REAL PYTHON

Building games can be a fun way to learn new Python concepts and practice techniques you’ve already learned. Plus, they make for great projects to share! This step-by-step tutorial shows you how to build a platform game using the arcade library. You’ll learn techniques for designing levels, sourcing assets, and implementing advanced features.


(`是也乎:`


![Platform](http://ydlj.zoomquiet.top/ipic/2021-05-05-ScreenShot%202021-05-05%2010.44.05.jpg)

卷轴游戏, 现在有完备的开发/设计/调试环境了...


)



- [Python 3.10.0b1 现在可用](https://pycoders.com/link/6220/web)
    + CPYTHON DEV BLOG

Python 3.8.10 and 3.9.5 have also been released.

- [Microsoft 成为 PSF 第三个 远见赞助商](https://pycoders.com/link/6214/web)
    + MICROSOFT.COM

- [EuroPython 2021: 呼吁赞助商](https://pycoders.com/link/6228/web)
    + EUROPYTHON.EU

- [Django Security 发行版发布: 3.2.1, 3.1.9, and 2.2.21](https://pycoders.com/link/6238/web)
    + DJANGO SOFTWARE FOUNDATION






-----------------------------------------
## 探讨/吐糟
> Discussions


- [“WARNING: Value for scheme.data Does Not Match” 每当我尝试安装/升级 pip 时](https://pycoders.com/link/6260/web)
    + STACK OVERFLOW

Are you seeing warnings about scheme.data, scheme.platlib, and other scheme.* items when installing with pip? While these warnings don’t affect the pip installation, they are noisy and annoying. Fortunately, the pip team has fixed them in the latest patch release, so upgrading to pip 21.1.1 or later should get rid of them for you.

(`是也乎:`

随着 Python 的上升, pip 版本的高速变化.
PyPi 不可用情况越来越多,

)



- [在 Stack Overflow 中最经常被复制的评论都是关于如何在 Matplotlib 中调整图形的大小](https://pycoders.com/link/6212/web)
    + REDDIT

In a recent blog post, Stack Overflow analyzed data the obtained during an April Fools gag about how people copy and paste code from their platform. One of the results from the data set indicates that to most copied comment comes from an answer about resizing figures in Matplotlib.

(`是也乎:`

扎心了老铁...

)


-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [用 Python 从头开始进行模拟电影画质模拟](https://pycoders.com/link/6229/web)
    + KEVIN MARTIN JOSE

In analog photography, you can achieve different “looks” for your photographs by selecting different kinds of film to shoot with. Digital camera manufacturers often include different presets to simulate different kinds of film. In this article, you’ll learn how to simulate different films on your own images using color lookup tables, or CLUTs, using NumPy and the Pillow image library.


(`是也乎:`

果断来了,
5年前就有中国团队作到了,
现在各种轮子都在出现,
可视化编程, 为什么不生成可实用的 py 代码?
当然可以的了

)



- [用 PySimpleGUI 简化 Python GUI 开发](https://pycoders.com/link/6221/web)
    + REAL PYTHON 
    + course

In this step-by-step course, you’ll learn how to create a cross-platform graphical user interface (GUI) using Python and PySimpleGUI. A graphical user interface is an application that has buttons, windows, and lots of other elements that the user can use to interact with your application.

(`是也乎:`


![PySimpleGUI](http://ydlj.zoomquiet.top/ipic/2021-05-05-ScreenShot%202021-05-05%2010.39.46.jpg)

`PySimpleGUI` 号称简单,
其实...


)




- [声明式验证](https://pycoders.com/link/6231/web)
    + DREW OLSON

Validating user input is one of the most common programming tasks. There are a number of approaches to validation and a host of third-party Python packages available on PyPI. One of these approaches that is common in the functional programming paradigm is applicative-style validation, which the author of this article calls declarative validation. In this short-yet-informative article, you’ll learn how declarative validation works and how to cook up a small validation library.


(`是也乎:`


当年有效性检验模块, 多数是 PHP 社区给出来的,
后来是 JS,
现在 Py 也要重新来一遍...

)


- [Python 新闻/ 4月以来有什么新变化?](https://pycoders.com/link/6211/web)
    + REAL PYTHON

April 2021 was an eventful month in the world of Python. In this article, you’ll get up to speed on everything that happened in the past month, including new sponsorships for the PSF, changes to Python error messages, and a community-led discussion over the future of type annotations.


(`是也乎:`


![News](http://ydlj.zoomquiet.top/ipic/2021-05-05-ScreenShot%202021-05-05%2010.40.12.jpg)

真蟒 版周刊.


)


- [用 Postgres/Uvicorn 和 Traefik 对 FastAPI 进行 Docker 化](https://pycoders.com/link/6259/web)
    + AMAL SHAJI 
    + • Shared by Amal Shaji

FastAPI is quickly gaining popularity in the world of asynchronous Python web frameworks. With more and more users flocking to the framework, the demand for Dockerized development and production workflows is growing. In this step-by-step tutorial, you’ll learn how to dockerize a FastAPI application using Postgres, Uvicorn, and Traefik.

(`是也乎:`

越来越多人将 FastAPI 和 Flask 对比了,
这其实没什么可比性;

但是, 谁让他们都是 F 家族的呢?

)



- [Podcast 倒带 2020-2021 年嘉宾集锦](https://pycoders.com/link/6245/web)
    + REAL PYTHON 
    + podcast

This week’s episode of the Real Python podcast is a bit different. Take a look back in this rewind episode featuring highlights from the many interviews over the past year or so of the show.


(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2021-05-05-ScreenShot%202021-05-05%2010.34.52.jpg)


solo, 主持人没请到嘉宾, 于是自己回顾当年印象最深的嘉宾们

)


-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [tablib: Python Module for Tabular Datasets in XLS, CSV, JSON, YAML, &C](https://pycoders.com/link/6227/web)
    + GITHUB.COM/JAZZBAND

(`是也乎:`


![tablib](http://ydlj.zoomquiet.top/ipic/2021-05-05-ScreenShot%202021-05-05%2010.31.39.jpg)

可以拿来作为各种数据源的输出端


)


- [wasmer-python: 适用于 Python 的 WebAssembly 运行时](https://pycoders.com/link/6247/web)
    + GITHUB.COM/WASMERIO

(`是也乎:`

叕一个 WASM.py 方案,
其实, 早说过了, 就看哪家方案, 首先被 Chrome 接受并编译到内核了...

当然, 这个还是用 Rust 来完成最终编译的...

)


- [gradio: 3分钟内创建用于对机器学习模型进行原型设计的UI](https://pycoders.com/link/6232/web)
    + GITHUB.COM/GRADIO-APP

- [tortoise-orm: Familiar Asyncio ORM for Python, Built With Relations in Mind](https://pycoders.com/link/6249/web)
    + GITHUB.COM/TORTOISE

- [mongo-arrow: 在MongoDB和Apache Arrow之间轻松移动数据](https://pycoders.com/link/6253/web)
    + GITHUB.COM/MONGODB-LABS


(`是也乎:`


> ...一种适合异构大数据系统的内存列存数据格式标准


天下大势: `分久必合, 合久必分`

NoSQL 之后,
数据重新探索出各种形态,
现在, 又需要一个统一标准可以在内存中相互融合统计/计算,
Apache 有很多项目都在尝试这个方向,
现在看 Arrow 是个共同方向了?

统一起来, 也方便 骇客 们嗯哼了...

)


-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6264/web)
    + April 28, 2020

(`是也乎:`

即便是线上的, 一样收费.

)

- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5590/web)
    + May 12 – 18, 2021

(`是也乎:`

反正很早都上 油管了, 随时可以 review,
当然, 这个随时, 随时了很多年都没刷光.

)

- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
    + June 2 – 6, 2021


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
- 首发: [Issue 471 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-471.html)
- 修订: [issue-471.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-471.md)


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
>> NN 4341


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/471)






