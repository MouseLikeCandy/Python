# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/20 19:13
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re
'''
需求: 替换叠词
'''
if __name__ == '__main__':
    regEx = r'\.'   # \. 表示单独的点
    repl = ''   # 空字符串
    str = '我我我我我......要要要要要要要要要要要要要要要......学学学....Python.编程'

    # 第一次替换: 去掉 .
    replacement = re.sub(regEx, repl, str)
    print(replacement)

    # 再次实现替换: 去重
    regEx = r'(.)\1+'  # . 表示除了换行之外的任意单个字符  (.)表示一个字符就是一个组, \1表示引用前面那个组, +表示至少两个或以上的相同字符
    repl = r'\1'        # 替换为引用一次
    words = re.findall(regEx, replacement)
    for word in words:
        print(f'{word} 出现多次')
    replacement1 = re.sub(regEx, repl, replacement)
    print(replacement1)

    regEx = r'(.)\1\1\1+'
    replacement2 = re.sub(regEx, repl, replacement)
    print(replacement2)