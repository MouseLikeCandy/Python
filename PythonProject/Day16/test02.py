# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/14 15:23
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
文本文件的复制
rt read text
# 人生苦短, 我用Python
'''

if __name__ == '__main__':
    # 上下文管理器对象open()
    # 1. 读取文件
    with open('test01.py', mode='rt', encoding='utf-8') as f_read:
        # 2. 写入文件
        with open('copy.py', mode='wt', encoding='utf-8') as f_write:
            # 3. 操作: 先读后写
            f_write.write(f_read.read())
