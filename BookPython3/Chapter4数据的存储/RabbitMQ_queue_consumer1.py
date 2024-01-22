# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：RabbitMQ_queue_consumer.py.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/10 15:48 
"""
import pika
import requests
import pickle

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape_queue'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
session = requests.Session()

# 清除队列（删除所有消息）
# channel.queue_delete(queue='scrape_queue')

# channel.queue_declare(
#     queue=QUEUE_NAME,
#     # arguments={'x-max-priority': MAX_PRIORITY},
#     durable=True
# )

def scrape(request):
    try:
        response = session.send(request.prepare())
        print(f'success scraped {response.url}')
    except requests.RequestException:
        print(f'error occurred when scraping {request.url}')


while True:
    method_frame, header, body = channel.basic_get(
        queue=QUEUE_NAME, auto_ack=True
    )
    if body:
        request = pickle.loads(body)
        print(f'Get {request}')
        scrape(request)