# amqps://iemrcyyb:Xv0e7mmtfoXAOzyCgRSHF17e58vzkZxZ@armadillo.rmq.cloudamqp.com/iemrcyyb 
import json
from kafka import KafkaProducer

# params = pika.URLParameters('amqps://iemrcyyb:Xv0e7mmtfoXAOzyCgRSHF17e58vzkZxZ@armadillo.rmq.cloudamqp.com/iemrcyyb');

# connection = pika.BlockingConnection(params)

# channel = connection.channel()
# Messages will be serialized as JSON 
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
    producer.send('Topic1', value=body)
    producer.flush()
