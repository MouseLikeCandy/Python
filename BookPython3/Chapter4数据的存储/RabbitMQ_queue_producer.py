# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：RabbitMQ_queue_producer.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/10 15:35 
"""
import pika

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 清除队列（删除所有消息）
channel.queue_delete(queue='scrape')

channel.queue_declare(
    queue=QUEUE_NAME,
    arguments={
        'x-max-priority': MAX_PRIORITY
    },
    durable=True
)

# channel.basic_publish(
#     exchange='',
#     routing_key=QUEUE_NAME,
#     body='Hello World!'
# )

while True:
    data, priority = input().split()
    channel.basic_publish(
        exchange='',
        routing_key=QUEUE_NAME,
        properties=pika.BasicProperties(priority=int(priority), delivery_mode=2),
        body=data
    )
    print(f'Put {data}')
