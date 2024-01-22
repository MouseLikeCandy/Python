# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 13:05
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
calendar 日历模块
跟日历相关的若干函数和类, 可以形成文本形式的日历
常用函数:
1.年
calendar.calendar(<年>)
calendar.prcal(<年>)
2.月
calendar.month(<年>, <月>)
calendar.prmonth(<年>, <月>)   输出

'''


import calendar

print(dir(calendar))

help(calendar.calendar)

month = calendar.month(2023, 5)
print(type(month))
print(month)

# print month
calendar.prmonth(2023, 5)

# 输出全年的日历
year = calendar.calendar(2023)
print(year)

calendar.prcal(2023)

# 闰年
leap_year = calendar.isleap(2023)
print(leap_year)

"""
        Return a matrix representing a month's calendar.
        Each row represents a week; days outside this month are zero.
        matrix矩阵 [[], [], [], []]
"""
r = calendar.monthcalendar(2023, 5)
print(r)

range = calendar.monthrange(2023, 2)
# (2, 28)   2: 表示本月从星期三开始, 28: 表示本月有28天
print(range)


weekday = calendar.weekday(2023, 2, 21)
print(weekday)