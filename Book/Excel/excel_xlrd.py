"""
xlrd    读取工作簿     *.xls/*.xlsx
xlwt    写入工作簿     *.xls

EXCEL:
*.xls 2003
*.xlsx 2007
Book工作簿 -> Sheet工作表 -> Cell单元格

xlrd:
1.使用 xlrd.open_workbook 方法载入工作簿
2.使用 sheet_by_index 等方法选取工作簿中的某个工作表
3.使用 cell_value 方法获取工作表中某个单元格中的信息
"""
import xlrd

book = xlrd.open_workbook('员工数据.xls')  # 读取工作簿

sheet = book.sheets()[0]
sheet = book.sheet_by_index(0)
sheer = book.sheet_by_name('员工导入数据')

# sheet.cell_value(row, col)
sheet.cell_value(1, 0)
sheet.cell_value(0, 1)

sheet_num = book.nsheets  # 获取工作簿中工作表数目
sheet_names = book.sheet_names()  # 获取工作簿中工作表名称列表
row_num = sheet.nrows  # 获取工作表中有值单元格的行数
col_num = sheet.ncols  # 获取工作表中有值单元格的列数

sheets = book.sheets()  # 获取工作簿中所有的工作表的列表
for sheet in sheets:
    row_num = sheet.nrows
    col_num = sheet.ncols
    for row in range(row_num):
        for col in range(col_num):
            # 输出单元格中的内容
            print(sheet.cell_value(row, col), end='\t\t')
        print("-" * 100)

time_value1 = sheet.cell_value(1, 7)
time_value2 = sheet.cell_value(15, 7)
print(f'time_value1 = {time_value1}')
print(f'time_value2 = {time_value2}')

# 将读入的日期数据转为元祖的形式
time_tuple = xlrd.xldate_as_tuple(time_value1, 0)

time_str1 = '-'.join(str('%02d' % i) for i in time_tuple[0:3])
time_str2 = ':'.join(str('%02d' % i) for i in time_tuple[3:6])
print(f'time_str = {time_str1 + " " + time_str2}')

time_str = f'%d-%0.2d-%0.2d %0.2d:%0.2d:%0.2d' \
           % (time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4], time_tuple[5])
print(f'time_str = {time_str}')
time_str = ''
# for time in time_tuple:
#     time_str += str(time)

for i in range(len(time_tuple)):
    if i < 2:
        time_str = time_str + str(time_tuple[i]) + '-'
    elif (i > 2) and (i < 5):
        time_str = time_str + str(time_tuple[i]) + ':'
    else:
        time_str = time_str + str(time_tuple[i]) + ' '

print(f'time_str = {time_str}')
# 将日期数据转为datatime对象
time_datetime = xlrd.xldate_as_datetime(time_value1, 0)
# 将datetime对象格式化为对应的字符串
time_str = time_datetime.strftime('%Y-%m-%d %H:%M:%S')
print(f'time_str = {time_str}')
