# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：excel_xlutils.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/5/9 12:08 
"""

'''
xlutils依赖于xlrd和xlwt
'桥梁'的作用
注意:
*.xlsx类型中记录的样式无法很好地展现在*.xls类型文件中
'''
import xlrd
from xlutils.copy import copy
# 读入数据, 获取Book对象
rd_book = xlrd.open_workbook('xlutils_test.xlsx')
# 连样式也一起复制
rd_book = xlrd.open_workbook('xlutils_test.xlsx', formatting_info=True)
# 获取工作簿中第一个工作表, 方便后续操作.
rd_sheet = rd_book.sheets()[0]
# 复制Book对象为Workbook对象
wt_book = copy(rd_book)
# 从Workbook对象中获取Sheet对象
wt_sheet = wt_book.get_sheet(0)
# 循环处理每一行第一列数据, 修改其中的内容
for row in range(rd_sheet.nrows):
    wt_sheet.write(row, 0, '修改内容')
wt_book.save('xlutils_test_copy.xls')

print(type(rd_book))
print(type(wt_book))
