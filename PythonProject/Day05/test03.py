# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/16 20:21
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 需求： 用户输入密码，有三次机会，如果正确，登陆成功
#       如果三次机会都输入错误，冻结此账户


# 执行一个‘三次循环’
for i in range(3):
    # 提示用户输入密码
    password = input('亲，请输入您的密码：')
    # 判断密码是否正确
    if password == '666':
        # 密码正确
        print('欢迎您！登陆成功！')
        break
    else:
        # 密码错误
        if i == 2:
            # 程序来到这里，说明这已经是第三次输入错误，需要冻结此账户。
            print('亲，您已经多次输入错误，此账户已被冻结，请联系XXX')
            # 跳出循环
            # 1. break
            # 2. continue
            # 3. else
        else:
            print(f'密码错误！还有{2-i}次机会！')

