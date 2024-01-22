# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：excel_xlwt.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/5/8 8:33 
"""
'''
xlwt:
1.实例化xlwt.Workbook类， 创建新工作簿
2.使用add_sheet方法创建新工作表
3.使用write方法将数据写入单元格
4.使用save方法保存工作簿

# 注意：
xlwt只支持*.xls格式的工作簿
不允许对相同单元格重复赋值
'''


import xlwt

# 创建 *.xls 类型文件对象 工作簿
people = xlwt.Workbook()

# 新建名为'Sheet1'的工作表
sheet = people.add_sheet('Sheet1')

# 写入数据到第一行第一列的单元格
# 按(row, col, value) 的方式添加数据
sheet.write(0, 0, '二两')

# 保存工作簿
people.save('people_xlwt.xls')
