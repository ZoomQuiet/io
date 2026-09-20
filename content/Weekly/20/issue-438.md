Title: Issue 438
Slug: issue-438
Date: 2020-09-16 11:42
Tags: Weekly,Python,pycoders,ZH


> 低于3.6 版本的 Python 皆已 EOL


原文: [PyCoder's Weekly - Issue #438](https://pycoders.com/issues/438)



![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)


- 200916 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200916 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------



- [从Python调 C/C++ 的幕后](https://pycoders.com/link/4874/web)
    + ANTON ZHDAN-PUSHKIN 
    + • Shared by 
    + Anton Zhdan-Pushkin

Take a walk through internals of ctypes, libffi, binary extensions, and other tools that power seamless interoperability of CPython and C.


(`是也乎:`

嗯哼, 允许自我推荐的?

![GCC](http://ydlj.zoomquiet.top/ipic/2020-09-16-ScreenShot%202020-09-16%2010.54.13.jpg)

不过, 这个漫画风格是喜欢的.

)

- [Python 中的面向数据的编程](https://pycoders.com/link/4860/web)
    + BRIAN KIHOON LEE

Python’s success in scientific and numerical computing is based largely on the performance of libraries like NumPy and SciPy. What is is that makes NumPy so effective, and where is numerical Python is headed in the future?

(`是也乎:`

面向数据编程,
嗯哼, 18年前, Limodou 在 PyCon中国大会上就提出过,
其实, 所有编程语言, 本质上都是这个实践行为;

只是有的语言将这个思想融合到了自身,比如说 LISP;
有的只能通过各种模块来融合.

)

- [用 conda-pack 收缩您的 Conda Docker 映像](https://pycoders.com/link/4887/web)
    + ITAMAR TURNER-TRAURING

If you’re building a Docker image that’s based on Conda, the resulting images can be huge. Learn one way to do shrink image sizes, by combining the conda-pack tool with multi-stage builds.

(`是也乎:`

甩干技巧.

)


- [The Real Python Podcast – Episode #26: 与Michael Kennedy 一起 Python 播客的5年: 成长/GIL/异步等](https://pycoders.com/link/4891/web)
    + REAL PYTHON 
    + podcast

Why is Python pulling in so many new programmers? Maybe some of that growth is from Python being a full-spectrum language. This week on the show we have Michael Kennedy, the host of the podcast “Talk Python to Me”. Michael reflects on five years of podcasting about Python, and many of the changes he has seen in the Python landscape.

(`是也乎:`


![Podcast](http://ydlj.zoomquiet.top/ipic/2020-09-16-ScreenShot%202020-09-16%2010.48.59.jpg)

)


- [pip 可用性调查](https://pycoders.com/link/4880/web)
    + PYTHON SOFTWARE FOUNDATION

(`是也乎:`

这个问卷大家都应该积极嗯哼一下,

光是加速墙内 pip 镜像群,
就值得嗯哼了..

)


- [Python 101 第二版发布](https://pycoders.com/link/4892/web)
    + MIKE DRISCOLL

- [seaborn 0.11.0 现已发布](https://pycoders.com/link/4882/web)
    + PYDATA.ORG

(`是也乎:`

seaborn 好同志,
是 matplotlib 的专用形象设计师,
真爱.

)


- [所有低于3.6的Python版本现已 EOL](https://pycoders.com/link/4870/web)
    + PYTHON.ORG

(`是也乎:`

End of Life (EOL) release cycle is frozen; no further changes can be pushed to it.

![EOL](http://ydlj.zoomquiet.top/ipic/2020-09-16-ScreenShot%202020-09-16%2010.45.43.jpg)

嗯哼? 俺比较好奇的是 `Łukasz` 怎么念?

)



## 探讨/吐糟
> Discussions


- [timeit 以及其 default_timer 完全不同意](https://pycoders.com/link/4876/web)
    + STACK OVERFLOW

Ah, the joys of benchmarking.

- [大家自 Epochs 以来 1600000000 秒快乐!](https://pycoders.com/link/4865/web)
    + REDDIT

As u/bananaEmpanada eloquently put it: Happy GNU year!

(`是也乎:`

不知不觉中已经工作了这么久....

不过 BLAME! 中, 是以小时为单位的.

)




## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [用 FastAPI 和 Streamlit 服务机器学习模型](https://pycoders.com/link/4875/web)
    + AMAL SHAJI 
    + • Shared by Amal Shaji

Both FastAPI and Streamlit are quickly gainaing popularity in the Python ecosystem. Learn how to use them together to deploy a machine learning model with a fast API and modern web interface.

(`是也乎:`

FastAI 在崛起, 毕竟是大学教授有推广班底...

)


- [Python 中的 CLI](https://pycoders.com/link/4886/web)
    + REAL PYTHON 
    + course

Command line arguments are the key to converting your programs into useful and enticing tools that are ready to be used in the terminal of your operating system. In this course, you’ll learn their origins, standards, and basics, and how to implement them in your program.

(`是也乎:`

![CLI](http://ydlj.zoomquiet.top/ipic/2020-09-16-ScreenShot%202020-09-16%2010.28.11.jpg)

俺的体验:
最早坚信自己撸最好;
后来喜欢 docopt, 
然后实用 fabric;
接着被迫升级到 invoke;
click 怎么用都感觉哪儿不对,
套上 Typer 后, 一切顺心了...


)



- [Pandas 图表: 面向初学者的 Python 数据可视化](https://pycoders.com/link/4863/web)
    + REAL PYTHON

In this tutorial, you’ll get to know the basic plotting possibilities that Python provides in the popular data analysis library pandas. You’ll learn about the different kinds of plots that pandas offers, how to use them for data exploration, and which types of plots are best for certain use cases.

(`是也乎:`


![Plot](http://ydlj.zoomquiet.top/ipic/2020-09-16-ScreenShot%202020-09-16%2010.26.33.jpg)

俺的经验, 还是各自干最擅长的,
Jupyter 组织过程,
Pandas 专心 dataframe;
用其它专门图表模块制图.

)


- [用 Pandas 读取 HTML 表格](https://pycoders.com/link/4861/web)
    + CHRIS MOFFITT

The pandas read_html() function can quickly scrape data from HTML tables. Learn how to use it, as well as some techniques for cleaning HTML data.


(`是也乎:`

Pandas 就象一个马戏团, 什么都能耍出来...

)


- [探索 Euler 解决 ODE 的方法](https://pycoders.com/link/4871/web)
    + HASSAM UDDIN

A great way to get comfortable with math concepts is to program them, and Python is a great language for exploring mathematical ideas, even if it’s not always the most efficient.

(`是也乎:`

Python 表述的直觉性, 
对于数学概念的探索更加友好.

)


- [从概念到与 Django 在一起生活两周](https://pycoders.com/link/4864/web)
    + MATT LAYMAN

How can you build a fully functional web application for a customer in a short period of time? Matt shares his experience building such a web app for a nonprofit organization while participating in a local virtual hackathon in Frederick, MD.

(`是也乎:`

试婚

)


- [Python 101: JSON简介](https://pycoders.com/link/4877/web)
    + MIKE DRISCOLL

Learn the basics of working with JSON with Python.

(`是也乎:`

JSON 应该也算中古技术了吧...

)

   
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code

- [VideoPose3D: 用视频中 2D 关键点轨迹高效进行 3D 人姿估计](https://pycoders.com/link/4890/web)
    + GITHUB.COM/FACEBOOKRESEARCH


- [Wav2Lip: 对野外视频进行准确口型同步](https://pycoders.com/link/4888/web)
    + GITHUB.COM/RUDRABHA

- [nagini: 基于 Viper 验证结构的 Python 3 静态验证程序](https://pycoders.com/link/4869/web)
    + GITHUB.COM/MARCOEILERS



- [pypyr: 自动化管道的任务运行器](https://pycoders.com/link/4885/web)
    + GITHUB.COM/PYPYR/PYPYR/ 
    + • Shared by yaythomas

(`是也乎:`

![pypyr](http://ydlj.zoomquiet.top/ipic/2020-09-16-ScreenShot%202020-09-16%2010.22.21.jpg)

走心了, 就是基于 Ymal 比较嗯哼...

可以视之为简化版本 Ansible ...

)


- [Staircase: 含 Step Functions 建模的数据分析包](https://pycoders.com/link/4893/web)
    + RAILING.READTHEDOCS.IO 
    + • Shared by Riley Clement

(`是也乎:`

Step Functions ~ 阶跃函数? 

)

- [awesome-falsehood: 程序员相信的虚事儿...](https://pycoders.com/link/4883/web)
    + GITHUB.COM/KDELDYCKE

(`是也乎:`

这可能是就程序猿界的 10万+ 套路集锦了.

![falsehood](http://ydlj.zoomquiet.top/ipic/2020-09-16-ScreenShot%202020-09-16%2010.18.04.jpg)

可以直接作为 fuzzy 测试的核心列表来用了..

)




## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ DjangoCon Europe 2020 (Online)](https://pycoders.com/link/4889/web)
    + September 18 to September 20, 2020

- [⋅ PyCon APAC 2020 (Online)](https://pycoders.com/link/4862/web)
    + September 19 to September 21, 2020

- [⋅ GeoPython 2020 & PyML 2020 (Online)](https://pycoders.com/link/4873/web)
    +  September 21 to September 23, 2020



## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

101camp12py 报名最后一周

![报名](http://ydlj.zoomquiet.top/ipic/2020-08-26-200816-reg-zip.jpg)

```

课程规划:

    报名截止 2020.09.21
    正式开课 2020.09.27
    课程结束 2020.11.08

```
详情 => [蟒营®编程思维提高班 Python版/ 第12期](https://py.101.camp/)


# PS:
- 首发: [Issue 438 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-438.html)
- 修订: [issue-438.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-438.md)


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
>> NN 4138


![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/438)






