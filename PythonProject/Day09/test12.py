# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/25 21:47
@Auth ： 异世の阿银
@File ：test12.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
递归函数应用
问题: 有5个人坐在一起, 
问第5个人多少岁?他说比第四个人大两岁.
问第4个人多少岁?他说比第三个人大两岁.
问第3个人多少岁?他说比第二个人大两岁.
问第2个人多少岁?他说比第一个人大两岁.
问第1个人多少岁?他说他10岁.
请问第5个人多大?
'''
def getAge(n):
    if n == 1:
        # 最后一个人,有返回结果
        return 10
    else:
        # 不是最后一个人, 比上一个人大两岁
        return getAge(n-1) + 2


if __name__ == '__main__':
    age = getAge(5)
    print(age)