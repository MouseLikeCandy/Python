# -*- coding: UTF-8 -*-
"""
@Project ：Python 
@File    ：RabbitMQ_queue_consumer.py.py
@IDE     ：PyCharm 
@Author  ：Ning
@Date    ：2024/1/10 15:48 
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
    arguments={'x-max-priority': MAX_PRIORITY},
    durable=True
)

def callback(ch, method, properties, body):
    print(f'Get {body}')

# channel.basic_consume(
#     queue='scrape',
#     auto_ack=True,
#     on_message_callback=callback
# )
#
# channel.start_consuming()


while True:
    input()
    method_frame, header, body = channel.basic_get(
        queue=QUEUE_NAME, auto_ack=True
    )
    if body:
        print(f'Get {body}')