'''
    一个.py就是一个模块，是一个用于学习模块创建和导入的文件
    import mudule                    导入整个模块
    import mudle as alias            导入并起别名 
    from module import name          导入特定函数/类
    from module import *             导入所有【不推荐】
'''

#1.导入整个模块（最清晰 推荐）
import utils
utils.load_config()
utils.count
utils.BaiZe('baize','26') #作为模块被导入时不执行

#2.从模块中导入特定功能（常用）
from utils import load_config
load_config()
from utils import BaiZe

#3.给模块或函数起别名
import utils as us











