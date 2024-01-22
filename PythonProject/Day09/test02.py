# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/25 20:04
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
  函数传参
# 位置参数
# 格式: 位置参数 *args (arguments / parameters 参数)  args,params
'''


# 定义一个功能,实现'多个'整形数值的累加和
# def get_sum(num1, num2, num3, num4, num5):
#     sum = num1 + num2 + num3 + num4 + num5
#     return sum
# 10, 20, 30, 40, 50

# get_sum(1, 2, 3, 4, 5, 7)
# TypeError: get_sum() takes 5 positional arguments but 6 were given

# 可变参数 / 位置参数
# args -> arguments 形式参数    *args -> postional arguments 位置参数

def get_sum(*args):
    print(type(args), args)
    sum = 0
    # 遍历元祖
    for value in args:
        print(value)
        sum += value

    # 循环结束后返回结果
    return sum


# 调用函数
# 参数在传递过程中,会自动包装为元组
result = get_sum(10, 20, 30, 40)
print(f'result = {result}')

result = get_sum(10, 20, 30, 40, 8, 9, 6)
print(f'result = {result}')

# 定义一个列表数据
number_list = [10, 11, 12, 13, 14]
# result = get_sum(number_list)
result = get_sum(*number_list)
# TypeError: unsupported operand type(s) for +=: 'int' and 'list'
print(f'result = {result}')

# 说明: *number_list会将列表中的元素一一取出然后重新包装为元组类型数据传入给函数实现运算

# 定义一个元组类型的数据
number_tuple = (10, 11, 12, 13, 14, 15)
# result = get_sum(number_list)
result = get_sum(*number_tuple)
print(f'result = {result}')

# 内部包装, 提前包装没有用
