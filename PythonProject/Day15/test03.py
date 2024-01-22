# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 13:23
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
datetime 模块
1.4个主要的类
    date 处理年月日
    time 处理时分秒
    datetime 处理日期 + 时间
    timedelta 处理时段(时间间隔)
2. 常用函数 / 方法
    datetime.date.today()
    datetime.datetime.now()
    datetime.datetime.isoformat() 标准时间(日期 T 时间)
3. 两个时间相减就使用 timedelta
'''
import datetime
# from datetime import datetime
# 获取今天的日期
today = datetime.datetime.today()
# datetime.today()
print(f'today = {today}')

# 获取当下的具体日期和时间
today = datetime.date.today()
print(f'today = {today}')

# 获取当下的具体日期和时间
now = datetime.datetime.now()
print(f'now = {now}')

print(now.isoformat())

# 可以使用strftime (string format time 字符串格式化时间) 自定义格式
import locale
locale.setlocale(locale.LC_CTYPE, 'Chinese')
f = now.strftime('%Y年%m月%d日 %H时%M分%S秒')
print(f)

# 可以使用 strptime (string parse time 字符串解析时间) 将字符串解析一个时间对象
datetime_str = '2023年05月13日 13:42:25'
parse_date = datetime.datetime.strptime(datetime_str, '%Y年%m月%d日 %H:%M:%S')
print(type(parse_date))
print(parse_date)

