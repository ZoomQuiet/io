# 思维图谱矢量化
> 20年来的顿悟

## background

zoomquiet.org 图谱式首页创建出20年, 突然发现可以不用那么折腾的..

## goal
> 应对上千个 node 的复杂图谱时..


- 体积尽可能小
- 支持浏览器中的放大
- 支持 .dot 脚本中的 URL 配置
- ..

## logging

最早是给 woodpecker.org.cn 构造首页时,
作为中国最早的一个 Python 技术社区, 就想 geek 一些,
所以:

- 尝试使用 freemind 编写思维导图来引导社区网站中丰富的分类资源
- 获得正向反馈后, 发现, 每次都需要使用 freemind 软件编辑再导出, 不够 geek
- 然后, 发现了 graphviz 通过一种 .dot 图形脚本, 使用指令自动生成各种图谱
    - 这种 CLI 工具, 当然可以用 Python 来控制
    - 而且, .dot 本质上就是 .txt 文件, 也容易通过版本管理系统来统一管理
- 就将 freemind 的图谱变成 graphviz 的了
    - 问题来了, 原先 freemind 中每个节点是可以绑定链接的,而且导出为 html 页面时, 这个链接也可以在网页中点击..
    - 怎么作到的呢? 研究导出的网页发现使用了一个古老的技术:
    - 图片热点, 也就是 `<map>` 标签中的 `<area>` 声明
    - 可以在 html 中指定图片使用一组热点, 也就是规定图片上什么位置上什么形状的区域有个可以点击的热点, 其中包含链接
    - 可见当年构造 HTML 以及浏览器时, 先贤们, 真的是什么都想明白了哪...
- 那么 graphviz 是否也支持图片热点呢?
    - 必须可以的, 挖掘了各种示例后, 发现了一个参数: `-Tcmapx`
    - 配套 `-o path/2/热点定义文件.map` 就可以获得图片对应所有链接的热点声明文件
    - 手工尝试一下, 果然可以
    - 于是用 Python 将所有行为串起来, 变成一个通用的图谱网页生成器:
        + 明确模板, .dot 文件, 以及网页标题之类参数后
        + 调用 graphviz 对应指令, 一般都是 `dot` 指令,生成图片, 以及 .map 声明
        + 然后, 将图片转化为 base64 编码的文本字串
        + 最后, 使用预先调试好的 .html 模板, 将关键资源拼装在一起:
            + 在合适的位置, 将图片使用 `<img src="data:image/png;base64,iVBORw0KG...` 形式, 从文件引用, 变成 base64 数据库文本使用
            + 并将 .map 文件内容也写到 合适的位置
            + 并注意, 在图片中追加 `usemap="#Alf_layla_wa_layla"` 声明, 说明使用哪组热点, 也就是要和 `<map id="Alf_layla_wa_layla" ..` 这里的 id 对应
- 好的, 一切工作了, 这样, 每次图谱有变化,嘦:
    - 修订 .dot 文件
    - 然后, 运行 `dotools/gen4dot2htm.py` 就可以获得最终完成更新的 .html 文件
    - 注意, 这时, 不用另外引用什么图片, html 内置了图片数据
    - 最后, 对应发布 .html 到合理的线上空间就好
- 其后, 社区变迁, 网站也从公司赞助的主机 apache 服务, 变成各种免费空间
    - 比如 github-pages, gitcafe.-pages, gitlab-pages ...
    - 但是, 整体流程从来没变过..


> 直到今天..

想对一个长期播客项目: `[天方夜谭]` 制作一个持续增长的树图;
结果发现, 超过1000+节点时, 图片也超过了50Mb, 尽管进行了分辨率控制, 以及要求输出 .gif 格式后, 可以将图片控制在10M 以内;

但是, .map 文件中区域坐标已经超过 8000, 网页打开检验时, 热点根本就飘了, 不知道去哪儿了..

> 这怎么整.,.

问了大模型们, 也没获得什么启发;
老老实实去官网看文档;

突然, 发现不知道什么时候支持输出 SVG 图形了;
这是个古老的矢量图片格式, 浏览器一直支持,
但是, graphivz 并不支持哪...

根据文档, 将输出参数变成: `-Tsvg_inline` ,
要求输出为 .html 文件, 结果用浏览器打开一看, OK 了;

根据不用热点了, 人家直接在 `<svg>` 标签中就嵌入了;

### 教训
> 官方文档一定要不时复习..

以及:

使用 SVG 输出时, `dpi = 150` 这种控制图片生成尺寸的参数;
得清除, 否则输出的 SVG 将意外裁剪, 无法完整输出;





## refer.
> graphviz version 12.2.1 (20241206.2353)

- [FreeMind](https://freemind.sourceforge.io/wiki/index.php/Main_Page)
- [Graphviz](https://graphviz.org/)
    + [SVG | Graphviz](https://graphviz.org/docs/outputs/svg/)
    + ..

## tracing

- 250510 DAMA init.


```
         _~---~_
     () /  ^ ☉  \ \/
       '_   ⎕   _'
       \ '--~--' |

...act by ferris-actor v0.2.4 (built on 23.0303.201916)



                    'c.          zoomq@ZQ160626rMBP 
                 ,xNMM.          ------------------ 
               .OMMMMo           OS: macOS Big Sur 10.16 24E263 arm64 
               OMMM0,            Host: MacBookPro18,4 
     .;loddo:' loolloddol;.      Kernel: 24.4.0 
   cKMMMMMMMMMMNWMMMMMMMMMM0:    Uptime: 23 days, 13 hours, 7 mins 
 .KMMMMMMMMMMMMMMMMMMMMMMMWd.    Packages: 419 (brew) 
 XMMMMMMMMMMMMMMMMMMMMMMMX.      Shell: bash 5.2.37 
;MMMMMMMMMMMMMMMMMMMMMMMM:       Resolution: 2048x1280, 1440x2560, 3360x1890 
:MMMMMMMMMMMMMMMMMMMMMMMM:       DE: Aqua 
.MMMMMMMMMMMMMMMMMMMMMMMMX.      WM: Spectacle 
 kMMMMMMMMMMMMMMMMMMMMMMMMWd.    Terminal: vscode 
 .XMMMMMMMMMMMMMMMMMMMMMMMMMMk   CPU: Apple M1 Max 
  .XMMMMMMMMMMMMMMMMMMMMMMMMK.   GPU: Apple M1 Max 
    kMMMMMMMMMMMMMMMMMMMMMMd     Memory: 11549MiB / 65536MiB 
     ;KMMMMMMMWXXWMMMMMMMk.
       .cooc,.    .,coo:.                                

```