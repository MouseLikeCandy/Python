# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/15 6:58
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re
'''
练习: 验证手机号码
'''

if __name__ == '__main__':
    # 手机号码规则 :
    # 1. 长度必须是11位
    # 2. 第一位只能是数字1
    # 3. 第二位可以是3, 4, 5, 7, 8
    # 4. 从第三位开始可以是 0-9
    regEx = r'^1[34578]\d{9}$'
    phone_number = '13366285946'
    matcher = re.match(regEx, phone_number)     # 从头开始匹配 (有限制)
    if matcher:
        # 匹配成功
        print(matcher.group())
    else:
        print('手机号码非法!')