Title: Issue 371
Slug: issue-371
Date: 2019-06-05 09:42
Tags: Weekly,Python,pycoders,ZH


原文: [PyCoder's Weekly - Issue #371](https://pycoders.com/issues/371)

![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)

------



- [Python 中的指针: 有什么意义? ](https://pycoders.com/link/1758/web)
    + REAL PYTHON

Get a clearer understanding of Python's object model and learn why pointers don't really exist in Python. You'll also cover ways to simulate pointers in Python without the memory-management nightmare.


(`是也乎:`

![Point](https://ipic.zoomquiet.top/2019-06-05-ScreenShot%202019-06-05%2010.10.55.jpg)

这个插图真心没 got 到技术点儿...

)

- [Python 和并发: CSP 和协同程序](https://pycoders.com/link/1772/web)
    + YING WANG

Nice overview of "communicating sequential processes" (CSP), a concurrency model similar to the notion of actor models, and how it can be implemented in Python.

(`是也乎:`

珢神很久没嗯哼点儿什么了...
等等, 嚓同音, 不是珢神...

简单说, 并行计算在 Py 中不是难事儿, 困难的只是在生产环境中稳定嗯哼起来?

反正作为学术问题, 这个方向还够养活几个博士的...

)

- [CNNs,第2部分:训练卷积神经网络](https://pycoders.com/link/1769/web)
    + VICTOR ZHOU

A nice walkthrough of deriving backpropagation for CNNs and implementing it from scratch in Python.

- [重写 Slack Python SDK](https://pycoders.com/link/1745/web)
    + RODNEY URQUHART

The lead maintainer of the Slack Python SDK gives a retrospective about refactoring the current SDK and migrating it from Python 2 to Python 3.

(`是也乎:`

嗯哼? 应该喜大普奔嘛? Py2->py3

)


- [Python 的 Caduceus 综合症](https://pycoders.com/link/1740/web)
    + VICKI BOYKIS

"Which of the two should the ecosystem tackle as a priority? Should they clean up all backwards compatibility first? (that would be PEP 594, 'removing dead batteries from the standard library') Should they focus on moving everyone over to the new features?"

(`是也乎:`

[Caduceus](http://www.rof.com/assets/images/2320-pq.jpg)

Py2/3 变成现实中纠缠态事务,难以决策

)


- [PyPI 现在支持双因素身份验证](https://pycoders.com/link/1761/web)
    + ERNEST W. DURBIN III

Protect your PyPI login with two-factor authentication using Time-based One-time Password (TOTP) app.

(`是也乎:`

但是, 镜像也就越来越困难...

)


- [Language Summit 闪电演讲(摘要)](https://pycoders.com/link/1757/web)
    + A. JESSE JIRYU DAVIS 
    + • Shared by Ricky White

Summaries of the lightning talks presented at the Python Language Summit at PyCon 2019.

(`是也乎:`

其实, 闪电演讲才是一个大会的灵魂.

)


- [PSF Q2 2019 筹款活动](https://pycoders.com/link/1780/web)
    + PYTHON.ORG

Support the Python Software Foundation by donating in the quarterly donation drive. Your donations help fund Python conferences, workshops, user groups, community web services, and more.




## 讨论
> Discussions

- [Python 3.8 性能新闻](https://pycoders.com/link/1735/web)
    + RAYMOND HETTINGER

"Today, code was checked in that substantially sped-up global lookups and builtin lookups. They are still slower than accessing locals and non-locals but only modestly so."

- [是否有人在生产中使用PyPy? ](https://pycoders.com/link/1755/web)
    + REDDIT

(`是也乎:`

好问题...其实, 一直有, 只是公司都没成功...

)


## 文章,教程和嗯哼 
> Articles, Tutorials and Talks


- [算法作为对象](https://pycoders.com/link/1766/web)
    + ANDY G 
    + • Shared by Python Bytes

"We usually think of an algorithm as a single function with inputs and outputs. [... ] This is fine until one actually attempts to implement it as a single function; all the little details add up until you're left with a gigantic, monolithic function."

- [用 Python 嗯哼 HTTP 请求](https://pycoders.com/link/1749/web)
    + REAL PYTHON video

The "requests" library is the de facto standard for making HTTP requests in Python. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application. This course shows you how to work effectively with "requests", from start to finish.

(`是也乎:`

!["requests"](https://ipic.zoomquiet.top/2019-06-05-ScreenShot%202019-06-05%2010.05.14.jpg)

没毛病的模块, 问题是可能永远进入不了内建模块...


)


- [OOP 在 Python 和 Java](https://pycoders.com/link/1732/web)
    + REAL PYTHON

Learn about the practical differences in Python vs Java for object-oriented programming. By the end, you'll be able to apply your knowledge to Python, understand how to reinterpret your understanding of Java objects to Python, and use objects in a Pythonic way.

(`是也乎:`

![OOP](https://ipic.zoomquiet.top/2019-06-05-ScreenShot%202019-06-05%2010.04.40.jpg)

等等, 为什么是印度MM ?
)



- [准确性:从分类到聚类评估](https://pycoders.com/link/1776/web)
    + STANISLAS MORBIEU 
    + • Shared by Stanislas Morbieu

Accuracy is often used to measure the quality of a classification. It is also used for clustering. However, the scikit-learn accuracy_score function only provides a lower bound of accuracy for clustering. This blog post explains how accuracy should be computed for clustering.

- [Python函数解包(* args和** kwargs)](https://pycoders.com/link/1767/web)
    + CARLOS BALDERAS 
    + • Shared by Carlos Balderas

15 quick examples to get a new Python coder comfortable with *args and **kwargs as parameters.

- [为业务安利 Python](https://pycoders.com/link/1751/web)
    + CHRIS MOFFITT

"Five to 10 years ago, it might have been quite an uphill battle to try to bring Python into your organization to solve your business problems. With the rise of Python's popularity in the Data Science world, you will have a much smaller hill to climb."

(`是也乎:`

隔壁 Rubista 在反思 Ruby 还有希望嘛?

Python 则依然在向商界推广...

)

- [Dataclasses and Attrs: 何时以及为何](https://pycoders.com/link/1734/web)
    + FLAVIO CURELLA

Python 3.7 introduced dataclasses, which design is based on the attrs library. This article shows the way the author uses dataclasses and attrs, why they think you should use both, and why attrs is still very relevant.



- [将数据验证用于鲁棒 API](https://pycoders.com/link/1775/web)
    + ENZO CALAMIA

How using schema-based data validation tools can help you write more robust web APIs.


(`是也乎:`

鲁棒的接口...

)

- [Python's Datatable Package 概述](https://pycoders.com/link/1762/web)
    + PARUL PANDEY

Datatable is a Python library for efficient multi-threaded data processing, with the support for out-of-memory datasets.

(`是也乎:`

专注嗯哼超过内存支持规范的大数据包

)

- [面向 Python  开发人员的Git和GitHub简介s](https://pycoders.com/link/1733/web)
    + REAL PYTHON video

What is Git, what is GitHub, and what's the difference? Learn the basics of Git and GitHub from the perspective of a Pythonista in this step-by-step course.

(`是也乎:`

![GitHub.py](https://ipic.zoomquiet.top/2019-06-05-ScreenShot%202019-06-05%2009.57.56.jpg)


很用心, 只是, Pythoneer 有不用 github 的嘛?

)

- [在 Heroku 上部署 Django 生产系统](https://pycoders.com/link/1773/web)
    + TESTDRIVEN.IO

How to simplify the process of deploying, maintaining, and scaling a production-grade Django app on Heroku.



## 好物
> Interesting Projects, Tools and Libraries, Projects & Code

- [PugSQL: 从磁盘上的一组SQL文件创建数据库函数的 Python 模块](https://pycoders.com/link/1744/web)
    + PUGSQL.ORG

(`是也乎:`

![PugSQL](https://pugsql.org/assets/images/pug-transparent.png)

是 clj [HugSQL](https://www.hugsql.org/) 的 Python 再制;

用自然的 Python 代码, 生成标准的 SQL 语句, 
来执行 DB 嗯哼...

)

- [lineflow: 适用于所有深度学习框架的简单 NLP 数据加载器](https://pycoders.com/link/1731/web)
    + GITHUB.COM/YASUFUMY 
    + • Shared by Yasufumi Taniguchi

- [rtv: 从终端浏览 Reddit](https://pycoders.com/link/1756/web)
    + GITHUB.COM/MICHAEL-LAZAR

(`是也乎:`

![rtv](https://github.com/michael-lazar/rtv/raw/master/resources/title_image.png)

还以为是 redis 的可视化 CLI 工具...
结果...


)


- [pico-pytest: 用于教育目的 PyTest 核心功能简约重新实现](https://pycoders.com/link/1739/web)
    + GITLAB.COM/OBESTWALTER



- [gluon-ts: Python 中的概率时间序列建模](https://pycoders.com/link/1765/web)
    + GITHUB.COM/AWSLABS

(`是也乎:`

时序处理越来越重要了...对应生态也在自然高速成长中

)


- [Parsl: Py 中的并行脚本语言](https://pycoders.com/link/1741/web)
    + PARSL-PROJECT.ORG

(`是也乎:`

好东西, 毕竟, 配置 Jupyter 嗯哼并行计算,还是比较麻烦...

![parsl](http://parsl-project.org/images/parsl-compute.png)

所以, 直接在 Jupyter 之上加强了...

)


- [both: Python 2 + 3 兼容层](https://pycoders.com/link/1759/web)
    + BAKKERTHEHACKER.GITHUB.IO

(`是也乎:`

其实, Py2/3 最大的冲突,不在语法, 而在生态体系哪...

很多优秀模块根本就没迁移/兼容到 py3;

所以, 这种混合新老代码, 想在一起自动和谐运行, 实在是对运行时环境的极大嗯哼

)


- [tensorwatch: 深度学习和强化学习的调试/监控和可视化](https://pycoders.com/link/1746/web)
    + GITHUB.COM/MICROSOFT

(`是也乎:`

叕一个 TF 周边...只是 Pythonic 的话, 不是应该多嗯哼 PyTorch?
)


- [metadsl: Framework for Domain Specific Languages in Python](https://pycoders.com/link/1743/web)
    + QUANSIGHT.ORG

- [BlackSheep: Fast HTTP Server/Client Microframework for Python Asyncio](https://pycoders.com/link/1771/web)
    + GITHUB.COM/ROBERTOPREVATO

(`是也乎:`

![sheep](https://raw.githubusercontent.com/RobertoPrevato/BlackSheep/master/black-sheep.svg?sanitize=true)

叕一只微框架...

完全 bottle 样, 只是用了 py 3 的糖:

    import asyncio
    from blacksheep.client import ClientSession


    async def client_example(loop):
        async with ClientSession() as client:
            response = await client.get('https://docs.python.org/3/')

            assert response is not None
            text = await response.text()
            print(text)


    loop = asyncio.get_event_loop()
    loop.run_until_complete(client_example(loop))



)


- [materials: Python 练习和示例项目](https://pycoders.com/link/1752/web)
    + GITHUB.COM/REALPYTHON

(`是也乎:`

真蟒 的各种文章/教程, 对应的代码.

)

## 📆🐍 活动/大会
> Events

- [⋅ PyCon Israel 2019](https://pycoders.com/link/1774/web)
    +  June 3 to June 6, 2019
    +  以色列

- [⋅ Canberra Python Meetup](https://pycoders.com/link/1736/web)
    +  June 6, 2019
    +  堪培拉,澳大利亚

- [⋅ Python Miami](https://pycoders.com/link/1754/web)
    + June 8 to June 9, 2019
    + USA

- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/1770/web)
    +  June 8, 2019
    +  印度

- [⋅ Leipzig Python User Group Meeting](https://pycoders.com/link/1763/web)
    +  June 11, 2019
    +  德国

- [⋅ PyCon CZ 2019](https://pycoders.com/link/1748/web)
    + June 14 to June 17, 2019
    + 捷克

- [⋅ Dash Conference](https://pycoders.com/link/1738/web) 
    + July 16–17 in NYC
    + 大苹果




## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [蟒营 Python 入门班](https://py.101.camp/)
    + 已开班, 进入 ch08
    + 下期可能 7月1

[![PyScaffold](https://pyscaffold.org/en/latest/_images/logo.png)](https://pyscaffold.org/en/latest/)

~ helps you setup a new Python project


- [What Can I Do With Python? – Real Python](https://realpython.com/what-can-i-do-with-python/)
    + FAQ

(`是也乎:`

![Do With Py](https://ipic.zoomquiet.top/2019-05-25-ScreenShot%202019-05-25%2010.27.25.jpg)

总是永远有人问这个问题...
当然, 这个问题任何一个技术社区都有人在问...

其实, 本质上并不是对应技术是否有什么能力,
而是相反...

)


### Jobs:
> ...

- [Wangjunyu/MemectRecruitment: 文因招聘](https://github.com/Wangjunyu/MemectRecruitment)
    + 北京
    + anti-996


# 是也乎

- 190605 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190605 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
