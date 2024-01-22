"""
行:外层循环
列:内层循环
图案  直角三角形 等腰三角形  菱形  中空图形
"""
for i in range(5):
    for j in range(5):
        print("*", end="\t")
    print()

print('-' * 100)

for i in range(5):  # [0, 1, 2, 3, 4]
    for j in range(i + 1):
        print("*", end='\t')
    print()

print('-' * 100)

for i in range(4):
    for j in range(7):
        print(f'*', end='\t')
    print()
"""
#分析等腰三角形
如果正常去输出一个等腰三角形,需要考虑哪些?


图不是画出来的,不要考虑成是一个矩阵或者是一个整体直接贴到了控制台输出,
而是一个一个字符,一行一行打印出来的,输出'*'后就结束了,后面是没有空格的
"""

# row = int(input('please enter a rows'))
# for i in range(row):
#     for j in range(row - i - 1):
#         print("", end="-")
#     for j in range(2 * i + 1):
#         print('*', end='')
#     print()

row = int(input('please enter a rows: '))

for i in range(row):  # 外层循环  一共多少行 [0, 1, 2, 3, 4]
    cur_row = i + 1  # 当前是第几行
    for j in range(row - cur_row):  # 内层循环  输出空格   输出多少个?
        print(f' ', end='')
    for j in range(2 * cur_row - 1):  # 内层循环  输出*  输出多少个?
        print(f'*', end='')
    print()  # 换行


"""
# 怎么变空心?
"""
row = int(input("请输入行数:"))
for i in range(row):  # row = 5 i [0, 1, 2, 3, 4]
    for j in range(row - i - 1):
        print(' ', end='')

    for j in range(2 * (i + 1) - 1):  # 输出*所在的范围
        if i == row - 1:
            print('*', end='')
            continue
        if j == 0 or j == (2 * (i + 1) - 1 - 1):  # 想判断是第一个或者是最后一个就输出*
            print('*', end='')
        else:
            print(' ', end='')
    print()
