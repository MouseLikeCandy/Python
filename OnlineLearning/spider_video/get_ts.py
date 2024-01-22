'''
实时流媒体/伪流媒体
http/https
音频文件.acc文件
视频文件.H264     分割成 m3u8文件和ts文件
'''

# 1. 找ts文件
# Network   搜索.ts 小片段

# 2. 找m3u8文件
# Network   搜索.m3u8

# 3. 使用ffmpeg


import requests
import re
import os
filePath = r'./ts04/'
file_list = []
# print(os.listdir(filePath))
for file in os.listdir(filePath):
    new_str = file.split('.')
    if new_str[1] == 'ts':
        print(new_str[0])
        new_file = '%06d' % int(new_str[0]) + '.ts'
        print(new_file)
        os.rename(os.path.join(filePath, file), os.path.join(filePath, new_file))

file_list = sorted(os.listdir(filePath))
# 生成一个可以给ffmpeg使用的文本文件
with open(r'./ts04/file_list.txt', 'w+') as f:
    for file in file_list:
        if file.split('.')[1] == 'ts':
            f.write("file '{}'\n".format(file))






