# Metamorphostreams

Metamorphostreams is a toy project aiming at re-implementing [Kafka](https://kafka.apache.org/) from scratch in Python.
The goal of this project was purely educational: to understand the main components of Kafka and the core principles
behind its implementation.

At this point, it is a work in progress: so far, only a very basic producer and broker have been implemented.
Hopefully, I will add some more bricks to this project in the future.

## Getting started

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Create the path configuration file (needed only once)
python setup.py
```

### Test scripts

To see how a producer communicates with brokers:

- launch broker servers in one terminal window:

```bash
python scripts/launch_brokers.py
```

- launch a producer in another window:

```bash
python scripts/launch_producer.py
```

Once that is set up, the producer sends messages to the brokers:

```text
Sent to ('127.0.0.1', 9093): b'\x80\x04\x95M\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\ttimestamp\x94GA\xd9\xb2\xaf\xf9j\xc7\x9b\x8c\x03key\x94C\x05key-2\x94\x8c\x05value\x94C\x1aThis is a test message: 2.\x94u.\x80\x04\x95M\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\ttimestamp\x94GA\xd9\xb2\xaf\xf9\xebn\xeb\x8c\x03key\x94C\x05key-4\x94\x8c\x05value\x94C\x1aThis is a test message: 4.\x94u.\x80\x04\x95M\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\ttimestamp\x94GA\xd9\xb2\xaf\xfa+\x93\x10\x8c\x03key\x94C\x05key-5\x94\x8c\x05value\x94C\x1aThis is a test message: 5.\x94u.'
Sent to ('127.0.0.1', 9092): b'\x80\x04\x95M\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\ttimestamp\x94GA\xd9\xb2\xaf\xf9*n]\x8c\x03key\x94C\x05key-1\x94\x8c\x05value\x94C\x1aThis is a test message: 1.\x94u.\x80\x04\x95M\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\ttimestamp\x94GA\xd9\xb2\xaf\xf9\xab\x1c\xe2\x8c\x03key\x94C\x05key-3\x94\x8c\x05value\x94C\x1aThis is a test message: 3.\x94u.\x80\x04\x95M\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\ttimestamp\x94GA\xd9\xb2\xaf\xfak\xba\xc3\x8c\x03key\x94C\x05key-6\x94\x8c\x05value\x94C\x1aThis is a test message: 6.\x94u.'
```

Those messages are correctly received and decoded by the brokers:

```text
Received message on 127.0.0.1:9093 (Broker 1): {'timestamp': 1724563429.668433, 'key': b'key-2', 'value': b'This is a test message: 2.'}
Received message on 127.0.0.1:9093 (Broker 1): {'timestamp': 1724563431.678645, 'key': b'key-4', 'value': b'This is a test message: 4.'}
```

## Next steps

- [ ] High-level: Implement a high-level kafka consumer
- [ ] Kafka components: Partition, Topic, Cluster
- [ ] Persistent storage: save messages on disk in each partition, add offsets on messages per partition
- [ ] Kafka concepts: recall offsets processed by each consumer group, consumer sends committed offset after polling and
  processing, ...
- [ ] Distributed: Handle synchronization when multiple brokers or consumer groups
