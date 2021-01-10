#!/usr/bin/env python3
# coding:utf-8

import pika

class MyMq:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, host=None, user=None, password=None, exchange='', queue=None, routing_key=None):
        if not user:
            user = 'zzlion'
            password = 'lixiong6660'
        host = host or '47.96.156.199'
        credentials = pika.PlainCredentials(user, password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=credentials))
        self.channel = self.connection.channel()

        self.exchange = exchange
        self.queue = queue
        self.routing_key = routing_key


    def set_queue(self, exclusive=False, durable=True):
        self.channel.queue_declare(queue=self.queue, exclusive=exclusive, durable=durable)
        return

    def delete_queue(self, queue):
        self.channel.queue_delete(queue=queue)

    def set_exchange(self, exchange_type='topic'):
        # exchange_type e.g. direct topic headers fanout
        self.channel.exchange_declare(exchange=self.exchange, exchange_type=exchange_type)
        return self.exchange

    def delete_exchange(self):
        self.channel.exchange_delete(exchange=self.exchange)

    def bind_routing_key(self):
        self.channel.queue_bind(exchange=self.exchange, queue=self.queue, routing_key=self.routing_key)

    def publish(self, body, delivery_mode=None):
        self.set_exchange()
        properties = pika.BasicProperties(delivery_mode= delivery_mode or 2) # 2 make message persistent
        self.channel.basic_publish(
            exchange=self.exchange, routing_key=self.routing_key, body=body, properties=properties
        )

    def callback(self, ch, method, properties, body):
        # default consume callback
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def prepare_channel(self):
        self.set_exchange()
        self.set_queue()
        self.bind_routing_key()

    def consume(self, auto_ack=True, on_message_callback=callback):
        self.prepare_channel()
        self.channel.basic_consume(queue=self.queue, auto_ack=auto_ack, on_message_callback=on_message_callback)
        self.channel.start_consuming()

    def __del__(self):
        self.connection.close()


class Client:

    def __init__(self):
        mq = MyMq(exchange='log', routing_key='english')
        mq.publish(body='hello world', delivery_mode=1)


class Server:

    def callback(self, ch, method, properties, body):
        print(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def __init__(self):
        mq = MyMq(exchange='log', queue='test_consumer', routing_key='english')
        mq.consume(on_message_callback=self.callback)


if __name__ == '__main__':
    # client = Client()
    server = Server()
