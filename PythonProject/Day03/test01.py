# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/11 20:02
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 判断小明的语文，数学，英语成绩是否全部合格

# 注意：变量命名时，一定要小写开头

chinese = int(input('亲，请输入您的语文成绩：'))
math = int(input('亲，请输入您的数学成绩：'))
english = int(input('亲，请输入您的英语成绩：'))   # 应该累死

# 判断分支结构
if chinese >=60 and math >= 60 and english >= 60:
    print("恭喜，全部及格")
else:
    print('很抱歉，还需继续努力')

print('程序继续向后执行。。。')
