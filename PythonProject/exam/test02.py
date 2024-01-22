'''
3次输入密码验证
'''

# for i in range(3):
#     password = input("亲，请输入密码：")
#     if password == "666888":
#         # 密码正确
#         print(f'欢迎！')
#         break
#     else:
#         # 密码错误
#         print(f"密码错误：还有{2 - i}次机会")
#         if i == 2:
#             print("亲，您的账户已经被冻结，请联系系统管理员。XXX")
#             break


for i in range(3):
    password = input("亲，请输入您的密码：")
    if password == "6668888":
        print("欢迎")
        break
    else:
        print(f"密码错误，请重新输入。")
else:
    print(f"亲，您的账户由于多次输入错误已经被锁定，请联系系统管理员XXX")