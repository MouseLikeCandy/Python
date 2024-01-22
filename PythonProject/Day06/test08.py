# -*- coding: utf-8 -*-
"""
@Time ： 2022/8/18 21:09
@Auth ： 异世の阿银
@File ：test08.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


'''
# 列表相关操作

# 列表    
    特点：
    1.列表是长度可变，整体中的元素可以‘增加，修改，删除，查询’
    2.列表中的元素（element）是可以重复的，并且每一个元素都有对应的下标（索引：正向索引/逆向索引）
    格式：
    [元素1，元素2，元素3，元素4，元素5，元素6，...]

    切片:
    列表名[start : stop : step]
    1.start 可以省略，默认从0开始
    2.stop  可以省略，默认到尾部
    3.step  可以省略，默认为1
'''
# 思考：如何存储多个数值？并且这个数值还可能不断增加
# 思考：为什么需要列表类型的数据呢？

# 张三，李四，王五，赵六，田七
name1 = '张三'
name2 = '李四'
name3 = '王五'
name4 = '赵六'
name5 = '田七'

# 内存中5块独立的空间，以下变量定义的数据是独立分散的数据，不方便实现整体的统一操作。
# Python 语言中有统一的整体类型吗？ list, tuple, set, dict这四个类型都是整体(序列)统一的类型。

names = ['张三', '李四', '王五', '赵六', '田七', '张三']
print(names)

# 1.遍历names这个整体
for i in range(len(names)):
    name = names[i]
    print(name)

# 遍历格式：for 变量名 in 列表名： 在循环内部可以直接操作变量名
# 2.序列可以直接在循环中遍历
for name in names:
    print(name)

# index 下标/索引
# Return first index of value.
# Raises ValueError if the value is not present.
# 返回查找值第一次出现的下标，如果这个查找的值不存在，程序会抛出ValueError值错误的异常.
index = names.index('张三')
print(f'index = {index}')
# index = names.index('风三')
# print(f'index = {index}')

# index(self, object, start, stop)
# self          不用管
# object        查找值
# start,stop    查找范围
index = names.index('张三', 1, 6)
print(f'index = {index}')

'''
需求：获取指定下标对应的元素
格式：列表名[index]
'''
name = names[3]
print(f'name = {name}')

# 逆向索引
name = names[-2]
print(f'name = {name}')


# 切出 '张三', '李四', '王五'
sub_names = names[0:3:1]
print(f'sub_names = {sub_names}')
# 切出 '王五','赵六'
sub_names = names[2:4:1]
print(f'sub_names = {sub_names}')
# 切出 '张三', '王五', '田七'
sub_names = names[::2]
print(f'sub_names = {sub_names}')
# 倒序列表
sub_names = names[::-1]
print(f'sub_names = {sub_names}')


# 需求：判断指定元素在列表中存在
# in
# not in

result = '张三' in names
print(f'result = {result}')

# 问题：张三在names列表中不存在吗？False
result = '张三' not in names
print(f'result = {result}')



'''
# 列表增添元素
# append    增加
# extend    扩展
# insert    插入
'''

# append: Append object to the end of the list.
# 在列表的末尾添加任意元素，
# 注意：该方法没有返回值，不需要接收
names.append('麻八')
print(names)

# extend : Extend list by appending elements from the iterable.
# 从一个可迭代的对象中拼接多个元素，从而实现原来列表的扩展
sub_names = ['Jack', 'Rose', 'Tom', 'Peter']
names.extend(sub_names)
print(names)

# insert : Insert object before index.
# 在给定的下标前面插入指定元素。
names.insert(6, '小九')
print(names)

'''
# 列表删除元素
# remove    
# pop    
# clear    
# del -> delete   内置函数，并不是列表的方法
'''
# remove : Remove first occurrence of value.
# Raises ValueError if the value is not present.
# 删除第一次出现的指定值
names.remove('张三')
print(names)

# pop : Remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range.
# 移除并返回指定下标的元素（默认如果不给下标，则移除最后一个元素）
names.pop()
print(names)

names.pop(0)
print(names)

# clear : Remove all items from list. 移除列表中所有元素
names.clear()   # 空列表
print(names)

# del
# del names[4]    # 建议使用remove,pop方法替代该行为
# del names       # 删除列表，后续该列表不能再被访问使用
# NameError: name 'names' is not defined
# print(names)


'''
# 列表修改元素： 
使用下标实现指定元素的修改
'''
names = ['张三', '李四', '王五', '赵六', '田七', '张三']
names[3] = '赵六'
print(names)

'''
排序： 不要对汉子进行排序，意义不大。（汉字有自己的排序规则： 百家姓）
# Sort the list in ascending order and return None.
# 按照升序实现列表元素的排序，该方法不返回任何结果。（意味着就是原来列表的排序）
'''
names.sort()
print(names)
# 数值列表实现排序 升序
num_list = [50, 60, 32, 43, 65, 32, 56, 90, 35, 63, 12]
num_list.sort()
print(num_list)

# 降序排序： The reverse flag can be set to sort in descending order
# 如果方法的'反转标志'被设置了，如果排序规则为降序排序
num_list.sort(reverse=True)
print(num_list)


# 字符串排序，按照字符的规则
# a-z, A-Z
# 字符串的比较是一个一个字符比较的，如果第一个字符就能决定顺序，之后的字符就不需要比较。
# 每一个字符都有对应的数值。编码表：ASCII码，A->65 a->97
country_list = ['China', 'America', 'Canada', 'India', 'France', 'Germany', 'Russia', 'Japan', 'Korea']
country_list.sort()
print(country_list)

# 内置函数：sorted()排序
num_list = [50, 60, 32, 43, 65, 32, 56, 90, 35, 63, 12]
# Return a new list containing all items from the iterable in ascending order.
# 根据可迭代对象的升序规则，返回一个所有原列表中元素的新列表。不改变原来列表中的元素，新列表才是排序规则的列表
# return 返回，程序中我们就需要定义一个变量接收返回的结果
sorted(num_list)
# reverse flag can be set to request the result in descending order.
# '反转标志'可以被设置来请求一个降序排列的结果。
sorted(num_list, reverse=True)
print(f'num_list = {num_list}')

'''
# 列表生成器： /列表构造器/列表推导式
# 生成一个指定元素的列表
'''

# 需求：[1,2,3,4,5,6,7,8,9,10]
# for i in range(1, 11, 1) 循环中的遍历语法
num_list = [i for i in range(1, 11, 1)]
print(num_list)

# 需求：[10,20,30,40,50,60,70,80,90,100]
num_list = [i*10 for i in range(1, 11, 1)]
print(num_list)

# 需求：[1,4,9,16,25,36,49,64,81,100]
# num_list = [i*i for i in range(1, 11, 1)]
num_list = [i**2 for i in range(1, 11, 1)]
print(num_list)

# 内置函数：实现列表中所有元素的累加和
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum(num_list)
print(f'result = {result}')

'''
通用操作：
1. + 可以将两个列表拼接成一个列表
2. * 可以将列表重复指定的次数
3. min()获取列表中的最小元素
4. max()获取列表中的最大元素
5. 列表.count(元素) 指定元素在列表中出现的次数
'''
num1_list = [10, 20, 30]
num2_list = [30, 40, 50]
# 思考两个列表相加，有没有返回结果
# 如何确定呢？直接输出'左边列表'查看即可
# 原来列表没有变化，说明 + 符号一定有返回结果.
new_list = num1_list + num2_list
print(new_list)

new_list = num1_list * 3
print(new_list)

num_list = [10, 90, 32, 45, 180, 87]
min_value = min(num_list)
max_value = max(num_list)
print(f'min_value = {min_value}, max_value = {max_value}')

num_list = [10, 20, 30, 10, 20, 30, 10, 20, 30]
count = num_list.count(30)
print(f'count = {count}')

'''
内置函数: enumerate()
enumerate 迭代器,如果传入一个列表,则将列表中的每一个元素与其对应的下标实现组合.
遍历列表, 需要使用下标时使用
'''
names = ['张三', '李四', '王五', '赵六', '田七', '张三']
# 遍历列表
for name in names:
    print(name)
# enumerate(列表) 返回的是一个一个的元组对象,格式:(0, '张三') 第一个元素为下标,第二个元素为列表中的元素
for name in enumerate(names):
    print(name)
# 遍历方式二:
print('-'*100)
for index, name in enumerate(names):
    print(index, '->', name)


'''
列表的嵌套
外层列表中的每一个元素,其实也是一个列表.
如何获取列表中的数据?再次遍历.
'''
list_data = [[11, 12], [21, 22, 23], [31, 32, 33, 34]]

# 定义一个用于统计的变量
group_sum = 0
company_sum = 0

# 1.获取列表中的每一个元素
for data in list_data:
    print(data)
    # 再次遍历, 需要清空之前小组的统计额, 开始一次新的小组统计
    group_sum = 0
    for element in data:
        print(element)
        # 统计第一个小组的销售额
        group_sum += element
    # 内层循环完毕后, 当前小组就完成了销售额的统计
    # 需要将当前的小组的销售额统计到公司的销售额中.
    print(f'group_sum = {group_sum}')
    company_sum += group_sum

# 循环结束后,查看公司的总销售额
print(f'company_sum = {company_sum}')
