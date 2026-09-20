Title: 蠎周刊(PyCoder)593
Slug: issue-593
Date: 2023-09-06 11:42
Tags: Weekly,Python,pycoders,ZH


> 创建漂亮的极坐标直方图


原文: [PyCoder's Weekly - Issue #593](https://pycoders.com/issues/593)



![pycoder](https://ipic.zoomquiet.top/2021-08-25-pycoder-s-weekly.png)


- 230906 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 13 分钟 完成格式转抄.
- 230906 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 37 分钟 完成快译,

------




- [用 Rich 创建 Python Wordle 克隆](https://pycoders.com/link/11398/web)
    + REAL PYTHON 
    + COURSE

In this step-by-step project, you’ll build your own Wordle clone with Python. Your game will run in the terminal, and you’ll use Rich to ensure your word-guessing app looks good. Learn how to build a command-line application from scratch and then challenge your friends to a wordly competition!

(`是也乎:`

![Rich](https://ipic.zoomquiet.top/2023-09-06-zshot%202023-09-06%2014.33.01.jpg)

Rich 这个框架名字起的真好,...

)



- [用 Python 和 Matplotlib 创建漂亮的极坐标直方图](https://pycoders.com/link/11373/web)
    + OSCAR JOHANSSON

“Polar histograms are great when you have too many values for a standard bar chart. The circular shape where each bar gets thinner towards the middle allows us to cram more information into the same area.” Learn how to create one using Python and Matplotlib.


(`是也乎:`


![极坐标](https://ipic.zoomquiet.top/2023-09-06-zshot%202023-09-06%2014.31.50.jpg)

这种图表...

)


- [Python 协议缓冲区简介](https://pycoders.com/link/11388/web)
    + MIKE DRISCOLL

Protocol buffers are a data serialization format that is language agnostic, analogous to Python’s pickle format. Learn how to write them in Python and communicate with other languages that support the protocol.

- [Django 安全版本：4.2.5、4.1.11 和 3.2.21已发布](https://pycoders.com/link/11399/web)
    + DJANGO SOFTWARE FOUNDATION








-----------------------------------------
## 探讨/吐糟
> Discussions

- [Python 为何获胜？](https://pycoders.com/link/11379/web)
    + HACKER NEWS

(`是也乎:`


也可以反过来想,
如何能让 Python 失败?
再看一路过来, 是最初的心愿重要,还是社区稳定发展重要...

)



- [Python 提案（受Lua启发）](https://pycoders.com/link/11393/web)
    + NED BATCHELDER

(`是也乎:`

```python
args = {'a':1, 0:98, 1:99, 'b':2}
f(**args)

#is the same as:

f(98, 99, a=1, b=2)

```

嗯哼, 这只能说好象有点儿意思哪...

)




-----------------------------------------
## 文章/教程/嗯哼 
> Articles, Tutorials and Talks


- [寻找适合 Python 编程的编码字体](https://pycoders.com/link/11382/web)
    + REAL PYTHON 
    + PODCAST

What should you consider when picking a font for coding in Python? What characters and their respective glyphs should you check before making your decision? This week on the show, we talk with Real Python author and core team member Philipp Acsany about his recent article, Choosing the Best Coding Font for Programming.

(`是也乎:`


![font](https://ipic.zoomquiet.top/2023-09-06-zshot%202023-09-06%2014.25.01.jpg)

根据不同心情吧,
不过, 事实反复证明过了,
关注运行时代码之外任何东西时, 就代表已经心不在程序上了...

)

- [Hidden Features of Python
Python 的隐藏特性](https://pycoders.com/link/11394/web)
    + SCOTT ROBINSON

Python is a powerful programming language that’s easy to learn and fun to play with. But beyond the basics, there are plenty of hidden features and tricks. This article covers debugging regexes, the ellipsis, dir(), chaining comparisons, and more little nuggets you may not know.


(`是也乎:`

每年都有人整理,不过,除非绝对必要, 否则, 还是能不用就嫑用...

)


- [假设检验测试](https://pycoders.com/link/11383/web)
    + HYPOTHESIS.READTHEDOCS.IO

Hypothesis is a property-based testing library. This style of testing uses ranges of scenarios rather than a single value, and then the tool explores the results. See also the intro article to strategy based testing.

- [PSF 被授权为 CVE 编号机构](https://pycoders.com/link/11395/web)
    + PYTHON SOFTWARE FOUNDATION

The Common Vulnerabilities and Exposures program identifies, catalogs, and discloses cybersecurity vulnerabilities. The Python Software Foundation has recently been added as a numbering authority, improving Python’s ability to disclose and respond to security issues.

- [将机器学习模型部署到 AWS Lambda](https://pycoders.com/link/11391/web)
    + JAN GIACOMELLI 
    + • Shared by Jan Giacomelli

This tutorial teaches how to deploy a machine learning (ML) model to AWS Lambda, via Serverless Framework, and execute it using Boto3. It also creates a CI/CD pipeline with GitHub Actions to automate the deployment process and run end-to-end tests.

- [Python 基础知识：Pathlib 和文件系统操作](https://pycoders.com/link/11378/web)
    + REAL PYTHON COURSE

In this video course, you’ll learn how to use the pathlib module to carry out file path operations with Python. These operations include creating, iterating over, searching for, moving, and deleting files and folders.


(`是也乎:`

![基础知识：Pathlib](https://ipic.zoomquiet.top/2023-09-06-zshot%202023-09-06%2014.21.15.jpg)

这可能是真的经典系列了....毕竟在 真蟒 上进行了这么多反复迭代

)


- [禁用直接推送到 GitHub 主分支](https://pycoders.com/link/11374/web)
    + JOHNNY METZ

If your development team uses the main branch for production and pull requests for feature management, you may want to disable the ability to (accidentally) push to main. This article shows you how.


(`是也乎:`


main 分支当成版本发现才有这问题,
如果使用版本分支就不会有这种心态了...

)


- [开始开源的 5 种方法](https://pycoders.com/link/11386/web)
    + STEFANIE MOLIN 
    + • Shared by Stefanie Molin

This article shares ideas for finding and making your first open source contribution, using examples from contributions the author has made to various projects.



(`是也乎:`

可以对于 Hacker 的5种角色,
不过, 对于中国, 只有两种类型: 真开源和徦开源

)


- [Python Functools 模块简介](https://pycoders.com/link/11396/web)
    + FLORIAN DAHLITZ

This article introduces you to the functions in Python’s functools module with real world examples to help show you how and when to use each feature.


(`是也乎:`

functools 的扩展...

)


- [Python 中的堆](https://pycoders.com/link/11376/web)
    + SHIVALI BHADANIYA 
    + • Shared by cody

Learn about both the min heap and max heap data structures using Python.








-----------------------------------------
## 好物/妙品/...
> Interesting Projects, Tools and Libraries, Projects & Code



- [compress: 文本压缩以生成击键扩展](https://pycoders.com/link/11385/web)
    + GITHUB.COM/ESCHLUNTZ

- [communitynotes: D为 Twitter 笔记提供支持的文档和代码](https://pycoders.com/link/11387/web)
    + GITHUB.COM/TWITTER

(`是也乎:`

马一龙逼出来的...

)


- [mljar: 用 ChatGPT 在 Matplotlib 中创建绘图](https://pycoders.com/link/11384/web)
    + GITHUB.COM/MLJAR 
    + • Shared by Piotr

- [ML-Recipes: 机器学习食谱集合](https://pycoders.com/link/11377/web)
    + GITHUB.COM/ROUGIER

- [Google 电子表格的 DictWriter 接口](https://pycoders.com/link/11370/web)
    + JACOB KAPLAN-MOSS




-----------------------------------------
## 📆🐍 活动/大会
> Events, MeetUp 真的是全球线下活动组织中心




- [Cloud Builder: Python Conf](https://pycoders.com/link/11372/web)
    + September 6 to September 7, 2023

- [Weekly Real Python Office Hours Q&A (Virtual)](https://pycoders.com/link/11380/web)
    + September 6, 2023

- [PyCon Estonia 2023](https://pycoders.com/link/11397/web)
    + September 7 to September 9, 2023

- [PyCon Portugal 2023](https://pycoders.com/link/11371/web)
    + September 7 to September 10, 2023

- [PyData Amsterdam 2023](https://pycoders.com/link/11368/web)
    + September 14 to September 17, 2023

- [Kiwi PyCon 2023](https://pycoders.com/link/11389/web)
    + September 15 to September 18, 2023

- [PyCon CZ 2023](https://pycoders.com/link/11392/web)
    + September 15 to September 18, 2023




-----------------------------------------
## 历史上这周


- 2022: [蠎周刊 PyCoder 541](https://weekly.pychina.org/issue/issue-541.html)
- 2021: [蠎周刊 488](https://weekly.pychina.org/issue/issue-488.html)
    + [pythonista-weekly : Pyw 515](https://weekly.pychina.org/python-weekly/pyw-515.html)
- 2020: [蠎周刊 435](https://weekly.pychina.org/issue/issue-435.html)
    + [pythonista-weekly : Pyw 465](https://weekly.pychina.org/python-weekly/pyw-465.html)
- 2019: [蠎周刊 384](https://weekly.pychina.org/issue/issue-384.html)
- 2018: [蠎周刊 333](https://weekly.pychina.org/issue/issue-333.html)
- 2017: [蠎加载 140](https://weekly.pychina.org/importpython/importpython-140.html)
- 2016: [蠎加载 89](https://weekly.pychina.org/importpython/importpython-89.html)
- 2015: [蠎周刊 182](https://weekly.pychina.org/issue/issue-182.html)
    + [蠎加载 48](https://weekly.pychina.org/importpython/importpython-48.html)
- 2014: [Issue 131](https://weekly.pychina.org/issue/issue-131.html)
- 2013: 空缺
- 2012: 空缺


-----------------------------------------
## DAMA
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)



- [大妈的多重宇宙 - YouTube](https://www.youtube.com/@Chaos42DAMA)
    + @Chaos42DAMA
    + 恢复各种嗯哼...
- [Zoom\.Quiet’s Chaos42 \| Substack](https://zoomquiet.substack.com/)
    + 古早:新闻组式写作
    + 欢迎订阅, 包含当前周刊



```
        _~-|∽~_
    \/ /  ← ◷  \ \/
      '_   ♢   _'
      > '-----' |

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```


-----------------------------------------
# PS:

- 首发: [Issue 593 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-593.html)
- 修订: [issue-593.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-593.md)

> Happy Pythoning!
>> Copyright © 2023 PyCoder’s Weekly, All rights reserved.
    
## PPS:
> 不觉中蟒周刊快译已经到了第10+2个年头

开始有小伙伴加入承担 `pythonisa` 周刊的翻译,
从来没提醒过, 可就这么默默坚持下来了...

问为什么:

    [皱眉]每周新闻资讯 怎么能错过 
    看看有什么新东西 
    当有新的发现时：
        what f**k 还能这样玩？ 还有这东西？
        每周开彩蛋[吃瓜]

`无法同意更多`...
很多社区贡献看起来辛苦,
其实受益最多的,
就是主动承担者也.

所以++> [锈周刊 -> Weekly :: China<Rustaceans>](https://weekly.rs.101.so/2023/index.html)

-------------

好文笔,感叹号年度配额: **2/3**

投稿/反馈邮箱:

    askdama@googlegroups.com

(邮件列表地址, 
当成正常邮件发送邮件就好, 不用注册, 不用翻越...)


-------------

ZoomQuiet/**[大妈](https://mp.weixin.qq.com/s/N5TuRRbF593D4Q90XdDA7g)**

就是四处 `是也乎,(￣▽￣)` 的那个[大妈](https://mp.weixin.qq.com/s/N5TuRRbF593D4Q90XdDA7g):



```python
全职嗯哼: 大妈的多重宇宙 - https://www.youtube.com/@Chaos42DAMA
私自嗯哼: ZoomQuiet (订阅号: ZoomQuiet42)
公开社群: 蟒营 (订阅号: Mainium)

as 创始组织者:
    CPyUG (mailling-list: python-cn@googlegroups.com)
    PyChina (订阅号: PyChinaOrg)
    本地社区: 
        GDG珠海 (订阅号: GDG-ZhuHai)
        AIGC珠海 

```

-------------



