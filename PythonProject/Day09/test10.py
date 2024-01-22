# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/25 21:25
@Auth ： 异世の阿银
@File ：str_split.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
阶乘:5!
5! = 5 * 4 * 3 * 2 * 1
递归思想:
将一个大问题逐步分解为规模更小的相似问题.

需求: 求5的阶乘.
递归: 5! 不知道结果是多少,但我知道5! = 5 * 4!
递归: 4! 不知道结果是多少,但我知道4! = 4 * 3!
递归: 3! 不知道结果是多少,但我知道3! = 3 * 2!
递归: 2! 不知道结果是多少,但我知道2! = 2 * 1!
递归: 1! 这里是有结果的,因为1! = 1,这里就结束了

说明:没有函数就无法书写递归调用
'''
# 循环思想
if __name__ == '__main__':
    result = 1
    for i in range(5, 0, -1):
        result *= 1
    print(f'result = {result}')


# 递归思想
# 定义一个获取阶乘结果的函数
def get_factorial(n):
    # 判断
    if n == 1:
        return 1
    else:
        return n * get_factorial(n - 1)


# 调用递归函数
result = get_factorial(5)
print(f'result = {result}')
