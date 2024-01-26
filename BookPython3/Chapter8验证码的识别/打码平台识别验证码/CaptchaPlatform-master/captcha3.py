import cv2
from chaojiying import Chaojiying

# USERNAME = 'MouseLikeCandy'
# PASSWORD = 'HaveChance2LOVE'
# SOFT_ID = '957502'
# CAPTCHA_KIND = '9101'
# FILE_NAME = 'captcha3.png'
# client = Chaojiying(USERNAME, PASSWORD, SOFT_ID)
# result = client.post_pic(open(FILE_NAME, 'rb').read(), CAPTCHA_KIND)
# print(result)


image = cv2.imread('captcha3.png')
image = cv2.circle(image, (179, 55), radius=10, color=(0, 0, 255), thickness=-1)
# image = cv2.circle(image, (191, 540), radius=10,
#                    color=(0, 0, 255), thickness=-1)
# image = cv2.circle(image, (293, 440), radius=10,
#                    color=(0, 0, 255), thickness=-1)
# image = cv2.circle(image, (350, 511), radius=10,
#                    color=(0, 0, 255), thickness=-1)
cv2.imwrite('captcha3_label.png', image)
