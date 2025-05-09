
from .conf import *



def extract_nav_entries(nav):
    """递归解析 mkdocs nav 配置，提取所有文档条目"""
    entries = []
    for item in nav:
        if isinstance(item, dict):
            for title, value in item.items():
                if isinstance(value, str):
                    entries.append({'title': title, 'path': value})
                elif isinstance(value, list):
                    entries.extend(extract_nav_entries(value))
        elif isinstance(item, list):
            # 处理可能的列表结构（根据实际配置调整）
            entries.extend(extract_nav_entries(item))
    return entries


@task
def reidx(c,limit=7, base_url=""):
    """replace index.md for latest upgrade posts.."""

    # 解析 SUMMARY.md 文件，提取章节和对应链接
    with open(CFG.cfyml, 'r', encoding='utf-8') as f:
        mkdocs_config = yaml.safe_load(f)


    nav_entries = extract_nav_entries(mkdocs_config.get('nav', []))
    filtered_entries = []
    
    for entry in nav_entries:
        path = entry['path']
        title = entry['title']
        filename = os.path.basename(path)
        
        # 跳过索引文件
        if filename.lower() in {'index.md', 'readme.md'}:
            continue
        
        # 提取时间戳 (YYYYMMDD)
        timestamp_match = re.search(r'\d{8}', filename)
        if not timestamp_match:
            continue
        
        timestamp_str = timestamp_match.group()
        try:
            # 解析时间戳并设置时区
            pub_time = datetime.strptime(timestamp_str, "%Y%m%d")
            pub_time = pub_time.replace(tzinfo=timezone(timedelta(hours=8)))
        except ValueError:
            continue
        
        # 生成页面链接
        #page_url = os.path.join(base_url, path.replace('.md', '.html')).replace('\\', '/')
        page_url = os.path.join(base_url, path.replace('.md', '/')).replace('\\', '/')
        filtered_entries.append({
            'title': title,
            'url': page_url,
            'time': pub_time
        })
    
    # 按时间降序排序并取前 limit 个
    sorted_entries = sorted(filtered_entries, key=lambda x: x['time'], reverse=True)[:limit]
    
    # 生成 Markdown 列表
    #md_list = [f"+ [{entry['title']}]({entry['url']})" for entry in sorted_entries]
    #md_content = "\n".join(md_list)
    #LOG.debug(f"appd_md:\n{md_content}")
    # 生成 HTML 列表
    md_list = [f"+ <a href='{entry['url']}'>{entry['title']}</a>" for entry in sorted_entries]
    md_content = "\n".join(md_list)
    LOG.debug(f"appd_md:\n{md_content}")

    _replace_md(c, md_content)

def _replace_md(c, 
        new_content, 
        mdfile="docs/index.md",
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
