from chaojiying import Chaojiying

# USERNAME = 'MouseLikeCandy'
# PASSWORD = 'HaveChance2LOVE'
# SOFT_ID = '957502'
# CAPTCHA_KIND = '9004'
# FILE_NAME = 'captcha2.png'
# client = Chaojiying(USERNAME, PASSWORD, SOFT_ID)
# result = client.post_pic(open(FILE_NAME, 'rb').read(), CAPTCHA_KIND)
# print(result)

'''
{'err_no': 0, 'err_str': 'OK', 'pic_id': '1239613311284330002', 'pic_str': '102,153|228,149', 'md5': '14d7121615d2756728215b35f221b5ea'}
识别出中心坐标
'''

import cv2

image = cv2.imread('captcha2.png')
image = cv2.circle(image, (102, 153), radius=10, color=(0, 0, 255), thickness=-1)
image = cv2.circle(image, (228, 149), radius=10, color=(0, 0, 255), thickness=-1)
cv2.imwrite('captcha2_label.png', image)
