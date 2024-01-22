# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：test1.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/9/22 11:25 
"""
str = "abchadawo123"
print(str[::-1])

# try:
#     n = 0
#     n = input("请输入一个整数: ")
#     def pow10(n):
#         return n**10
# except:
#     print("程序执行错误")

# txt = open("book.txt", "r", encoding="utf-8")
# print(txt)
# print(txt.readlines())
# for line in txt:
#     print(line)
#
#
# import sys
# print(sys.version)
#
# import turtle as t
# def DrawCctCircle(n):
#     t.penup()
#     t.goto(0, -n)
#     t.pendown()
#     t.circle(n)
# for i in range(20,80,20):
#     DrawCctCircle(i)
# t.done()

x = 2
y = 4.01
print(x**y)

if x == y:
    print(1)
elif x != y:
    print(2)

print(1.23e-4+5.67e+8j.real)

s = "11+5in"
print(eval(s[1:-2]))