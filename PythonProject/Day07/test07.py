# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/20 21:29
@Auth ： 异世の阿银
@File ：test07.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
    字典的操作：
    1.增加 scores[key] = value 如果key不存在，操作就是增加
    2.删除 del scores[key]
    3.修改 scores[key] = value 如果key存在，操作就是修改
    4.查询 (1)scores[key]   (2)scores.item()
'''

scores = {'张三': 100, '李四': 99, '王五': 88, '赵六': 66}
# 增加
scores['马八'] = 59
print(scores)
# 修改
scores['马八'] = 60
print(scores)
# 删除
# 格式:  del 字典 -> 含义:删除整个字典,这时字典就已经不存在了.
#       del 字典[key]-> 含义为删除字典中指定的键值对
del scores['马八']
print(scores)
# 查询/获取
# 格式: 字典[key] 如果字典中不存在指定的key,程序会报错KeyError
score = scores['张三']
print(f'score = {score}')
# 使用get(key)来获取对应的值, 如果字典中没有对应的key,那么该方法返回None 建议使用get
# 选中移动快捷键: Ctrl + shift + 上下方向键
zhang_san = scores.get("张三")
print(f'zhang_san = {zhang_san}')


'''
判断指定的key在字典中是否存在
# in        
# not in    
'''
result = "张三" in scores
print(f'result = {result}')

# 应用
if "张三" in scores:
    # 执行下一步操作
    print('存在')
