from .conf import *


def get_first_header(filepath):
    """从 Markdown 文件中提取第一个标题"""
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('# '):
                return line[2:].strip()
    return None

def build_nav(directory, base_path=''):
    """递归扫描目录并构建导航结构"""
    nav = []
    for item in sorted(os.listdir(directory)):
        item_path = os.path.join(directory, item)
        rel_path = os.path.join(base_path, item)
        if os.path.isdir(item_path):
            index_file = os.path.join(item_path, 'index.md')
            sub_nav = build_nav(item_path, rel_path)
            if os.path.exists(index_file):
                header = get_first_header(index_file)
                if header and sub_nav:
                    # 直接使用 header 作为键，不手动加引号
                    nav.append({header: sub_nav})
                elif sub_nav:
                    nav.append({item: sub_nav})
            elif sub_nav:
                nav.append({item: sub_nav})
        elif item.endswith('.md') and item != 'index.md':
            header = get_first_header(item_path)
            if header:
                # 直接使用 header 作为键
                nav.append({header: rel_path})
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
        header = get_first_header(root_index)
        if header:
            # 直接使用 header 作为键
            nav.append({header: 'index.md'})
        else:
            nav.append({'index': 'index.md'})
    
    # 扫描子目录和文件
    for item in sorted(os.listdir(docs_dir)):
        item_path = os.path.join(docs_dir, item)
        if os.path.isdir(item_path):
            sub_nav = build_nav(item_path, item)
            if sub_nav:
                index_file = os.path.join(item_path, 'index.md')
                if os.path.exists(index_file):
                    header = get_first_header(index_file)
                    if header:
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