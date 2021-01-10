#!/usr/bin/env python3
# coding:utf-8

import pika
from .my_mq import MyMq

credentials = pika.PlainCredentials('zzlion', 'lixiong6660')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='47.96.156.199', credentials=credentials))
channel = connection.channel()

result = channel.queue_declare(queue='', exclusive=True)
callback_queue = result.method.queue

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n -2)

def on_request(ch, method, props, body):
    n = int(body)
    print(n)
    response = fib(n)

    channel.basic_publish(exchange='', routing_key='rpc_queue', properties=pika.BasicProperties(reply_to=callback_queue, ),
                          body=str(response))

channel.basic_qos(prefetch_count=1)
channel.basic_consume()
