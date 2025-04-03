#import sys
#from pathlib import Path
## 动态获取项目根目录，假设项目根目录是当前文件的上两级
#current_file = Path(__file__).resolve()
#api_path = current_file / "api"  # / "lib"
#sys.path.append(str(api_path))

# 导入模块
from inv.conf import *
#from lib.settings import CFG, LOG

from inv.mkdocs import *
from inv.latestor import *

#   support stuff func.
def cd(c, path2, echo=True):
    os.chdir(path2)
    if echo:
        print("\n\t crt. PATH ===")
        c.run("pwd")
        c.run("echo \n")

@task
def ver(c):
    """echo crt. verions"""
    print(
        f"""{CFG.project}
    ~> {CFG.desc} <~
    ~> version   {CFG.version} <~
    ~> powded by {CFG.author} <~
    ~> feedback to {CFG.feedback} <~
    ~> all right reserved: {CFG.license} <~
    """
    )
    # print(CFG.output)
    return None
    # 使用 sys.modules 获取当前加载的所有模块对象
    loaded_modules = list(sys.modules.keys())
    # 打印所有加载的模块对象
    print(
        f"""
    loaded_modules: {len(loaded_modules)}
        """
    )
    return None
    for i in loaded_modules:
        print(f"{i}")



@task
def upd(c):
    """update all the stuff"""
    flush(c)
    reidx(c)
    return None
