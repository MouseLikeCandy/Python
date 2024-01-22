# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：RabbitMQ_queue_producer.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/10 15:35 
"""
import pika
import requests
import pickle

TOTAL = 100
QUEUE_NAME = 'scrape_queue'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 清除队列（删除所有消息）
# channel.queue_delete(queue='scrape_queue')

channel.queue_declare(
    queue=QUEUE_NAME,
    durable=True
)

for i in range(1, TOTAL + 1):
    url = f'https://ssr1.scrape.center/detail/{i}'
    request = requests.Request('GET', url)
    channel.basic_publish(
        exchange='',
        routing_key=QUEUE_NAME,
        properties=pika.BasicProperties(delivery_mode=2),
        body=pickle.dumps(request)
    )
    print(f'Put request of {url}')
