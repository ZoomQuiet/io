---
title: "Issue 365"
summary: ""
date: "2019-04-24T09:15:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

原文: [PyCoder's Weekly - Issue #365](https://pycoders.com/issues/365)
![realpython](https://img.realpython.net/3b531c6b64e7b41603a68ad2d1d535fb)
------

- [Requests III: HTTP同时为人类和机器](https://pycoders.com/link/1491/web)  
  - PYTHON-REQUESTS.ORG
Requests is getting a makeover slated for release in 2020: asyncio, HTTP/2, connection pooling, timeouts, Python 3.6+, and more.
- [Python 学习路径](https://pycoders.com/link/1465/web)
  - REAL PYTHON
Step-by-Step Python learning paths and study plans for beginner, intermediate, and advanced Python developers.
(`是也乎:`
![Paths_Watermarked](https://files.realpython.com/media/Real-Python-Learning-Paths_Watermarked.714b04cebe68.jpg)
俺就赞个图, 真正的自学路径, 不可能按照这种来的...
入门, 其实就一瞬间...建立/有意识的知道如何建立任意命题的 MVP 就 KO 80% 问题了.
)
- [在您组织内打包 Python 嗯哼](https://pycoders.com/link/1478/web)
  - STEFAN SCHERFKE
What do you do when your organization uses Python for in-house development and you can't (or don't want to) make everything Open Source? Where do you store and manage your code? How do you distribute your packages? Stefan lays out his approach in this detailed article.
(`是也乎:`
gitlab+conda ?
有趣的经验...
    $ ownconda --help
    Usage: ownconda [OPTIONS] COMMAND [ARGS]...
      Support tools for local development, CI/CD and Conda packaging.
    Options:
      --help  Show this message and exit.
    Commands:
      build                 Build all recipes in RECIPE_ROOT in the correct...
      check-for-updates     Update check for external packages in RECIPE_ROOT.
      ci                    Run a GitLab CI pipeline locally.
      completion            Print Bash or ZSH completion activation script.
      dep-graph             Create a dependency graph from a number of Conda...
      develop               Install PATHS in develop/editable mode.
      gitlab                Run a task on a number of GitLab projects.
      lint                  Run pylint for PATHS.
      make-docs             Run sphinx-build and upload generated html...
      prune-index           Delete old packages from the local Conda index at...
      pylintrc              Print the built-in pylintrc to stdout.
      pypi-recipe           Create or update recipes for PyPI packages.
      sec-check             Run some security checks for PATHS.
      show-updated-recipes  Show updated recipes in RECIPE_ROOT.
      test                  Run tests in PATHS.
      update-recipes        Update Conda recipes in RECIPE_ROOT.
      upload                Upload Conda packages in PKG_DIR.
      validate-recipes      Check if recipes in RECIPE_ROOT are valid.
原来是 ownconda 的广告.
![packaging](https://stefan.sofa-rockers.org/images/packaging-git-flow.png)
)
- [通过 Vettery 找 Python 相关工作](https://pycoders.com/link/1499/web)
  - VETTERY
  - sponsor
Vettery specializes in developer roles and is completely free for job seekers. Interested? Submit your profile, and if accepted, you can receive interview requests directly from top companies seeking Python devs. Get started →
(`是也乎:`
有远程 SOHO 的, 但是, 首先能用英文流畅的交流是个关键门槛.
)
- [Flask vs Django: 选择你的 Python Web 框架](https://pycoders.com/link/1483/web)
  - DAMIAN HITES
What are the main differences between Django and Flask? What are their respective strengths and weaknesses? Read Damian's article to find out.
(`是也乎:`
不涉及复杂功能, 数据库...
俺用 Bottle
)
- [基于 NASA Image Search API 造作个 Python GUI 应用](https://pycoders.com/link/1460/web)
  - MIKE DRISCOLL
Learn how to build a Python GUI app for browsing the NASA image library from scratch using the wxPython toolkit.
(`是也乎:`
wxPython ... 上古神品...在 Qt 开源后, 几乎无人讨论了...
)
- [Python 仅位置参数](https://pycoders.com/link/1468/web)
  - JAKE EDGE
Inside baseball about [PEP 570](https://pycoders.com/link/1493/web).
(`是也乎:`
前几周已经嗯哼过几篇了..
)

## 讨论
>
> Discussions

- [为毛用 Anaconda?](https://pycoders.com/link/1477/web)
  - REDDIT
(`是也乎:`
从俺的体验, conda 解决了一个难点:
大型软件的编译安装问题...
类似 Qt/OpenCV/Pandas/Jupter/...
无论 apt/yum 都已经解决了, 但是, 想和系统环境合理分离,
就非常麻烦, 以往用 Pyenv 然后用 pip 来编译安装,
只能管理 PyPi 发行的, 但是 Qt/CV 并不在 PyPi 中,
所以, conda 其实解决了一个跨平台/语言 第三方关联复杂框架的安装/升级/复用/...环境问题,
但是, 想用起来, 俺现在的组合是:
conda 管理 Python 大版本和大依赖软件,
pipenv 在其下管理依赖模块以及运行时环境的切换;
当然, 如果没有第三方, 非 Python 依赖软件的玕,  pyenv 就足够了.
)
- [适合面试的纹身](https://pycoders.com/link/1462/web)
  - REDDIT
Now that's some dedication!

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [如何在 Python 中嗯哼 PDF](https://pycoders.com/link/1473/web)
  - REAL PYTHON
In this step-by-step tutorial, you'll learn how to work with PDF files in Python. You'll see how to extract metadata from preexisting PDFs . You'll also learn how to merge, split, watermark, and rotate pages in PDFs using Python and PyPDF2.
- [Python 开发者10个最常见错误](https://pycoders.com/link/1485/web)
  - MARTIN CHIKILIAN
A list of harmful patterns & pitfalls you can avoid in your own Python code. This is an older post but it still applies as of 2019. Worth a read!
- [用 Python 发送电子邮件](https://pycoders.com/link/1492/web)
  - REAL PYTHON video
In this course, you'll learn how to send emails using Python. Find out how to send plain-text and HTML messages, add files as attachments, and send personalized emails to multiple people. Later on you'll build a CSV-powered email sending script from scratch.
(`是也乎:`
![Emails](https://files.realpython.com/media/Sending-Emails-With-Python_Watermarked.6fee62c5f3b9.jpg)
发邮件从来不是问题, 问题是对方如何收到....
)
- [Google Coral TPU USB加速器入门](https://pycoders.com/link/1484/web)
  - ADRIAN ROSEBROCK
Learn how to get started with your Google Coral TPU Accelerator on Raspberry Pi and Ubuntu. You'll then learn how to perform classification and object detection using Google Coral's USB Accelerator.
- [公司在 2019 年期望从 Python Devs 中得到什么?](https://pycoders.com/link/1496/web)
  - ANDREW STETSENKO
  - • Shared by Andrew Stetsenko
"We took 300 job specs for Python developers, scraped from StackOverflow, AngelList, LinkedIn, and the websites of some fast-growing tech companies worldwide. From all these descriptions, we extracted the skills which were mentioned most frequently"
- [Raspberry Pi 用于计算机视觉和深度学习](https://pycoders.com/link/1501/web)
  - PYIMAGESEARCH
  - sponsor
You can teach your Raspberry Pi to "see" using Computer Vision, Deep Learning, and OpenCV. Let Adrian Rosebrock show you how →
- [Python,R 和 Scala 顶级数据科学库的比较](https://pycoders.com/link/1494/web)
  - CORIERS.COM
This is an infographic comparing commit frequency and other metrics for the most popular data science libraries in Python, R, and Scala.
(`是也乎:`
无论任何一个方面, Py 都不是最强的,
但是,易学好用, PK 掉其它所有.
)
- [时间模块指南](https://pycoders.com/link/1490/web)
  - REAL PYTHON
Learn how to use Python's time module to represent dates and times in your application, manage code execution, and measure performance.
- [Python 中创建热图](https://pycoders.com/link/1479/web)
  - GEODOSE.COM
- [使用插件扩展 Mypy](https://pycoders.com/link/1463/web)
  - MYPY-LANG.BLOGSPOT.COM
  - • Shared by Ricky White

## 好物
>
> Interesting Projects, Tools and Libraries

- [puppeteer: An Opinionated Way to Manage Ansible Projects](https://pycoders.com/link/1487/web)
  - GITHUB.COM/HAANI-NIYAZ
- [datatest: 用于TDD 的数据工具 Data-Wrangling and Data Validation](https://pycoders.com/link/1476/web)
  - GITHUB.COM/SHAWNBROWN • Shared by Shawn Brown
(`是也乎:`
嗯哼? 专注时间相关代码的TDD?
)
- [markplates: Templated Line-Based File Inclusions in Markdown Texts](https://pycoders.com/link/1466/web)
  - GITHUB.COM/JIMA80525
- [totext.py: 将 URL 或 RSS Feed 转换为纯文本](https://pycoders.com/link/1489/web)
  - RAYMII.ORG
(`是也乎:`
Pocket 们专有技能哪...
就看对中国式网页的解析能力了.
真的可用, 结合其它工具, 就是自制 稍后阅读工具了.
)
- [PySnooper: 永远不要再使用打印进行调试](https://pycoders.com/link/1470/web)
  - GITHUB.COM/COOL-RR
(`是也乎:`
愿望是好的,
但是, 相比 logging 可以全局控制输出级别,
以及 pdb 真正的彻入,
勺子的形式和挖出来的运行时信息并不足以简单替代 print()
)
- [dephell: Python 项目管理 (Packages, Venvs, and More)](https://pycoders.com/link/1486/web)
  - GITHUB.COM/DEPHELL
(`是也乎:`
叕一个运行时环境管理工具

> ...DepHell tested on Linux and Mac OS X with Python 3.5, 3.6, 3.7. And one of the coolest things that DepHell ran by DepHell on Travis CI.
嗯哼, 非常喜闻乐见了...
)

- [flipper-client: 简单但功能强大的功能标记工具](https://pycoders.com/link/1474/web)
  - GITHUB.COM/CARTA
- [inline_python: 在 Rust 代码中嵌入 Python 代码](https://pycoders.com/link/1498/web)
  - DOCS.RS
(`是也乎:`
嗯哼?
将 py 嵌入到 rust 中,
执行结果, rust 直取?
这种功能是为了吸引 Pythonista 进入 rust?
)

## 📆🐍 活动/大会
>
> Events

- [⋅ SciPy Japan 2019](https://pycoders.com/link/1469/web)
  - April 23 to April 25, 2019
- [⋅ Python Sudeste 2019](https://pycoders.com/link/1475/web)
  - April 26 to April 29, 2019
- [⋅ PythOnRio Meetup](https://pycoders.com/link/1464/web)
  - 里约热内卢
  - April 27, 2019
- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/1481/web)
  - 印度 April 27, 2019
- [⋅ Dominican Republic Python User Group](https://pycoders.com/link/1497/web)
  - 多米尼加共和国
  - April 30, 2019
- [⋅ PyCon US 2019](https://pycoders.com/link/1480/web)
  - May 1 to May 10, 2019
- [⋅ PyDays Vienna](https://pycoders.com/link/1472/web)  
  - 越南 May 3 to May 5, 2019

## DAMA
>
> ❤️ Happy Pythonic!
(`大妈私人无责任播报`)

- [蟒营 Python 入门班](https://py.101.camp/)
  - 已开班, 进入 ch02
  - 下期可能 7月中

### Jobs
>
> ...
>
# 是也乎

- 190424 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 190424 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.
