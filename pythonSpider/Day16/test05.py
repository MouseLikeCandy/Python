# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/20 19:00
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re
'''
需求: 隐藏手机号码的中间4位数字

# 手机号的规则因国家和地区而异。以下是一些常见的手机号规则：
# 手机号长度：大多数国家和地区的手机号长度为11位数，但也有例外。
# 国家代码：手机号通常包含一个国家代码，用于标识国家或地区。国家代码通常是一个或多个数字，例如中国的国家代码是+86。
# 区域代码：某些国家或地区可能还有区域代码，用于标识特定的地区或城市。区域代码通常是一个或多个数字，例如中国的区域代码是各省市的区号。
# 号码段：手机号的前几位数字通常被称为号码段，用于标识特定的移动网络运营商。不同的运营商可能有不同的号码段。
# 格式化：手机号通常会以一定的格式进行展示，例如在某些国家中，手机号可能以3-4-4的格式展示，即前三位、中间四位和后四位分别用短横线分隔。

# 手机号码编码规则是什么？
'''
if __name__ == '__main__':
    regEx = r'(1[34578]\d)(\d{4})(\d{4})'   # 将11位的手机号码分为了3组    # 当前规则为自定义的
    telphone = '需要的朋友们请联系: 13366285946'

    # 隐藏 - > 替换
    repl = r'\1****\3'   # \数字   表示引用正则中的指定组
    replacement = re.sub(regEx, repl, telphone)
    print(replacement)
