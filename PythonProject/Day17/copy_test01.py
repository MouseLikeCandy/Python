# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/15 19:58
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
os模块     : operating system, 主要用于对单个文件进行操作
Shutil模块 : shell utilities , 命令工具模块, 该模块拥有许多文件/文件夹操作功能.包括复制,移动,重命名,删除...
'''
import os
if __name__ == '__main__':
    # command 命令 notepad.exe  记事本   mspaint(micro soft paint) 微软画板  calc.exe计算器
    # exe -> executable 可执行的
    os.system(r'D:\CommonSoft\WeChat\WeChat.exe')
    os.system('mspaint.exe')
    os.system('notepad.exe')
    os.system('calc.exe')

