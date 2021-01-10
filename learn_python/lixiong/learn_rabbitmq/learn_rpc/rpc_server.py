#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 下午 10:43:12
# @Author  : zzlion
# @File    : rpc_server.py
# @Reference:

import pika

credentials = pika.PlainCredentials('zzlion', 'lixiong6660')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='47.96.156.199', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    n = int(body)
    print(" [.] fib({})".format(n))
    response = fib(n)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1) # 负载均衡的设置
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
