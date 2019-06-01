import pika

exchangeserver = str('192.168.1.222')

credentials = pika.PlainCredentials('homebutler', 'homebutler')
parameters = pika.ConnectionParameters(exchangeserver,5672,'/', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='homebutler')

channel.basic_publish(exchange='',routing_key='homebutler',body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()