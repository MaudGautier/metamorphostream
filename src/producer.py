import pickle
import random
import socket


class KafkaProducer:
    def __init__(self, brokers_addresses):
        self.brokers_addresses = brokers_addresses

    def _send_to_broker(self, broker_address, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((broker_address.split(':')[0], int(broker_address.split(':')[1])))
            sock.sendall(pickle.dumps(message))
            print(f"Sent to {broker_address}: {message}")

    def send(self, topic, key, data):
        broker_address = random.choice(self.brokers_addresses)
        self._send_to_broker(broker_address, data)
