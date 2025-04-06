from .conf import *


def get_first_header(filepath):
    """从 Markdown 文件中提取第一个标题"""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('# '):
                return line[2:].strip()
    return None

def extract_date_from_filename(filename: str) -> datetime | None:
    """从文件名中提取日期，前8位为 yyyymmdd 格式"""
    if len(filename) >= 8 and filename[:8].isdigit():
        try:
            return datetime.strptime(filename[:8], '%Y%m%d')
        except ValueError:
            return None
    return None

def build_nav(directory: str, base_path: str = '') -> list:
    """递归扫描目录并构建导航结构"""
    nav = []
    subdirs_with_years = []  # 存储含年份的子目录 (year, subdir)
    other_subdirs = []       # 存储其他子目录
    files_with_dates = []    # 存储含日期的文件
    other_files = []         # 存储其他文件

    # 遍历目录中的所有文件和子目录
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        rel_path = os.path.join(base_path, item)
        if os.path.isdir(item_path):
            # 检查子目录是否为纯数字（视为年份）
            if item.isdigit():
                try:
                    year = int(item)  # 将子目录名转换为整数年份
                    subdirs_with_years.append((year, item))
                except ValueError:
                    other_subdirs.append(item)
            else:
                other_subdirs.append(item)
        elif item.endswith('.md') and item != 'index.md':
            # 处理 Markdown 文件
            if date := extract_date_from_filename(item):
                files_with_dates.append((date, item, rel_path))
            else:
                other_files.append((item, rel_path))

    # 对含年份的子目录按年份倒序排序
    # 使用 reverse=True 确保年份从大到小（如 25 在 24 之前）
    subdirs_with_years.sort(key=lambda x: x[0], reverse=True)

    # 处理含年份的子目录
    for _, subdir in subdirs_with_years:
        sub_nav = build_nav(os.path.join(directory, subdir), os.path.join(base_path, subdir))
        if sub_nav:
            index_file = os.path.join(directory, subdir, 'index.md')
            if os.path.exists(index_file):
                if header := get_first_header(index_file):
                    nav.append({header: sub_nav})
                else:
                    nav.append({subdir: sub_nav})
            else:
                nav.append({subdir: sub_nav})

    # 处理其他子目录，按名称升序排序
    # 使用 sorted 保持非年份子目录的字母顺序
    for subdir in sorted(other_subdirs):
        sub_nav = build_nav(os.path.join(directory, subdir), os.path.join(base_path, subdir))
        if sub_nav:
            index_file = os.path.join(directory, subdir, 'index.md')
            if os.path.exists(index_file):
                if header := get_first_header(index_file):
                    nav.append({header: sub_nav})
                else:
                    nav.append({subdir: sub_nav})
            else:
                nav.append({subdir: sub_nav})

    # 对含日期的文件按日期倒序排序
    # 保持文件按时间从新到旧排列
    files_with_dates.sort(key=lambda x: x[0], reverse=True)

    # 添加含日期文件到 nav
    for _, _, rel_path in files_with_dates:
        if header := get_first_header(os.path.join(directory, rel_path.split('/')[-1])):
            nav.append({header: rel_path})

    # 添加其他文件到 nav，按名称升序排序
    for item, rel_path in sorted(other_files):
        if header := get_first_header(os.path.join(directory, item)):
            nav.append({header: rel_path})

    # 处理当前目录的 index.md，插入到导航开头
    index_path = os.path.join(directory, 'index.md')
    if os.path.exists(index_path):
        nav.insert(0, os.path.join(base_path, 'index.md'))

    return nav

def _build_nav(directory: str, base_path: str = '') -> list:
    """递归扫描目录并构建导航结构"""
    nav = []
    files_with_dates = []
    other_files = []

    # 遍历目录中的所有文件和子目录
    for item in sorted(os.listdir(directory)):
        item_path = os.path.join(directory, item)
        rel_path = os.path.join(base_path, item)
        if os.path.isdir(item_path):
            # 递归处理子目录
            if sub_nav := build_nav(item_path, rel_path):
                index_file = os.path.join(item_path, 'index.md')
                if os.path.exists(index_file):
                    if header := get_first_header(index_file):
                        nav.append({header: sub_nav})
                    else:
                        nav.append({item: sub_nav})
                else:
                    nav.append({item: sub_nav})
        elif item.endswith('.md') and item != 'index.md':
            # 处理 Markdown 文件
            if date := extract_date_from_filename(item):
                files_with_dates.append((date, item, rel_path))
            else:
                other_files.append((item, rel_path))

    # 对包含日期的文件按日期倒序排序
    files_with_dates.sort(key=lambda x: x[0], reverse=True)

    # 添加含日期文件到 nav
    for _, _, rel_path in files_with_dates:
        if header := get_first_header(os.path.join(directory, rel_path.split('/')[-1])):
            nav.append({header: rel_path})

    # 添加其他文件到 nav
    for item, rel_path in sorted(other_files):
        if header := get_first_header(os.path.join(directory, item)):
            nav.append({header: rel_path})

    # 处理当前目录的 index.md
    index_path = os.path.join(directory, 'index.md')
    if os.path.exists(index_path):
        nav.insert(0, os.path.join(base_path, 'index.md'))

    return nav


@task
def flush(c):
    """扫描 docs 目录并更新 MkDocs 的 nav 配置"""
    _yaml = CFG.cfyml  # 'mkdocs.yml'，从配置中获取 YAML 文件路径
    docs_dir = CFG.docs  # 'docs'，从配置中获取文档目录路径
    nav = []

    # 处理根目录的 index.md
    root_index = os.path.join(docs_dir, 'index.md')
    if os.path.exists(root_index):
        if header := get_first_header(root_index):
            nav.append({header: 'index.md'})
        else:
            nav.append({'index': 'index.md'})

    # 扫描子目录和文件
    for item in sorted(os.listdir(docs_dir)):
        item_path = os.path.join(docs_dir, item)
        if os.path.isdir(item_path):
            if sub_nav := build_nav(item_path, item):
                index_file = os.path.join(item_path, 'index.md')
                if os.path.exists(index_file):
                    if header := get_first_header(index_file):
                        nav.append({header: sub_nav})
                    else:
                        nav.append({item: sub_nav})
                else:
                    nav.append({item: sub_nav})

    # 读取现有配置
    with open(_yaml, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    # 更新 nav 配置
    config['nav'] = nav
    
    # 写回配置文件
    with open(_yaml, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, allow_unicode=True, sort_keys=False)
    
    print("MkDocs nav 配置已更新。")