
@task
def gen(c,limitmes=14):
    """echo crt. verions"""

    # 1. 定义网站 URL 和 SUMMARY.md 文件位置
    base_url = CFG.buri #'https://mybooksite.com/'
    summary_md_path = f'{CFG.rpath}/{CFG.summ}'

    # 2. 初始化 RSS 生成器
    fg = FeedGenerator()
    fg.id(base_url)
    fg.title('ZoomQuiet.io RSS')
    fg.subtitle('lasted updates from ZoomQuiet.io')
    fg.link(href=base_url, rel='self')
    fg.author( {'name':'Chaos42DAMA','email':'askDAMA@googlegroups.com'} )
    fg.language('zh-CN')
    fg.description(f'RSS feed contains the latest {CFG.last} updates items from ZoomQuiet.io gen. by mdBook|{CFG.follow}')  # 添加全局描述

    # 3. 定义存储条目的列表
    entries = []

    # 4. 解析 SUMMARY.md 文件，提取章节和对应链接
    with open(summary_md_path, 'r', encoding='utf-8') as f:
        summary_content = f.read()

    # 5. 使用正则表达式解析 markdown 链接
    link_pattern = re.compile(r'\[(.*?)\]\((.*?)\)')

    for match in link_pattern.findall(summary_content):
        title = match[0]  # 链接文本 (页面标题)
        relative_path = match[1].strip()  # 链接地址 (相对路径)
        
        # 处理相对路径，生成完整的页面 URL
        page_url = os.path.join(base_url, relative_path).replace('\\', '/')
        #file_path = os.path.join('./src', relative_path).replace('\\', '/')
        file_path = f'./src/{relative_path}'
        #LOG.info(f"base_url:{base_url}")
        #LOG.info(f"relative_path:{relative_path}")
        #LOG.info(f"page_url:{page_url}")
        #LOG.debug(f"parse:{file_path}")
        #LOG.info(f".md:{page_url.split('/')[-1]}")
        _mdfile = page_url.split('/')[-1]
        #LOG.debug(f"parse:{file_path}")
        if _mdfile == "README.md":
            #LOG.info(f"IGNORE README.md in \n{file_path}")
            continue
        elif len(_mdfile) <= 10:
            #20241109.md
            LOG.info(f"IGNORE file name too short")
            continue
        elif _mdfile[:8].isdigit():
            #LOG.info(f"parse {title} date:{_mdfile[:8]}")
            published_time = datetime.strptime(_mdfile[:8], "%Y%m%d")
            # 设置时区为北京时间 (UTC+8)
            beijing_timezone = timezone(timedelta(hours=8))
            published_time = published_time.replace(tzinfo=beijing_timezone)
            #LOG.info(f"parsed:{published_time}")
            with open(file_path, 'r', encoding='utf-8') as md_file:
                markdown_content = md_file.read()
            # 使用 markdown 库将 Markdown 转换为 HTML
            html_content = markdown.markdown(markdown_content)

            # 将条目信息存入字典
            entry_data = {
                'id': relative_path,
                'title': title,
                'link': page_url,
                'published': published_time,
                'description': f'ESSAY: {title} - Last updated(at){published_time.isoformat()}',
                'content': html_content,
            }
            
            # 将条目添加到列表中
            entries.append(entry_data)

        else:
            LOG.info(f"IGNORE all OTHERS files:\n{_mdfile}")
            continue
    

    #return None
    # 6. 对条目按发布时间排序，获取最近的 20 个条目
    reverse_entries = sorted(entries, key=lambda e: e['published'], reverse=True)[:limitmes]
    sorted_entries = sorted(reverse_entries, key=lambda x: x['published'], reverse=False)
    
    # 7. 将排序后的条目添加到 RSS feed 中
    for entry_data in sorted_entries:
        LOG.debug(f"add_entry:\n{entry_data['id']}:{entry_data['published']}")
        entry = fg.add_entry()
        entry.id(entry_data['id'])
        entry.title(entry_data['title'])
        entry.link(href=f"{entry_data['link'][:-3]}.html")
        entry.published(entry_data['published'].isoformat())
        entry.description(entry_data['description'])  # 添加条目的 description
        entry.content(entry_data['content'], type='html')  # 添加 markdown 文件的内容

    # 8. 生成 RSS 文件
    fg.rss_file('rss.xml')

    LOG.info('RSS feed 生成ed: rss.xml')
    LOG.info(f"total {len(sorted_entries)} entries in RSS feed")
    
    appd_md = []
    for entry_data in reverse_entries:
        #LOG.debug(f"{entry_data['id']}:{entry_data['title']}:{entry_data['link'][:-3]}.html")
        appd_md.append(f"+ [{entry_data['title']}]({entry_data['link'][:-3]}.html)")
    LOG.debug(f"appd_md:\n{appd_md}")
    _replace_md(c, "\n".join(appd_md))

def _replace_md(c, 
        new_content, 
        mdfile="src/README.md",
        mkstart="> :::..",
        mkend="> ..:::",
        ):
    """假设我们有一个Markdown文件md_template.md，内容如下：
    我们约定在以下两行之间的内容将被替换
    > ::..
    这是要被替换的内容
    > ..::
    """

    # 读取Markdown文件
    with open(mdfile, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # 初始化一个空列表来存储更新后的内容
    updated_lines = []

    # 标志位，用于判断是否在替换区域内
    in_replacement_area = False

    # 遍历每一行，进行替换
    for line in lines:
        if line.strip() == mkstart:
            # 如果遇到开始标志行，设置标志位为True，并添加新内容
            in_replacement_area = True
            updated_lines.append(line)
            updated_lines.append("\n")
            updated_lines.append("\n")
            updated_lines.append(new_content)
            updated_lines.append("\n")
            updated_lines.append("\n")
            continue
        elif line.strip() == mkend:
            # 如果遇到结束标志行，设置标志位为False，并跳出循环
            in_replacement_area = False
            updated_lines.append(line)
            continue

        if not in_replacement_area:
            # 如果不在替换区域内，直接添加原始内容
            updated_lines.append(line)
        else:
            # 如果在替换区域内，跳过添加
            continue

    # 将更新后的内容写入文件
    with open(mdfile, "w", encoding="utf-8") as file:
        file.writelines(updated_lines)
    #LOG.info(f"update {mdfile} within:\n{mkstart}\n...\n{mkend}\n\tdone!")
