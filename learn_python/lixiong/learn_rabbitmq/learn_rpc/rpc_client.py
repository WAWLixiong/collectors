#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 下午 10:23:29
# @Author  : zzlion
# @File    : rpc_client.py
# @Reference:
import pika
import uuid
import time


class FibonacciRpcClient(object):

    def __init__(self):
        credentials = pika.PlainCredentials('zzlion', 'lixiong6660')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='47.96.156.199', credentials=credentials))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body
        time.sleep(10)

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)
