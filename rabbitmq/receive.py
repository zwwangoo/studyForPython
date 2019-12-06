import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

print('Waiting for Message.')


def callback(ch, method, properties, body):

    print('Received %r' % (body,))
    time.sleep(4)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 告诉生产者，消息处理完成


# 类似权重，按能力分发，如果有一个消息，就不在给你发
# channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_message_callback=callback,
                      queue='hello')

channel.start_consuming()
