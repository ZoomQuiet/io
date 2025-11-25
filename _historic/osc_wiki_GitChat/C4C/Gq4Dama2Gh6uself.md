# GQ:6: 你在github

[TOC]


## 所以?

[GitHub System Status](https://status.github.com/messages)

gh 从上线第一天就公开了系统的整体状态:

- 在维持稳定的响应速度的同时
- 各种数据在高速增长
- 参考: [GitHub Octoverse 2016](https://octoverse.github.com/)
    + 580万 活跃用户
    + 33万 活跃组织
    + 近2000万 活跃仓库
    + 1000多万 打开的 issue
- 如此宏大的代码社交场所中
- 我应该投身在其中来作什么?!


## 使用 gh 的合理姿势

先嗯哼一下, 导言中的扣子, 在笔者看来 `学习的层级`, 从低到高:

                知己何不知 Know Unknow
            知己何已知 Know Knowed
        不知己知何 Unknow know
    不知己不知 Unknow Unknow


以往不知道 gh 的大家, 知道世界上有 gh 这样有趣的大坑后,
也仅仅上升到 `Unknow know` 而已

常言到:

    忘记的就是不重要的
    不知道就是不必要的
    事实往往不是这样的
    (￣⊥￣)

但是, 有了 `github` 这个组合式绳头儿,
我们就可以自行持续挖掘/演练/使用/优化下去, 
直到将 gh 变成自己日常的一部分,
享受 gh 提供的一切, 强化自己的创造性输出.

正如[如何成为一名Hacker](http://man.lupaworld.com/content/develop/joyfire/project/7.html#I660) 中分析的,
针对任何一个开源项目而言,成为有影响力的 hacker ,可以从以下几个方向上折腾:

- dev
- test
- doc
- ops
- Evangelist


当然,多数都是复合型的, 同时是核心开发者又同时也是文档维护等等...

简单的说, 在 gh ,最正义的行为无外两种:

    找到喜欢的<-加入进去
    创造想要的->折腾出来

只是 gh 开创性的为创造提供了全新的姿势:

    fork

见到好的, 立即可以 fork 成自己的:

- 随时 clone 到本地,任性折腾
- 一但有所得, 随时可以用 PR 反馈回去
- 也可以就此不回头, 折腾出自己心目中的她
- 嗯哼, 当然, 得吻合原生仓库的 许可证 协议
    + 好在, 多数都选择很宽松的许可证
    + 支持我们的再发布
    + 但是, 要提醒的, 还是有部分项目, 选择的是特殊的许可证
    + 要是没注意, 被起诉时, 是异常被动的...
    + 比如: [react/PATENTS at master · facebook/react](https://github.com/facebook/react/blob/master/PATENTS)

## gh-api ?
~ [GitHub Developer | GitHub Developer Guide](https://developer.github.com/)

gh 发展的这么快, 最大的功臣, 应该就是异常友好的开放接口了:

- 从一开始, gh 的 RESTful 接口, 就是经常拿来当典范的设计
- 简洁/清晰/明确/可预见/一致性的将 gh 的几乎所有数据公开了出来
- 限制也很嗯哼, 合法的免费请求限制:
    + X-RateLimit-Limit: 5000
    + X-RateLimit-Remaining: 4966
    + X-RateLimit-Reset: 1372700873
    + 足够完成日常的开发/测试
- 由此为基础, gh 吸引了可以说海量的第三方服务/工具/平台来接入, 进行:
    + 使用 gh 进行 OAuth2 认证
    + 基于 gh 行为激发/传递其它数据处理
    + 使用 gh 数据进行额外测试/编译/发布/...
    + ...
- 仅仅基于 gh-repo 来进行联动, 还不过瘾:
    + hubot 更加任性的将各种开放接口扩展到了桌面
    + 通过 coffeescript 的简洁声明
    + 就可以通过桌面聊天界面控制/查询各种可能的远程服务/事务/过程/...
    + 事实上, hubot 已经成为很多团队聊天工具的聊天工具...
    + 呃, 或是说, 变成了一个可配置/增强的, 沟通管理后台/智能助理/...



## 次级市场/服务
~ 官方统计, 最活跃的第三放接入

- [Slack](https://github.com/integrations/slack)
- [Heroku Review Apps](https://github.com/integrations/heroku-review-apps)
- [Travis CI](https://github.com/integrations/travis-ci)
- [Circle CI](https://github.com/integrations/circle-ci)
- [ZenHub](https://github.com/integrations/zenhub)
- [Gitter](https://github.com/integrations/gitter)
- [Waffle\.io](https://github.com/integrations/waffle)
- ...

如果都不知道, 真心得补课了...

更多的请自行挖掘: [GitHub Marketplace](https://github.com/marketplace)

## Awesome Awesome

- 由于 gh 中项目/仓库以及 fork 的临时/永久分支实在太多了
- 又由于通过 gh-repo 来维护/发布/增补 一个有用的索引太方便了
- 所以, 有心(主要是耐心;-)之人, 一般会维护一种叫 `Awesome` 的文档:
    + [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) 索引了主要的 awesome
    + 是的, 由于这一行为高速发展以及不得不整理出 awesome 的 awesome
    + 重要的是这类行为和 gh 团队没一毛銭关系, 完全是自发的
    + 可以说, gh 已经是事实上的开源项目的第一空间
    + 就象图书馆, 达到一定数量时:
        * 必然的要求有书目/索引出现
        * 数量进一步增加后, 书目录本身超过一定数量
        * 就不得不追加索引的索引, 以便加速查询
- 是的, 能自发生成一些创造者自己都始料未及的事务
    + 证明, 已经形成了可持续发展的独立生态了
    + 拥有以自己为核心的生态环境
    + 这是所有技术公司梦寐以求的境界
    + gh 作到了,用了5年 
    + 通过高速积累了1000万个仓库, 以及背后的程序员们的行为

### tool-box
~ 随着 gh 生态的高速发展, 服务于 gh 本身的工具也在持续创新中 


比如: [Octomender](https://octomend.com/)    

- 根据你的 star 积累
- 智能分析出当前 gh 中哪些仓库
- 应该是你有兴趣但是没发现的

那么, 对于各种团队/项目/工程,一但用起来了 gh:

- 自然的面临各种管理相关的统计分析
- 活跃/覆盖/bug 分布/...etc.
- 就些都可以通过 gh 公开的接口, 配合其它工具组合完成
- 只是, 不一定有刚好吻合我们当前需求的组合


> 所以...

知道 gh 后, 在这个越来越热闹的空间中应该作什么?

- 并没有什么统一的法则要求
- 但是, 从 gh 提供的主要功能可以感受的到
- 这个平台,倾向我们持续分享真正有用的代码/知识/信息/...
- 通过代码令世界更美好
    + 嘦出于这个心态
    + 你的一切努力
    + 无法后台系统/关联服务/参与成员/推荐算法/...
    + 都是入眼走心的

> 所以...

- gh 不是秀场, 哗众取宠的行为,总是第一时间被 程序猿 识破而无视之.
- gh 只是工具, 努力为创新者们服务
- 我们进入 gh, 享受 gh, 必须的:
    + 创造出更好的物事
    + 来回报 gh 的这种无私

> 所以...

在一个几乎算无限辽阔的 cyber 空间中,
我们必须也只能扮演好自己,
这种所有行为都有 URI 来标定的电子证据生态中,
各种想学习赌神试图通过长期的习性伪造, 来传达一种自己所不具备的特性的尝试,
注定都是要失败的...

> (真的有人这么尝试过, 号称 gh 中提交 PR 最多的工程师...
结果发现基本都是单词和标点的修订, 立即上了所有公司的黑名单...
)



## 提问
~ 是的, GitQ 不是单向灌输, 双向交流才真诚

- 在 gh 中折腾什么最重要?
- 如果 gh 被和谐了, 你准备怎么作?
- 围绕 gh 还可能诞生什么产品/服务/平台?


## 是也乎

- 170911 init.

