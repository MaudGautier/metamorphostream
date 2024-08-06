import time

from src.producer import KafkaProducer

brokers_addresses = ['127.0.0.1:9092', '127.0.0.1:9093']
producer = KafkaProducer(brokers_addresses)

count = 0
while True:
    count += 1
    topic = 'my-topic'
    key = f'key-{count}'
    data = f'This is a test message: {count}.'
    producer.send(topic, key, data)
    time.sleep(1)
