# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：SmsForwarder_server.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/26 12:39 
"""
from flask import Flask, request, jsonify
from loguru import logger


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def receive():
    sms_content = request.form.get('content')
    logger.debug(f'received {sms_content}')
    # 解析内容并将其保存到db或mq
    return jsonify(status='success')


if __name__ == '__main__':
    app.run(debug=True)