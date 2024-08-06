import threading

from src.broker import Broker

# Setup broker addresses (same as used in your producer)
broker1 = Broker('127.0.0.1', 9092)
broker2 = Broker('127.0.0.1', 9093)
brokers = [broker1, broker2]

# Start each broker on a separate thread
threads = []
for broker in brokers:
    t = threading.Thread(target=broker.start, args=())
    t.start()
    threads.append(t)

for t in threads:
    t.join()
