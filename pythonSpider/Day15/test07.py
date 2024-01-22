# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/15 7:04
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re


if __name__ == '__main__':
    '''
    电子邮箱的@符号固定的,前面的是用户名,后面的一般都是公司的域名信息.
    530180782@qq.com
    toocle01@netsun.com
    chuangling@chuangling.net
    gyby5911@alibaba.com.cn
    zpm6480@mail.hz.zj.cn
    Zhangsan@163.com
    1. 用户名可以是数字,字母,和下划线.
    2. 公司域名可以是数字,字母,和下划线
    '''
    # 笼统的邮箱匹配规则
    regEx = r'\w+@\w+(\.\w+){1,3}'      # 组 (\.\w+)
    email = 'zpm6480@mail.hz.zj.cn'

    matcher = re.match(regEx, email)
    if matcher:
        print(matcher.group())
    else:
        print('邮箱非法')