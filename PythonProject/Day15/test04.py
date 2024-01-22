# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/13 14:02
@Auth ： 异世の阿银
@File ：test04.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''

'''
import datetime, time

now = datetime.datetime.today()
print(now)

# timetuple()
# now.timetuple() =
# time.struct_time(tm_year=2023, tm_mon=5, tm_mday=13, tm_hour=14,
#                   tm_min=5, tm_sec=28, tm_wday=5, tm_yday=133, tm_isdst=-1)
# 返回的结果类似C语言的结构体
print(f'now.timetuple() = {now.timetuple()}')

# 1683958081.0
timestamp = time.mktime(now.timetuple())
print(f'timestamp = {timestamp}')

# 一天前/一个月前是哪个日期?
r = datetime.datetime.fromtimestamp(1683958081.0 - 60*60*24*30)
print(r)