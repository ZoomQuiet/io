---
title: "Issue 410"
summary: ""
date: "2020-03-04T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> EOF不是字符
原文: [PyCoder's Weekly - Issue #410](https://pycoders.com/issues/410)
![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200304 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200304 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------

- [Python Requests 高级用法](https://pycoders.com/link/3682/web)
  - DANI HODOVIC
“While it’s easy to immediately be productive with requests because of the simple API, the library also offers extensibility for advanced use cases. If you’re writing an API-heavy client or a web scraper you’ll probably need tolerance for network failures, helpful debugging traces and syntactic sugar.”
- [EOF不是字符](https://pycoders.com/link/3685/web)
  - RUSLAN SPIVAK
Do you know how an application knows when a read operation reaches the end of a file? In this interesting read, explore what EOF (end-of-file) really is by writing your own version of the Linux cat command in ANSI C, Python, Go, and JavaScript.
- [用 Django ORM 进行双重检查的锁定](https://pycoders.com/link/3688/web)
  - LUKE PLANT
The double-checked locking pattern is useful when you need to restrict access to a certain resource to stop simultaneous process from working on it at the same time. Learn how to apply this pattern in Django using the ORM and database level locking features.
- [Python Bindings: 从 Python 调用 C 或 C++](https://pycoders.com/link/3701/web)
  - REAL PYTHON
What are Python bindings? Should you use ctypes, CFFI, or a different tool? In this step-by-step tutorial, you’ll get an overview of some of the options you can use to call C or C++ code from Python.
(`是也乎:`
![Bindings](http://ydlj.zoomquiet.top/ipic/2020-03-04-ScreenShot%202020-03-04%2010.47.07.jpg)
虽然 Py 们好用又好写,
但是, 真正比拼的还是对 C/C++ 们的调用能力,
毕竟这个世界底层是 C 家族的.
)
- [PyPy 状态 Blog: PyPy 和 CFFI 已迁移到 Heptapod](https://pycoders.com/link/3671/web)
  - MOREPYPY.BLOGSPOT.COM
PyPy has moved the center of their development off Bitbucket and to the new foss.heptapod.net/pypy
(`是也乎:`
因为 Bitbucket 凉了...
俺的仓库也得迁移了...
foss.heptapod.net <- GitLab企业版, 免费使用环境...
)
- [PyCon 2020: March 2 COVID-19 下的更新](https://pycoders.com/link/3709/web)
  - PYCON.BLOGSPOT.COM
“As of March 2, PyCon 2020 in Pittsburgh, PA is scheduled to happen.”
(`是也乎:`
技术大会也被疫情了
)
- [对匹兹堡 PyCon 感到兴奋的 19 个理由](https://pycoders.com/link/3669/web)
  - EMILY MOREHOUSE
(`是也乎:`
Pittsburgh PyCon 的宣传文案来了...
)

## 讨论
>
> Discussions

- [调查: PyLadies对您意味着什么?](https://pycoders.com/link/3663/web)
  - TWITTER.COM/
  - LOOOORENANICOLE
(`是也乎:`
被老爹点过名的品牌活动,
现在越来越会进行 SNS 营销了.
)
- [Dictionary Union (PEP 584) 将合并入 Python 3.9](https://pycoders.com/link/3680/web)
  - REDDIT
(`是也乎:`
开始大讨论了...
)

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [用 CMake 和 Setuptools 为 C++ 项目打包和分发 cppyy 生成的 Python绑定](https://pycoders.com/link/3700/web)
  - CAMILLE SCOTT
“I rewrote the cppyy CMake modules to be much more user friendly and to work using only Anaconda/PyPI packages, and to generate more feature-complete and customizable Python packages using CMake’s configure_file, while also supporting distribution of cppyy pythonization functions.”
(`是也乎:`
沈游侠曰过:
    每个程序猿
    总会去写
    自己反复用一生的 makefile
实在是 CMake 这工具, 早已就解决了一切自动化编译问题.
)
- [从头开始的 Python 多项式回归](https://pycoders.com/link/3673/web)
  - RICK WIERENGA
Polynomial regression is a core concept underlying machine learning. Learn how to build a polynomial regression model from scratch in Python by working you a real world example to predict salaries based on job position.
- [如何实现 Python 堆栈](https://pycoders.com/link/3679/web)
  - REAL PYTHON
  - video
Learn how to implement a stack data structure in Python. You’ll see how to recognize when a stack is a good choice for data structures, how to decide which implementation is best for a program, and what extra considerations to make about stacks in a threading or multiprocessing environment.
(`是也乎:`
![pop](http://ydlj.zoomquiet.top/ipic/2020-03-04-ScreenShot%202020-03-04%2010.40.34.jpg)
打年糕? 这梗用的好.
)
- [显式传递 Python 线程状态](https://pycoders.com/link/3665/web)
  - VICTOR STINNER
Eric Snow has been working on solving multi-core Python via subinterpreters since 2015. In this article, core developer Victor Stinner discusses how state is passed between interpreters and summarizes his proposal for explicitly passing state to internal C function calls.
(`是也乎:`
多线程状态, 这一直是玄学问题哪...
不过, 这也是 PL 重要的科题了...可以养活很多博士了.
)
- [nbdev: 用 Jupyter 笔记本 几乎操作一切](https://pycoders.com/link/3683/web)
  - JEREMY HOWARD
A Python programming environment called nbdev, which allows you to create complete python packages, including tests and a rich documentation system, all in Jupyter Notebooks.
(`是也乎:`
这的确是 IPython 独立为 Jupyter 的原因,
![smalltalk](https://www.fast.ai/images/nbdev/smalltalk.png)
不过想学 smalltalk 们代码/运行时合体, 还有距离哪
)
- [处理旧版代码](https://pycoders.com/link/3662/web)
  - ISHA TRIPATHI
Learn about some of the common problems you encounter when dealing with legacy codebases and how to overcome them in an efficient way that balances delivery with code quality.
(`是也乎:`
俗称屎山.
)
- [Python 中带有 ordered_enum 的完全有序枚举](https://pycoders.com/link/3689/web)
  - WILLIAM WOODRUFF
Python’s enum.Enum does not provide ordering by default. See how ordering can be added to enums and why these orderings are useful in the first place.
(`是也乎:`
无论字典们内部数据结构多科学,
排序, 还是日常最常见的期待.
)
- [有条件承保](https://pycoders.com/link/3677/web)
  - NIKITA SOBOLEV
  - • Shared by sobolevn
Sometimes your code has to take different paths based on the external environment. Make sure that your coverage follows it smoothly.
(`是也乎:`
爽滑的进行外部目录依赖变更..
还是靠人的事先清醒的规划哪...
)
- [部署机器学习模型: gRPC 和 TensorFLow 服务](https://pycoders.com/link/3704/web)
  - RUBIKSCODE.NET
Learn how to deploy TensorFlow models and consume predictions via gRPC.
(`是也乎:`
叕见 gPRC ... 所以, 俺一直说:
    人生苦短 Python 当歌
)
- [Pinterest 的技术堆栈演进时间表](https://pycoders.com/link/3670/web)
  - STACKSHARE.IO
Plenty of Python in there…
(`是也乎:`
从 MySQL 到 Apache Druid ,
叕一则技术栈演变故事...
)
- [用 Python 动态编程特性来测量 DNA 相似性](https://pycoders.com/link/3686/web)
  - ANDREW TREADWAY
(`是也乎:`
当年, 这可是 Perl 的领域..现在也都是 Py 的了
)
- [将元数据添加到 PDF](https://pycoders.com/link/3668/web)
  - DANIEL ROY GREENFELD
(`是也乎:`
自动化批量处置 pdf 的好物
)
- [如何将 Python 字典数据 转换为 Pandas DataFrame](https://pycoders.com/link/3693/web)
  - ERIK MARSJA
(`是也乎:`
非常实用哪...毕竟, 中间有 numpy 在乱来...
)
- [用 Arcade 和 Python-Banyan 进行点对点游戏](https://pycoders.com/link/3707/web)
  - ALAN YORINKS
  - • Shared by Alan Yorinks
- [Django Speed Handbook: 加快Django应用的速度](https://pycoders.com/link/3691/web)
  - OPENFOLDER.SH
  - • Shared by Shibel
(`是也乎:`
分享人, 差点儿以为是 `西贝` ...
)

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [doit: 任务管理和自动化工具](https://pycoders.com/link/3672/web)
  - PYDOIT
(`是也乎:`
想法很好...
可惜, 用起来太复杂了点儿...
)
- [StellarGraph: 针对图的机器学习](https://pycoders.com/link/3681/web)
  - STELLARGRAPH
(`是也乎:`
叕一则针对图形的 ML 框架,
但是, 不是小样本的..
)
- [cppyy: 自动 Python-C++ 绑定](https://pycoders.com/link/3674/web)
  - WLAV
(`是也乎:`
叕一个 Py->C++ 转换工具, 不知道靠谱卟
)
- [Funnelplot: 用于可视化子组方差的简单漏斗图生成](https://pycoders.com/link/3698/web)
  - JOHNHW
(`是也乎:`
![output_6_1](https://github.com/johnhw/funnelplot/raw/master/docs/images/output_6_1.png)
神奇哪, 首次见到在 windows 平台上完成的示例, 而且老实的将错误也记录下来了:

```python
# load some example data
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
from funnelplot.core import funnel
# create a suitable axis
fig,ax = plt.subplots(figsize=(4,6))
ax.set_frame_on(False)
# funnel plot, using 0.5% -> 99.5% interval
funnel(df=data("Caschool"), x="testscr", group="county", percentage=99.5, error_mode="data")
C:\Users\John\Dropbox\devel\funnelplot\funnelplot\core.py:14: RuntimeWarning: invalid value encountered in true_divide
  return band / np.sqrt(group_size)
C:\Users\John\Dropbox\devel\funnelplot\funnelplot\core.py:14: RuntimeWarning: divide by zero encountered in true_divide
  return band / np.sqrt(group_size)
```

)

- [flakehell: Legacy-First Wrapper Around Flake8 Linter 使其超赞](https://pycoders.com/link/3687/web)
  - WE MAKE SERVICES
- [Parse: 基于 Python format() 语法的规范解析字符串](https://pycoders.com/link/3675/web)
  - RICHARD JONES
- [ordered_enum: Python 完全排序枚举](https://pycoders.com/link/3684/web)
  - WILLIAM WOODRUFF
- [napkin: Python 作为用编写 PlantUML 序列图的 DSL](https://pycoders.com/link/3678/web)
  - GITHUB.COM/PINETR2E
(`是也乎:`
虽然 UML 的理想没实现, 但是, UML 图元是真正深入人心了...
PlantUML 是非常赞的图形脚本工具, 但是, 毕竟语法很囧;
![distributed_control](https://github.com/pinetr2e/napkin/raw/master/images/distributed_control.png)
这样的图, DSL 为:

```python
@napkin.seq_diagram()
def distributed_control(c):
    user = c.object('User')
    order = c.object('Order')
    orderLine = c.object('OrderLine')
    product = c.object('Product')
    customer = c.object('Customer')
    with user:
        with order.calculatePrice():
            with orderLine.calculatePrice():
                product.getPrice('quantity:number')
                with customer.getDiscountedValue(order):
                    order.getBaseValue().ret('value')
                    c.ret('discountedValue')
```

嗯哼? 也没好哪儿去哪...对比:

```python
@startuml
participant User
participant Order
participant OrderLine
participant Product
participant Customer
User -> Order : calculatePrice()
activate Order
    Order -> OrderLine : calculatePrice()
activate OrderLine
    OrderLine -> Product : getPrice(quantity:number)
    OrderLine -> Customer : getDiscountedValue(Order)
activate Customer
    Customer -> Order : getBaseValue()
    activate Order
    Customer <-- Order: value
    deactivate Order
    OrderLine <-- Customer: discountedValue
deactivate Customer
deactivate OrderLine
deactivate Order
@enduml
```

)

- [People-Detector: 照片和视频中的人物检测](https://pycoders.com/link/3706/web)
  - GITHUB.COM/HUMANDECODED
  - • Shared by Tom
- [pytest-monitor: pytest插件/用于在测试会话期间分析资源使用情况](https://pycoders.com/link/3708/web)
  - GITHUB.COM/CFMTECH
  - • Shared by Jean-Sébastien Dieu
- [Generate 从日期字符串生成Python strftime() 格式代码](https://pycoders.com/link/3696/web)
  - PYSTRFTIME.COM
  - • Shared by Lachlan Eagling

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyTexas 2020](https://pycoders.com/link/3667/web)
  - May 16 to 17, 2020
  - in Austin,
  - TX
- [⋅ HackBVICAM National Student’s Convention 2k20](https://pycoders.com/link/3676/web)
  - March 13 to March 14, 2020

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [中国「远程办公」大考](https://edu.csdn.net/huiyiCourse/detail/1159)
  - 抗击疫情，
  - 科技公司在行动
  - 系列
(`是也乎:`
2020.2.29 CSDN 继续线上技术峰会,
大妈, 吐糟完毕:
[拙见/ 什么是自驱力?](https://mp.weixin.qq.com/s/pi7JosExERPM-zRt27bA_A)
现场录音-> [CSDN/远程办公大考/大妈主持/吐糟生肉版/fm.101.camp 蟒营™电台 钩陈各种值得探讨](https://fm.101.camp/2020/csdn-soho-panel.html)
)

# PS

- 首发: [Issue 410 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-410.html)
- 修订: [issue-410.md](<https://github.com/PyChina/weekly/blob/master/content/Issue/issue-410>  .md)

-------------
>> NN 3942
好文笔,感叹号年度配额: **1/3**
-------------
ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g)**
就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF485D4Q90XdDA7g):

```python
私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开课程: 蟒营 (订阅号: Mainium)
全国大会: PyChina (订阅号: PyChinaOrg)
本地社区: 
    GDG珠海 (订阅号: GDG-ZhuHai)
    TFUG珠海 (订阅号: ZH_TFUG)
历史吐糟: Chaos42 (订阅号 PythoniCamp)
```

-------------
