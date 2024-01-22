# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 9:33
@Auth ： 异世の阿银
@File ：module4.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
# from 包名.模块名 import *
# from . import *           # 不常用
'''
# 导入 Day14.module1 模块下的所有内容
# from Day14.module1 import *

# 这是导入 Day14 包下的所有内容吗? 好像什么都没导入
# 需要配合该包下的__init__.py文件使用. 需要定义导入哪些模块 __all__ = ['module1']
from Day14 import *
# from . import *   # 不等于上一条语句


if __name__ == '__main__':
    print(module1.x)
    module1.method_one()
    # module2.method_one()