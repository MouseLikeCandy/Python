# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：exam01.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/9/21 8:44 
"""
'''
例1：键盘输入字符串s，按要求把s输出到屏幕，格式要求:宽度为30个字符，星号字符*填充，居中对齐。如果输入字符串超过30位，则全部输出。
'''
# // 考生文件初始代码
# s = input("请输入一个字符串:")
# print("{______}".format(s))

# // 参考答案
# s = input("请输入一个字符串:")
# print("{:*^30}".format(s))
'''
例2：根据斐波那契数列的定义，F(0)=0，F(1)=1,F(n)=F(n-1)+F(n-2)(n>=2)，输出不大于50的序列元素。
例如:屏幕输出实例为:0.1.1.2.3…(略)
'''
# // 考生文件初始代码
# a, b = 0, 1
# while ______:
#    print(a, end=',')
#    a, b = ______

# // 参考答案
# a, b = 0, 1
# while a <= 50:
#    print(a, end=',')
#    a, b = b, a+b


# def function(n):
#     if n == 0:
#         result = 0
#     elif n == 1:
#         result = 1
#     elif n >= 2:
#         result = function(n-1) + function(n-2)
#     return result
#
#
# if __name__ == '__main__':
#     for i in range(51):
#         if function(i) <= 50:
#             print(function(i))
#         else:
#             break

'''
例3：键盘输入一句话，用jieba分词后，将切分的词组按照在原话中逆序输出到屏幕上，词组中间没有空格。
示例如下:   输入:我爱老师   输出:老师爱我
'''
# // 考生文件初始代码
# import jieba
# txt = input("请输入一段中文文本:")
# ______
# for i in ls[::-1]:
#    ______
# // 参考答案
# import jieba
# txt = input("请输入一段中文文本:")
# ls = jieba.lcut(txt, cut_all=True)
# print(list(ls))
# for i in ls[::-1]:
#     print(i, end="")

'''
例4：键盘输入正整数n，把n输出到屏幕，格式要求:宽度为30个字符，@填充，右对齐，带千位分隔符。若输入正整数超30位，则真实长度输出。
例:键盘输入正整数n为5201314，屏幕输出@@@@@@@@@@@@@@@@@@@@@5,201,314
'''
# // 考生文件初始代码
# n = eval(input("请输入正整数:"))
# print("{______}".format(n))

# // 参考答案
# n = eval(input("请输入正整数:"))
# print("{0:@>30,}".format(n))

'''
例5：a、b是两列表变量，列表a为[11,3.8]已给定，键盘输入列表b，计算a中元素与b中对应元素乘积的累加和。
例:键盘输入列表b为[4.,5.2]，则屏幕输出计算结果为75
'''
# // 考生文件初始代码
# a = [11,3,8]
# b =  eval(input()) #例如：[4,5,2]
# ______
# for i in ______:
#    s += a[i]*b[i]
# print(s)

# // 参考答案
# a = [11, 3, 8]
# b = eval(input())
# s = 0
# for i in range(3):
#    s += a[i] * b[i]
# print(s)

# a = [11, 3, 8]
# b = eval(input("请输入列表b:(逗号分隔)"))
# s = 0
# for i in range(len(a)):
#    s += a[i] * b[i]
# print(s)

'''
例6：以255为随机数种子，随机生成5个在1(含)到50(含)之间的随机整数，每个随机数后跟随一个空格进行分隔，屏幕输出这5个随机数。
'''
# // 考生文件初始代码
# import random
# ______
# for i in range(______):
#    print(______, end=" ")

# // 参考答案
# import random
# random.seed(255)    # 有种子, 随机数是固定不变的
# for i in range(5):
#    print(random.randint(1, 50), end=" ")

'''
例7：从键盘输入一个1~26之间的数字，对应于英文大写字母表中的索引，在屏幕上显示输出对应的英文字母。
示例如下:请输入一个数字:1 输出大写字母:A
'''
# // 考生文件初始代码
# s = eval(input("请输入一个数字："))
# ls = [0]
# for i in range(65,91):
#    ls.append(chr(_____))
# print("输出大写字母：{}".format(_____))

# // 参考答案
# s = eval(input("请输入一个数字："))
# ls = [0]
# for i in range(65, 91):
#    ls.append(chr(i))
# print("输出大写字母：{}".format(ls[s]))

'''
例8：从键盘输入一个有十进制的数字保存在变量s中，转换为二进制数输出显示在屏幕上，
示例如下:请输入一个十进制数:25 转换成二进制数是:11001
'''
# // 考生文件初始代码
# s = input("请输入一个十进制数：")
# num = _____
# print("转换成二进制数是：{_____}".format(_____))

# // 参考答案
# s = input("请输入一个十进制数：")
# num = int(s)
# print("转换成二进制数是：{:b}".format(num))

'''
例9：从键盘输入一个中文字符串变量s，内部包含中文逗号和句号。计算字符串s中的中文词语数。
示例如下: 请输入一个中文字符串，包含标点符号:问君能有几多愁?恰似一江春水向东流。中文词语数:9
'''

# // 考生文件初始代码
# import _____
# s = input("请输入一个中文字符串，包含标点符号：")
# m =_____
# print("中文词语数：{}".format(_____))

# // 参考答案
# import jieba
# s = input("请输入一个中文字符串，包含标点符号：")
# m = jieba.lcut(s)
# print("中文词语数：{}".format(len(m)))

'''
例10：请将列表lis内的重复元素删除，并输出。
例如:若列表为[2,8,3,6,5,3,8]，输出为[8,2,3,5,6]
'''
# // 考生文件初始代码
# lis = [2,8,3,6,5,3,8]
# new_lis = _____
# print(new_lis)

# // 参考答案
lis = [2, 8, 3, 6, 5, 3, 8]
new_lis = list(set(lis))
print(new_lis)

'''
例11：输入一个水果名，判断它是否在列表lis中，并输出判断结果。
例如:输入:猕猴桃 输出:猕猴桃在列表lis中
'''
# // 考生文件初始代码
# fruit = input('输入水果：')
# lis = ['苹果','哈密瓜','橘子','猕猴桃','杨梅','西瓜']
# if _____:
#    _____
# else:
#    _____

# // 参考答案
# fruit = input('输入水果：')
# lis = ['苹果','哈密瓜','橘子','猕猴桃','杨梅','西瓜']
# if fruit in lis:
#    print(fruit + '在列表lis中')
# else:
#    print(fruit + '不在列表lis中')

'''
例12：编写一个函数，使之能够实现字符串的反转。将字符串"goodstudy"输入到函数中，运行并输出结果。
'''


# // 考生文件初始代码
# def str_change(str) :
#    return _____
# str = input("输入字符串：")
# print(str_change(_____))

# // 参考答案
# def str_change(str):
#     return str[::-1]
# str = input("输入字符串：")
# print(str_change(str))

'''
例13：循环获得用户输入，直至用户输入Y或者y字符退出程序。
'''
# // 考生文件初始代码
# while _____:
#    s = input("请输入信息：")
#    if _____:
#        break

# // 参考答案
# while True:
#    s = input("请输入信息：")
#    if s == "y" or s == "Y":
#        break

'''
例14：使用calendar模块，从键盘输入年份，输出，当年的日历。
'''
# // 考生文件初始代码
# import calendar
# year = _____(input("请输入年份："))
# table = _____(year)
# print(table)

# // 参考答案
# import calendar
# year = int(input("请输入年份："))
# table = calendar.calendar(year)
# print(table)

'''
例15：输入下面的绕口令，将其中出现的字符“兵”，全部替换为“将”，输出替换后的字符串。
八百标兵奔北坡，炮兵并排北边跑，炮兵怕把标兵碰，标兵怕碰炮兵炮。八了百了标了兵了奔了北了坡，把了标了兵了碰,标了兵了怕了碰了炮了兵了炮。
'''
# // 考生文件初始代码
# s = input("请输入绕口令：")
# print(s._____("兵","将"))

# // 参考答案
# s = input("请输入绕口令：")
# print(s.replace("兵","将"))

'''
例16：读取考生文件夹下的“poem.txt"的内容，去除空行和注释行后，以行为单位进行排序，并将结果输出到屏幕上。输出结果为:
A Grain of Sand
And a heaven in a wild flower,
And eternity in an hour.
Hold infinity in the palm of your hand,
To see a world in a grain of sand,
'''
'''
// 考生文件夹中的poem.txt
#Title
A Grain of Sand
#William Blake
To see a world in a grain of sand,
And a heaven in a wild flower,
Hold infinity in the palm of your hand,
And eternity in an hour.
'''
# // 考生文件初始代码
# _____
# result = []
# for line in _____:
#    _____
#    if len(line) != 0 and line[0] != "#":
#        _____
# result._____
# for line in result:
#    print(line)
# f.close()

# // 参考答案
# f = open("poem.txt", "r")
# result = []
# for line in f.readlines():
#    line = line.strip()
#    if len(line) != 0 and line[0] != "#":
#        result.append(line)
# result.sort()
# for line in result:
#    print(line)
# f.close()

'''
例17：请在屏幕上输出以下杨辉三角形:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
'''
# // 考生文件初始代码
# a = []
# for i in range(8):
#    a.append([])
#    for j in range(8):
#        a[i].append(0)
# for i in range(8):
#    a[i][0] = 1
#    _____
# for i in range(2,8):
#    for j in range(1,i):
#        a[i][j] = _____
# for i in range(8):
#    for j in range(i+1):
#        print("{:3d}".format(a[i][j]),end=" ")
#    print()

# // 参考答案
# a = []
# for i in range(8):
#    a.append([])
#    print(len(a))
#    print(a)
#    for j in range(8):
#        a[i].append(0)
# for i in range(8):
#    a[i][0] = 1
#    a[i][i] = 1
# for i in range(2, 8):
#    for j in range(1, i):
#        a[i][j] = a[i-1][j-1] + a[i-1][j]
# for i in range(8):
#    for j in range(i+1):
#        print("{:3d}".format(a[i][j]), end=" ")
#    print()

'''
例18：在一组单词中，查找出所有长度最长的单词，如果给定的一组单词是: “cad”“VB’” “Python” “MATLAB” "hello " "world"则输出结果为:
the longest words are:
                     Python
                     MATLAB
'''
# // 考生文件初始代码
# def proc(strings):
#    m = 0
#    lst = []
#    for i in range(len(strings)):
#        if len(strings[i]) _____ m:
#            m = len(strings[i])
#    for i in range(len(strings)):
#        if len(strings[i]) _____ m:
#            lst.append(strings[i])
#    return _____
#
# strings = ['cad' ,'VB', 'Python', 'MATLAB', 'hello', 'world']
# result = proc(strings)
# print("the longest words are:")
# for item in result:
#    print("{: >25}".format(item))

# // 参考答案
# def proc(strings):
#    m = 0
#    lst = []
#    for i in range(len(strings)):
#        if len(strings[i]) > m:
#            m = len(strings[i])
#    for i in range(len(strings)):
#        if len(strings[i]) == m:
#            lst.append(strings[i])
#    return lst
#
# strings = ['cad' ,'VB', 'Python', 'MATLAB', 'hello', 'world']
# result = proc(strings)
# print("the longest words are:")
# for item in result:
#    print("{: >25}".format(item))

'''
例19：接收用户输入的一个小于20的正整数，在屏幕上逐行递增显示从01到该正整数，数字显示的宽度为2，不足位置补0，后面追加一个空格，
然后显示’>'号，‘>’号的个数等于行首数字。例如: 输入：2
输出：
01>
02>>
'''
# // 考生文件初始代码
# n = input('请输入一个正整数:')
# for i in range(____________):
#    print('____________'.format(i, ____________))
# // 参考答案
# n = input('请输入一个正整数:')
# print(type(eval(n)))
# for i in range(1, eval(n)+1):
#    print('{:0>2} {}'.format(i, '>'*i))

'''
例20：让用户输入一串数字和字母混合的数据，然后统计其中数字和字母的个数，显示在屏幕上。
例如: 输入：fda243fdw3 输出：数字个数:4，字母个数:6
'''
# // 考生文件初始代码
# ns = input("请输入一串数据：")
# dnum,dchr = ____________
# for i in ns:
#    if i.isnumeric():
#        dnum += ____________
#    elif i.isalpha():
#        dchr += ____________
#    else:
#        pass
# print('数字个数：{}，字母个数：{}'.format(____________))

# // 参考答案
# ns = input("请输入一串数据：")
# dnum,dchr = 0,0
# for i in ns:
#    if i.isnumeric():
#        dnum += 1
#    elif i.isalpha():
#        dchr += 1
#    else:
#        pass
# print('数字个数：{}，字母个数：{}'.format(dnum,dchr))

