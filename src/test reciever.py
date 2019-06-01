#!/usr/bin/env python
import pika

exchangeserver = str('192.168.1.222')

credentials = pika.PlainCredentials('homebutler', 'homebutler')
parameters = pika.ConnectionParameters(exchangeserver, 5672, '/', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='homebutler')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback ,queue='homebutler',   no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
