---
title: "Issue 396"
summary: ""
date: "2019-11-27T14:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> Guido: 代码的可读性如此重要...
原文: [PyCoder's Weekly - Issue #396](https://pycoders.com/issues/396)
![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 191127 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 191127 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------

- [PyCon 2020 注册已上线](https://pycoders.com/link/2970/web)
  - PYCON.ORG
PyCon is the largest annual gathering for the community that uses and develops the open-source Python programming language. April 15–23 in Pittsburgh. Pro-tip: Get your early bird tickets today.
(`是也乎:`
PyCon2020 早鸟票已经有了,,,
)
- [Python KeyError 异常以及如何处理它们](https://pycoders.com/link/2975/web)
  - REAL PYTHON
  - video
KeyError exceptions are often caused by a bad key lookup in a dictionary, but there are a few other situations when a KeyError can be raised as well. Knowing how to handle these exceptions is essential to writing good Python code.
(`是也乎:`
![KeyError](http://ydlj.zoomquiet.top/ipic/2019-11-27-ScreenShot%202019-11-27%2012.39.10.jpg)
等等, 这个是常见, 但是, 不难追踪哪...
)
- [实用 Unicode (2012)](https://pycoders.com/link/2969/web)
  - NED BATCHELDER
Timeless tutorial that teaches the basics of Unicode, and how both Python 2 and Python 3 work, as well as some key tips on solving Unicode problems.
- [Guido van Rossum 论 Python 如何令思维的代码表述更轻松](https://pycoders.com/link/2964/web)
  - DROPBOX.COM
A conversation with the creator of the world's most popular programming language on removing brain friction for better work.
(`是也乎:`
![Guido](http://ydlj.zoomquiet.top/ipic/2019-11-27-ScreenShot%202019-11-27%2012.41.40.jpg?imageView2/2/w/420)

>> 全文如下:
The Mind at Work: Guido van Rossum on how Python makes thinking in code easier
By Anthony Wing Kosner
Published on November 25, 2019
A conversation with the creator of the world's most popular programming language on removing brain friction for better work.
Nothing defines the 21st century more than the ubiquitous effects of computer programming. Almost everything we do, particularly at work, is mediated by screens displaying the results of the enormous amount of computation that we now take for granted. If you're one of the 99.7% of the human race that are not programmers, how all of this happens is a bit of a mystery. As science fiction writer Arthur C. Clarke quotably wrote, "Any sufficiently advanced technology is indistinguishable from magic."
Of course, it isn't magic. It is, however, both complicated and complex, with codebases of tech companies measured in millions of lines of code. When you're reasoning about a real system you might want to build in code, you're thinking about the complex relationships between different functions over time. Your code can be more or less complicated in how it is written and structured, but the problem you're trying to solve has an inherent complexity that can't be reduced to something simpler.
Becoming a programmer is not just about ideas, and you won't last long at it if you can't deal with the laser-focused details of describing your ideas in code. "I'm a little skeptical of the claim that the systems thinking is primary there, because it's much easier to come up with an idea for a system than it is to take an idea and turn it into working code," says Guido van Rossum, the creator and retired BDFL (Benevolent Dictator for Life) of the Python programming language. JavaScript still owns the web, and Java runs 2.5 billion Android phones, but for general purpose programming and education, Python has become the default standard.
If anyone has made turning an idea into working code easier, for more people, it's Van Rossum over his 30-year history with Python. And he's done it with a self-effacing grace and an understated humor—the language is named after the surreal comedy of Monty Python, not the actual Burmese python. In its quiet way, the Python programming language has managed to make some of the complications of programming computers less difficult for our brains to manage.
To understand how Van Rossum accomplished this amazing feat, we have to go back into the history of computing to the era of mainframes and machine language. "The mainframe is a machine that costs many millions of dollars, and the combined pay of all those programmers is peanuts compared to the cost of the mainframe," he says, explaining that cost logically prioritized machine time over human time. "But as I experienced desktop workstations and PCs, I realized that a change of mindset about cost of the programmer's time versus cost of the computer's time was overdue." Van Rossum doesn't think he was the first person to observe this shift, but he really capitalized on it in the design of Python.
This simple idea of giving humans priority over machines is at the core of the philosophy behind Python. Certainly the fact that it's an interpreted language as opposed to a compiled language means that the programmer gets immediate feedback about the code they're writing without needing to take the time to recompile it after making each change. This is very common now, but thirty years ago it was quite controversial because the conventional wisdom was that faster (for the computer) was better. Updating this belief has had a large positive impact on the productivity of programmers.
"In Python, every symbol you type is essential."
—Guido van Rossum
"There are a whole bunch of common programming tasks that are easy in Python," says Van Rossum. "For someone who is not yet a programmer, who wants to become a programmer, for those people Python is particularly easy to get." Indeed, many computer science schools are switching over from Java to Python, because it's much easier to grasp for beginners. The reasons behind this are complex, with many factors each reducing little bits of friction. What's simple is the philosophy behind all of the improvements: Everything should have a necessary purpose. The lack of extraneous code makes it easier to focus on what you need to pay attention to. "In Python, every symbol you type is essential," Van Rossum says.
This concision makes it easy to accomplish something meaningful in Python, which is one of the reasons for its wide adoption. "The typical way that we introduce Python to beginning programmers is also important. We can show them very small snippets of code that require very little understanding of terminology and concepts from programming before they make sense," Van Rossum explains, "whereas the smallest Java program, for example, contains a whole bunch of what are, to the uninitiated eye, noise characters."
This quietness and simplicity of design makes it easier to see what's going on. "Python for me is incredibly visual," says Van Rossum. "When I read Python, I definitely see it as a two-dimensional structure, rather than one-dimensional, like language. That is probably because Python uses indentation for grouping, but probably also because my mind just likes thinking visually."
He's not the only one, of course, who thinks visually. We all do to some extent. But he's particularly sensitive to the effects of the visual on cognition. "Some poorly formatted text can drive me crazy. They interrupt my visual parsing of the flow and the structure, and in that sense, I do think in Python," Van Rossum admits. "I can grasp code much better when it's formatted properly." It takes more information to resolve the uncertainty about what code indentations mean if they're arbitrary than if those indentations have a clear purpose, as they do in Python. So if the experience is easier, it's because fewer bits of information have to be processed for you to know what's going on.
Python's readability is not just typographic, but conceptual. Van Rossum thinks Python may be closer to our visual understanding of the structures that we are representing in code than other languages because, "Python makes that structure mandatory."
"While I was researching my book, CODERS," says author Clive Thompson, "I talked to a lot of developers who absolutely love Python. Nearly all said something like 'Python is beautiful.' They loved its readability—they found that it was far easier to glance at Python code and see its intent. Shorn of curly brackets, indented in elegant visual shelves, anything written in Python really looks like modern poetry." They also find that Python is fun to write, which is more important than it may seem. As Thompson writes, "When you meet a coder, you're meeting someone whose core daily experience is of unending failure and grinding frustration."
"You primarily write your code to communicate with other coders, and, to a lesser extent, to impose your will on the computer."
—Guido van Rossum
Building the priority of the programmer's time into the language has had a curious effect on the community that's grown around it. There's a social philosophy that flows out of Python in terms of the programmer's responsibility to write programs for other people. There's an implicit suggestion, very much supported by Van Rossum in the ways he talks and writes about Python, to take a little more time in order to make your code more interpretable to someone else in the future. Expressing your respect for others and their time through the quality of your work is an ethos that Van Rossum has stealthily propagated in the world. "You primarily write your code to communicate with other coders, and, to a lesser extent, to impose your will on the computer," he says.
The universality of the culture that's spread around Python has achieved some measure of what Van Rossum intended two decades ago with a short-lived project called CP4E (Computer Programming for Everybody). "I'm usually not a very visionary thinker. People always ask me, what's next for Python, and I never know. But I put on my most visionary hat, and assumed that it would make sense for everyone to learn programming." Personal computers had been around for 20 years, but mostly they were glorified typewriters and calculators. Van Rossum asked, "isn't it crazy that all those people have computers, and very few of them learn to program?"
In the time since, he has focused on making programming easier to learn and easier to do through the advancements in Python, now at version 3.7. He still thinks that programming teaches generally valuable skills, like problem solving, following directions carefully, and understanding what directions mean. But he's also found that, "there are certain introductions to programming that are fun for kids to do, but they're not fun for all kids, and I don't think I would want to make it a mandatory part of the curriculum."
At the same time, the need for people to program their computers has also diminished because of the growth of software, particularly on the web, that allows you to intuitively do what used to require programing to accomplish. "I'm not so sure that it needs to happen anymore," Van Rossum says of CP4E. "I think computers have made it to that point, where they're just a useful thing that not everybody needs to know what goes on inside."
"Python is now also the language of amateurs, and I mean that in the best possible way."
—Guido van Rossum
But that are a growing number of people who are using Python in many fields. "The currently prevailing theory about Python's unexpected success," says Van Rossum, "is that at some point, it established itself into data science and machine learning, and scientific data processing in general, and once you have critical mass, it's easier for everyone to use the same system as their colleagues and their competitors, than to try something different." And even though it started as purely a tool for professional programmers, Van Rossum says, "Python is now also the language of amateurs, and I mean that in the best possible way."
A successful open source software project, like Python, has to be easy to learn for beginners, but also have practical application to real world problems that more advanced users will want to solve. Just as for beginners you want to keep things simple so all of their brain energy is spent on learning the complications of the programming environment, for advanced users you want to help them manage the complexity of these competing abstractions. Part of the motivation for making the implementation of Python as simple as possible is to be able to change your mind, to learn, to iterate. "If you write a prototype in Python and you get it to work, often, that's not a very big effort," says Van Rossum, "and then you can afford to throw away your prototype and write the same thing again based on what you've learned. You can still write it in Python, but the second version will be much better than the first."
Part of the enduring appeal of Python is the optimism and humility of starting over. "If you've invested much more time into writing and debugging code, you're much less eager to throw it all away and start over." Co-founder and CEO, Drew Houston wrote the first prototype of Dropbox in Python on a five-hour bus ride from Boston to New York. "The early prototypes of Dropbox were thrown away, largely, many times," says Van Rossum.
What can we learn from Python about how to design better tools for thinking? Tim Peters, one of Python's major contributors, offers some clues in the aphoristic The Zen of Python, in which he channels Van Rossum's guiding principles. Particularly relevant to our present discussion are this pair: "Simple is better than complex. Complex is better than complicated." This could almost be a recipe for how the brain prioritizes its functions to use energy efficiently.
Equally important for Van Rossum is the social aspect of thinking and building tools. What has he taken away from his thirty year journey with Python? "I have learned that you can't do it alone, which is not an easy lesson for me. I've learned that you don't always get the outcome that you went for, but maybe the outcome you get is just as good, or better."
>> 简单说:
`Python 之禅` 真的包含了老爹所有关键思考成果.
)

- [Python 3.9a1 新特性](https://pycoders.com/link/2986/web)
  - PYTHON.ORG
The first draft changelog for Python 3.9 alpha 1 is out, if you want to stay on top of the latest CPython developments.
- [Python 中异常引发改进](https://pycoders.com/link/2965/web)
  - MOSHE ZADKA
How to include contextual information in your exceptions for easier root cause analysis.
(`是也乎:`
讲真, 内置的已经足够好了...
)
- [Django 迁移测试](https://pycoders.com/link/2982/web)
  - NIKITA SOBOLEV
A web app outage post-mortem with useful tips and tools for testing Django migrations.
(`是也乎:`
Django 的 Migrations 可以说是最强大的自成体系的知名工具了...
今年 PyCon19中国 就有专门主题探索具本质行为,
只是如何测试, 涉及到外部数据库, 还真的是值得讨论的事儿...
)

## 讨论
>
> Discussions
NIL

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [Python 社区专访 Brian Okken](https://pycoders.com/link/2966/web)
  - REAL PYTHON
Brian Okken is perhaps best known as the author of Python Testing with pytest, as well as being the host of two Python-related podcasts. Find out more about the man behind the voice, his new meetup in Portland, and the advice he'd like to give to anyone who's new to testing software.
(`是也乎:`
![Interview](http://ydlj.zoomquiet.top/ipic/2019-11-27-ScreenShot%202019-11-27%2012.39.58.jpg)
等等,这档节目一直没采访过老爹的?
)
- [Python 3 byte / str 分隔问题](https://pycoders.com/link/2978/web)
  - JOHN GOERZEN
  - opinion
The original title of the article is The Incredible Disaster of Python 3 so this was probably written with some frustration still fresh on someone's mind. Nevertheless I think it's important to look at aspects of Python that developers might be struggling with and that could be improved. Related discussion on Hacker News.
- [Python 中无效的语法: SyntaxError的常见原因](https://pycoders.com/link/2972/web)
  - REAL PYTHON
In this step-by-step tutorial, you'll see common examples of invalid syntax in Python and learn how to resolve the issue. If you've ever received a SyntaxError when trying to run your Python code, then this is the guide for you.
(`是也乎:`
![Syntax](http://ydlj.zoomquiet.top/ipic/2019-11-27-ScreenShot%202019-11-27%2012.34.13.jpg)
语法错误应该是最友好和常见的警告了...
但是, 这又是阻止小白们进入自由世界最大的坑...
)
- [教学 Python 33集: Eric Matthes 访谈](https://pycoders.com/link/2983/web)
  - TEACHINGPYTHON.FM
  - podcast
Kelly and Sean interview Eric Matthes, author of Python Crash Course, about how he began programming, what led him to teaching, and the important lessons from Python to be learned both inside and outside of the classroom.
- [用 Python 检测人的"思维强度"](https://pycoders.com/link/2963/web)
  - JOHN DAVID CHIBUK
How to get started with fNIRS sensing data specifically oxygenated hemoglobin "HbO2/HbO" data for analyzing a data stream from a sensor.
- [用 Python 计算 FLOPS 和其他 CPU 计数器](https://pycoders.com/link/2980/web)
  - BOJAN NIKOLIC
How the python-papi package can be used to measure the FLOP requirements of any section of a Python program.
- [符号数学在 Python](https://pycoders.com/link/2967/web)
  - ALEXANDRU GRIS
(`是也乎:`
输入:
    import sympy as sp
    sp.init_printing() # or init_session(). init_session does much more
    x = sp.Symbol('x')
    sp.pprint(sp.Integral(sp.sqrt(1/x), x))
获得:
    ⌠
    ⎮     ___
    ⎮    ╱ 1
    ⎮   ╱  ─  dx
    ⎮ ╲╱   x
    ⌡
可以说很萌了...
数学计算一直是计算机的核心使命, 只是数学各种专用符号, 以往都在 TeX 基础上折腾,
没想到, ASCII-art 果断没放弃...
)
- [Qt Python GUI 应用的登录](https://pycoders.com/link/2987/web)
  - PLUMBERJACK.BLOGSPOT.COM

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [munggoggo: 基于消息的异步代理框架](https://pycoders.com/link/2985/web)
  - GITHUB.COM/SYSID
  - • Shared by Thomas Weber
- [pytest-quarantine: 管理预期的测试失败](https://pycoders.com/link/2968/web)
  - GITHUB.COM/ENERGYSAGE
(`是也乎:`
前几期推荐过...专注管理预期失败的测试案例
)
- [dovpanda: Directions Overlay for Working With Pandas](https://pycoders.com/link/2976/web)
  - GITHUB.COM/DOVPANDA-DEV
(`是也乎:`
叕一个试图网络化 Pandas 运算的模块
)
- [blueberry-python-data: 用 fNIRS 进行数据实验](https://pycoders.com/link/2974/web)
  - GITHUB.COM/BLUEBERRYXTECH
  - • Shared by John David Chibuk
(`是也乎:`
兰莓
)
- [Numba: 用于 NumPy 代码的 JIT 编译器](https://pycoders.com/link/2962/web)
  - PYDATA.ORG
(`是也乎:`
JIT 技术越来越嗯哼了
)
- [tsaug: 增强时序](https://pycoders.com/link/2981/web)
  - GITHUB.COM/ARUNDO
(`是也乎:`
叕一个时序相关模块,
可见大数据后, 时序数据正在兴起
)
- [Mitogen: 编写分布式自我复制程序的库](https://pycoders.com/link/2973/web)
  - NETWORKGENOMICS.COM
(`是也乎:`
![Mitogen](https://d33wubrfki0l68.cloudfront.net/be86b6f40a357000aaa1338b3542cfaedb0e0a12/d106b/_images/mitogen.svg)
嗯哼? 立志作 fab/inv/Ansible 们的基础框架...
简直就是使用 蠕虫病毒 原理来完成自动复制和扩散....
)
- [superdelegate: 将方法和属性委托给子对象的简写形式](https://pycoders.com/link/2979/web)
  - PYPI.ORG
  - • Shared by Jim Anderson
- [autohooks: Git Hooks 和 Python](https://pycoders.com/link/2988/web)
  - GITHUB.COM/GREENBONE
  - • Shared by Björn Ricks

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PythonRio Meetup](https://pycoders.com/link/2956/web)
  - November 30, 2019
  - 巴西
- [⋅ Melbourne Python Users Group](https://pycoders.com/link/2958/web)
  - December 2, 2019
  - Australia
- [⋅ Heidelberg Python Meetup](https://pycoders.com/link/2961/web)
  - December 4, 2019
  - 德国

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- **[蟒营 Python 入门班](https://py.101.camp/)**
  - 101camp4py
  - 101camp5py
(`(￣▽￣)`:
第4期已开始, 为期6周;
    200112 按时结束
第5期年后再来:
    200203 应该上线
)

# 是也乎
>
> NN 3837

- 首发: [Issue 396 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-396.html)
- 改进: [issue-396.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-396.md)
