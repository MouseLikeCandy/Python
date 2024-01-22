# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：SPLASH_render.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/18 16:10 
"""
import requests
from urllib.parse import quote


url = 'http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
response = requests.get(url)
with open('image/jingdong.png', 'wb') as file:
    file.write(response.content)

lua = '''
function main(splash)
    return 'hello'
end
'''

lua = '''
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://www.httpbin.org/get")
    return {html=treat.as_string(response.body),
        url=response.url,
        status=response.status
    }
end
'''

url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)
