---
title: "蠎加载 172"
summary: ""
date: "2018-05-07T11:42:00"
tags:
  - "Weekly"
  - "ImportPython"
  - "Zh"
---

![importpython-barnner.png](http://0.zoomquiet.top/ZQCollection/snap/importpython-barnner.png?imageView2/2/h/210)

- 原文: [Import Python Weekly Newsletter - Issue No 172](http://importpython.com/newsletter/no/172/)
- 欢迎, **来 [PyChina/weekly](https://github.com/PyChina/weekly) 共同翻译/增订/推荐 周刊 蠎消息 ;-)**

## 该读

~ 文章, Blog, 教程...

- [TensorFlow Dev Summit 2018](https://www.youtube.com/watch?v=kSa3UObNS6o)
  - TensorFlow, google
Join the TensorFlow team as they kick off the 2018 TensorFlow Dev Summit! The TensorFlow Dev Summit brings together a diverse mix of machine learning users from around the world for a full day of highly technical talks, demos, and conversations with the TensorFlow team and community.
- [如何使用 Python 中 textblob 分类器自动分配 Jira Issue?](https://medium.com/@hseyinapan/how-to-assign-jira-issues-automatically-using-textblob-classifier-in-python-1a36beec01f7)
  - text classification
I’ve used Python’s textblob classifier to simply classify issues according to assignees from their description and headers. Classified issues used to classify newly created issues and results are recorded to a database. 2019 issues used as training set and %82 assignment accuracy have been achieved. As the training set grows bigger accuracy could be better.
(`是也乎:`
嗯哼,目测只有在客服 Issue 方向有用...
)
- [基本 Python 面试题和答案](https://simpliv.wordpress.com/2018/05/02/basic-python-interview-questions-and-answers/)
  - interview questions
(`是也乎:`
叕一辑 FAQ.py, 应聘专用
)
- [Python 开发者画像: 用什么 作什么](https://www.infoworld.com/article/3269582/python/python-developers-profiled-what-you-use-what-you-do.html#tk.rss_all)
  - survey
A survey of 9,500 developers shows what Python programmers use and what they work on. See how typical you are as a Python developer
(`是也乎:`
![developers](https://images.idgesg.net/images/article/2018/05/python-profile_version-you-use-100756599-large.jpg)
等等吧, 所以,  Py2 即便官方不维护, 也不影响其广泛的使用...
)
- [最佳免费 Python 可视化包](http://lxer.com/module/newswire/ext_link.php?rid=255424)
  - visualization
Nice curated list.
(`是也乎:`
可视化的方向一定是专业化,
通用的, 考虑到输出, 推荐 [Bokeh](https://www.linuxlinks.com/bokeh-python-interactive-visualization-library/);
考虑日常推荐: [pandas](https://www.linuxlinks.com/pandas-python-data-analysis-library/) 呃, 其实用的就是: [matplotlib](https://www.linuxlinks.com/matplotlib/)
)
- [在 Python 中回归一个比例](https://danvatterott.com/blog/2018/05/03/regression-of-a-proportion-in-python/)
  - statistics
I frequently predict proportions (e.g., proportion of year during which a customer is active). This is a regression task because the dependent variables is a float, but the dependent variable is bound between the 0 and 1. Googling around, I had a hard time finding the a good way to model this situation, so I’ve written here what I think is the most straight forward solution.
(`是也乎:`
数据归一化的常见招术式:
    from sklearn.datasets import make_regression
)
- [用 Python 对非数字数据进行聚类](https://visualstudiomagazine.com/articles/2018/04/01/clustering-non-numeric-data.aspx)
  - numeric_data
Clustering data is the process of grouping items so that items in a group (cluster) are similar and items in different groups are dissimilar. After data has been clustered, the results can be analyzed to see if any useful patterns emerge. For example, clustered sales data could reveal which items are often purchased together (famously, beer and diapers).
- [主题建模评估: 主题一致性](https://datascienceplus.com/evaluation-of-topic-modeling-topic-coherence/)
  - topic modeling
In this article, we will go through the evaluation of Topic Modelling by introducing the concept of Topic coherence, as topic models give no guaranty on the interpretability of their output. Topic modeling provides us with methods to organize, understand and summarize large collections of textual information. There are many techniques that are used to obtain topic models. Latent Dirichlet Allocation (LDA) is a widely used topic modeling technique to extract topic from the textual data.
- [Announcing PyTorch 1.0 for both research and production](https://code.facebook.com/posts/172423326753505/announcing-pytorch-1-0-for-both-research-and-production/)
  - pytorch
PyTorch 1.0 takes the modular, production-oriented capabilities from Caffe2 and ONNX and combines them with PyTorch's existing flexible, research-focused design to provide a fast, seamless path from research prototyping to production deployment for a broad range of AI projects.
(`是也乎:`
江湖传说:to be politically correct at Google
    import torch as tf
)
- [用 Python 基于 Google 位置记录分析通勤情况 | nvbn blog](https://nvbn.github.io/2018/05/01/commute/)
  - visualization, location, commute
Since I moved to Amsterdam I’m biking to work almost every morning. And as Google is always tracking the location of my phone, I thought that it might be interesting to do something with that data.
(`是也乎:`
![Google Location](https://nvbn.github.io/assets/commute/3d.png)
反正都被追踪了, 那么除了 google 自动分析
我们自己也应该可以...
)
- [PostgreSQL: 跨函数调用共享数据](https://www.cybertec-postgresql.com/en/postgresql-sharing-data-across-function-calls/)
  - postgres
Recently I did some PostgreSQL consulting in the Berlin area (Germany) when I stumbled over an interesting request: How can data be shared across function calls in PostgreSQL? I recalled some one of the other features of PostgreSQL (15+ years old or so) to solve the issue. Here is how it works.
(`是也乎:`
OpenResty 从一开始就内置了一个对象数据库来解决跨请求的数据共享/操作...
)
- [正态性测试](https://medium.com/@rrfd/testing-for-normality-applications-with-python-6bf06ed646a9)
  - testing, data science
So you have a dataset and you’re about to run some test on it but first, you need to check for normality. Think about this question, “Given my data … if there is a deviation from normality, will there be a material impact my results?”
(`是也乎:`
被测试数据对象集本身的正常状态检测
)
- [从 subscene.com 批量下载字幕 – Scribbleghost](https://medium.com/scribbleghost/batch-download-subtitles-from-subscene-com-2dac050c661a)
  - project
Ever just wanted to download a bunch of subtitles to check which one fits the video? Subscene got everything, but it can be tedious to download subtitles one by one.
- [前沿效益: 用 scipy 优化投资组合分配](https://medium.com/@kyle.jinhai.li/efficient-frontier-optimize-portfolio-with-scipy-57456428323e)
  - scipy
Given 4 assets’ risk and return as following, what could be the risk-return for any portfolio built with the assets. One may think that all possible values should fall inside the area. But it is possible to go beyond the bond, because combining inversely correlated assets can construct a portfolio with lower risk.
- [Python/networkx 图形魔术](https://medium.com/@oliviercruchant/python-networkx-graph-magic-260309cce484)
  - networkx
Basic graph representation function on top of networkx graph library.
(`是也乎:`
networkx 是对 Graphviz 的 Pythonic 封装,
基于 dot 等工具的稳定, 可以尽情折腾...
)
- [使用 Python 和 Apache Spark 的阅读计划建议](https://blog.opendigerati.com/reading-plan-recommendations-using-python-and-apache-spark-e1d20c560a69)
  - spark, recommendation
My goal in this post is simply to share how we at YouVersion are leveraging machine learning tools to generate product recommendations.

## 好物

~ 包/模块/库/片段...

- [mass_archive](https://github.com/motherboardgithub/mass_archive)
  - 68 Stars, 11 Fork
A basic tool for pushing a web page to multiple archiving services at once.
(`是也乎:`
叕一个多重备份工具,
当然并不支持国内的各种云空间的...
)
- [sublime_black](https://github.com/csurfer/sublime_black)
  - 39 Stars, 0 Fork
Sublime Text package to format python code using black formatter.
(`是也乎:`
gfm 之后, 各种语言都开始了自己代码自动化格式化的尝试...
不过, 哈...
)
- [pinboard-backup](https://github.com/QuinnyPig/pinboard-backup)
  - 5 Stars, 0 Fork
This backs up Pinboard bookmarks to DynamoDB.
(`是也乎:`
叕一则 AWS 生态夯实工具...
)
- [pipenv-pipes](https://github.com/gtalarico/pipenv-pipes)
  - 5 Stars, 1 Fork
Pipes - PipEnv Environment Switcher
(`是也乎:`
等等, 这名字越来越象 硅谷剧集那家公司的名称了....
![pipes](https://raw.githubusercontent.com/gtalarico/pipenv-pipes/master/docs/static/pipes-gif.gif)
嗯哼, 其实更加复杂了...
)
- [cognises](https://github.com/plotlabs/cognises)
  - 4 Stars, 1 Fork
Flask Cognises: AWS Cognito group based authentication with user management
(`是也乎:`
AWS 叕一则专用嗯哼配置工具
)
- [gsync](https://github.com/moskomule/gsync)
  - 3 Stars, 0 Fork
Simple PyDrive wrapper and command line tool.
(`是也乎:`
首先当然是 CLI 封装为要, 否则, 自动化难以嵌入...

> 有总比没有的好
作者通透哪...
)

- [Chinese_models_for_SpaCy](https://github.com/howl-anderson/Chinese_models_for_SpaCy)
  - 3 Stars, 0 Fork
Models for SpaCy that support Chinese
(`是也乎:`
专门用来支持 中文 的嗯哼...
)
- [pyjson5](https://github.com/Kijewski/pyjson5)
  - 3 Stars, 0 Fork
A JSON5 serializer and parser library for Python 3 written in Cython.
(`是也乎:`
叕一发 JSON5 的嗯哼, 问题是 JSON 实在太容易崩了哪...
)
- [Palette_Bot](https://github.com/JoshuaScript/Palette_Bot)
  - 3 Stars, 0 Fork
A Reddit bot that generates a color palette for images it is called upon
(`是也乎:`
叕一发 reddit bot 专注进行图片颜色提取,
比如说:
![Palette_Bot](https://camo.githubusercontent.com/1fb3079dbd9e75817346d99cdd2ad5d4197f3258/68747470733a2f2f692e726564642e69742f32356c69713666626a357a7a2e6a7067)
获得:
![Palette_Bot](https://camo.githubusercontent.com/7e6c27ffb4569bd4b67a67dbaecb1009ab6dd45d/68747470733a2f2f692e696d6775722e636f6d2f6731766c766e502e6a7067)
)
- [countryinfo](https://github.com/porimol/countryinfo)
  - 3 Stars, 3 Fork
A python module for returning data about countries, ISO info and states/provinces within them.
(`是也乎:`
将国家信息整合到一个模块中以便随时可以舒服的获得....
)
- [desktop-entry-creator](https://github.com/faheel/desktop-entry-creator)
  - 2 Stars, 1 Fork
A user-friendly GUI for creating desktop entries for installed applications on Linux
(`是也乎:`
![desktop-entry-creator](https://raw.githubusercontent.com/faheel/desktop-entry-creator/master/screenshot.png)
Linux 桌面快捷方式的话....
的确, 比较嗯哼, 但是, 多数也都是指向一个 CLI 工具呢
)

### (￣▽￣)

- [TopSim: 在 Py3 中针对查询有效地搜索最相似的字符串.](https://github.com/chuanconggao/TopSim)
  - 0 Stars, 0 Fork
Search the most similar strings against the query in Python 3. State-of-the-art algorithm and data structure are adopted for best efficiency. For both flexibility and efficiency, only set-based similarities are supported right now, including Jaccard and Tversky.
(`是也乎:`

> 叕一个 Py 实现的搜索模块...当然, 对中文是否支持就不一定了
18.5.1 via: Chuancong Gao • 8 hours ago
> 您好，我是TopSim的作者。感谢您介绍我的Python包。TopSim从设计时就是语言无关的，所以完全支持中文。最新的更新更是优化了体验。谢谢支持。🙏
Full support of Chinese/Japanese/Korean.
$ cat test
    地三鲜
    红烧肉
    烤全牛
    木须肉
    土豆炖牛肉
$ cat test | topsim-cli "牛肉" -k 3 -s tversky
    土豆炖牛肉   0.666
    红烧肉 0.3332
    木须肉 0.3332
`(￣▽￣)` 没毛病, 可以大力使用之 ;-)
)

- [Pandas documentation sprint](https://python-sprints.github.io/pandas/#location)
  - 新年, events
  - [Pandas 文档冲刺\(Doc\. SPRINT\)珠海GDG DevFest2018 系列活动 \| Zhuhai GDG \(Zhuhai, China\) \| Meetup](https://www.meetup.com/Zhuhai-GDG/events/248466729/?success=email_sent) 完成...
*[30 Amazing Python Projects for the Past Year \(v\.2018\)](https://medium.mybridge.co/30-amazing-python-projects-for-the-past-year-v-2018-9c310b04cdb3)* 其中有几个国货,也都超过 1000+星了...
<- [Qix-/better-exceptions: Pretty and useful exceptions in Python, automatically.](https://github.com/Qix-/better-exceptions) 效果惊艳...

## 是也乎

- 180507 [Zoom.Quiet](http://zoomquiet.io) 42 分钟完成快译
- 180507 [Zoom.Quiet](http://zoomquiet.io) 用时 7 分钟完成格式化.
