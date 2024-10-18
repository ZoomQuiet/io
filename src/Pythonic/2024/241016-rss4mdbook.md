# 如何给 mdBook 挂上 RSS?
> Rust 开发的 SSG 引擎...

## background
经网友支持, 开通了 [Follow](https://follow.is/#features),
然后, 就遇到第一个问题:

[ZoomQuiet.io](https://zoomquiet.io/)

第 N 次重构的私人网站,
由 [mdBook](https://rust-lang.github.io/mdBook/index.html)
生成, 并没有 RSS 源提供给 Follow 哪...

## goal

- 简洁, 快速的追加 RSS.xml 给 mdBook 生成的网站
- 可以追加到 gh-actions 中, 以便其它人协作时, 不用折腾本地环境

## logging

### rss4mdbook.rs
> 其实原先解决过这个问题的

mdBook 是 Rust 社区进行文档组织发布的标准选择,
其地位等于 Python 社区中:

- Markdown 发明之前的 [Sphinx](https://www.sphinx-doc.org/en/master/examples.html)
- Markdown 发明之后的 [GettMkDocs](https://www.mkdocs.org/getting-started/)

相比其它 [SSG/静态站点生成器](https://www.cloudflare.com/zh-cn/learning/performance/static-site-generator/)
这类生成器, 最大的好处就在:

- 不像 Jekyll 之类, 要求在所有 Markdown 文章的顶部, 必须提供一组 meta 信息
    - 以便 SSG 解析使用
    - 而这些文本和内容无关, 完全是面向编译器工具的
    - 非常分散注意力, 也破坏了 Markdown 文本的纯粹性
- 而是, 约定将 .md 文件放在哪个指定目录中就好
    - SSG 引擎将自动扫描并根据内置规则, 完成良好的编译和发布

而 mdBook 是由 Rust 开发的,
其网页生成速度是所有 SSG 中最快的;

当初就是为了学习 Rust 而专门安装使用过 mdBook 来发布相关学习笔记:

- [锈<周刊::2024> \- 锈周刊 \-> Weekly :: China<Rustaceans>](https://weekly.rs.101.so/)
- [成为 Rustacean - be Rustaceans](https://rs.101.so/)

当然也发现没有 RSS 生成的问题, 也顺手用 Rust 来编写工具解决:

- [rss4mdbook - crates.io: Rust Package Registry](https://crates.io/crates/rss4mdbook)
- 在本地也组织有 `pub.sh` 来自动完成网站编译,扫描生成RSS,注入,并提交发布
- 问题在:
    - 用 Rust 完成, 本地安装编译, 有点儿复杂, 其它人难以使用
    - 用 Rust 编写, 如果有什么功能变化, 修改也比较困难
    - 而且, 使用这个工具, 暂时只能完全在本地配置好执行环境, 然后使用发布脚本来完成, 如果本地环境因为各种环境失效, 自己也无法简单的立即恢复 RSS 生成.

### gh-actions
> GitHub 这么良心的提供了免费微服务渠道, 必须得大力薅

和 GPT 们合作, 快速撸了个脚本: [tasks.py](https://github.com/zoom-quiet/io/blob/main/tasks.py)

- 使用 Invoke 作为 CLI 指令框架
- 调用 `inv gen` 指令自动完成:
    - 读取 `SUMMARY.md` 网站总索引文件
    - 逐一拼装文件路径, 读取所有应该发布的 .md 文件内容
    - 使用 markdown 模块编译为 html , 作为文章内容编组为 RSS 的条目信息
    - 再根据所有文件的系统属性, 以更新时间排序, 只发布最新 14 个文章
    - 最终将所有合理的内容, 输出为 `rss.xml` 文档

接下来, 重构 GitHub 仓库中的 `.github/workflow` 目录里的 Actions 脚本,
才发现又一坑:

- 原先是分为 `build.yaml` 以及 `pages.yaml` 两个构建脚本的
- 通过 `dawidd6/action-download-artifact@v3` 这种中间行为进行成果交互

```yaml
...
      - name: Download artifact
        id: download-artifact
        uses: dawidd6/action-download-artifact@v3
        with:
          name: book-and-rss
          path: book/
          workflow: build.yml
```

想在 `mdbook` 指令之后, 追加 `inv` 指令还好说,
但是, 如何将生成的 `rss.xml` 文件也合理的传递到 `pages.yaml` 的行为流中,
完全出乎意料;

质问了 GPT 们很久, 也无法在 gh-actions 中看到流畅的交接过程;

### CF-Pages
> 是的, 互联网菩萨 Cloudflare 也有 Pages 服务, 而且简洁无比, 值得上

结合之前的折腾 **"[迁移 gh-pages 到 Cloudflare](241014-cf-pages.html)"** 经验,
也使用 `gh-pages` 分支, 作为工作成果的中间缓存区,
再配置 `CF-Pages` 服务, 对应复制发布就好, 不用在 Cloudflare 端在进行任何编译工作;

进一步的经验:

- gh-actions 的 workflow 机制还远没成熟
- 不同的文件, 代表要拉起不同的虚拟机, 不同 Docker 之间的文件传递, 涉及太多安全问题, 远没那么简洁可以配置明白
- 所以, 能不拆分, 就别折腾
- 将编译和发布(其实就是推送到指定仓库分支中)行为,在一个 `.yaml` 文件中完成即可

参考: [build-and-deploy.yml](https://github.com/zoom-quiet/io/blob/main/.github/workflows/build-and-deploy.yml)

实用技巧只有:

```yaml
...
      # Step 6: Check and prepare files for deployment
      - name: Prepare deployment files
        run: |
          echo "Listing generated files in book/"
          ls -al book/
          echo "Copy RSS and other files to book directory"
          cp -v rss.xml book/
          cp -v CNAME book/
          cp -v .nojekyll book/
          mv -v book ../

      # Step 7: Checkout the gh-pages branch
      - name: Checkout gh-pages branch
        uses: actions/checkout@v4
        with:
          ref: gh-pages

      # Step 8: Deploy to gh-pages branch
      - name: Deploy to gh-pages
        run: |
          rm -rfv *
          cp -rv ../book/* .
          ls -al ./
          git config --local user.name "github-actions[bot]"
...
          git push origin gh-pages
```

- 通过 `ls -al book/` 这种列显指令, 可以在 Actions 日志中, 看到阶段成果, 以便确认调试进展
- 通过 `cp -v rss.xml book/` 之类的指令, 将需要注入到目标静态网站目录中的额外文件都事先复制进去
- 然后, 将 `book` 这种经济计划成果目录, 直接移动到工作目录, 也就是微服务中的仓库复本目录
    - 再切换分支, 这样不会引发冲突
    - 现在, 清除所有文件
    - 最后, 从移到外层目录的成果目录中, 复制所有文件进来
    - 完成完备的更新
    - 现在进行标准的 git 提交+推送 行为就完成了自动编译
- 这时, `CF-Pages` 就会被触发, 自动同步 `gh-pages` 分支中的所有文件,并发布到约定域名中;
    - 是的 Cloudflare 本身也有 DNS 服务功能
    - 就不用像 GitHub 那样用 `CNAME` 之类的交接文案来驱动后端其它服务进行域名绑定
    - 而是直接在控制界面中简单的说明, Cloudflare 就将自动生成配置, 完成检验, 并上线最新域名解析

### 发布 RSS

最后的最后, 别忘记发布 `rss.xml` 到网站界面中;
俺是修改 `index.hbs` 模板文件,追加个标准 HTML 链接:

     <a href="/rss.xml"><b>RSS</b>

以便让自己以及各种工具知道网站拥有 RSS 源;


## refer.
[Follow](https://follow.is/#features)


- [使用 follow 重塑我的信息输入系统 - 少数派](https://sspai.com/post/91283)
- [rust-lang/mdBook: Create book from markdown files. Like Gitbook but implemented in Rust](https://github.com/rust-lang/mdBook)
    - [rss4mdbook - crates.io: Rust Package Registry](https://crates.io/crates/rss4mdbook)
- [Sphinx — Sphinx documentation](https://www.sphinx-doc.org/en/master/examples.html)
- [Getting Started - MkDocs](https://www.mkdocs.org/getting-started/)

## tracing

- 241018 DAMA .init

