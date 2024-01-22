# try except 异常捕捉
a = -1
b = '2'
try:
    c = a + b
except:
    print('错误!整形与字符串型不可直接相加')

b = 2
try:
    c = a + b
except TypeError as e:
    print('错误!整形与字符串型不可直接相加')
    print(f'具体报错细节:{e}')
else:
    print('相加成功')
finally:
    print('try 是否抛出异常都执行')


# if a != b:
#    raise TypeError

def error_fun():
    try:
        name = input('请输入名称:')
        if name.isspace():
            raise ValueError('name 不可是空格')
        if name.isdigit():
            raise ValueError('name 不可是数字')

        name = name + 123

    except TypeError as e:
        print(f'类型错误:{e}')

# error_fun层的上一层
try:
    error_fun()
except ValueError as e:
    print(f'{e}, 请重试')
    error_fun()


import traceback

try:
    l = [1, 2, 3]
    num = len(l)
    _ = l[num]
except:
    traceback.print_exc()
    with open('error.log', 'a') as f:
        errorinfo = traceback.format_exc()
        f.write(errorinfo)

