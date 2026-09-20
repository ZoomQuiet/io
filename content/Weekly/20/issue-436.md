---
title: "Issue 436"
summary: ""
date: "2020-09-02T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> 请写更多惯用 Pythonic 代码
原文: [PyCoder's Weekly - Issue #436](https://pycoders.com/issues/436)
![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)

- 200902 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200902 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------

- [增强算术分配展开](https://pycoders.com/link/4779/web)
  - BRETT CANNON
Augmented arithmetic assignment happen whenever you do a bit of arithmetic while also assigning a value, such as a += 1. Learn how this assignment works under the hood and how the discovery of a bug in Python lead to the conclusion that most people never use the **= operator.
- [通用Python数据结构 (指南)](https://pycoders.com/link/4755/web)
  - REAL PYTHON
In this tutorial, you’ll learn about Python’s data structures. You’ll look at several implementations of abstract data types and learn which implementations are best for your specific use cases.
(`是也乎:`
![Guide](http://ydlj.zoomquiet.top/ipic/2020-09-02-ScreenShot%202020-09-02%2012.18.36.jpg)
Python 内置数据结构真的是常讲常新哪...
)
- [Python 依赖注入](https://pycoders.com/link/4771/web)
  - JAN GIACOMELLI
  - • Shared by Jan Giacomelli
Learn how to use dependency injection to write loosely-coupled yet highly-cohesive code.
(`是也乎:`
一切为了 **松耦合+高内聚**
)
- [写更多惯用 Pythonic 代码](https://pycoders.com/link/4787/web)
  - MARTIN HEINZ
  - • Shared by Martin Heinz
Learn some of the idioms and conventions that can make your Python code more readable, effective, concise and reliable.
- [Real Python Office Hours](https://pycoders.com/link/4753/web)
  - REAL PYTHON
The Real Python Office Hours is a weekly hangout where members of Real Python get the chance to interact with each other as well as Real Python authors and video course instructors. Join us live on Wednesday mornings!
(`是也乎:`
![Office](http://ydlj.zoomquiet.top/ipic/2020-09-02-ScreenShot%202020-09-02%2012.15.44.jpg)
在线开放日, 大家可以直接和 真蟒 成员交流.
)
- [Django 安全发行版: 3.1.1/3.0.10和2.2.16](https://pycoders.com/link/4773/web)
  - DJANGO SOFTWARE FOUNDATION

## 探讨/吐糟
>
> Discussions

- [Python 3.8 f字符串支持 = 用来自记录表达式和调试](https://pycoders.com/link/4781/web)
  - REDDIT
(`是也乎`:
比如:
    from datetime import date
    user = 'eric_idle'
    member_since = date(1975, 7, 31)
    f'{user=} {member_since=}'
输出:
    "user='eric_idle' member_since=datetime.date(1975, 7, 31)"
海象语法糖之后,
Python 将包含越来越多不会生龋齿的糖...
)
- [Python 单行程序的吞吃蛇游戏](https://pycoders.com/link/4777/web)
  - REDDIT
That’s a.... creative one-liner!
(`是也乎:`
代码:[oneliners/snake\.py at master · tjf801/oneliners · GitHub](https://github.com/tjf801/oneliners/blob/master/snake.py)

> (lambda pygame=**import**('pygame'),random=**import**('random'),WIDTH=800
> ...
> )())())())()))()
真的是只有一行,不过长达 3.18K;
可以说, 将 Python 多范式特性玩到位了,
将 Python 写成 LISP 没毛病.
)

## 文章/教程/嗯哼
>
> Articles, Tutorials and Talks

- [The Real Python 播客 – Episode #24: 打包Python应用程序的选项：Wheels，Docker等](https://pycoders.com/link/4774/web)
  - REAL PYTHON
  - podcast
Have you wondered, how should I package my Python code? You’ve written the application, but now you need to distribute it to the machines it’s intended to run on. It depends on what the code is, the libraries it depends on, and with whom do you want to share it. This week on the show we have Itamar Turner-Trauring, creator of the website pythonspeed.com. We discuss his article “Options for Packaging Your Python Code: Wheels, Conda, Docker, and More,” covering the how of sharing your code.
(`是也乎:`
![Episode](http://ydlj.zoomquiet.top/ipic/2020-09-02-ScreenShot%202020-09-02%2012.12.22.jpg)
)
- [为什么没人在谈论 Pandas NamedAgg?](https://pycoders.com/link/4757/web)
  - DEAN LANGSAM
  - • Shared by Dean Langsam
The as keyword from SQL is a wonderful one. You can create a complex function on a database column, and then give it an explicit name. This name can be used later in the pipeline as a reference. pandas, even though superior to SQL in most ways, really lacked this until fairly recently. Not anymore…
(`是也乎:`
凉凉有很多原由,
在 Python 世界, 最大的原因就是不够 Pythonic.
)
- [通过两个简单的例子介绍约束优化](https://pycoders.com/link/4769/web)
  - ROHAN-KEKATPURE.GITHUB.IO
  - • Shared by Rohan D. Kekatpure
Optimization algorithms are the backbone of machine learning and deep learning. Get your hands dirty by solving two classic numerical problems. You’ll learn how to translate an abstract problem into Python code, as well as how to implement a couple of optimization algorithms.
- [用 openpyxl 在 Python 中编辑 Excel 电子表格](https://pycoders.com/link/4754/web)
  - REAL PYTHON
  - course
In this course, you’ll learn how to handle spreadsheets in Python using the openpyxl package. You’ll learn how to manipulate Excel spreadsheets, extract information from spreadsheets, create simple or more complex spreadsheets, including adding styles, charts, and so on.
(`是也乎:`
![openpyxl](http://ydlj.zoomquiet.top/ipic/2020-09-02-ScreenShot%202020-09-02%2011.45.35.jpg)
csv 毕竟不太香...
)
- [如何将普通 gzip 存档转换入数据库](https://pycoders.com/link/4775/web)
  - ARTEM GOLUBIN
  - • Shared by Artem Golubin
If you have a large CSV file, you might use gzip to compress the file when you are storing it. But here’s a thought: why not compress each row of the file and concatenate them into a database of smaller files? Learn how and why you might want to do this.
(`是也乎:`
gzip 毕竟是开源的, 实在被  Python 们玩儿透了..
)
- [Django 重定向](https://pycoders.com/link/4758/web)
  - REAL PYTHON
  - course
In this course, you’ll learn everything you need to know about HTTP redirects in Django. All the way from the low-level details of the HTTP protocol to the high-level way of dealing with them in Django.
(`是也乎:`
![Redirects](http://ydlj.zoomquiet.top/ipic/2020-09-02-ScreenShot%202020-09-02%2011.46.14.jpg)
)
- [应该知道的 5对 Python 魔术方法](https://pycoders.com/link/4783/web)
  - YONG CUI
Magic, or “dunder,” methods are an important part of creating custom classes in Python. Learn about some commonly used magic methods by exploring hem in pairs that are frequently used together.
- [用 Python 和 开放飞行数据 构建自己的航班跟踪应用程序](https://pycoders.com/link/4768/web)
  - GEOMATICS
Learn how to use open air traffic data to plot aircraft positions on a map and build an interactive web application using the Bokeh plotting framework.
(`是也乎:`
Bokeh 是个好框架, 只是后来取消直接图片输出, 是个囧操作...
)

## 好物/妙品/
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [pippi: Python 的计算机音乐](https://pycoders.com/link/4766/web)
  - GITHUB.COM/LUVSOUND
(`是也乎:`
不是创作平台, 是后期处理框架.
)
- [gzipi: 用于索引 Gzip 文件以支持类似随机访问的工具](https://pycoders.com/link/4756/web)
  - GITHUB.COM/PROFOUNDNETWORKS
- [DearPyGui: GPU 加速的 Python GUI 框架](https://pycoders.com/link/4782/web)
  - GITHUB.COM/HOFFSTADT
- [django-newsfeed: A News-Curator and News Subscription Package for Django](https://pycoders.com/link/4765/web)
  - GITHUB.COM/SAADMK11
  - • Shared by Maksudul Haque
- [hickory: Hickory, Dickory, Dock… 在命令行上进行 Python 调度!](https://pycoders.com/link/4760/web)
  - GITHUB.COM/MAXHUMBER
  - • Shared by Max Humber
(`是也乎:`
反正大家就是对 crontab 看不上眼,
太难以调试了...
不过, 无论什么其它方案, 都难以拼过 crontab 的稳定哪
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Beginner Python Study Group](https://pycoders.com/link/4770/web)
  - September 9, 2020
  - Webinar
(`是也乎:`
zoom 提供的网络活动服务.
![Webinar](http://ydlj.zoomquiet.top/ipic/2020-09-02-ScreenShot%202020-09-02%2011.26.25.jpg)
)
- [⋅ PyCon Taiwan 2020](https://pycoders.com/link/4767/web)
  - September 5 to September 7, 2020
(`是也乎:`
真的猛士是无视疫情的...
)

## DAMA
>
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

# PS

- 首发: [Issue 436 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-436.html)
- 修订: [issue-436.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-436.md)

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
>> NN 4124
![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/436)
