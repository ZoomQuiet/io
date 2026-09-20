Title: Issue 437
Slug: issue-437
Date: 2020-09-09 11:42
Tags: Weekly,Python,pycoders,ZH


> 探索 Python 在太空探索中的作用


原文: [PyCoder's Weekly - Issue #437](https://pycoders.com/issues/437)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 200909 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200909 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------




- [探索 Python 在太空探索中的作用](https://pycoders.com/link/4800/web)
    + MICROSOFT

In this learning path from Microsoft, you’ll get an introduction to Python, and be inspired to learn, discover, and create using Python-based data science and machine learning to help generate knowledge about the world beyond Earth.


(`是也乎:`

一门语言是否有统治地位, 还得看是否经得住上天,
毕竟在外空间, 硬盘都随时有字节被反转的可能,
所以, 对应运行时的容错能力就非常重要了...

)

- [一个 Bash 命令开始新的一天](https://pycoders.com/link/4796/web)
    + DOAA MAHELY

When faced with the repetitive task of opening the same browser tabs, the same code IDE, and starting the same local server to start her workday, one resourceful Pythonista wrote a Python script to simplify her morning routine.

(`是也乎:`

将 Py 脚本注入 Bash ...
更多乐趣, 更难迁移...
)


- [适用于 Python 的“结构模式匹配”/第2部分](https://pycoders.com/link/4801/web)
    + JAKE EDGE

The saga of PEP 622 continues with updates to the proposed structure of the match statement—which has some similarities to a switch statement—and a discussion on the best way to document objections to a PEP.



- [Python 反应式编程简介](https://pycoders.com/link/4815/web)
    + ROMAIN PICARD

Learn how to write event-driven code using the RxPY library, which is the Python implementation of the ReactiveX framework.


(`是也乎:`

[Reactive Programming with Python](https://www.amazon.com/Hands-Reactive-Programming-Python-Event-driven-ebook/dp/B07JY76FX5)

已经有对应图书出版了:

![RxPY](http://ydlj.zoomquiet.top/ipic/2020-09-09-ScreenShot%202020-09-09%2011.16.11.jpg)

简单说, 现在我们的应用, 可以不依赖用户行为触发了,
而可以主动根据更多条件主动响应各种状态变化来行动;

可以说是 IFTTT 的语言/框架化.
或是说, 函式编程的泛化?

)

- [聪明测试 不难](https://pycoders.com/link/4793/web)
    + LUKE PLANT

The more tests a project has, the better, right? Well, maybe not!




- [Python 3.5.10 现在可用](https://pycoders.com/link/4795/web)
    + PYTHON.ORG

This could be the last release for 3.5!

(`是也乎:`

嗯哼? 刚刚老爹在 Twitter 赞了 3.8.X ,怎么这儿才 3.5.10 ?

)


- [Real Python 视频字幕现在可用](https://pycoders.com/link/4817/web)
    + REAL PYTHON

(`是也乎:`

![Subtitles](http://ydlj.zoomquiet.top/ipic/2020-09-09-ScreenShot%202020-09-09%2011.07.04.jpg)

也就是说, 可以玩弹幕了?

)


## 探讨/吐糟
> Discussions


- [为每月 5万5千 用户运行 Python 应用的成本](https://pycoders.com/link/4808/web)
    + HACKER NEWS

True costs depend on so many factors, and there are tons of scenarios and strategies discussed in this thread.

(`是也乎:`

不听不听,
反正现在俺的产品用户数量42人都没达到...
)


- [当字符串的引号不匹配时，为什么Python没有给出任何错误? ](https://pycoders.com/link/4797/web)
    + STACK OVERFLOW

How well do you know your quotes?



## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [在 Asyncio 中异步打开和关闭文件](https://pycoders.com/link/4822/web)
    + CHRIS WELLONS

Python has no support for asynchronous file operations. But some operating systems support asynchronous file I/O, and languages such as .NET come with this support built-in. So how could you go about implementing this in Python?

(`是也乎:`

那么如何保证可用?

)

- [用 Python 和 Selenium 构建并发 Web 爬虫](https://pycoders.com/link/4818/web)
    + POSTED BY 
    + CALEB POLLMAN CALEB POLLMAN 
    + • Shared by Michael Herman

Learn how to speed up your web scrapers with some multithreading.

(`是也乎:`

芹菜 早已整体解决这事儿了, 不用生撸了

)

- [The Real Python Podcast – Episode #25: Data Version Control in Python and Real Python Video Transcripts](https://pycoders.com/link/4820/web)
    + REAL PYTHON 
    + podcast

Wouldn’t it be nice to a use a form of version control for data? Something that would allow you to track and version your datasets and models. Well, that’s what the tool called DVC is designed to do. This week on the show, David Amos is here and he’s brought another batch of PyCoder’s Weekly articles and projects.

(`是也乎:`

![Podcast](http://ydlj.zoomquiet.top/ipic/2020-09-09-ScreenShot%202020-09-09%2011.29.36.jpg)

竟然有 MM 立即听了起来...

)


- [fastcore: 一个被低估的Python库](https://pycoders.com/link/4807/web)
    + FAST.AI

fastcore is a Python library that extends the language with utilities designed to enhance productivity. Learn about the different features fastcore provides, and then check out the project on GitHub to learn how the features are implemented.


(`是也乎:`

每个社区都希望被被低估...

)


- [数据科学的软件工程技巧和最佳实践](https://pycoders.com/link/4824/web)
    + AHMED BESBES

Jupyter notebooks are a great way to explore data, but they are limited when it comes to producing something that is extensible and maintainable. Get an overview of software engineering best practices designed to help data scientists move beyond the notebook.


(`是也乎:`

Jupter 的硬广, 的确, 现在 `IPy[:NB]` 
已经是 REPL/IDE 之外, 
又一个值得长期使用的好界面,
而且越来越方便了.

)

- [在 Python 中探索 HTTPS 和加密术](https://pycoders.com/link/4791/web)
    + REAL PYTHON 
    + course

In this course, you’ll gain a working knowledge of the various factors that combine to keep communications over the Internet safe. You’ll see concrete examples of how to keep information secure and use cryptography to build your own Python HTTPS application.

(`是也乎:`

![Cryptography](http://ydlj.zoomquiet.top/ipic/2020-09-09-ScreenShot%202020-09-09%2010.57.31.jpg)

感谢 Python 生态, 一切都是现成可用的

)


- [税务律师用 Python](https://pycoders.com/link/4809/web)
    + ANDREW MITCHEL

See how one tax attorney uses Python to automate grueling and repetitive tasks and improve his business. While the article is non-technical, it’s always fun to see how Python is used in diverse fields.

- [PyTorch vs Tensorflow 适用于您的深度学习项目](https://pycoders.com/link/4798/web)
    + REAL PYTHON

PyTorch vs Tensorflow: Which one should you use? Learn about these two popular deep learning libraries and how to choose the best one for your project.


(`是也乎:`


![PyTorch](http://ydlj.zoomquiet.top/ipic/2020-09-09-ScreenShot%202020-09-09%2010.54.20.jpg)

Keras 都被 TF 吸收了,
另外还有个 FastAI ,
其实, 具体用哪个并不是框架本身决定的,
还得看各自缘份了...

毕竟几个框架真正作用的算法是相同的, 
只是涉及的运行时生态以及代码风格各有不同.

很可能以后都融合在专用 TPU 中,
根本不用专门学习一个什么框架, 用自然语言就可以完成训练了.

)
    
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code


- [python-adventure: 原创巨大洞穴冒险游戏，运行在Python 3中](https://pycoders.com/link/4806/web)
    + GITHUB.COM/BRANDON-RHODES

-   [pyducers: 受Clojure启发的转换器库](https://pycoders.com/link/4816/web)
    + GITHUB.COM/FURIEL

(`是也乎:`

叕一则 Clojure 传染成果;
嘦自己感觉好就是好...

只是, 无法生成 JVM 可用字节代码, 这个工具很鳮肋了哪.

)

- [RxPY: 适用于Python的反应式扩展](https://pycoders.com/link/4794/web)
    + GITHUB.COM/REACTIVEX


- [Fixit: 基于 LibCST 的 Lint 框架](https://pycoders.com/link/4810/web)
    + GITHUB.COM/INSTAGRAM

(`是也乎:`

Instagram 团队分享的静态代码分析工具.

)


- [clifford: Python 的几何代数](https://pycoders.com/link/4792/web)
    + GITHUB.COM/PYGAE

(`是也乎:`

几何以及代数, 中学生的恶梦

)


- [fastcore: 为 Fastai 库增压](https://pycoders.com/link/4805/web)
    + GITHUB.COM/FASTAI

(`是也乎:`Fastai库为Python增压

FastAI 一己之力, 在 google 们中间闯出了自己的道路.

)

- [makesite: 为 Python 程序猿服务的简单/轻巧且无魔术的静态站点/博客生成器](https://pycoders.com/link/4823/web)
    + GITHUB.COM/SUNAINAPAI



- [Django 生成器](https://pycoders.com/link/4821/web)
    + DJANGOBUILDER.IO

- [hydra: 用于优雅配置复杂应用程序的框架](https://pycoders.com/link/4799/web)
    + HYDRA.CC 
    + • Shared by Shagun Sodhani

(`是也乎:`

开始面向优雅编程了?

![hydra](http://ydlj.zoomquiet.top/ipic/2020-09-09-ScreenShot%202020-09-09%2010.48.03.jpg)

只是叕一个 海德拉 , 外国人起名都这般直的?
)



## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ DjangoCon Europe 2020 (Virtual)](https://pycoders.com/link/4804/web)
    + September 18 to September 20, 2020

## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

101camp12py 正在报名

![报名](http://ydlj.zoomquiet.top/ipic/2020-08-26-200816-reg-zip.jpg)

```

课程规划:

    报名截止 2020.09.21
    正式开课 2020.09.27
    课程结束 2020.11.08

```
详情 => [蟒营®编程思维提高班 Python版/ 第12期](https://py.101.camp/)


# PS:
- 首发: [Issue 437 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-437.html)
- 修订: [issue-437.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-437.md)


-------------

好文笔,感叹号年度配额: **1/3**

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
>> NN 4131


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/437)






