# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/15 18:32
@Auth ： 异世の阿银
@File ：test05.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
用户注册和登录
'''
# 自定义一个用户类
class User(object):
    # 初始化数据
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # 数据的封装
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password


# 定义一个用户管理类
class UserManager(object):
    # 类数据
    # users = [user1, user2, user3]
    users = []
    # 黑名单
    # black_users = ['张三', '李四', '王五' ...]
    black_users = []
    # 文件名称
    users_filename = 'users.txt'
    black_users_filename = 'black.txt'

    # 读取数据
    @classmethod
    def read_file(cls, filename):
        if filename == cls.users_filename:
            # users列表
            with open(cls.users_filename, mode='a+', encoding='utf-8') as f:
                f.seek(0)   # 从第一行开始读
                for line in f.readlines():
                    # 张三=333\n
                    # 换行处理
                    line = line.strip()
                    # 切割字符串
                    datas = line.split('=')
                    username = datas[0]
                    password = datas[1]
                    # 封装为User对象
                    user = User(username, password)
                    # 存储
                    cls.users.append(user)
        else:
            with open(cls.black_users_filename, mode='a+', encoding='utf-8') as f:
                f.seek(0)
                for line in f.readlines():
                    line = line.strip()
                    cls.black_users.append(line)
    # 写入数据
    @classmethod
    def write_file(cls, filename):
        if filename == cls.users_filename:
            # users列表
            with open(cls.users_filename, mode='wt', encoding='utf-8') as f:
                for user in cls.users:
                    data = f'{user.username}={user.password}'
                    f.write(data + '\n')
        else:
            # black_users列表
            with open(cls.black_users_filename, mode='wt', encoding='utf-8') as f:
                for username in cls.black_users:
                    f.write(username + '\n')
    # 注册
    @classmethod
    def register(cls):
        # 用户名(不允许重复)
        while True:
            username = input('亲,请输入注册的账号:')
            # 判断该用户名是否已经被注册
            for user in cls.users:
                if user.username == username:
                    # 重复了
                    print('该账户已经被注册,请重新选择.')
                    break
            else:
                # 程序来到这里, 说明for循环是正常结束的, 而不是break结束的.
                # 如果for 内部没有break, 说明username没有重复.因此外层的while循环也可以结束了.
                break
        # 密码(长度, 两次密码是否一致)
        while True:
            password = input('亲, 请输入密码: ')
            # 长度
            if len(password) >= 3:
                # 确认密码
                repassword = input('亲, 请再次输入密码: ')
                if password == repassword:
                    # 密码一致
                    break
                else:
                    # 密码不一致
                    print('两次密码不一致.')
            else:
                # 长度不够
                print('密码长度至少大于等于3.')

        # 根据用户名和密码创建一个User对象
        user = User(username, password)
        # 将封装完成的user对象存储到users列表中.
        cls.users.append(user)

        # 写入数据
        cls.write_file(cls.users_filename)

        print('注册成功!')

    # 登录
    @classmethod
    def login(cls):
        # 用户名(存在)
        username = input('亲, 请输入登录账号: ')
        # 定义一个存在用户的下标
        user_index = -1
        for user in cls.users:
            user_index += 1
            if user.username == username:
                # 用户存在
                break
        else:
            # 用户不存在
            # 如果用户登录的用户名不存在, 还需要继续登录吗? 不需要了, 应该先注册.
            # 可以直接结束登录程序
            print('该用户不存在, 请先注册!')
            return

        # 密码
        # 取出存在的用户
        user = cls.users[user_index]

        # 判断该用户是否为黑名单中的用户
        for user_name in cls.black_users:
            # 当前用户名称如果等于黑名单中的用户名, 说明该用户已经被锁定, 无需输入密码了.
            if user_name == username:
                # 黑名单
                print('该账号已经被锁定. 请联系管理员XXX.')
                return


        # 密码输入提供3次机会
        for i in range(1, 4):
            password = input('亲, 请输入密码: ')
            if user.password == password:
                # 登陆成功
                print('登录成功!')
                break
            else:
                # 密码错误
                if i == 3:
                    # 说明该用户3次密码输入错误
                    print('您已多次密码输入错误, 该用户已被锁定, 请联系管理员XXX.')
                    # 将当前用户添加到黑名单中
                    cls.black_users.append(user.username)
                    cls.write_file(cls.black_users_filename)
                    return
                print(f'密码错误! 您还有{3-i}次机会')

    # 展示界面
    @staticmethod
    def show_menu():
        # 读取文件中的数据到程序
        UserManager.read_file(UserManager.users_filename)
        UserManager.read_file(UserManager.black_users_filename)
        menu = '''
        **************************************************************
        ************** 注册[1] 登录[2] 退出[0] ************************
        **************************************************************     
        '''
        while True:
            print(menu)
            # 提示用户输入操作
            choice = input('亲,请输入您的操作:')
            if choice == '1':
                # 注册
                UserManager.register()
            elif choice == '2':
                # 登录
                UserManager.login()
            elif choice == '0':
                # 退出
                print('感谢您的使用,再见!')
                break
            else:
                print('操作有误, 请重新选择.')

if __name__ == '__main__':
    UserManager.show_menu()