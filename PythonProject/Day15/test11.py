# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 14:52
@Auth ： 异世の阿银
@File ：test11.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
编码格式

思考: 计算机底层到底存储什么数据?  计算机底层只能存储0跟1. (计算机原理) -> 集成电路(晶体管 通电1/不通电0)  
# 摩尔定律: 每隔18个月, 计算机的存储和运行效率就会在原来计算机的基础上翻一倍.
#          每隔18个月, 使用1美元就可以买到比原来性能高一倍的计算机设备.
文本数据: 英文, 汉字...
非文本数据: 图片,音频,视频...      
A -> 65 -> 0100 0001
软件根据规则翻译0和1

转换的过程: 存储 -> 编码    读取 -> 解码

'''


# 对于汉字, 主要关注  GBK 和 UTF-8(通用)
str = '我爱你'

# 编码
encode1 = str.encode(encoding='gbk')
encode2 = str.encode(encoding='utf-8')

print(encode1)  # 6个字节, 一个汉字对应2个字节
print(encode2)  # 9个字节, 一个汉字对应3个字节

# 解码
decode1 = encode1.decode(encoding='gbk')
decode2 = encode2.decode(encoding='utf-8')

print(decode1)
print(decode2)


# 乱码: 编解码不一致
decode3 = encode1.decode(encoding='utf-8')
print(decode3)