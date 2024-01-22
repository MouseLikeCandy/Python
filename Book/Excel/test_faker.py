from faker import Faker

fake = Faker(locale='zh_CN')

print('姓名：', fake.name())
print('国家:', fake.country())
print('省份:', fake.province())
print('地址：', fake.address())
print('公司：', fake.company())
print('邮编：', fake.postcode())

print('身份证号：', fake.ssn(min_age=18, max_age=58))
print('出生日期：', fake.date(pattern="%Y-%m-%d", end_datetime=None))
print('电话：', fake.phone_number())
print('邮箱：', fake.email())
print('银行卡号：', fake.credit_card_number(card_type=None))
