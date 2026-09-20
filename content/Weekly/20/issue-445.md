Title: Issue 445
Slug: issue-445
Date: 2020-11-04 11:42
Tags: Weekly,Python,pycoders,ZH


> 希望初级开发人员知道些什么?


原文: [PyCoder's Weekly - Issue #445](https://pycoders.com/issues/445)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 201104 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 201104 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [用 scipy.fft 进行 傅立叶变换 :Python 的信号处理](https://pycoders.com/link/5130/web)
    + REAL PYTHON

In this tutorial, you’ll learn how to use the Fourier transform, a powerful tool for analyzing signals with applications ranging from audio processing to image compression. You’ll explore several different transforms provided by Python’s scipy.fft module.


(`是也乎:`


![fft](http://ydlj.zoomquiet.top/ipic/2020-11-04-ScreenShot%202020-11-04%2014.36.56.jpg)

专注信号处理的模块, 
当然有, 不然那么多大型天线收集到的数据怎么处理?


)


- [Python 后背梗 #4: 如何执行Python字节码](https://pycoders.com/link/5124/web)
    + VICTOR SKVORTSOV

Here’s a joke you may have heard from Python developers: “Is Python interpreted or compiled? Yes.” When your program runs, the Python source code is compiled to bytecode. This in-depth article explores how bytecode gets executed.


- [用 SimPy 在 Python 中模拟真实世界的过程](https://pycoders.com/link/5140/web)
    + REAL PYTHON 
    + course

In this step-by-step course, you’ll see how you can use the SimPy package to model real-world processes with a high potential for congestion. You’ll create an algorithm to approximate a complex system, and then you’ll design and run a simulation of that system in Python.

(`是也乎:`

![SimPy](http://ydlj.zoomquiet.top/ipic/2020-11-04-ScreenShot%202020-11-04%2014.35.31.jpg)

SimPy ~ 简单的世界, 用 Python 来模拟物理反应...

缩写太重要了. 马上就没什么合适的3字母缩写给自己项目用了.


)


- [五个高级 Django 技巧](https://pycoders.com/link/5120/web)
    + STEVEN PATE 
    + • Shared by Steven Pate

Dive into advanced django tips, including Q objects, annotations, prefetch objects, custom querysets, and custom model managers.

(`是也乎:`

Q ~ 星际旅行中那个无聊的至高能量智慧生物?

)



- [为何在导入过程中运行代码不是一个好主意 (以及如何发生) 的分析](https://pycoders.com/link/5133/web)
    + CHRIS SIEBENMANN

Code that runs when a module is imported is usually a code smell. But sometimes there’s no way around it.

(`是也乎:`

等等, import 不就是用来乱入的?

)


- [2020 年 Python 开发人员调查已延长至 11月7日](https://pycoders.com/link/5125/web)
    + TWITTER.COM/THEPSF

- [介绍 Pants v2](https://pycoders.com/link/5137/web)
    + BENJY WEINBERGER

(`是也乎:`

> Pants is a scalable build system for monorepos: codebases containing multiple projects, often using multiple programming languages and frameworks, in a single unified code repository.

嗯哼, 只是为什么要用多数语言来开发一个重要的系统?


)


- [Pyston v2 发布](https://pycoders.com/link/5143/web)
    + PYSTON.ORG

(`是也乎:`

很久没 Pyston 的消息了,
因为 老爹 的退休嘛?

)


- [Django Bugfix 发布: 3.1.3, 3.0.11, and 2.2.17](https://pycoders.com/link/5117/web)
    + DJANGO SOFTWARE FOUNDATION

- [Raspberry Pi 400 人计算机套件现已上市](https://pycoders.com/link/5144/web)
    + RASPBERRYPI.ORG 
    + • Shared by Bartosz Zaczyński


(`是也乎:`

硬件, 和OS 类似, 宁可用老一代稳定版本,
也不抢先撞新版本.

)



## 探讨/吐糟
> Discussions


- [Python 中的函数式编程案例](https://pycoders.com/link/5132/web)
    + REDDIT

Is functional programming just lots of map()and filter() calls, or is it something else?

(`是也乎:`

嗯哼, 多范式语言的好处就是可以自由选择, 
没人逼你用 FP.

)


- [正在部署我的第一个数据科学应用程序 ... 是否得学其中的所有课程？](https://pycoders.com/link/5116/web)
    + REDDIT

Swimming in a sea of git, cron, SSH, and Linux. Am I doing this right?



## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [The Real Python 播客 – Episode #33: 超越Python和Al Sweigart的基本知识](https://pycoders.com/link/5128/web)
    + REAL PYTHON 
    + podcast

You probably have heard of the bestselling Python book, “Automate the Boring Stuff with Python.” What are the next steps after starting to dabble in the Python basics? Maybe you’ve completed some tutorials, created a few scripts, and automated repetitive tasks in your life. This week on the show, we have author Al Sweigart to talk about his new book, “Beyond the Basic Stuff with Python: Best Practices for Writing Clean Code.”


(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2020-11-04-ScreenShot%202020-11-04%2014.29.16.jpg)

)


- [单个文件中的 Django REST API](https://pycoders.com/link/5115/web)
    + ADAM JOHNSON

Can you build an entire Django application in a single file? Well, yes, you can! Explore how to make a small Django API using only Django core features that all contained in—you guessed it—just one file.

(`是也乎:`


叕一个 mini-Django 尝试.

)

- [OpenPyXL: 通过 Python 来使用 Microsoft Excel](https://pycoders.com/link/5119/web)
    + MIKE DRISCOLL

Ah, Excel. Everyone loves to hate it. But let’s face it. Excel is one of the most popular pieces of software ever written. But you love Python, not Excel, which is why you might want to learn OpenPyXL.

(`是也乎:`


既然 Excel 创造了世界,
那么, Python 自然也可以控制 Excel

)


- [Django 入门, 第 3 部分: Django 视图授权](https://pycoders.com/link/5131/web)
    + REAL PYTHON

This tutorial covers how to restrict your web pages to users with different roles through Django view authorization. You’ll learn about HttpRequest.user objects, view decorators that authenticate, and how to notify your users with the Django messages framework.

(`是也乎:`


![Django](http://ydlj.zoomquiet.top/ipic/2020-11-04-ScreenShot%202020-11-04%2014.28.35.jpg)

)


- [编写高性能并行 Python 代码](https://pycoders.com/link/5114/web)
    + THIAGO CANDIDO

“In what cases is the use of libraries for concurrent application development appropriate and can result in increased performance using Python?”


- [用 Wolfram Alpha API 和 Python 构建您的下一个项目](https://pycoders.com/link/5136/web)
    + MARTIN HEINZ 
    + • Shared by Martin Heinz

WolframAlpha is a powerful search and computation engine. Learn how to use it’s API to bring its functionality into your own Python programs!

(`是也乎:`

既然是 Wolf 创造了一切,
那么, Python 的一切也值得替代了.

)



- [Python 中的现代测试驱动开发](https://pycoders.com/link/5142/web)
    + JAN GIACOMELLI

Interested in how TDD works? This guide will walk you through the process, using modern tools and techniques, from start to finish.

(`是也乎:`

叕一个 TDD 扫盲文, 基于 pytest

![pytest](http://ydlj.zoomquiet.top/ipic/2020-11-04-ScreenShot%202020-11-04%2014.26.40.jpg)

)

- [希望初级开发人员知道些什么?](https://pycoders.com/link/5147/web)
    + ENDY AUSTIN

Some of these are things even senior devs need to be reminded of sometimes!

(`是也乎:`

永远的8rong8chi...

)


   
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [SkyAR: 视频中的动态天空替换和协调](https://pycoders.com/link/5135/web)
    + GITHUB.COM/JIUPINJIA

(`是也乎:`


这应该是哪个飞行游戏中泄漏出来的?

)


- [nlp_profiler: 使用一个/多个文本列来分析数据集](https://pycoders.com/link/5118/web)
    + GITHUB.COM/NEOMATRIX369 • Shared by Mani Sarkar

- [Liszt: A Personal Organization Software With a Script Engine for Automation](https://pycoders.com/link/5112/web)
    + GITHUB.COM/RWANDAPINOCLE

- [vscode-stories: VSCode 的故事](https://pycoders.com/link/5129/web)
    + GITHUB.COM/BENAWAD

(`是也乎:`

VSCode 的胜利应该是 geek 在 M$ 肚皮中的胜利...

这种历史传说一定要抓在自己手中哪...

)

- [code-video-generator: 用 Manim 生成代码演练视频](https://pycoders.com/link/5134/web)
    + GITHUB.COM/SLEUTH-IO

(`是也乎:`

Intro to Code Video Generator - YouTube 

     https://www.youtube.com/watch?v=Jn7ZJ-OAM1g 

为了在直播时不用手忙脚乱的调整代码演示,
干脆用代码生成最漂亮的代码演示...

)

- [dataclassframe: 具有多索引和批量操作的数据类的容器](https://pycoders.com/link/5145/web)
    + GITHUB.COM/JOSHLK

(`是也乎:`

Pandas 的 dataframe 之后, frame 就流行了

)

- [duhdoy: Sarcasm-Inator](https://pycoders.com/link/5123/web)
    + GITHUB.COM/SANGARSHANAN

- [stumpy: 用于计算矩阵配置文件的库](https://pycoders.com/link/5139/web)
    + GITHUB.COM/TDAMERITRADE


(`是也乎:`

真 Matrix ... 专注多机多CPU 高计算性能测试.
)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

![PyCon2020中国](http://ydlj.zoomquiet.top/ipic/2020-11-04-ScreenShot%202020-11-04%2008.51.39.jpg)

- PyCon2020中国
    + 11.28~29
    + 在线
- [⋅ Python Brasil 2020](https://pycoders.com/link/5113/web)
    + November 2 to November 9, 2020


## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

![14py](http://ydlj.zoomquiet.top/ipic/2020-10-28-barnner-101camp-wx14py.png)


# PS:
- 首发: [Issue 445 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-445.html)
- 修订: [issue-445.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-445.md)


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
>> NN 4187


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/445)






