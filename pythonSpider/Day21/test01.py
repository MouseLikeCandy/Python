# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/14 18:06
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
关键字yield
出现在函数中表示'推送'数据
'''

def fun(n):
    for i in range(n):      # range(5) => [0, 1, 2, 3, 4]
        print(f'执行了 {i + 1} 次循环')
        # 返回一个结果
        # return 关键字在函数中表示返回结果,一旦返回结果,函数就会弹栈
        # return i ** 2
        yield i ** 2    # 返回一个生成器对象

if __name__ == '__main__':
    # 调用函数
    # 如果调用函数,这个函数使用 yield 返回结果, 其实返回的是一个生成器对象
    # 生成器对象可以使用 python 中的 next() 内置函数从生成器对象中取出数值

    result = fun(5)     #需求: 希望fun()函数执行5次
    print(f'result = {result}')     # result = <generator object fun at 0x00000276B4D024F8>

    # 取值 next(iterator) 迭代器对象 / 遍历器对象(生成器是可以直接遍历的)
    value1 = next(result)
    print(f'value1 = {value1}')

    value2 = next(result)
    print(f'value2 = {value2}')

    value3 = next(result)
    print(f'value1 = {value3}')

    value4 = next(result)
    print(f'value2 = {value4}')

    value5 = next(result)
    print(f'value1 = {value5}')

    # value6 = next(result)
    # print(f'value2 = {value6}')

'''
使用yield报错输出位置可能在最上方,也可能在中间或后面
报错信息的输出和执行信息的输出不在同一条线程, 报错信息在子线程输出
 
yield关键字的作用: 在多线程中实现多个线程之间的配合
一条线程负责生成数据
另一条线程需要其生成的数据进行处理

scrapy 大量使用了yield关键字, scrapy用了多线程(异步执行)实现的
'''

'''
生成器相比一次列出所有内容的优势:
1) 更节省内存空间
2) 响应更迅速
3) 使用更灵活
'''