from chaojiying import Chaojiying

USERNAME = 'MouseLikeCandy'
PASSWORD = 'HaveChance2LOVE'
SOFT_ID = '957502'
CAPTCHA_KIND = '1006'   # 验证码类型 http://www.chaojiying.com/price.html
FILE_NAME = 'captcha1.png'
client = Chaojiying(USERNAME, PASSWORD, SOFT_ID)
result = client.post_pic(open(FILE_NAME, 'rb').read(), CAPTCHA_KIND)
print(result)