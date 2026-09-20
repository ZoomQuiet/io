Title: Issue 359
Slug: issue-359
Date: 2019-03-13 17:17
Tags: Weekly,Python,pycoders,ZH


原文: [PyCoder's Weekly - Issue #359](https://pycoders.com/issues/359)

![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)

------




- [用 PEP 8 撰写真正 Pythonic 代码](https://pycoders.com/link/1177/web)
    + REAL PYTHON video

Learn how to write high-quality, readable code by using the Python style guidelines laid out in PEP 8. Following these guidelines helps you make a great impression when sharing your work with potential employers and team mates. Learn how to make your code PEP 8 compliant with these bite-sized lessons.

(`是也乎:`

没那么简单, 团队习惯兼容的配置又能有用, 太难
)

- [在Python中实施单一责任原则(SRP)](https://pycoders.com/link/1197/web)
    + NIKITA SOBOLEV

The Single Responsibility Principle (or SRP) is an important concept in software development. The main idea of this concept is: all pieces of software must have only a single responsibility. Nikita's article guides you through the complex process of writing simple code with some hands-on refactoring examples. You'll use callable classes, SRP, dependency injection, and composition to write simple Python code. Nice read!

(`是也乎:`

Python 是个橡皮泥, 嘦愿意, 总是能嗯哼成喜欢的样子...

)


- [如何使用测试 CI 和代码覆盖率设置 Python 项目以取得成功](https://pycoders.com/link/1190/web)
    + JEFF HALE

How to add tests, CI, code coverage, and more. Very detailed writeup.

(`是也乎:`

非常详细...以致难以简单的向团队交付...

    Install Black
    Create .pycache
    Install pytest
    Create Tests
    Sign up for Travis CI and Configure
    Create .travis.yaml
    Test Travis CI
    Add Code Coverage
    Add Coveralls
    Add PyUp

看起来步骤不多...但是,,,,

)


- [用 Python 和 OpenCV 检测真/假面孔](https://pycoders.com/link/1184/web)
    + ADRIAN ROSEBROCK

Learn how to detect liveness with OpenCV, Deep Learning, and Keras. You'll learn how to detect fake faces and perform anti-face spoofing in face recognition systems with OpenCV.

- [用 pyenv 管理多个 Python 版本](https://pycoders.com/link/1187/web)
    + REAL PYTHON

In this step-by-step tutorial, you'll learn how to install multiple Python versions and switch between them with ease, including project-specific virtual environments, even if you don't have sudo access with pyenv.

(`是也乎:`

其实 PyEnv 比 pipenv 灵活就在,
不仅仅是将运行时版本进行了管理, 
而且可以简便的将 Python 版本环境, 工程模块依赖环境, 
在本地自由结合到任意工程目录上.

就是缺少一个一键将当前环境所有依赖模块冻结为压缩文件,
并能简洁的传送到远方主机, 一键完成再安装配置的工具...

毕竟, 总是有些模块是依赖外部 GCC 之类工具现场编译的.

)


- [2005 年以来 Python 包的增长](https://pycoders.com/link/1180/web)
    + PYDIST.COM

"The Python ecosystem has been steadily growing [since 2005]. After the first few years of hyper growth as PyPI gained near-full adoption in the Python community, the number of packages actively developed each year—meaning they had at least one release or new distribution uploaded—has increased 28% to 48% every year."


(`是也乎:`

每年 28%~48% 的增长,
比中国 GDP 高, 但是远远小于 node.js 的.

)


## 讨论
> Discussions


- [Loop 和 "Else" 条款](https://pycoders.com/link/1172/web)
    + PYTHON.ORG

"What is the Pythonic way to handle the situation where if a condition exists the loop should be executed, but if it does not something else should be done?"

- [登录: admin 口令: admin](https://pycoders.com/link/1204/web)
    + TWITTER.COM/REALPYTHON

(`是也乎:`

核武器的...

)


- [Python 之禅 源码完全违反了 Python 之禅](https://pycoders.com/issues/359)
    + REDDIT

"I was clicking around in PyCharm and noticed that the this module in CPython violates basically all of these principles."




## 文章,教程和嗯哼 
> Articles, Tutorials and Talks

- [嫑令丫的可调用](https://pycoders.com/link/1211/web)
    + MOSHE ZADKA

You can make any Python object callable by adding a __call__ method to it. Like operator overloading this seems like a nifty idea at first... but is it really? Moshe's article goes over some use cases and examples to discuss whether making objects callable is a good idea or not.

- [Python Pandas: 使用内/外/左侧/右侧 连接来合并数据帧](https://pycoders.com/link/1178/web)
    + THISPOINTER.COM

How to merge different Dataframes into a single dataframe using Pandas' DataFrame.merge() function. Merging is a big topic, so this part focuses on merging dataframes using common columns as Join Key and joining using Inner Join, Right Join, Left Join and Outer Join.

(`是也乎:`

可以说又是一个比喻用错喻体导致的常见嗯哼...

)


- [用 Python 介绍神经网络](https://pycoders.com/link/1174/web)
    + VICTOR ZHOU

A simple explanation of how neural networks work and how to implement one from scratch in Python. Nice illustrations!

(`是也乎:`

华人? Princeton University 19 级...

![network3](https://victorzhou.com/media/neural-network-post/network3.svg)

还是大堆公式, 以及相似的图谱, 
并没减少理解难度...

)


- [向 Python 导入任何东西](https://pycoders.com/link/1199/web)
    + ALEKSEY BILOGUR • Shared by Aleksey Bilogur

An intro to module loaders and finders so you can "hack" Python's import system for fun and profit.

(`是也乎:`

有毒

)


- [Poetry 和 Packagr 的私有 Python 包管理](https://pycoders.com/link/1188/web)
    + CHRISTOPHER DAVIES


(`是也乎:`

叕一个模块管理机制...可以说当年 老爹 没想明白的事儿, 至今也没人整明白.

)


- [我在一周内学会了 Python 并且只对 Sorta 感到后悔](https://pycoders.com/link/1207/web)
    + MEZEROTM.COM

- [为什么你想要 Python 有显示依赖注入](https://pycoders.com/link/1192/web)
    + GITHUB.COM/DOBIASD

"In other languages, e.g., Java, explicit dependency injection is part of daily business. Python projects however very rarely make use of this technique. I'd like to make a case for why it might be useful to rethink this approach."

- [理解并改进 Conda 的表现](https://pycoders.com/link/1210/web)
    + ANACONDA.COM

Update from the Conda team regarding Conda's speed, what they're working on, and what performance improvements are coming down the pike.

(`是也乎:`

不同 Jupter 全力在分布式 web 界面上支持多种语言,
Conda 找到了自己的发展道路 -> 在本地运行时环境上 给开发者 一致性体验.

)


- [Python 用 Doc2Vec 检测句子相似性](https://pycoders.com/link/1181/web)
    + KANOKI.ORG

Using Python to estimate the similarity of two text documents using the Doc2Vec module.

- [Iterating with Simplicity: Evolving a Django app with Intercooler.js](https://pycoders.com/link/1208/web)
    + ADAM STEPINSKI





## 好物
> Interesting Projects, Tools and Libraries


- [ctyped: 用类型提示为共享库构建 Ctypes 接口](https://pycoders.com/link/1214/web)
    + GITHUB.COM/IDLESIGN • Shared by Juan Rodriguez

- [iodide-project/pyodide: 在浏览器中 WASM 上运行 CPython](https://pycoders.com/link/1186/web)
    + GITHUB.COM/IODIDE-PROJECT

And not just that, it's a full Python scientific stack, compiled to WebAssembly for running in the browser. More info here.

(`是也乎:`

构建失败中...
)

- [Pyckitup: 在WebAssembly上运行的Python游戏引擎](https://pycoders.com/link/1193/web)
    + PICKITUP247.COM



- [PEP 8 Speaks: GitHub Integration for Python Code Style](https://pycoders.com/link/1183/web)
    + PEP8SPEAKS.COM

A GitHub app to automatically review Python code style over Pull Requests. 

(`是也乎:`

绝对是 M$ 有銭任性而追加的嗯哼...

)

- [ArchiveBox: 开源自托管 Web 存档](https://pycoders.com/link/1202/web)
    + GITHUB.COM/PIRATE

(`是也乎:`

依赖: wget, chromium, and youtube-dl
)

- [minik: 无服务器世界的 Web 框架](https://pycoders.com/link/1209/web)
    + GITHUB.COM/EABGLOBAL • Shared by PythonistaCafe

(`是也乎:`

非常 Bottle

)

## 📆🐍 活动/大会
> Events

- [⋅ Python Atlanta](https://pycoders.com/link/1203/web)
    + March 14, 2019 USA
- [⋅ Karlsruhe Python User Group (KaPy)](https://pycoders.com/link/1196/web)
    + March 15, 2019 卡尔斯鲁厄 德国
- [⋅ Django Girls Rivers 2019 Workshop](https://pycoders.com/link/1176/web) 
    + March 15 to March 17, 2019 河上?
- [⋅ PyCon Odessa](https://pycoders.com/link/1216/web)
    + March 17, 2019 敖德萨 乌克兰
- [⋅ PyCon SK 2019](https://pycoders.com/link/1217/web)
    + March 22 to March 25, 2019 布拉迪斯拉发 斯洛伐克


## DAMA
> ❤️ Happy Pythonic!

(`大妈私人无责任播报`)

# 是也乎

- 190313 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190313 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
