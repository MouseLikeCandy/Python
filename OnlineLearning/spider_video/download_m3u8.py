# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：download_m3u8.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/12/15 12:12 
"""
'''
爬取 .m3u8 视频文件涉及到以下步骤：

1.获取 .m3u8 文件的 URL。
2.下载并解析 .m3u8 文件，获取媒体片段（.ts 文件）的 URL 列表。
3.逐个下载媒体片段。
4.如果 .m3u8 文件中包含加密信息，需要获取解密密钥并在下载时进行解密。
'''
import requests
from Crypto.Cipher import AES   # pip install pycryptodome
from Crypto.Util.Padding import unpad
from urllib.parse import urljoin

# 下载并解密m3u8
def download_and_decrypt_m3u8(m3u8_url, output_folder='./'):
    if m3u8_url:
        # Step 1: 获取 .m3u8 文件的内容
        response = requests.get(m3u8_url)
    else:
        print(f'm3u8_url is{m3u8_url}')
    if response.status_code == 200:
        m3u8_content = response.text
        print(m3u8_content)
    else:
        print(f"Failed to fetch .m3u8 content. Status code: {response.status_code}")
        return

    # # Step 2: 解析 .m3u8 文件，获取媒体片段的 URL 列表和加密信息
    # base_url = m3u8_url.rsplit('/', 1)[0]
    # ts_urls, encryption_info = parse_m3u8(m3u8_content, base_url)
    #
    # # Step 3: 获取密钥内容
    # key_url = encryption_info.get('URI', '')
    # key = get_key(key_url)
    #
    # if key is not None:
    #     # Step 4: 解密并保存每个媒体片段
    #     for i, ts_url in enumerate(ts_urls):
    #         encrypted_ts = requests.get(ts_url).content
    #         decrypted_ts = decrypt_aes(encrypted_ts, key, encryption_info.get('IV'))
    #         ts_filename = f"segment_{i + 1}.ts"
    #         ts_path = f"{output_folder}/{ts_filename}"
    #         with open(ts_path, 'wb') as ts_file:
    #             ts_file.write(decrypted_ts)
    #         print(f"Downloaded and decrypted {ts_filename}")

def parse_m3u8(m3u8_content, base_url):
    ts_urls = []
    encryption_info = {}
    for line in m3u8_content.split('\n'):
        if line.startswith('#EXT-X-KEY'):
            encryption_info = parse_encryption_info(line)
        elif line.endswith('.ts'):
            ts_urls.append(urljoin(base_url, line.strip()))
    return ts_urls, encryption_info

def parse_encryption_info(line):
    # 在实际情况中，你可能需要编写一个更复杂的解析函数，以提取加密信息
    # 这里简化为只提取 URI 和 IV
    encryption_info = {}
    parts = line.split(',')
    for part in parts:
        key, value = part.split('=')
        encryption_info[key] = value.strip('"')
    return encryption_info

def get_key(key_url):
    # 发送请求获取密钥内容
    response = requests.get(key_url)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to fetch key. Status code: {response.status_code}")
        return None

def decrypt_aes(encrypted_data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data


if __name__ == "__main__":
    # m3u8_url = "https://example.com/video/stream.m3u8"
    m3u8_url = "https://vip.lz-cdn.com/20220316/41_12c4e19e/1200k/hls/mixed.m3u8"
    m3u8_url01 = "https://vip.lz-cdn.com/20220316/41_12c4e19e/1200k/hls/mixed.m3u8"
    m3u8_url02 = "https://vip.lz-cdn.com/20220316/42_fe2272ce/1200k/hls/mixed.m3u8"
    output_folder = "./output_folder"
    download_and_decrypt_m3u8(m3u8_url, output_folder)
