import time
import pika

amqp_config = {
    'user': 'guest',
    'password': 'guest',
    'host': 'localhost',
    'port': '5672'
}

connection = pika.BlockingConnection(
    pika.URLParameters(
        'amqp://{user}:{password}@{host}:{port}/%2F'.format(**amqp_config)))
channel = connection.channel()
channel.queue_declare('hello')

count = 1

try:
    while True:
        message = 'Hello World! %s' % count

        print('sent ', message)
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=message)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt:
    connection.close()
