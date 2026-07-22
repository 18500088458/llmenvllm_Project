import sys
import os

print(sys.path)

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

print(sys.path)

import config
config.configInit()

#子目录脚本无法导入根目录下的模块时使用sys.path
# print(sys.path)

def textsplit():
    print("我是文本分割工具")
