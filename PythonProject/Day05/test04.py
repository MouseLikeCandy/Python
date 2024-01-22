# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/16 20:21
@Auth ： 异世の阿银
@File ：test03.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
for + range()
    执行体
else:
    如果程序不是通过break跳出，那么循环结束后，会自动执行else语句。
'''

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
        print(f'密码错误！')

else:   # 特别注意： 此行的else关键字属于for循环  # 自然结束
    print('亲，您已经多次输入错误，此账户已被冻结，请联系XXX')
# 如果循环正常结束，也就是没有遇到break跳出循环的情况下，最后执行else语句


