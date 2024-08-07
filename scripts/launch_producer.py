import time

from src.producer import KafkaProducer, ProducerRecord

brokers_addresses = [('127.0.0.1', 9092), ('127.0.0.1', 9093)]
producer = KafkaProducer(brokers_addresses=brokers_addresses,
                         key_serializer=lambda key: key.encode('utf-8'),
                         value_serializer=lambda value: value.encode('utf-8')
                         )

count = 0
while True:
    count += 1
    topic = 'my-topic'
    key = f'key-{count}'
    data = f'This is a test message: {count}.'
    record = ProducerRecord(key=key, value=data)
    producer.send(topic=topic, record=record)
    time.sleep(1)
