# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：excel_pandas.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/5/11 10:02 
"""
'''
Pandas第三方库可以很完美地替代Excel完成除单元格样式设置外的所有功能.
Pandas依赖于xlrd和xlwt
理解Series和DataFrame
Series: 一组数据 + 标签索引, 每一行/每一列 都是Series对象, 类似工作表中的一行或一列.
DataFrame: 表格型的数据结构, 行索引 + 列索引, Series组成的字典, 类似于工作簿中的一个工作表.
多个Series可以组成一个DataFrame
'''
import pandas as pd

# 实例化Series对象
s1 = pd.Series([1, 2, 3], index=[10, 20, 30], name='s1')

print(s1)  # 输出Series对象
print(s1.index)  # 输出Series对象的索引
print(s1[10])  # 输出Series对象的索引为10的值

# 创建Series对象
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')
# 使用Series对象实例化DataFrame对象
df = pd.DataFrame([s1, s2, s3])
print(df)

# 通过字典形式构建DataFrame对象
df2 = pd.DataFrame({
    s1.name: s1,
    s2.name: s2,
    s3.name: s3
})
print(df2)

filepath = 'people_pandas.xlsx'
# 读取工作簿中名为Sheet1的工作表
people = pd.read_excel(filepath, sheet_name='Sheet1')
# 跳过前5行, 从第6行开始读取
people1 = pd.read_excel(filepath, header=5, sheet_name='Sheet1')
# 跳过前4行, 取E列 到 H列
people3 = pd.read_excel(filepath, sheet_name='Sheet1', skiprows=4, usecols='E:H')

# 指定id列为索引, dtype设置某一列数据的类型
people2 = pd.read_excel(filepath, sheet_name='Sheet1', index_col='id', dtype={'gender': str, 'birthday': str})

print(people1)
print(people3)
print(people2)

# 通过字典形式构建DataFrame
df = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['张三', '李四', '王五'],
    'age': [28, 25, 30]
})

df.to_excel('people_pandas_index1.xlsx')
# 自定义索引
df = df.set_index('id')
df.to_excel('people_pandas_index2.xlsx', sheet_name='Sheet2')

# 填表people_pandas_test01.xlsx
# 读入工作簿
people4 = pd.read_excel('people_pandas_01.xlsx', skiprows=4, usecols='B:E',
                        dtype={'ID': str, 'gender': str, 'birthday': str})
from datetime import date, timedelta

# 开始日期
startday = date(2019, 7, 1)
for i in people4.index:
    # 累加ID
    people4.at[i, 'ID'] = i + 1
    # 判断性别
    people4.at[i, 'gender'] = 'Male' if i % 2 == 0 else 'Female'
    # 计算生日日期
    people4.at[i, 'birthday'] = date(startday.year + i, startday.month, startday.day)

# inplace 表示就地修改DataFrame, 不必再重新创建一个新的DataFrame来存储修改后的状态
people4.set_index('ID', inplace=True)
people4.to_excel('people_pandas_01_c.xlsx')

# 修改一列, money + 1000 的三种方法
people5 = pd.read_excel('people_pandas_02.xlsx', index_col='ID')


# 加工资, x代表当前cell中的值
def add_1000(x):
    return x + 1000


# Series对象加1000
people5['money'] = people5['money'] + 1000
# apply会逐个元素地调用函数
people5['money'] = people5['money'].apply(add_1000)
# apply会逐个元素地调用匿名函数
people5['money'] = people5['money'].apply(lambda x: x + 1000)

people5.to_excel('people_pandas_02c.xlsx')

# 工作表中的数据自动排序 sort_values
people6 = pd.read_excel('people_pandas_03.xlsx')
# sort_values表示按值排序
people6.sort_values(by='工资', inplace=True, ascending=False)
print(people6)
# 多列排序, 开除工资高但做事不靠谱的人
people6.sort_values(by=['靠谱', '工资'], ascending=[True, False], inplace=True)
print(people6)

# 数据过滤
people7 =pd.read_excel('people_pandas_04.xlsx', index_col='ID')
# 检查people7 DataFrame中是否有NaN
print(people7.isnull().any())   # 输出所有列True为列中含有Nan
# 清除NaN的行
people7.dropna(inplace=True)    # 将缺失数据所对应的行删除
# 分数及格的女性
pass_women = people7[(people7['性别'] == 'F') & (people7['分数'] >= 60)]
print(pass_women)

def score_50_to_90(a):
    return 50 <= a < 90

def age_20_to_30(a):
    return 20 <= a < 30

# 50~90分的20~30岁的男性, 利用loc将满足条件的数据保留. 性别 -> 分数 -> 年龄
mans_50_to_90 = people7[people7['性别'] == 'M'].loc[
    people7['分数'].apply(score_50_to_90)
    ].loc[people7['年龄'].apply(age_20_to_30)]
print(mans_50_to_90)

# 实现数据的拆分
people8 = pd.read_excel('people_pandas_05.xlsx', index_col='ID')
# 将Full Name拆分成'姓氏'列与'名字'列
df = people8['Full Name'].str.split(expand=True)  # expand=True 返回DataFrame对象
print(df)
# 创建'姓氏'列
people8['姓氏'] = df[0]
# 创建'名字'列
people8['名字'] = df[1]
print(people8)

# 将Full Name拆分成'姓氏'列与'名字'列
# ser = people8['Full Name'].str.split(expand=False)  # expand=False 返回Series对象
# print(ser[1])
# df = pd.DataFrame({
#     ser.name: ser
# })

people8.to_excel('people_pandas_05c.xlsx')

# 多表联合操作
# 需求: 获取年龄大于20且分数大于60的学生姓名

# 学生姓名表
name = pd.read_excel('student_name_pandas_01.xlsx', sheet_name='name', index_col='ID')
# 分数表
score = pd.read_excel('student_score_pandas_02.xlsx', sheet_name='score', index_col='ID')
# 年龄表
age = pd.read_excel('student_age_pandas_03.xlsx', sheet_name='age', index_col='编号')

# 合并
# fillna方法将NaN都填充为0   姓名表 合并 分数表
table = name.merge(score, how='left', on='ID').fillna(0)
# 将分数列中的数据类型设置为整型
table['分数'] = table['分数'].astype(int)

# 姓名表 合并 分数表 再合并 年龄表
table2 = table.merge(age, how='left', left_on=name.index, right_on=age.index).fillna(0)
table2['年龄'] = table2['年龄'].astype(int)

print(table2)

pass_student = table2[(table2['年龄'] >= 20) & (table2['分数'] >= 60)]
print(pass_student)
pass_student.to_excel('student_pandas_04.xlsx')


# 对Excel数据进行统计运算
df = pd.DataFrame([
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3]
], columns=['col1', 'col2', 'col3', 'col4'])

print(df)
df1 = df.mean(axis=1)  # mean方法用于求某一行或者某一列的平均数
print(df1)
df2 = df.drop('col4', axis=1)  # drop方法用于删除某一行或者列
print(df2)

people9 = pd.read_excel('people_pandas_09.xlsx', index_col='ID')
column_names = ['小测1', '小测2', '小测3']

# 对每一行中的每一列进行求和操作
row_sum = people9[column_names].sum(axis=1)
row_mean = people9[column_names].mean(axis=1)

total = '总分'
average = '平均分'
people9[total] = row_sum
people9[average] = row_mean
column_names += [total, average]

# axis默认值为0, 对每一列中的每一行进行求平均操作
col_mean = people9[column_names].mean()
col_mean['名称'] = 'Summary'
# append方法添加新的一行, ignore_index为True,表示忽略index
people9 = people9._append(col_mean, ignore_index=True)

print(people9)
people9.to_excel('people_pandas_09c.xlsx')

# 使用Pandas实现数据的可视化
import matplotlib.pyplot as plt

students = pd.read_excel('people_pandas_10.xlsx')
name = '名称'
score = '分数'
age = '年龄'

# sort_values 方法排序, inplace表示原地修改, ascending从大到小
students.sort_values(by=score, inplace=True, ascending=False)
# 绘制柱状图
plt.bar(students[name], students[score])

# 设置标题
plt.title('Students Score', fontsize=16)
# 设置X轴与Y轴名称
plt.xlabel('Name')
plt.ylabel('Score')
# X轴中要显示的名字太长, 利用rotation将其旋转90度,方便显示
plt.xticks(students[name], rotation=90)
# 紧凑型布局
plt.tight_layout()
plt.show()

# 重新绘制柱状图
plt.bar(students[name], students[score], color='orange')
# Font Properties 文字属性
from matplotlib.font_manager import FontProperties
# 传入字体路径, 实例化对应的字体, SimHei.ttf表示黑体
myfont = FontProperties(fname=r'C:\Windows\Fonts\STHUPO.TTF')
# 指定渲染字体
plt.title('学生分数', fontproperties=myfont, fontsize=16)
plt.xlabel(name, fontproperties=myfont)
plt.ylabel(score, fontproperties=myfont)
plt.xticks(students[name], rotation=90)
plt.tight_layout()
plt.show()


# 绘制折线图
students = pd.read_excel('people_pandas_11.xlsx')
name = 'Full Name'
score = '分数'
age = '年龄'
xRange = 'xRange'
# students.sort_values(by=score, inplace=True, ascending=False)

# 指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决符号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
# 绘制折线图
# xRange = range(1, 111, 10)
students.plot(x='number', y=[score, age])
plt.title('学生分数', fontproperties=myfont, fontsize=26, fontweight='bold')
# 重新绘制X轴坐标
# plt.xticks(students[xRange], students[name], rotation=90)
plt.xticks(students['number'], rotation=90)
plt.show()

# 绘制散点图
students = pd.read_excel('people_pandas_12.xlsx')
name = '名称'
weight = '体重'
height = '身高'
students.plot.scatter(x=weight, y=height)
plt.title('学生体重', fontsize=16, fontweight='bold')
plt.xlabel(weight)
plt.ylabel(height)
plt.show()