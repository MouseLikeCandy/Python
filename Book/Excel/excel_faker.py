"""
xlrd    读取工作簿     *.xls/*.xlsx
xlwt    写入工作簿     *.xls

EXCEL:
*.xls 2003
*.xlsx 2007
工作簿 -> 工作表 -> 单元格
"""
import xlwt
from faker import Faker  # 从faker模块导入Faker这个类

# 实例化，保存到变量fake中
fake = Faker(locale='zh_CN')


def save_to_excel():
    # 新建工作簿
    work_book = xlwt.Workbook(encoding='utf-8')
    # 添加工作表
    work_sheet = work_book.add_sheet('员工导入数据')
    excel_head = ['员工(必填)', '企业名称(必填)', '手机号(必填)', '地址', '邮编', '国家', '身份证号', '入职时间', '省份', '邮箱', '银行卡号']
    for h in range(len(excel_head)):
        # 写入单元格，参数：写入第i行j列的单元格（从0开始计数）
        work_sheet.write(0, h, excel_head[h])

    # 添加构造的随机数据
    for i in range(1000):
        # 随机姓名
        name = fake.name()
        country = fake.country()
        province = fake.province()
        address = fake.address()
        company = fake.company()
        postcode = fake.postcode()
        ssn = fake.ssn(min_age=18, max_age=58)
        date = fake.date_time().strftime("%Y-%m-%d %H:%M:%S")
        phone_number = fake.phone_number()
        email = fake.email()
        card_number = fake.credit_card_number(card_type=None)

        work_sheet.write(i + 1, 0, name)
        work_sheet.write(i + 1, 1, company)
        work_sheet.write(i + 1, 2, phone_number)
        work_sheet.write(i + 1, 3, address)
        work_sheet.write(i + 1, 4, country)
        work_sheet.write(i + 1, 5, postcode)
        work_sheet.write(i + 1, 6, ssn)
        work_sheet.write(i + 1, 7, date)
        work_sheet.write(i + 1, 8, province)
        work_sheet.write(i + 1, 9, email)
        work_sheet.write(i + 1, 10, card_number)
    # 保存工作簿
    work_book.save('员工数据.xls')


if __name__ == '__main__':
    save_to_excel()
