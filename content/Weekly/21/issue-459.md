Title: Issue 459
Slug: issue-459
Date: 2021-02-10 11:42
Tags: Weekly,Python,pycoders,ZH


> 指导委员会接受 PEP 634


原文: [PyCoder's Weekly - Issue #459](https://pycoders.com/issues/459)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 210210 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210210 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------


- [Python 的整数如何工作](https://pycoders.com/link/5696/web)
    + VICTOR

Python’s integer datatype is pretty different from most other languages because they allow arbitrary precision. Learn how integers work under the hood in this in-depth article.




- [Python 初学者友好与对高级用户支持功能之间纠结](https://pycoders.com/link/5701/web)
    + ANDRÉ ROBERGE

Python has made some big improvements to tracebacks in recent versions. See how tracebacks have evolved over the last couple of major releases and where there’s still some work left to be done. Check out the discussion on Hacker News.


- [在 Cython 中实现 C++ 虚函式](https://pycoders.com/link/5713/web)
    + JUAN DIEGO CABALLERO 
    + • Shared by JDC

Learn how one team created Python bindings for a C++ library by implementing virtual functions in Cython. This article is a follow-up to an article we featured last year.

- [用 hypothesis 基于属性的测试以及相关用例](https://pycoders.com/link/5700/web)
    + YING WANG

Testing software is hard. Property-based testing can help you create more effective tests. Learn how to do property-based testing with the hypothesis framework by looking at some real-world use cases.

(`是也乎:`


![珢神?](http://ydlj.zoomquiet.top/ipic/2021-02-10-ScreenShot%202021-02-10%2011.05.44.jpg)

不是那个 珢神...

)

- [Python 指导委员会接受 PEP 634](https://pycoders.com/link/5695/web)
    + PYTHON.ORG

Pattern matching, which adds a kind of switch-case statement to Python, has been accepted.

(`是也乎:`

PEP 的受理速度越来越快了

)


- [用 Pip 和 Virtualenv 管理 Python 依赖关系](https://pycoders.com/link/5726/web)
    + REAL PYTHON 
    + course

Get up to speed with Python dependency management quickly and go from “writing scripts” to “building applications” with this complete course.

(`是也乎:`


![Virtualenv](http://ydlj.zoomquiet.top/ipic/2021-02-10-ScreenShot%202021-02-10%2011.02.39.jpg)

)

## 探讨/吐糟
> Discussions


- [Python 内联缓存很成功](https://pycoders.com/link/5707/web)
    + RAYMOND HETTINGER

“In 3.9, access to builtins and globals had sped-up considerably. In 3.10, regular attribute access and access to __slots__ are also faster. Most everyday Python programs will benefit. This is a huge win.”



## 文章/教程/嗯哼 
> Articles, Tutorials and Talks



- [Homebrew Python 并不适合您](https://pycoders.com/link/5709/web)
    + JUSTIN MAYER 
    + opinion

Installing Python on macOS with Homebrew is pretty easy, but it comes with some quirks that might not make it the best choice for your development environment. Learn why you might not want to install Python this way and how to fix some common issues you might encounter with Homebrew.

(`是也乎:`

Homebrew 毕竟是个人作品,
在 官方没有介入前, 只能说可用, 不应该作为生产环境.

)



- [Python 开发人员专用 C 和 Dash 数据可视化](https://pycoders.com/link/5702/web)
    + REAL PYTHON 
    + podcast

Are you interested in building interactive dashboards with Python? How about a project that takes a flat data file all the way to a web-hosted interactive dashboard? This week on the show, David Amos is back, and he’s brought another batch of PyCoder’s Weekly articles and projects.

(`是也乎:`

![podcast](http://ydlj.zoomquiet.top/ipic/2021-02-10-ScreenShot%202021-02-10%2011.03.04.jpg)

)


- [所有 Python 都很慢/但有些则比其他的要快](https://pycoders.com/link/5694/web)
    + ITAMAR TURNER-TRAURING

Python is not the fastest language around, so any performance boost helps, especially if you’re running at scale. It turns out that depending where you install Python from, its performance can vary quite a bit: choosing the wrong version of Python can cut your speed by 10-20%.

(`是也乎:`

参考沈游侠的嗯哼,
Python 快其实并不在运行时,
而是整个工程推进的速度哪.

)

- [如何加快 Scikit 学习模型训练](https://pycoders.com/link/5704/web)
    + MICHAEL GALARNYK 
    + • Shared by Michael Galarnyk

Sometimes scikit-learn models can take a long time to train. In this article, you’ll explore three approaches to optimizing the model training process.


(`是也乎:`


调整参数之后...

)


- [Python 内部函数: 有什么用?](https://pycoders.com/link/5708/web)
    + REAL PYTHON

Learn what inner functions are in Python, how to define them, and what their main use cases are.


(`是也乎:`

好就好在内建, 不用任何额外安装管理...

![Inner](http://ydlj.zoomquiet.top/ipic/2021-02-10-ScreenShot%202021-02-10%2011.04.33.jpg)

)


- [在 Ubuntu 20.04 上的 Python 中构建 Discord Bot](https://pycoders.com/link/5706/web)
    + MASON EGGER 
    + • Shared by Mason Egger

Learn how to build a Discord bot and host it on the DigitalOcean platform.

(`是也乎:`

Discord 是叕一个 Slack 竞品?

)



- [Qt Designer 和 Python: 更快构建 GUI 应用](https://pycoders.com/link/5705/web)
    + REAL PYTHON

Learn how to use Qt Designer to create GUIs from your windows and dialogs and use them in your Python applications.

(`是也乎:`

![Designer](http://ydlj.zoomquiet.top/ipic/2021-02-10-ScreenShot%202021-02-10%2010.56.41.jpg)

其实, 真不如手写...

)


## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [archivy: 自托管知识库](https://pycoders.com/link/5721/web)
    + GITHUB.COM/ARCHIVY

(`是也乎:`


本地私人知识仓库, 
最大的问题就是难以跨屏哪...

一直以来各种折腾后,
发现 Apple 的备忘录竟然是个 MVP 私人知识仓库,
除了搜索不怎么灵之外.

)

- [reloadr: Python 热代码重载工具](https://pycoders.com/link/5714/web)
    + GITHUB.COM/HOH

(`是也乎:`

嗯哼? 这个结合 Supervisor 可是能真正拓展 Python 应用系统的鲁捧性哪.

)

- [django-unicorn: 神奇的 Django 全栈框架](https://pycoders.com/link/5720/web)
    + GITHUB.COM/ADAMGHILL

(`是也乎:`

![unicorn](http://ydlj.zoomquiet.top/ipic/2021-02-10-ScreenShot%202021-02-10%2010.54.32.jpg)

嗯哼? 唯一不支持 Websockets 的框架?

)


- [watchpoints: Python 的易用性观察点等效库](https://pycoders.com/link/5692/web)
    + GITHUB.COM/GAOGAOTIANTIAN 
    + • Shared by Tian Gao

(`是也乎:`

gdb 中单一功能模块化后 ,也很香.

)


- [PipeLayer: 用于创建管道的 Python 库](https://pycoders.com/link/5722/web)
    + GITHUB.COM/GREATER-THAN 
    + • Shared by Andrew Benson

(`是也乎:`

其实 `|` 就是天然管道装配器,
只是, 流水线调试起来太麻烦了...

)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心



- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/5698/web)
    + February 3, 2020

(`是也乎:`

即便是线上的, 一样收费.

)


- [⋅ PyCascades 2021 (Virtual)](https://pycoders.com/link/5609/web)
    + February 19 – 21, 2021

(`是也乎:`

![Diamond](http://ydlj.zoomquiet.top/ipic/2021-01-20-ScreenShot%202021-01-20%2009.40.38.jpg)


)


- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5590/web)
    + May 12 – 18, 2021

(`是也乎:`

反正很早都上 油管了, 随时可以 review,
当然, 这个随时, 随时了很多年都没刷光.

)

- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
    + June 2 – 6, 2021

(`是也乎:`

![DjangoCon](http://ydlj.zoomquiet.top/ipic/2021-02-03-ScreenShot%202021-02-03%2010.27.25.jpg)

浪漫的欧洲? 这是要线下了?

)


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


# PS:
- 首发: [Issue 459 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-459.html)
- 修订: [issue-459.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-459.md)


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
>> NN 4285


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/459)






