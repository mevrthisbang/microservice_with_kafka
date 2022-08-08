# amqps://iemrcyyb:Xv0e7mmtfoXAOzyCgRSHF17e58vzkZxZ@armadillo.rmq.cloudamqp.com/iemrcyyb 
# import pika, json
import json
from kafka import KafkaProducer
# params = pika.URLParameters('amqps://iemrcyyb:Xv0e7mmtfoXAOzyCgRSHF17e58vzkZxZ@armadillo.rmq.cloudamqp.com/iemrcyyb');

# connection = pika.BlockingConnection(params)

# channel = connection.channel()

# def publish(method, body):
#     properties = pika.BasicProperties(method)
#     channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
def serializer(message):
    return json.dumps(message).encode('utf-8')

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['kafka:9093'],
    value_serializer=serializer
)


def publish(body):
    # properties = pika.BasicProperties(method)
    # channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
    producer.send('Topic2', value=body)
    producer.flush()
