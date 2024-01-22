# -*- coding: utf-8 -*-
"""
@Time ： 2022/9/1 21:08
@Auth ： 异世の阿银
@File ：test06.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
定义一个Calculator 计算器类
'''


class Calculator:
    # 初始化方法
    def __init__(self, price, color):
        self.price = price
        self.color = color

    # 行为
    # 求和的功能 (任意数量的整型数值之和)
    # 没有使用self参数, 参数冗余, 浪费性能
    def get_sum(self, *args):
        # 位置参数 *args是什么类型的数据? 元组
        sum = 0
        for num in args:
            sum += num
        return sum


if __name__ == '__main__':
    # 1.创建一个Calculator对象
    calc = Calculator(9.9, '粉红色')
    # 2.求和
    sum = calc.get_sum(10, 20, 30, 40, 50)
    print(f'sum = {sum}')


'''
栈区(stack): 执行函数和方法
堆区(heap): 存储对象数据(每个对象数据独立)
代码区(code_zone): 存储模型数据(类模板)

# 通过堆区中的对象,找到该对象对应类型的执行方法.
# 中间环节经过了堆区, 一个对象经过堆区应该做什么? 取数据
# 没有用到self, 代码不合理

数据: 
1.对象数据 (每个对象独享自己的数据, 各个对象之间的数据互不影响)
2.类数据 (类数据在内存中仅有一份, 类数据被所有对象所共享)
行为:
1.对象行为 (对象访问自己数据的行为, 自己数据从哪来?从self来)
2.类行为 (类行为不能访问对象数据)
'''

# 思考: 程序来到堆区的目的是什么? 堆区中存储了什么?
# 回答: 堆区中仅仅存储了该对象所属的数据.

# 思考: 该代码在执行get_sum()行为的时候,有使用到堆区中该对象的数据吗?

# 既然一个行为是 '对象行为' self, 那么该行为中一定会使用该对象的数据.
# 如果没有使用对象数据, 那就不是对象行为

