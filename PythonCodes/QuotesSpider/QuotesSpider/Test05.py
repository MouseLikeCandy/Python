# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/7 20:10
@Auth ： 异世の阿银
@File ：Test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
:       建议该属性是什么类型
->      指定返回值类型
'''

def jack(name: str = "") -> bool:
    return False


print(jack(name="jack"))
