# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 19:28
@Auth ： 异世の阿银
@File ：test13.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
# 这个错误是外部原因造成的, 但是我们需要对这个问题进行提前预处理, 保证程序的健壮性.
ZeroDivisionError: division by zero
ValueError: invalid literal for int() with base 10
'''

if __name__ == '__main__':
    try:
        # 可能出现异常的代码
        num1 = int(input('亲, 请输入第一个整数: '))
        num2 = int(input('亲, 请输入第一个整数: '))

        result = num1 / num2

    # 异常处理
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    # 其他的异常处理
    except BaseException as e:  # BaseException  基类异常, 前面都不能捕获到异常, 那么BaseException就能够捕获到.
        print(e)
    else:
        # 如果没有发生异常, 执行else语句. 如果发生异常, 则不执行else语句.
        print(f'result = {result}')
    finally:
        # 无论是否发生异常, 最后都会执行finally语句块
        # 关闭资源的处理, 文件, 数据库, 连接池....
        print('finally语句块被执行....')

    print('程序执行后续代码...')