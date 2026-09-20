---
title: "Issue 401"
summary: ""
date: "2020-01-01T17:42:00"
tags:
  - "Weekly"
  - "Python"
  - "pycoders"
  - "ZH"
---

> Python 2.7 今天正式退休
原文: [PyCoder's Weekly - Issue #401](https://pycoders.com/issues/401)
![PyCoder](https://cdn.pycoders.com/37bdf31dc645f968ffb90196e5d38ff5)

- 200101 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 42 分钟 完成快译
- 200101 [Zoom.Quiet](http://zoomquiet.io/)(大妈) 用时 17 分钟 完成格式转抄.

------

- [Python 2.7 Retires Today](https://pycoders.com/link/3187/web)
  - PYTHONCLOCK.ORG
Python 2.7 will not be maintained past Jan 1st, 2020. So long Python 2, and thank you for your years of faithful service. Python 3, your time is now!
(`是也乎:`
当然, 海量 Py2.7 兼容代码, 将继续在非官方支持下良好运行到永远...
)
- [对 Python之禅 的冥想](https://pycoders.com/link/3194/web)
  - MOSHE ZADKA
"The Zen of Python is not 'the rules of Python' or 'guidelines of Python'. It is full of contradiction and allusion. It is not intended to be followed: it is intended to be meditated upon. In this spirit, I offer this series of meditations on the Zen of Python."
(`是也乎:`
蟒之禅 的原义就是引发沉思,而不是终止之...
)
- [Python 计时器功能: 监视代码的三种方法](https://pycoders.com/link/3191/web)
  - REAL PYTHON
Learn how to use Python timer functions to monitor how fast your programs are running. You'll use classes, context managers, and decorators to measure your program's running time. You'll learn the benefits of each method and which to use given the situation.
(`是也乎:`
![Timer](http://ydlj.zoomquiet.top/ipic/2020-01-01-ScreenShot%202020-01-01%2017.33.52.jpg)
总之: [codetiming](https://pypi.org/project/codetiming/) 内置计时器;
[time.perf_counter()](https://docs.python.org/3/library/time.html#time.perf_counter) 提供精确计时;
[timeit](https://docs.python.org/3/library/timeit.html) 专用运行时计时;
[cProfile](https://docs.python.org/3/library/profile.html) 专用性能分析器;
[pstats](https://docs.python.org/3/library/profile.html#pstats.Stats) CLI 性能分析工具;
[KCachegrind](https://kcachegrind.github.io/) GUI 工具来观察性能分析数据;
![KcgShot3Small.gif (GIF Image, 260 × 218 pixels)](https://kcachegrind.github.io/images/KcgShot3Small.gif)
[line_profiler](https://github.com/rkern/line_profiler) 单行代码性能监察;
[memory-profiler](https://pypi.org/project/memory-profiler/) 内存监察工具.
)
- [开源移民情绪困扰](https://pycoders.com/link/3196/web)
  - ARMIN RONACHER
The creator of Flask reflects on the Python 2 to 3 migration and how the Python community handled the transition. Interesting read!
(`是也乎:`
和 `数字游民` 不同, 移民指就基础运行平台的迁移,
不象 Python 1.x -> 2.x 的迁移, 亳无压力,
因为, 当年根本就没什么成规模的 1.x 工程.
所以, 技术工程迁移, 多数阻力不在技术, 而在情绪, 就象人月神话,以及其它真实软件工程心理学著作中论及的...
代码相处时间久了, 一样有感情的, 被迫迁移到完全无感觉的新平台中, 就象改嫁...
)
- [Python  REPL和Shell集成技巧](https://pycoders.com/link/3183/web)
  - JOHN D. COOK
Some good tips and ways to minimize the context interruption when moving between the shell and a Python session.
(`是也乎:`
厨子说的总是有用的....
)
- [俺名片能运行 Linux+MicroPython](https://pycoders.com/link/3197/web)
  - GEORGE HILLIARD
Embedded systems engineer builds a card-sized computer that boots Linux and runs MicroPython. Cool!
(`是也乎:`
网红事件了...
![MicroPython](https://www.thirtythreeforty.net/posts/2019/12/my-business-card-runs-linux/businesscard-top_huad90566bef925e8b01048d4355f78bd6_6751801_1024x1024_fit_q80_box.jpg)
已经有人准备将之复制并配置为实体 BTC 銭包了...
)
- [PyPy 7.3.0 发布](https://pycoders.com/link/3190/web)
  - PYPY BLOG

## 讨论
>
> Discussions
NIL

## 文章,教程和嗯哼
>
> Articles, Tutorials and Talks

- [Python Packaging 生态](https://pycoders.com/link/3186/web)
  - NICK COGHLAN
"[It] seems worthwhile for me to write-up my perspective as one of the lead architects for that ecosystem on how I characterize the overall problem space of software publication and distribution, where I think we are at the moment, and where I'd like to see us go in the future."
(`是也乎:`
简单的说, 还在春秋战国时代, 远没有稳定下来
)
- [2019十大真蟒文章](https://pycoders.com/link/3198/web)
  - TALK PYTHON
  - podcast
I was a guest on Mike Kennedy's Talk Python podcast and we discussed a shortlist of 10 interesting tutorials published on Real Python in 2019. So if you're looking to expand your year-end reading list you'll find some inspiration there. It's always a treat to be on Mike's show—definitely check out his podcast!
(`是也乎:`
果然, 每年必须的 top1 文章/问题/讨论都是相同的:
    如何运行你的 Python 脚本?
这其实, 也展示出了编程和非编程世界的根本差异.
)
- [用 Python 对数据排序](https://pycoders.com/link/3181/web)
  - REAL PYTHON
  - video
In this step-by-step course, you'll learn how to sort in Python. You'll know how to sort various types of data in different data structures, customize the order, and work with two different ways of sorting in Python.
(`是也乎:`
![Sorting](http://ydlj.zoomquiet.top/ipic/2020-01-01-ScreenShot%202020-01-01%2017.23.45.jpg)
Python 丰富的数据类型, 也就意味着有丰富的排序技巧...
)
- [批量训练: 如何拆分数据?](https://pycoders.com/link/3200/web)
  - OLEG ŻERO
Creating data batches for model training evaluated in context of loading data using Python generators, HDF5 files and NumPy using a sound processing machine-learning model as an example.
- [如何使用 Pandas get_dummies 在 Python 中创建虚拟变量](https://pycoders.com/link/3195/web)
  - ERIK MARSJA
Dummy variables (or binary/indicator variables) are often used in statistical analyses as well as in more simple descriptive statistics.
- [Python 类型提示和 MyPy 教程](https://pycoders.com/link/3199/web)
  - GUILHERME KUNIGAMI
This post covers mypy in general terms as well many examples demonstrating the syntax and capabilities of this type checker.
- [Pipx: 在虚拟环境中安装/卸载和升级 Python 软件包](https://pycoders.com/link/3201/web)
  - ERIK MARSJA
Here you will learn how to install, uninstall, & upgrade Python packages using the pipx tool.
(`是也乎:`
![Pipx](https://www.marsja.se/wp-content/uploads/2019/12/using_pipx_to_run_a_python_app_temporary.jpg)
---w
)
- [魔法-虫洞: 将嗯哼从一台计算机安全地转移到另一台计算机](https://pycoders.com/link/3188/web)
  - MAGIC-WORMHOLE.READTHEDOCS.IO
(`是也乎:`
一本免费魔法书...
)
- [Python 进行堆排序](https://pycoders.com/link/3182/web)
  - OLIVERA POPOVIĆ

## 好物
>
> Interesting Projects, Tools and Libraries, Projects & Code

- [drf_dynamics: 用于 Django REST 框架的动态查询集和序列化程序设置](https://pycoders.com/link/3179/web)
  - GITHUB.COM/IMBOKOV
  - • Shared by Ilya Bokov
Handles the hassle of handling the amount of fields to be serialized and queryset changes for each request for you.
- [Astropy: Python 天文学](https://pycoders.com/link/3192/web)
  - ASTROPY.ORG
(`是也乎:`
Astropy -> 熵, 好词儿
)
- [AI_Sudoku: 从照片中提取数独谜题并解决](https://pycoders.com/link/3193/web)
  - GITHUB.COM/NEERU1207
- [ffmpeg-python: FFmpeg的Python绑定](https://pycoders.com/link/3180/web)
  - GITHUB.COM/KKROENING
(`是也乎:`
![formula](https://raw.githubusercontent.com/kkroening/ffmpeg-python/master/doc/formula.png)
其实, FFmpeg 本身的控制界面足够稳了...
只是能将:
    ffmpeg -i input.mp4 -i overlay.png -filter_complex "[0]trim=start_frame=10:end_frame=20[v0];\
    [0]trim=start_frame=30:end_frame=40[v1];\
    [v0][v1]concat=n=2[v2];[1]hflip[v3];\
    [v2][v3]overlay=eof_action=repeat[v4];\
    [v4]drawbox=50:50:120:120:red:t=5[v5]"\
    -map [v5] output.mp4
变成:
    import ffmpeg
    in_file = ffmpeg.input('input.mp4')
    overlay_file = ffmpeg.input('overlay.png')
    (
        ffmpeg
        .concat(
            in_file.trim(start_frame=10, end_frame=20),
            in_file.trim(start_frame=30, end_frame=40),
        )
        .overlay(overlay_file.hflip())
        .drawbox(50, 50, 120, 120, color='red', thickness=5)
        .output('out.mp4')
        .run()
    )
还是值得的...
)
- [Magic-Wormhole: 将嗯哼从一台计算机安全地转移到另一台计算机](https://pycoders.com/link/3188/web)
  - MAGIC-WORMHOLE.READTHEDOCS.IO
- [pyopengl: 适用于 Python 的 OpenGL 绑定](https://pycoders.com/link/3184/web)
  - GITHUB.COM/MCFLETCH
(`是也乎:`
C++ 专属领域终于也被入侵了...
)

## 📆🐍 活动/大会
>
> Events, MeetUp 真的是全球线下活动组织中心

- [⋅ PyDelhi User Group Meetup](https://pycoders.com/link/3177/web)
  - January 4, 2020
  - 印度
- [⋅ Melbourne Python Users Group, 澳洲](https://pycoders.com/link/3176/web)
  - January 6, 2020
- [⋅ Dominican Republic Python User Group](https://pycoders.com/link/3169/web)
  - January 7, 2020
  - 中美洲
- [⋅ Heidelberg Python Meetup](https://pycoders.com/link/3170/web)
  - January 8, 2020
  - 德国
- [⋅ Python North East](https://pycoders.com/link/3172/web)
  - January 8, 2020
  - 英国
- [⋅ PyStaDa](https://pycoders.com/link/3166/web)
  - January 8, 2020
  - ??
- [⋅ pyCologne User Group Treffen](https://pycoders.com/link/3168/web)
  - January 8, 2020
  - 404
- [⋅ Santa Cruz Python Meetup](https://pycoders.com/link/3174/web)
  - January 8, 2020
  - USA
- [⋅ PyMNTos](https://pycoders.com/link/3167/web)
  - January 9, 2020
  - USA
- [⋅ Python Atlanta](https://pycoders.com/link/3171/web)
  - January 9, 2020
  - USA

## DAMA
>
> ❤️ Happy Pythonic ;-(`大妈私人无责任播报`)

- **[蟒营 Python 入门班](https://py.101.camp/)**
  - 4py :-}
  - 5py ;-)
(`(￣▽￣)`:
第4期已开始, 为期6周;
    当前 ch2
    200112 按时结束
年后第5期就来:
    200203 值得上线
)
- [从1965年到2019年,最受欢迎的编程语言 (动画)](https://pycoders.com/link/3100/web)
  - TWITTER.COM/MARCUSBORBA
(`是也乎:`
网红小视频也出现了...
最后3秒, Python 疯狂反转一切.
)

# 是也乎
>
> NN 3879

- 首发: [Issue 401 ~蠎周刊 ~汇集全球蠎事儿 ;-)](http://weekly.pychina.org/issue/issue-401.html)
- 修订: [issue-401.md](https://github.com/PyChina/weekly/blob/master/content/Issue/issue-401.md)
