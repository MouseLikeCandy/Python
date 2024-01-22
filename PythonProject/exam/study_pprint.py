
from pprint import pprint

# 列表对象

test = [1, 2 , [3, 4, [5, 6, 7], 8], 9, 10]

# 限制输出层级最多为两层

pprint(test, depth = 2)

# 一行最大字符数为5, 4格缩进

pprint(test, width = 5, indent = 4)

# 单个对象, width无效

pprint('1234567', width = 5)