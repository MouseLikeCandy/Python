# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/20 21:35
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

'''
# 内置函数: zip()
# zip 字典生成器
'''

# 定义两个列表
names = ['张三', '李四', '王五', '赵六']
scores = [100, 99, 88, 66, 59, 90, 45]

# 需求：实现合并, 将对应的名称和对应的成绩形成一个字典数据
# 1.定义一个空字典
name_dict = {}

# 2.生成对应的下标
# 存在长度不匹配的风险
# 获取两个列表长度中较小的列表长度
length = len(scores) if len(names) > len(scores) else len(names)
for i in range(length):
    key = names[i]
    value = scores[i]
    # print(key, value)
    # 将key 与value封装到字典中
    name_dict[key] = value

# 使用zip
zip_score = zip(names, scores)
print(zip_score)
for item in zip_score:
    print(item)

for key, value in zip(names, scores):
    print(key, value)
    name_dict[key] = value
print(name_dict)


