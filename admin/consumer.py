# amqps://iemrcyyb:Xv0e7mmtfoXAOzyCgRSHF17e58vzkZxZ@armadillo.rmq.cloudamqp.com/iemrcyyb 

import json
import os
import django
from kafka import KafkaConsumer
# import pika
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

consumer = KafkaConsumer(
        'Topic2',
        bootstrap_servers=['kafka:9093'],
        auto_offset_reset='earliest'
)
for message in consumer:
    print('Received from main')
    data = message.value
    id = json.loads(data.decode("utf-8").replace("'", '"'))
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')

# params = pika.URLParameters('amqps://iemrcyyb:Xv0e7mmtfoXAOzyCgRSHF17e58vzkZxZ@armadillo.rmq.cloudamqp.com/iemrcyyb');

# connection = pika.BlockingConnection(params)

# channel = connection.channel()

# channel.queue_declare(queue='admin')

# def callback(ch, method, properties, body):
#     print('Received from main')
#     id = json.loads(body.decode("utf-8"))
#     print(id)
#     product = Product.objects.get(id=id)
#     product.likes = product.likes + 1
#     product.save()
#     print('Product likes increased!')


# channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

# print('Started Consuming')

# channel.start_consuming()

# channel.close()