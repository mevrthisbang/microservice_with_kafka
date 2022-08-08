# amqps://iemrcyyb:Xv0e7mmtfoXAOzyCgRSHF17e58vzkZxZ@armadillo.rmq.cloudamqp.com/iemrcyyb 
import json
from main import Product, db
from kafka import KafkaConsumer

# params = pika.URLParameters('amqps://iemrcyyb:Xv0e7mmtfoXAOzyCgRSHF17e58vzkZxZ@armadillo.rmq.cloudamqp.com/iemrcyyb');

# connection = pika.BlockingConnection(params)

# channel = connection.channel()

# channel.queue_declare(queue='main')
consumer = KafkaConsumer(
        'Topic1',
        bootstrap_servers=['kafka:9093'],
        auto_offset_reset='earliest'
)
for message in consumer:
    byte_body = message.value
    body = byte_body.decode('utf8').replace("'", '"')
    data = json.loads(body)
    if data.get('method') == 'product_created':
        product = Product(id=data['body']['id'], title=data['body']['title'], image=data['body']['image'])
        try:
            db.session.add(product)
            db.session.commit()
            print('Product created')
        except Exception as e:
            db.session.rollback()
        finally:
            db.session.close()
            continue
    elif data.get('method') == 'product_updated':
        product = Product.query.get(data['body']['id'])
        product.title = data['body']['title']
        product.image = data['body']['image']
        db.session.commit()
        print('Product updated')
    elif data.get('method') == 'product_deleted':
        product = Product.query.get(data['body'])
        db.session.delete(product)
        db.session.commit()
        print('Product deleted')
# def callback(ch, method, properties, body):
#     print('Received from admin')
#     data = json.loads(body)
#     print(data)

#     if properties.content_type == 'product_created':
#         product = Product(id=data['id'], title=data['title'], image=data['image'])
#         db.session.add(product)
#         db.session.commit()
#         print('Product created')
#     elif properties.content_type == 'product_updated':
#         product = Product.query.get(data['id'])
#         product.title = data['title']
#         product.image = data['image']
#         db.session.commit()
#         print('Product updated')
#     elif properties.content_type == 'product_deleted':
#         product = Product.query.get(data)
#         db.session.delete(product)
#         db.session.commit()
#         print('Product deleted')

# channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

# print('Started Consuming')

# channel.start_consuming()

# channel.close()