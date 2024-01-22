# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/14 15:29
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
非文本文件的复制
rb read binary  读取二进制文件, 没有编码
# 图片中的jpg是一个图片压缩的技术
'''

if __name__ == '__main__':
    # 1. 读取文件
    # with open(r'D:\Edge浏览器下载\1.jpg', mode='rb', encoding='utf-8'):
    with open(r'D:\Edge浏览器下载\1.jpg', mode='rb') as f_read:
        # 2. 写入文件
        with open(r'D:\Edge浏览器下载\1copy.jpg', mode='wb') as f_write:
            # 3. 操作
            f_write.write(f_read.read())

