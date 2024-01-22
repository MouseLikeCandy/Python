# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 20:03
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
需求：法老的金字塔
    *
   * *
  *   *
 *     *
*********
'''

# 1.定义一个变量， 记录行数
row = 5

# 2.外层循环，控制行数
for i in range(1, 6):   # [1, 2, 3, 4, 5]
    # 2.1 内层循环， 控制’空格‘的数量
    for j in range(row - i):
        print(' ', end='')
    # 2.2 内层循环， 控制‘星星’的数量

    for k in range(i * 2 - 1):
        # 3. 判断, 在第一行和最后一行，则正常输出
        if i == 1 or i == row:
            print('*', end='')
        else:
            # 星星输出的中间行
            # 说明： 只要第一颗星星和最后一颗星星输出，中间的星星全部使用空格代替。
            if k == 0 or k == i * 2 - 2:
                print('*', end='')
            else:
                print(' ', end='')
    print()
