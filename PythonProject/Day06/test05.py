# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 20:41
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 练习： 判断支付密码是否合法 ？ 全部由数字组成

password = input('亲，请输入密码：')
# 字符串是一个序列，序列可以直接遍历
# 1.使用下标取出字符串中对应的字符
# 2.直接遍历

for i in range(len(password)):
    # character 字符
    character = password[i]
    # print(character, type(character))

    # 判断
    # if character >= '0' and character <= '9':
    if '0' <= character <= '9':
        # 数字字符  （什么都不做）
        pass    # 让语法通过   条件成立，我们什么都不想做。
    else:
        # 非数字字符
        print('密码是不合法的。')
        break
else:   # 如果for循环不是break跳出的，最后会执行else语句
    print('密码是合法的。')

print('-' * 100)

# 2.直接对序列遍历
for i in password:  # password就是那个字符串
    # i 就是字符串中的每一个字符
    # print(i, type(i))
    if '0' <= i <= '9':
        pass
    else:
        print('密码是不合法的。')
        break
else:
    print('密码是合法的。')

print('-' * 100)

# isdecimal() 十进制的字符串内容
# result = password.isdecimal()   #True / False
# result = password.isdigit()
result = password.isnumeric()
if result:
    print('密码合法')
else:
    print('密码不合法')
