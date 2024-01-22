# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：test_JavaScript.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2023/12/21 7:46 
"""
import requests
import execjs

js_code = """
// Your JavaScript code here
var url = window.location.href;
// ...
"""

'''
Python 调用 js 文件，报 execjs._exceptions.ProgramError: SyntaxError: 缺少 ';' 错误
原因：execjs 默认使用了windows的JScript 引擎导致的
解决办法：
安装nodejs，下载地址：https://nodejs.org/zh-cn/download/
默认安装，默认配置环境变量即可
关闭IDLE
再次打开IDLE,打开相应的PY文件即可正常
'''

print(f"JS运行时: {execjs.get().name}")


# 获取JavaScript内容
js_url = "https://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/hls.js/0.8.8/hls.light.min.js"
js_content = requests.get(js_url).text
# 解析JavaScript代码
ctx = execjs.compile(js_content)
# 提取变量值
variable_name = "MANIFEST_LOADING"
variable_value = ctx.eval(variable_name)
print(f"The value of {variable_name} is: {variable_value}")


try:
    # 在 compile 函数中不指定运行时
    ctx = execjs.compile(js_code)
    href_value = ctx.eval('window.location.href')
    print(f"The value of window.location.href is: {href_value}")
except execjs.RuntimeError as e:
    print(f"Error evaluating JavaScript: {e}")
