---
title: "从迅雷到 Pikpak .. 一次可以说流畅的迁移"
summary: "本地大空间以及配套下载流程的演变.."
date: "2026-06-17"
tags:
  - "Pythonic"
  - "26"
---

# 从迅雷到 Pikpak .. 一次可以说流畅的迁移
> 本地大空间以及配套下载流程的演变..


## background
> 事儿是这么开始的..

基于这篇文章的经验: [永不消逝的存储@高博](https://zhuanlan.zhihu.com/p/657653244)

在 gao.bo 的支持下, 上了 `QNAP TS-212`

一下子打开了备份资源的野心; 
叕经过了一系列设备的曲折(参考尾部外一篇小故事),
现在有一组专用的 SSD 外接硬盘进行高速操作(视频编辑...);

一组 RAID 陈列进行资源储存:

- 20.0T ~ T22x2RAID1: 中国+日本影视
- 50.9T ~ T14x5RAID5: 欧美影视+综艺
- 36.4T ~ T10x5RAID5: 其它资源

而且主要下载渠道是 thunder/迅雷 SVIP 会员;
日常操作习惯经过多年磨合早已形成:

- 多方搜索, 拿到资源链接, 一般都是 `magnet:?xt=urn:btih:5aa7...`
- 右击链接, 在弹出菜单中, 使用 `复制干净的链接`
- 打开剪贴板监察, thunder 将自动感知并创建下载任务
- 批量追加任务后, 根据下载情况, 批量删除下载速度不佳


## goal
> 问题来了..

之前硬盘是直接通过 USB 硬盘座通过 type-c HUB 接入 macOS 的;
一直以来没什么问题;

但是, 迁移到桌面磁盘阵列后, thunder 突然报 `磁盘空间不足` 然后,
都下载到 99% 的任务就标红了;
可对应 RAID 还有10多Tb 空间可用;

这怎么肥四?

## logging
> 最简单粗暴的方法...

直接拉开 Claude 4.8 max 就问, 然后知道了:
> Yottamaster 这类 DAS 的 USB-SATA 桥接芯片有自己的固件级休眠，和 macOS 的"关闭硬盘自动休眠"是两回事：你关掉的是 macOS 侧的电源管理，但机柜固件自己的待机/掉电逻辑你关不掉。屏保触发系统降低 USB 总线活动后，桥接芯片让 RAID5 阵列进入低功耗，再唤醒时阵列重新枚举，空间被瞬间卸载再挂载。
> 迅雷的下载会话持有的是旧的文件句柄/挂载点，重挂载后路径虽然名字相同，但底层 inode 变了，迅雷拿到的 statvfs() 返回值在重挂载的瞬间是 0 或异常值——于是报"磁盘空间不足"。这完美解释了为什么单盘硬盘座没问题：单盘 USB 座唤醒只需重新就绪一个磁盘（毫秒级），而 5 盘 RAID5 重新枚举+校验需要数秒，期间卷处于不一致状态，迅雷正好踩中。

那么无非是几种应对姿势:

- 改进 thunder 兼容这种重挂载的情况
- 不用 thunder 使用其它无视这种情况的下载器
- 改进 阵列不再自动休眠

将 LLM 支的快招先用了一遍:

- 系统配置中, 关闭自动休眠, 关闭屏保, 给 thunder 所有磁盘权限...
- 使用 `caffeinate -dimsu` 强制下载期间持有：阻止显示器睡眠(-d)、磁盘睡眠(-m)、系统睡眠(-s)、用户活动假象(-u) ...
- 甚至于, 用 LLM 快速生成了一个专用小脚本, 在 thunder 下载期间, 不断的读取目标空间指定目录的元数据, 以便 RAID 一直都有有效 IO 行为,而不可能休眠...

> 但是, 没用, 照样报 `磁盘空间不足` 然后, 拒绝下载;

那么又没有 thunder 的源代码, 不可能改进这方面的问题;
就只能尝试替代了;

首先推荐的是 aria2/aria2-next + AriaNg, 配套对应浏览器插件,
可以完成原先复制链接自动创建任务, 并可以进入任务包选择不必要的文件不下载;

> 但是, 这要安装多个应用;

然后, 发现 Motrix/MotrixNext, 是 macOS 兼容的 thunder 同类软件;
特别是 MotrixNext 还是 rust 重构的应用;
官方还提供了对应浏览器插件, 右击菜单中有 `使用 Motrix Next 下载`,
立即就可以通过本地 `:29110` 端口连接到 MotrixNext 内置 `aria2-next` 服务,
并完成任务创建;

这个官方插件, 可以感知 磁力+ED2K+thunder+.. 各种常见资源协议链接;

> 但是, 在大陆本地家庭宽带环境中, MotrixNext 能完成 bt 种子下载的概率非常小;

原先通过 SVIP 帐号加持的 thunder 下载时, 基本上每100个下载任务中, 还能有20个以内可以完成资源探索, 然后, 在 100Kb/s 的下载速度下完成下载;

而现在切换到本地的 MotrixNext(aria2内核)时, 每100个下载任务中, 幸运的话也就有不到10个可以完成资源探索...

这...基本不可用了;

然后 LLM 又忽悠俺说:

- Bt 种子大概率在海外有, 国内不多
- 而且 GFW 有各种限制和自动 block
- 所以,如果有海外主机的话, 可以将下载任务丢到海外主机上, 完成下载后, 再回拉落入 RAID 空间


而推荐的下载引擎就是: qBittorrent, 配套  Caddy 的多线程下载支持,
通过 Hy2 伪装代理回拉落地;

好吧, 反正现在各种软件的安装配置以及网络调试都是 CodeX(gpt 5.5)在折腾了,
俺也就提出个构思, 就可以快速看到结果;

所以, 为了安全, 在 LA 的主机安装配置好 qBittorrent+Caddy 后,
只监听本地 127.0.0.1 的约定端口;
然后, 通过 SSH 套上 Hy2 伪装成标准的 UDP 请求, 反向代理回内网;
俺就可以:

- 访问 http://127.0.0.1:16881/ 操作海外主机上的 qBittorrent 创建任务
- 访问 http://127.0.0.1:18093/ 看到约定下载完成目录中的文件, 右击 `使用 Motrix Next 下载` 完成回拉任务的自动创建


> 但是, 海外的 qBittorrent 也无法提高资源命中率, 每100个下载任务中, 幸运的话也就有不到2个可以完成资源探索...

再吼 LLM, Opus 4.8 这时, 开始安利以 PikPak 为首的各种付费云下载服务,
也就是和 thunder 付费服务类似的:

- 给入下载任务
- 人家到自己的 CDN 中匹配, 如果有瞬间复制一份到你的云盘中
- 然后, 再使用原创加密加速协议, 下载到你的本地
- 是的, 通过专有 app


一开始, 推荐的是 TorBox, 但是, 注册尝试了一下, 发现和 qBittorrent 没什么不同;

再尝试 PikPak, 瞬间资源出现在云盘中;

> 但是使用推荐的可挂机自动运行的 rclone ,配置好后,
在 macOS 本地, 下载速度只有 1Mb 左右;

而在海外主机上, 能达到 17Mb , 这..还是免费帐号, 没付费呢;

于是, 在 LLM 配合下, 尝试各种姿势, 想加速从海外主机下载指定文件到本地...
没想到, 使用了各种工具/线路/策略/....

都无法突破 200Kb 的大文件下载速度;

这才意识到, GFW 的威力真的很强大, 从海外想高速下载,

- 要么使用专用高速线路
- 要么使用专用高速线路上配套专用压缩算法
- 要么使用有中国线路的云盘, 先上传云盘, 然后再用对应服务商的内部线路和专用软件下载到本地空间
- ...

于是, 思前想后, 发现, 当初付费 thunder 的 SVIP 帐号, 就是因为免费帐号根本不给加速, 也就是不给你用人家的 CDN 资源来加速下载;

那么, PikPak 为什么不付费升级为 VIP 来完成加速?

> 但是, 付费后, 才发现, PikPak 分区域会员和全球会员, 价格不同, 线路不同速度也不同...

而每年将近 300RMB 的区域帐户,
使用官方 PikPak 的下载速度, 还不到 200Kb/s;

而使用开源广谱 CLI 下载工具 rclone , 还能达到 1.5Mb/s 的下载速度;

不过, 可喜的是, 付费后, PikPak 云盘空间达到 10Tb, 
而平均 100个下载任务中, 能有80个任务瞬间完成`下载` 出现在云盘中;

好吧, 这样一来, 通过 rclone 在 CLI 中的可以完成推送下载任务到云盘指定目录中,
当然也可以自动巡查约定目录下载情况, 然后组织回拉任务队列, 
以 1Mb/s 的速度挂机持续自动下载回 RAID 空间中;

至此问题总算基本解决;
对应支持脚本也是 LLM 生成的



## summary

好吧, 没想到作为多年的 迅雷用户, 而且是付费用户,
竟然被 桌面RAID磁盘阵列 的保护机制触发了 thunder 的 bug,
不得不找替代, 还真有: [pikpak](https://mypikpak.com/drive/activity/invited?invitation-code=64629172)

可以看看教程先:
https://mypikpak.com/s/VOvKRmsNZ44UwtjjzRwXqYXOo2

类似 thuber 的付费云下载服务,
这东西, 感觉在海外有海量 CDN 缓存
很多 bt 资源, 立即就完成了下载；

唯一的问题是人家的 CDN 空间都在海外, 想拉回 功夫 网层层和谐的本地磁盘阵列空间, 一般姿势都不行;

幸好支持 rclone , 这是数据同步神器, 是 rsync 的升级版本,
支持 50多种专有服务, 其中包含 Pikpak;
支持 推送下载任务到 Pikpak, 当然也支持删除对应文件/目录,
以及下载指定文件目录;

进一步的还发现, 支持对云盘中的指定文件进行分片并行下载;
通过 Python 组织的下载脚本, 可以完成以下支持:

```
...
子命令：
  watch              监控剪贴板，发现链接即提交 PikPak（纯提交，不下载）
  check              巡查云端：本地对比 queue.json，只查新目录，删消失项（默认每4分钟）
  pull               纯下载：全局分片池，跨文件持续 N 分片并行，拉满速度
  finalize           合成收尾：拼接分片→校验→删云端→加✅→标记done（与下载解耦）
  add URL            手动提交单个链接
  status             显示四进程运行状态与全局进度（-f 守护监察每4秒刷新）
  cloud              列出云端内容（标注哪些是将下载的大视频）
  mark               历史兼容：给队列中已完成项的本地资源补 ✅ 前缀
  cleanup            手动清理云端删除失败的残留目录（cleanup skipped 还清理历史小目录）

典型用法（四个终端，职责彻底单一化，最大化解耦+并行）：
  终端1： ./rcsync.py watch -v            # 提交任务
  终端2： ./rcsync.py check -v            # 巡查云端维护队列
  终端3： ./rcsync.py pull -v             # 全局分片池纯下载
  终端4： ./rcsync.py finalize -v         # 合成收尾（不占下载带宽）
  随时 ： ./rcsync.py status -f

说明：
  - 四进程解耦：check 巡查 / pull 下载 / finalize 收尾 / status 只读监察，互不阻塞。
  - pull 全局分片池：跨文件持续保持 N 个分片并行（--transfers），某文件尾部
    分片不足 N 时自动混入下一文件的分片填满，消除降速空窗，始终拉满速度。
  - 分片下完即置 assembling 交 finalize，pull 立刻继续下别的分片不等合成。
  - check 本地对比，只对新目录递归扫描，几百个已知目录不重复扫描。
  - queue.json 文件锁保护，多进程并发读写安全；done 记录永久保留防重复下载。
  - 大文件阈值用 --min-size；分块大小用 --chunk-size；并发分片数用 --transfers。

支持链接：magnet / thunder:// / ed2k:// / ftp(s):// / *.torrent；不接受普通网页。

```

这样一来, 经过多年磨合早已形成的日常习惯操作也得以兼容::

- 多方搜索, 拿到资源链接, 一般都是 `magnet:?xt=urn:btih:5aa7...`
- 启动 rcsync.py watch -v
- 网页中右击链接, 使用 `复制干净的链接`, 
- 将自动感知并通过 rclone 创建下载任务
- 批量追加任务后, 根据下载情况, 不定期到 Pikpak 管理后台批量删除下载失败的任务

现在, 已经有 4Tb 已经完成下载的任务在云盘等待 rclone 下载到本地磁盘阵列空间中;
而通过 文件分片池管理, 确保同时有4片 512M 的下载任务在进行,
网络情况好时, 可以达到 20M+ 的下载速度;
而且, 因为是 CLI 工具, 对于磁盘阵列的重新挂载现象很钝感/智能恢复;
可以24小时持续自动进行, 占用系统资源也不多;

比之前使用 thunder / Aric2+MotrixNext / .. 还要简洁流畅;

这..就是 LLM 带来的加速了;
以往, 光是要摸明白 rclone 对 Pikpak 的支持, 都得几天;
现在, 说明心愿, 立即就调研出来了,
而且, 落到 Python 脚本, 几乎不用调试, 立即可用;


PS:
全程都是 Claude Opus 4.8 xhigh 协助,
在网页对话中完成...

## refer.

> 以下链接均经检索核验为真实可达来源(2026-06)。

**TorBox 官方 API 与 SDK**
- TorBox 官方 API 文档:https://api-docs.torbox.app/
- TorBox API(Postman 镜像,含速率限制):https://documenter.getpostman.com/view/29572726/2s9YXo1zX4
- TorBox 官方 Python SDK 仓库:https://github.com/TorBox-App/torbox-sdk-py
- TorBox Python SDK · Torrents 服务文档:https://github.com/TorBox-App/torbox-sdk-py/blob/main/documentation/services/TorrentsService.md
- TorBox Python SDK · WebDownloads/Debrid 服务文档:https://github.com/TorBox-App/torbox-sdk-py/blob/main/documentation/services/WebDownloadsDebridService.md
- TorBox Python SDK · torrents.py 源码:https://github.com/TorBox-App/torbox-sdk-py/blob/main/src/torbox_api/services/torrents.py
- torbox-api · PyPI:https://pypi.org/project/torbox-api/

**qBittorrent 自动化**
- qbittorrent-api · PyPI:https://pypi.org/project/qbittorrent-api/
- qbittorrent-api 文档(Read the Docs):https://qbittorrent-api.readthedocs.io/
- qbittorrent-api 仓库:https://github.com/rmartin16/qbittorrent-api

**SSH 端口转发 / 隧道**
- SSH 隧道安全端口转发完整指南(LocalForward/GatewayPorts):https://oneuptime.com/blog/post/2026-03-02-how-to-configure-ssh-tunnels-for-secure-port-forwarding-on-ubuntu/view
- SSH 本地端口转发(-L)配置(含 ~/.ssh/config 示例):https://oneuptime.com/blog/post/2026-03-20-ssh-local-port-forwarding-ipv4/view
- SSH 隧道配置完整指南(GatewayPorts / autossh 保活):https://cubepath.com/docs/Network%20Configuration/ssh-tunnel-configuration-port-forwarding
- SSH 端口转发可视化指南(本地/远程转发):https://iximiuz.com/en/posts/ssh-tunnels/
- SSH 端口转发入门(GatewayPorts 说明):https://linuxconfig.org/introduction-to-ssh-port-forwarding

**Caddy 静态文件服务 / Range 支持**
- Caddy file_server 指令文档:https://caddyserver.com/docs/caddyfile/directives/file_server
- Caddy 官网(明确支持 Range/ETag):https://caddyserver.com/
- Caddy fileserver 包文档(Range/If-Range 等处理):https://pkg.go.dev/github.com/caddyserver/caddy/v2/modules/caddyhttp/fileserver

**Tracker 列表源**
- ngosang/trackerslist:https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt

**Debrid 选型对比(沿用 v1)**
- Real-Debrid vs TorBox 对比(2026):https://factually.co/fact-checks/electronics-tech/real-debrid-vs-torbox-privacy-performance-comparison-2026-2ebbe3
- TorBox vs Real-Debrid 速度/缓存实测(2026):https://factually.co/fact-checks/electronics-tech/torbox-vs-real-debrid-speed-cache-tests-2026-ef35cb
- Real-Debrid 替代品与双服务策略:https://iptvranking.com/real-debrid-alternatives/


## 外一篇: 本地大空间的演化
> 一切都是从U盘开始的...

私人电脑, 最早一台是2000年配置的, 
花了2万多, 配置了主机/显示器/扫描仪/彩色打印机/...
硬盘有 680M;

所以, 大文件归档保存, 那时是 VCD 刻录, 一张极限 780M;
后来升级到 DVD 能保存4GB;
但是, 数据准备, 以及后续寻找使用, 都很费时费力;

在尝试了 ZIP/MO 之后, 因为是台式机,
就通过 IPC 接口, 上移动硬盘来管理文件, 但是每次都要重启,
很不实用;

后来, 移动硬盘出现了, 从1G 到 1T,没用几年;
本地也从主机变成了笔记本电脑, 再怎么配置, 硬盘也不过 1T,
很快就被各种下载资源填满;

于是, 移动 2吋硬盘也多了起来 5T 两只, 8T 一个,
不久也满了, 下载的电影也只能看一部删除一部, 
可想长期保存反复看的资源增长的很快,
而且, 格式也很快从  .rmvb 进化为 .mp4/mkv, 兰光的都要几十G 一部片了;

进一步发现, 3吋 SATA 硬盘比 2吋的性价比要合理的多,
在闲鱼, 可以找到 50元/TB 以下的各种二手盘;

于是, 通过 USB 硬盘盒/快接头,
MBP 笔记本日常接一组硬盘, 16T一块, 14T 三块, 12T 两块...

虽然有硬盘盒休眠保护,
但是, 一年过去, 各硬盘都出现问题,异响;
赶紧再找硬盘, 追加 USB 快接头, 用 rsync 抢救迁移数据;

又发现, USB 和 USB 不同, 因为复制指令是通过 MBP 的 macOS 发出的,
所以, 两个挂在同一 USB HUB 上的硬盘间进行数据复制时,
速度都要从 MBP 绕一一下, USB 链路的速度就变成了瓶颈;
USB2 的线和 HUB, 只有10M 不到的速度;

不得不逐一升级了线缆以及HUB, 都达到 USB3.2 水平, 全 type-c 接口,
那全功能线(8K/Hz 视频, 240W充电, 40Gbps), 1.2m 的要70+RMB,
全速 HUB 更加可怕...

这样, 复制速度才能提高到 200M 左右;
而 16T 数据复制也得要几天;
如果这期间老硬盘支撑不住, 大半数据就永远丢失了;

而且, 一堆硬盘, 要分别存放不同分类的视频, 想快速找到对应的,
也是个越来越困难的事儿;

最终在朋友提醒下, 知道了 NAS, 体验后发现, 多数功能暂时没有使用场景;
进一步找到了桌面磁盘阵列,
以及 RAID5 这种最均衡的格式;

这才将一堆单盘, 变成了三组磁盘阵列,
只现在就期待, 哪天哪个磁盘出问题了,
直接热替换那块硬盘即可, 不用再用几天时间去迁移复制...

> 上帝保祐吃完了饭的人民们...


## tracing

- 260625 DAMA 发布
- 260618 DAMA 阶段优化
- 260601 DAMA 寻求其它...
- 260501 DAMA thunder 出错
- 260401 DAMA init.




```
nn 6238

           _~--~~_
       () /  ◴ ◕  \ \/
         '_   ⎕   _'
         ( '--∽--' \

...act by ferris-actor v0.2.4 (built on 23.0303.201916)
```
