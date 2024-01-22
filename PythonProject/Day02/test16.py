# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/10 20:18
@Auth ： 异世の阿银
@File ：test16.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 作业：ｓｃｏｒｅ　０　－１００　　超范围的非法数值如何处理
score = int(input('亲，请输入您的成绩：'))
if score > 100 or score < 0:
    print(f'{score} 成绩无效')
elif score >= 80:
    print(f'{score} 成绩等级为优秀')
elif score >= 70:
    print(f'{score} 成绩等级为良好')
elif score >= 60:
    print(f'{score} 成绩等级为中等')
else:
    print(f'{score} 成绩等级为差')

print('程序继续向后执行...')
# 键盘录入某个月份，判断这个月份所属季节
# 3,4,5--》春
# 6,7,8--》夏
# 9,10,11--》秋
# 12,1,2--》冬
# 超范围如何处理
month = int(input('亲，请输入一个月份：'))
if month > 12 or month < 0:
    print(f'无效的月份')
elif 3 <= month <= 5:
    print(f'{month}月份为春季！')
elif 6 <= month <= 8:
    print(f'{month}月份是夏季！')
elif 9 <= month <= 11:
    print(f'{month}月份为秋季！')
else:
    print(f'{month}月份为冬季！')

# 让用户输入孩子的语文、数学、英语 成绩，判断孩子是否全部及格。
math = int(input('亲，请输入您的数学成绩：'))
english = int(input('亲，请输入您孩子的英语成绩：'))
chinese = int(input('亲，请输入您孩子的语文成绩：'))

if math < 0 or math > 100 or english > 100 or english < 0 or chinese > 100 or chinese <0:
    print(f'您孩子的语文、数学、英语成绩至少有一门成绩无效')
elif math >= 60 and english >= 60 and chinese >= 60:
    print(f'恭喜您！您孩子的三门成绩全部及格了！')
else:
    print('您孩子的语文、数学、英语成绩至少有一门不及格！')


# ATM取钱
balance = 1000
operate = int(input('欢迎使用ATM提款机，请选择您的操作：'))
if operate == 1:
    print('退卡成功！')
elif operate == 2:
    money = int(input('请输入取款金额：'))
    if money > 1000:
        print('余额不足！')
    else:
        print(f'本次取款金额为{money}元，有效余额{balance - money}元')
        print(f'是否进行其他操作？\n ')
else:
    print('非法操作！')