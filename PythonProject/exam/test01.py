"""
python
九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}= {j * i}', end='\t')
    print()

print('-' * 100)
for i in range(9):  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for j in range(i + 1):
        print(f'{j + 1}*{i + 1} = {(j + 1) * (i + 1)}', end='\t')
        #  print(f'{j + 1}*{i + 1}多加一个空格输出改变= {(j + 1) * (i + 1)}', end='\t')
    print()
