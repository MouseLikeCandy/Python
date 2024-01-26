from chaojiying import Chaojiying

USERNAME = 'MouseLikeCandy'
PASSWORD = 'HaveChance2LOVE'
SOFT_ID = '957502'
CAPTCHA_KIND = '6004'
FILE_NAME = 'captcha4.png'
client = Chaojiying(USERNAME, PASSWORD, SOFT_ID)
result = client.post_pic(open(FILE_NAME, 'rb').read(), CAPTCHA_KIND)
print(result)
'''
{'err_no': 0, 'err_str': 'OK', 'pic_id': '1239613511284330007', 'pic_str': '大象', 'md5': '799e99a3bad3826cff3a459adeee0224'}
'''