Title: Issue 394
Slug: issue-394
Date: 2019-11-13 11:42
Tags: Weekly,Python,pycoders,ZH

> 俺的 Python 开发环境 2020 版

原文: [PyCoder's Weekly - Issue #394](https://pycoders.com/issues/394)

![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 191113 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 191113 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------


- [PSF 寻求开发商以提高 pip 品质](https://pycoders.com/link/2898/web)
    + PYFOUND.BLOGSPOT.COM 
    + • Shared by Brian Rutledge

The Python Software Foundation Packaging Working Group is receiving funding to work on the design, implementation, and rollout of pip's next-generation dependency resolver. Funding has been allocated to secure a senior developer and an intermediate developer, starting in December 2019 or January 2020. RFP open now through November 22.




- [俺的Python开发环境,2020版](https://pycoders.com/link/2901/web)
    + JACOB KAPLAN-MOSS

The co-creator of Django explains his Python environment: "My setup pieces together pyenv, poetry, and pipx. It's probably a tad more complex than is ideal for most Python users, but for the things I need, it's perfect." Related discussion on Hacker News.

(`是也乎:`

来了, 又来了, 每年更新最具有引战体质话题...

pipenv 被弃用非常明智...
)




- [何时在Python中使用列表推导](https://pycoders.com/link/2899/web)
    + REAL PYTHON

Python list comprehensions make it easy to create lists while performing sophisticated filtering, mapping, and conditional logic on their members. In this tutorial, you'll learn when to use a list comprehension in Python and how to create them effectively.

(`是也乎:`

![Comprehension](http://ydlj.zoomquiet.top/ipic/2019-11-13-ScreenShot%202019-11-13%2011.33.25.jpg)

最讨巧也最容易滥用的技巧...

简单说:

    在应该使用时

)



- [Python中的"解析"](https://pycoders.com/link/2889/web)
    + ASTHASR.GITHUB.IO

"Don't be afraid to create new, more specific data types for your specific use cases. It's okay to represent different data, used for different purposes, with different data structures, and makes later generalization easier!"

(`是也乎:`


毕竟 Python 内置的, 而对其它对象的分析, Python 生态中工具也是最多的...

所以, 嫑怕, 放心定制自己舒服的...
)



- [使用 Keras 和深度学习发现自然灾害](https://pycoders.com/link/2880/web)
    + ADRIAN ROSEBROCK

In this tutorial, you will learn how to automatically detect natural disasters (earthquakes, floods, wildfires, cyclones/hurricanes) with up to 95% accuracy using Keras, Computer Vision, and Deep Learning.



- [Python 成为 GitHub 第二受欢迎的语言](https://pycoders.com/link/2905/web)
    + DEVELOPER-TECH.COM

GitHub has published its latest State of the Octoverse report which provides fascinating insights into the development industry.

(`是也乎:`


第一当然是 JAVA 了, 报告中还有其它有趣的结论:

谁是增长最快的语言? 哪个编辑器最受欢迎...

当然, 无论调查如何, 自己舒服的才是最好的.

)


- [简单便携式 Python 解释器的复杂路径](https://pycoders.com/link/2903/web)
    + GLAUBER COSTA

"We needed a Python interpreter that can be shipped everywhere. You won't believe what happened next!"

(`是也乎:`

简单说, 用专用工具来完成...别自己乱来...
)


- [那些最为低估的 Python 软件包](https://pycoders.com/link/2885/web)
    + EYAL TRABELSI

(`是也乎:`

除了 this 模块之外, 在各种领域都散落有官方一直没注意到的神奇模块,
当然, 多数都是和大数据相关的, pandas 插件, 数据清理/探索, 以及性能检测什么的...

值得逐一尝试体验...

)

- [停止使用 utcnow 以及 utcfromtimestamp](https://pycoders.com/link/2890/web)
    + PAUL GANSSLE

(`是也乎:`

简单说 datetime 才是最好的选择.
)


## 讨论
> Discussions



NIL



## 文章,教程和嗯哼 
> Articles, Tutorials and Talks


- [Python Lambda 函数测验](https://pycoders.com/link/2882/web)
    + REAL PYTHON

Python lambdas are little, anonymous functions, subject to a more restrictive but more concise syntax than regular Python functions. Test your understanding on how you can use them better!

(`是也乎:`

真蟒 少见的随堂测试, 大家可以尝试一下看对 Lambda 应用场景理解的是否嗯哼

)


- [Teaching Python 第 31 集: 2024年学校中的 Python](https://pycoders.com/link/2888/web)
    + TEACHINGPYTHON.FM 
    + podcast

"In this episode, Kelly and Sean discuss plausible trends in machine learning, artificial intelligence, augmented and virtual reality, and data science that we may see in schools by 2024. We focus on 5 areas from microscale in the classroom to macro across the entire educational system."

(`是也乎:`

未来的教育中, Python 应该什么样?

AI 将泛滥, 工具将更加丰富, 老师将更加无力, 学生自主行为必然得到越来越大的加强

)


- [如何在 Python 中用 Asyncio 处理协程](https://pycoders.com/link/2881/web)
    + ERIK MARSJA

Learn about coroutines in Python by example. More specifically, you'll see how to handle coroutines using asyncio.

- [用 Python 思考递归](https://pycoders.com/link/2883/web)
    + REAL PYTHON 
    + video

In this course, you'll learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.

(`是也乎:`


![Recursively](http://ydlj.zoomquiet.top/ipic/2019-11-13-ScreenShot%202019-11-13%2011.15.36.jpg)

递归...其实, 至今见过最精巧的 Recursively 都是在 LISP 生态中...


)


- [如何用 Pandas 在 Python 中读取 Stata 文件](https://pycoders.com/link/2897/web)
    + ERIK MARSJA

Learn how to read Stata (.dta) files in Python and how to write a Stata file to CSV and Excel files.

- [用 Flask 和 Vue.js 开发单页应用程序](https://pycoders.com/link/2891/web)
    + MICHAEL HERMAN

A step-by-step walkthrough of how to set up a basic CRUD app with Vue and Flask.

(`是也乎:`

Flask 的热点关联一直很专业

)

- [现代 Web 中的 Tornado 框架](https://pycoders.com/link/2902/web)
    + MANADOMA.COM

Exploring a Tornado use case in low memory environment.

(`是也乎:`

Tornado 严格意义上并不是框架, 而是基础组件,
当然, 也可以独立使用, 所以, 在小内存环境中很得趣...

)


- [在 Python 中管理许多 extras_require 依赖关系的更好实践](https://pycoders.com/link/2900/web)
    + HAN XIAO

(`是也乎:`

叕一个模块依赖管理思路...
只是, 第三方没什么好说的, 一但定型都是固定的,
工程内部自制模块的管理才是困难点吧...


)


- [Python VS Common Lisp, 工作流和生态系统](https://pycoders.com/link/2894/web)
    + LISP-JOURNEY.GITLAB.IO


(`是也乎:`

等等, 这有什么好比较的? 关注方向都相反的吧...

)

- [用 Python 解开 Quantum Supremacy 基准测试](https://pycoders.com/link/2896/web)
    + M. SOHAIB ALAM

- [11 个新 Python Web 框架](https://pycoders.com/link/2908/web)
    + DEEPSOURCE.IO

(`是也乎:`

一半都是5年以上老框架了,,,,而且多数都是专注 RESTful API 生成的, 
并不是通用 web 应用框架

)

- [Laziness 和 Streams](https://pycoders.com/link/2886/web)
    + JEREMIAH MALINA

- [在 GCP 上用 Python 创建 Slack 应用](https://pycoders.com/link/2884/web)
    + WILL LARSON



- [用 stylecloud 生成时尚词云](https://pycoders.com/link/2893/web)
    + ABDUL MAJED




## 好物
> Interesting Projects, Tools and Libraries, Projects & Code

- [SeleniumBase: 用 Python 轻松进行 Web 自动化和测试](https://pycoders.com/link/2906/web)
    + GITHUB.COM/SELENIUMBASE

(`是也乎:`


![SeleniumBase](https://camo.githubusercontent.com/193f6a58d5b263f9977ff69e46bb8e0eb1d891b5/68747470733a2f2f63646e322e68756273706f742e6e65742f68756266732f3130303030362f696d616765732f6d795f66697273745f746573745f6769662e676966)

首先, 还是得起一个完整的 浏览器哪...

)

- [flupy: Python 和您 Shell 间流畅数据管道](https://pycoders.com/link/2887/web)
    + GITHUB.COM/OLIRICE

(`是也乎:`

CLI 果然是最好的界面

)


- [rele: 易于使用的 Google Pub/Sub](https://pycoders.com/link/2904/web)
    + GITHUB.COM/MERCADONA

(`是也乎:`

好是好, 可惜不存在哪..

)


- [pythran: Python -> C++ 转换器](https://pycoders.com/link/2907/web)
    + GITHUB.COM/SERGE-SANS-PAILLE


(`是也乎:`

这真的稳定了, 那 C++ 老司机可就惨了...

)


- [pytest-quarantine: 管理预期的失败测试](https://pycoders.com/link/2895/web)
    + GITHUB.COM/ENERGYSAGE 
    + • Shared by Brian Rutledge

(`是也乎:`

这就叫专注... pytest 的插件,专门管理一定失败的安全带.

    $ pytest --quarantine
    ====== test session starts ======
    ...
    collected 1380 items
    added mark.xfail to 661 of 661 items from quarantine.txt

    ...

    ====== 719 passed, 661 xfailed in 300.51 seconds ======

)


## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Python Atlanta](https://pycoders.com/link/2875/web)
    + November 14, 2019
    + USA

- [⋅ Karlsruhe Python User Group (KaPy)](https://pycoders.com/link/2877/web)
    + November 15, 2019
    + 德国

- [⋅ Chattanooga Python User Group](https://pycoders.com/link/2879/web)
    + November 15, 2019
    + USA

- [⋅ BangPypers](https://pycoders.com/link/2874/web)
    + November 16, 2019
    + 印度

- [⋅ PyLadies Dublin](https://pycoders.com/link/2876/web)
    + November 21, 2019
    + 爱尔兰


## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- **[蟒营 Python 入门班](https://py.101.camp/)**
    + 第4期
    + 101camp4py

第4期已上线, 为期6周;

    191124 报名结束
    191201 正式开课
    200112 按时结束



# 是也乎
> NN 3829

- 首发: [Issue 394 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-394.html)
- 改进: [issue-394.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-394.md)




