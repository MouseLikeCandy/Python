# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：PLAYWRIGHT_cmd.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/19 15:58 
"""
import os

# playwright
# 先手动操作一遍，然后playwright会按之前的动作生成一系列操作的代码
os.system('playwright codegen -o E:\Python\BookPython3\Chapter7JavaScript动态渲染页面爬取\PLAYWRIGHT_script.py -b webkit')

print('playwright codegen -o PLAYWRIGHT_script.py -b webkit')
