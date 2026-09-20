---
title: "蠎加载 127"
summary: ""
date: "2017-06-01T16:42:00"
tags:
  - "Weekly"
  - "ImportPython"
  - "Zh"
---

![importpython-barnner.png](http://zoomq.qiniudn.com/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)

- 原文: [Import Python Weekly Newsletter - Issue No 127](http://importpython.com/newsletter/no/127/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读

~ 文章, Blog, 教程...

- [Python 函式不是你所想咯](https://powerfulpython.com/blog/python-functions-arent-what-you-think/)
  - core-python, functions
Python functions cannot have names. In this world view, every function is a nameless, anonymous object. Code like "def to_percent(numbers)" creates a nameless function object, then stores it in a variable called "to_percent".
(`是也乎:`
不同的世界观中, Py 的函式机制都可以自洽
)
- [Python API 清单](http://python.apichecklist.com/)
  - checklist
Useful checklist for build good Python libraries APIs. Based on "How to make a good library API" PyCon 2017 talk.
(`是也乎:`
PyCon2017 最新主题分享的检查列表,
)
- [Api Star](http://anthonyfox.io/2017/06/api-star/)
  - video
This is a presentation I gave at a local python user group in Nashville, PyNash. The topic of the night was to pick a lesser-known or up and coming library that many folks may not be aware of yet and give a 10 minute overview.
(`是也乎:`
✨ 🚀 ✨
![apistar](http://anthonyfox.io/images/apistar.gif)
真的解决大问题的好思路...
等等: [API STAR by Anthony Fox](http://slides.com/anthonyfox/api-star#/)
这种幻灯平台,简直了...
)
- [实现基于角色的访问控制](https://medium.com/@tasdikrahman/implementing-role-based-access-control-a2bbcb4dfdb0)
  - role
easyrbac has a very simple API to interact around and create Roles and Users
- [Ethereum 周刊 - #offtopic](http://ethereumweekly.com/newsletter/)
  - newsletter
If you are into cryptocurrency check out Ethereumweekly.com started by a friend. It's a weekly newsletter on all things Ethereum, Blockchain. A good way to understand what the buzz on cryptocurrency is all about.
(`是也乎:`
有关网络安全/区块链 的周刊
)
- [用 Python 和 Pandas 对价格进行分析和评级](http://blog.ayoungprogrammer.com/2017/05/using-python-and-pandas-to-analyze-price-targets-and-ratings.html/)
  - pandas
I recently began investing and was wondering how good analysts are at predicting the future of a company.
- [用 Machine Learning 进行文本分类](https://medium.com/click-bait/text-classification-using-machine-learning-cff96602c264)
  - machine learning
In this post, we will be trying to make a text classifier that will make use of the 20 news groups dataset originally developed by Ken Lang to classify documents into different categories based on their content.
- [在 Python 中用起 YAML](http://infinidum.com/post/Using-YAML-in-python)
  - YAML
YAML stands for "YAML Ain't Markup Language" and is mostly used in configuration files. YAML, in contrary to JSON, is made to be very readable and is not designed to be used for api's or other communication protocols. This is because the parsing of a YAML file requires the computer a little bit more effort than parsing a JSON file.
(`是也乎:`
Yaml 虽然比 JSON 可读,但是无论创建和解析都比较嗯哼...
)
- [转换 cURL 指令为 Python requests](https://curl.trillworks.com/)
  - curl
Web app to convert syntax.
(`是也乎:`
德政! 这才是为用户着想,将系统管理员从 shell 中扑救出来..
<-- `Convert curl syntax to Python, Node.js, PHP`
)
- [Riddler Nation 擂台冠军; 基于代理的建模方法 | Curtis Miller's Personal Website](https://ntguardian.wordpress.com/2017/05/29/winning-the-battle-for-riddler-nation-an-agent-based-modelling-approach/)
  - numpy, pandas, quiz, puzzle
Solution to Oliver Roeder puzzle in in FiveThirtyEight called “The Riddler”.
- [在 Python 用 Excel-样 列名来索引](https://wycd.net/posts/2017-05-30-python-excel-columns-to-list-indexes.html)
  - codesnippet
(`是也乎:`
就两行代码:
    def to_idx(letters):
        val = lambda i, x: (26**i) * (ord(x.lower()) - ord('a') + 1)
        return sum([val(i, x) for i, x in enumerate(letters[::-1])]) - 1
效果:
    >>> to_idx('A')
    0
    >>> to_idx('AH')
    33
    >>> to_idx('XFD')
    16383
)
- [用 Bokeh, Flask 和 Python 3 构建响应式 Bar Charts](https://www.fullstackpython.com/blog/responsive-bar-charts-bokeh-flask-python-3.html)
  - chart
Bokeh is a powerful open source Python library that allows developers to generate JavaScript data visualizations for their web applications without writing any JavaScript. While learning a JavaScript-based data visualization library like d3.js can be useful, it's often far easier to knock out a few lines of Python code to get the job done.
(`是也乎:`
Bokeh 是个专用库,
能将 py 数据对象转换为 JS 的.
)
- [揭露 Python 3.6 的私人字典 Version](http://jakevdp.github.io/blog/2017/05/26/exposing-private-dict-version/)
  - core-python, dict
- [PyBites – 如何编写 Python Class](http://pybit.es/python-classes.html)
  - oops
(`是也乎:`
简单的说, 8股化,
简单的说, 要习惯在创建临时脚本时,就要将类化的工作减到最小...
)

## 好物

~ 包/模块/库/片段...

- [pmbootstrap](https://github.com/postmarketOS/pmbootstrap)
  - 312 Stars, 15 Fork
Sophisticated chroot/build/flash tool to develop and install postmarketOS
(`是也乎:`
[postmarketOS: Aiming for a 10 year life-cycle for smartphones ♻](https://ollieparanoid.github.io/post/postmarketOS/)
![postmarketOS](https://ollieparanoid.github.io/img/2017-05-26/i9100/filled-thumb.jpg)
这才是梗...真爱
)
- [gitsuggest](https://github.com/csurfer/gitsuggest)
  - 193 Stars, 6 Fork
A tool to suggest github repositories based on the repositories you have shown interest in.
(`是也乎:`
github 生态又一层: 专用推荐工具
![gitsuggest](https://camo.githubusercontent.com/dd8f2af10e9c35b3badd855d32a1a409b0a3f3e0/687474703a2f2f692e696d6775722e636f6d2f356a35596e4c522e676966)
)
- [python-QuickUI](https://github.com/ac1235/python-QuickUI)
  - 90 Stars, 2 Fork
Scientific One-Liner Interactive GUI Library
(`是也乎:`
    >>> import numpy as np
    >>> from quickui import *
    >>> forall(a = slider(1,10,0.1), b = slider(1,10,0.1)).show(
    ...    plot(lambda a,b: [np.arange(1,10),
    ...    np.sin(np.arange(1,10)**a) + b/a]))
![using_numpy_matplotlib](https://github.com/ac1235/python-QuickUI/raw/master/Gallery/using_numpy_matplotlib.png)
这种界面除了程序猿,无人能忍的...
而且一眼即知, 纯粹的 Tkiner+Matplotlib 的包装而已
更加要命的, 文档没有,,,,
)
- [asgiworker](https://github.com/tomchristie/asgiworker)
  - 10 Stars, 1 Fork
An ASGI Gunicorn worker class.
- [paragraph2vec](https://github.com/thunlp/paragraph2vec)
  - 10 Stars, 2 Fork
Paragraph Vector Implementation
(`是也乎:`
中国学生作品... REAME 写的那叫个残念...
)
- [news-audit](https://github.com/clips/news-audit)
  - 3 Stars, 0 Fork
Fake news detection, Google Summer of Code 2017
(`是也乎:`
学生作品: 徦新闻识别器
)

### (￣▽￣)

- [Public Lecture with Google DeepMind's Demis Hassabis - YouTube](https://www.youtube.com/watch?v=0X-NdPtFKq0)
  - Neural Network
(`是也乎:`
仓库 -> [torch/nn](https://github.com/torch/nn)
Lua 如此简单的语言, 也在深度学习中可以折腾起来...
)
Lua 深入到这么前沿的领域哪....

# 是也乎

- 170601 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 170601 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
