# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/9 21:41
@Auth ： 异世の阿银
@File ：test14.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
双分支结构
注意冒号
if 。。。 else ...
如果。。。 否则。。。
需求：如果你儿子的成绩及格了，就奖励他，否则，打他。

'''

# 1.定义变量,接收用户的输入数据
score = int(input('亲，请输入您儿子的成绩：'))

# 2.双分支结构判断
if score >= 60:
    print('及格')
    print('恭喜你，你儿子真棒，')
else:
    print('不及格')
    print('很抱歉不及格')

print('程序继续向下执行...')


# 缩进快捷键
# 向右缩进：Tab
# 向左缩进：SHIFT + TAB
