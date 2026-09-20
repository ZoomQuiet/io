---
title: "Issue 463"
summary: ""
date: "2021-03-10T11:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> 4000 个徦模块在 PyPI
原文: [PyCoder's Weekly - Issue #463](https://pycoders.com/issues/463)
![pycoder](http://ydlj.zoomquiet.top/ipic/2020-06-03-pycoder-s-weekly.png)

- 210310 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 210310 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成格式转抄.

------

- [Poison Packages: 用户在用 4000 个徦模块访问 Python 社区](https://pycoders.com/link/5890/web)
  - PAUL DUCKLIN
Recently, a PyPI user going by the name “Remind Supply Chain Risks” uploaded nearly 4000 fake modules to the index, many of which were named as common misspellings of popular packages. Learn about the incident in this article, and read all the way to the end for four tips every Python developer should follow.
(`是也乎:`
    Fake News
    Fake Modules
    Fake People
    Fake ...
![PyPI](http://ydlj.zoomquiet.top/ipic/2021-03-10-ScreenShot%202021-03-10%2009.03.59.jpg)
)
- [Atlas: 从 Python 巨石到托管平台的旅程](https://pycoders.com/link/5898/web)
  - NAPHAT SANGUANSIN
  - AND UTSAV SHAH
See how dropbox migrated their internal systems from a monolith architecture to something more service-oriented without disrupting their users while also minimizing the operation cost that typically comes with owning a service.
(`是也乎:`
Dropbox 的奇幻想之旅
![monolith](http://ydlj.zoomquiet.top/ipic/2021-03-10-ScreenShot%202021-03-10%2009.08.08.jpg)
)
- [更快地检测/诊断和解决代码级问题, 从而优化 Python 应用性能](https://pycoders.com/link/5865/web)
  - DATADOG
  - sponsor
Datadog’s Continuous Profiler allows you to find the most resource-consuming parts in your production code all the time, at any scale, with minimal overhead. Improve MTTR, enhance user experience and reduce cloud provider costs with Datadog APM. Start troubleshooting your Python apps today →
(`是也乎:`
良心赞助商.
)
- [Django View 授权: 限制访问](https://pycoders.com/link/5871/web)
  - REAL PYTHON
  - course
Learn how to restrict your web pages to users with different roles through Django view authorization. You’ll learn about HttpRequest.user objects, view decorators that authenticate, and how to notify your users with the Django messages framework.
(`是也乎:`
![Authorization](http://ydlj.zoomquiet.top/ipic/2021-03-10-ScreenShot%202021-03-10%2009.03.18.jpg)
)
- [Django 3.2 令人兴奋的新功能](https://pycoders.com/link/5877/web)
  - HAKI BENITA
Django 3.2 is just around the corner and it’s packed with new features. Django versions are usually not that exciting — and that’s a good thing — but this time many features were added to the ORM.
(`是也乎:`
是的, 没什么特性比增强 ORM 要来的兴奋/实用
)
- [PEP 621 最终](https://pycoders.com/link/5869/web)
  - PYTHON.ORG
In the near future, you’ll be able to store project metadata in pyproject.toml.
(`是也乎:`
从 yaml 开始, 现在 toml 也转正了,
世界终究回到了 ML 的手中...
)
- [Python 3.10.0a6 可用于测试](https://pycoders.com/link/5870/web)
  - PYTHON.ORG
Test it out today and take structural pattern matching for a spin!

-----------------------------------------

## 探讨/吐糟
>
> Discussions

- [意外地二次幂: 当 Python 比 C++ 快之时](https://pycoders.com/link/5866/web)
  - HACKER NEWS
Seemingly trivial choices in programming language design can lead to pretty surprising results. If you like time complexity, check out the research paper behind the discussion.
(`是也乎:`
C# 会不高兴的.
)
- [self 和 reduce() 有趣用法](https://pycoders.com/link/5883/web)
  - REDDIT

-----------------------------------------

## 文章/教程/嗯哼
>
> Articles, Tutorials and Talks

- [用 Python 制作合成器: 振荡器](https://pycoders.com/link/5881/web)
  - ALAN
Learn how to create oscillators using Python as a foundation for creating your own software synthesizers. This article is one of a three-part series. The other articles cover modulators and controllers.
(`是也乎:`
电子管时代的艺术创作,
在晶体管时代, 用代码来模拟
)
- [如何从 DataFrame 中删除列/ 并附带一些额外信息](https://pycoders.com/link/5880/web)
  - MATTHEW WRIGHT
Learn several ways to remove a column from a pandas DataFrame and take a peek at how column deletion works under the hood.
- [用 Python 享用 API 并使用 gRPC 构建微服务](https://pycoders.com/link/5873/web)
  - REAL PYTHON
  - podcast
Have you wanted to get your Python code to consume data from web-based APIs? Maybe you’ve dabbled with the requests package, but you don’t know what steps to take next. This week on the show, David Amos is back, and he’s brought another batch of PyCoder’s Weekly articles and projects.
(`是也乎:`
![podcast](http://ydlj.zoomquiet.top/ipic/2021-03-10-ScreenShot%202021-03-10%2008.58.51.jpg)
)
- [在生命游戏中找到蒙娜丽莎](https://pycoders.com/link/5885/web)
  - ATUL VINAYAK
Could you find an initial state for Conway’s Game of Life that, after a few iterations, displays the Mona Lisa?
(`是也乎:`
![Conway’s](http://ydlj.zoomquiet.top/ipic/2021-03-10-ScreenShot%202021-03-10%2009.13.28.jpg)
其实, 可以演化出任何你想要的图形
)
- [Python lambda 的替代语法?](https://pycoders.com/link/5886/web)
  - JAKE EDGE
Some discussion crept up this week among core developers about adding an arrow operator for simplifying lambda functions. No plans have been made yet for a PEP, but some developers acknowledged some benefits of the idea.
(`是也乎:`
理性上, 形式并不重要, 重要的应该是编译出来的中间代码效率;
可现实中,
形式大过一切.
)
- [在 Monadical 最爱的五个 Django 模块](https://pycoders.com/link/5891/web)
  - KARIM
  - • Shared by Karim
The folks at Monadical love Django, and they’ve put together a list of some of their favorite packages.
- [The Real Python 播客: 已经一年了!](https://pycoders.com/link/5895/web)
  - REAL PYTHON
The Real Python Podcast just reached a major milestone: its fiftieth episode! In this article, you’ll look at some of the awesome guests we’ve had and topics we’ve covered, and you’ll get a preview of the exciting things happening in the future.
(`是也乎:`
![Podcast](http://ydlj.zoomquiet.top/ipic/2021-03-10-ScreenShot%202021-03-10%2008.55.20.jpg)
无论什么事儿,一但沉迷进去很容易坚持下来的
)

-----------------------------------------

## 好物/妙品/
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [dgl: 图上的深度学习](https://pycoders.com/link/5876/web)
  - GITHUB.COM/DMLC
(`是也乎:`
![dgl](http://ydlj.zoomquiet.top/ipic/2021-03-10-ScreenShot%202021-03-10%2008.53.35.jpg)
有认真设计 Logo 的
![Deep](http://ydlj.zoomquiet.top/ipic/2021-03-10-ScreenShot%202021-03-10%2008.53.41.jpg)
大杂烩.
)
- [django-lifecycle: 声明性模型生命周期挂钩/ 是信号的替代方法](https://pycoders.com/link/5874/web)
  - GITHUB.COM/RSINGER86
(`是也乎:`
对 Signals 的超越.
)
- [django-polymorphic: 具有自动向下转换功能的/改进型 Django 模型继承](https://pycoders.com/link/5878/web)
  - GITHUB.COM/DJANGO-POLYMORPHIC
(`是也乎:`
独步天下的 Django ORM 也只能配合 独步天下的专用增强
)
- [jax:  Python + NumPy 程序的可组合转换](https://pycoders.com/link/5897/web)
  - GITHUB.COM/GOOGLE
- [C-is-for-Camera: Python 模拟的 35mm 相机](https://pycoders.com/link/5896/web)
  - GITHUB.COM/EVILDMP
(`是也乎:`
![Canonet G-III QL17](http://ydlj.zoomquiet.top/ipic/2021-03-10-ScreenShot%202021-03-10%2008.51.28.jpg)
真机...
)

-----------------------------------------

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ Real Python Office Hours (Virtual)](https://pycoders.com/link/5872/web)
  - March 10, 2020
(`是也乎:`
即便是线上的, 一样收费.
)
- [⋅ Python Web Conference 2021 (Virtual)](https://pycoders.com/link/5761/web)
  - March 22 – 26, 2021
- [⋅ PyCon Israel 2021 (Virtual)](https://pycoders.com/link/5809/web)
  - May 2 – 3, 2021
(`是也乎:`
以色列, 全球创新热点地区...
)
- [⋅ DjangoCon Europe 2021](https://pycoders.com/link/5680/web)
  - June 2 – 6, 2021
- [⋅ PyCon 2021 (Virtual)](https://pycoders.com/link/5590/web)
  - May 12 – 18, 2021
(`是也乎:`
反正很早都上 油管了, 随时可以 review,
当然, 这个随时, 随时了很多年都没刷光.
)

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

- 首发: [Issue 463 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-463.html)
- 修订: [issue-463.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-463.md)

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
>> NN 4313
![RPP](http://ydlj.zoomquiet.top/ipic/2020-05-13-real-python-logo-square.28474fda9228.png?imageView2/2/w/463)
