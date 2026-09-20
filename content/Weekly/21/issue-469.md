---
title: "Issue 469"
summary: ""
date: "2021-04-21T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> 200 行 Python 检验基本音乐理论
原文: [PyCoder's Weekly - Issue #469](https://pycoders.com/issues/469)
![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)

- 210421 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210421 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------

- [通过阅读代码进行学习: Python 标准库设计决策解释](https://pycoders.com/link/6145/web)
  - ADRIAN
Along your Python learning journey, someone may have told you that a great way to level up your skills is to read code written by other people. That’s definitely true, but it’s not easy to find good sources of code to read and study. Python offers some advantages here because not only is the code open source, but the discussion surrounding design decisions is public, too.
(`是也乎:`
阅读代码?
其实, 就是用经验在运行代码.
如果经验不足以理解,
那就应该第一时间真实运行起来...
)
- [用 Python 和 Keras 学习文本分类](https://pycoders.com/link/6141/web)
  - REAL PYTHON
  - course
Learn about Python text classification with Keras. Work your way from a bag-of-words model with logistic regression to more advanced methods leading to convolutional neural networks. See why word embeddings are useful and how you can use pretrained word embeddings. Use hyperparameter optimization to squeeze more performance out of your model.
(`是也乎:`
![Keras](http://ydlj.zoomquiet.top/ipic/2021-04-21-ScreenShot%202021-04-21%2008.55.20.jpg)
纱翁总是逃不了的,
只是在中国, 很少有团队拿毛选来作分析数据...
)
- [流利的Django: 应该知道的 8个 Django 模板标签](https://pycoders.com/link/6146/web)
  - GIRL THAT LOVES TO CODE
The Django template language has some powerful features that can simplify your templates and solve a number of problems. Learn about eight template tags that you might not have heard of in this listicle that’s full of practical examples.
(`是也乎:`
从终极 -> 精通 -> 流畅 -> ...
技术界的用词总是一阵阵儿的...
)
- [Python 3.10 将包含改进的错误消息](https://pycoders.com/link/6135/web)
  - TWITTER.COM/PYBLOGSAL
If you mistype an attribute name, you’ll get suggestions from existing attributes!
- [PSF 正在招聘 Python 打包项目经理!](https://pycoders.com/link/6158/web)
  - PYTHON SOFTWARE FOUNDATION
(`是也乎:`
总**包**工头
)
- [Flask 2.0 即将推出/已可进行测试](https://pycoders.com/link/6136/web)
  - REDDIT
- [Google 成为 PSF 的第一个有远见的赞助商](https://pycoders.com/link/6134/web)
  - TWITTER.COM/THEPSF

-----------------------------------------

## 探讨/吐糟
>
> Discussions

- [PEP 563, PEP 649, 和 pytantic 的未来](https://pycoders.com/link/6153/web)
  - GITHUB.COM/SAMUELCOLVIN
Python 3.7 introduced postponed evaluation of type annotations behind the from future import **annotations** switch, a feature originally proposed in PEP 563. Libraries like pydantic, used extensively in the popular FastAPI framework, have found it difficult to support PEP 563, which is set to become the default in Python 3.10. A new PEP aims to alleviate some of the issues, but sentiment is mixed.
(`是也乎:`
无论 Python 怎么升级,
Py2.7.10 总是好用的.
嘦 老爹不死, 总是可以号称 Pythonic 的...
)
- [为毛 Python 返回 \[15\] 当 \[0xfor x in (1, 2, 3)\] ?](https://pycoders.com/link/6144/web)
  - STACK OVERFLOW
If you thought this unusual expression would return an error, you’re not alone. There’s actually a lot of nuance to how this works, and would probably trip up even experienced Python devs. See this tweet from Ned Batchelder for even more discussion.
(`是也乎:`
这类为毛系统质问, JS 世界最多...
)

-----------------------------------------

## 文章/教程/嗯哼
>
> Articles, Tutorials and Talks

- [200 行 Python 代码检验基本音乐理论](https://pycoders.com/link/6138/web)
  - MANOHAR VANGA
Music has always had a close relationship with mathematics and makes heavy use of repeated patterns and formulas. These characteristics make music ripe for investigation with code. This article covers some of the basics of Western music theory with examples in Python. The article is quite accessible — no knowledge of reading sheet music needed! After you’ve read the article, check out the discussion on Hacker News.
(`是也乎:`
有趣...

```python
{'Aeolian': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
 'Dorian': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
 'Ionian': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
 'Locrian': ['C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'],
 'Lydian': ['C', 'D', 'E', 'F#', 'G', 'A', 'B'],
 'Mixolydian': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
 'Phrygian': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb']}
```

用程序自动生成和弦?
)

- [Python vs Java 中 OrderedDict 与 dict 以及面向对象的编程](https://pycoders.com/link/6168/web)
  - REAL PYTHON
  - podcast
Are you looking for a bit of order when working with dictionaries in Python? Are you aware that the Python dict has changed over the last several versions and now keeps items in order? Could you learn more about object-oriented programming in Python by comparing it to another language? Find out more in this week’s installment of the Real Python Podcast.
(`是也乎:`
![56](http://ydlj.zoomquiet.top/ipic/2021-04-21-ScreenShot%202021-04-21%2008.49.03.jpg)
毫无感觉就到56期了,
自怼圈也是,
这周6已经是第210次直播了...
)
- [用 Python 理解和生成 UPC-A 条形码](https://pycoders.com/link/6163/web)
  - YASOOB KHALID
Have you ever wondered how the barcodes you see on products work? Did you know that the first barcodes originated from Morse code? This article teaches you how UPC-A barcodes, one of the current barcode standards, work and how you can create them from scratch using Python.
(`是也乎:`
![Barcode](http://ydlj.zoomquiet.top/ipic/2021-04-21-ScreenShot%202021-04-21%2008.50.24.jpg)
这是一个大家族...
)
- [用 Heroku 部署 Python Flask 应用示例](https://pycoders.com/link/6142/web)
  - REAL PYTHON
In this step-by-step tutorial, you’ll learn how to create a Python Flask example web application and deploy it using Heroku. You’ll also learn how to set up Heroku Pipelines to create a deployment workflow with staging and production environments.
(`是也乎:`
![Heroku](http://ydlj.zoomquiet.top/ipic/2021-04-21-ScreenShot%202021-04-21%2008.46.26.jpg)
Heroku 的确是个令人愉快的游乐场,
但是, 真心不是一个可作生产环境的地方...
)
- [在命令行构建 Python 的目录树生成器](https://pycoders.com/link/6152/web)
  - REAL PYTHON
In this step-by-step project, you’ll create a Python directory tree generator application for your command line. You’ll code the command-line interface with argparse and traverse the file system using pathlib.
(`是也乎:`
![Directory](http://ydlj.zoomquiet.top/ipic/2021-04-21-ScreenShot%202021-04-21%2008.44.24.jpg)
tree 指令的山寨过程...
![CLI](http://ydlj.zoomquiet.top/ipic/2021-04-21-ScreenShot%202021-04-21%2008.45.31.jpg)
)

-----------------------------------------

## 好物/妙品/
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [splitflap: DIY Split-Flap 式显示](https://pycoders.com/link/6157/web)
  - GITHUB.COM/SCOTTBEZ1
(`是也乎:`
![Split-Flap](http://ydlj.zoomquiet.top/ipic/2021-04-21-ScreenShot%202021-04-21%2008.43.13.jpg)
Hard core, 没用任何公板,
从0设计制造.
)
- [TTS: 用于语音合成的深度学习工具包](https://pycoders.com/link/6164/web)
  - GITHUB.COM/COQUI-AI
- [PyCall.jl: 从 Julia 语言调用 Python 函数](https://pycoders.com/link/6133/web)
  - GITHUB.COM/JULIAPY
(`是也乎:`
Julia 想说: **やめて**
)
- [collie_recs: PyTorch 中的深度学习混合推荐系统](https://pycoders.com/link/6137/web)
  - GITHUB.COM/SHOPRUNNER
  - • Shared by Nathan Jones
- [bodywork-core: 将机器学习项目部署到 Kubernetes 的 MLOps 工具](https://pycoders.com/link/6148/web)
  - GITHUB.COM/BODYWORK-ML
(`是也乎:`
K8s 的复杂, 促进了工具市场的嗯哼...
)
- [simplematch: 最小/超级可读的字符串模式匹配](https://pycoders.com/link/6147/web)
  - GITHUB.COM/TFELDMANN
  - • Shared by Thomas Feldmann
(`是也乎:`

```python
import simplematch as sm
def mood_convert(smiley):
    moods = {
        ":)": "good",
        ":(": "bad",
        ":/": "sceptic",
    }
    return moods.get(smiley, "unknown")
sm.register_type("smiley", r":[\)\(\/]", mood_convert)
sm.match("I'm feeling {mood:smiley} *", "I'm feeling :) today!")
>>> {"mood": "good"}
```

怎么也学习不会正则表达式的福音...
)
-----------------------------------------

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/6140/web)
  - March 31, 2020
(`是也乎:`
即便是线上的, 一样收费.
)
-[⋅ GeoPython 2021](https://pycoders.com/link/6119/web)
  - April 22 – 24, 2021
- [⋅ PyCon Israel 2021 (Virtual)](https://pycoders.com/link/5809/web)
  - May 2 – 3, 2021
(`是也乎:`
以色列, 全球创新热点地区...
)
- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5590/web)
  - May 12 – 18, 2021
(`是也乎:`
反正很早都上 油管了, 随时可以 review,
当然, 这个随时, 随时了很多年都没刷光.
)
- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
  - June 2 – 6, 2021
- [⋅ PyCon India 2021](https://pycoders.com/link/6052/web)
  - September 17 – 20, 2021

-----------------------------------------

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- [gruns/icecream: 🍦 Never use print() to debug again.](https://github.com/gruns/icecream)
  - github
(`是也乎:`
独创 logging + debug 模块
)
- [沈崴的个人空间 -  ( ゜- ゜)つロ 乾杯~ Bilibili](https://space.bilibili.com/272001170/)
  - 哔哩哔哩
(`是也乎:`
老司机开新坑, 时隔10年,
沈游侠再次开声, 值得关注:
![Bilibili](httpstp://ydlj.zoomquiet.top/ipic/2021-01-06-ScreenShot%202021-01-06%2010.14.10.jpg)
)
- [如何持证 \(SSL\) 开车 — 蟒营™ 怂怼录](https://blog.101.camp/ts/190130-jump-into-ssl/)
  - UPYUN
(`是也乎:`
私人初体验,
现在 http/https 资源混用浏览器越来越傲娇了,
最好有工具可以统一迁移...
)

-----------------------------------------

# PS

- 首发: [Issue 469 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-469.html)
- 修订: [issue-469.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-469.md)

-------------

好文笔,感叹号年度配额: **2/3**
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
>> NN 4341
![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/469)
