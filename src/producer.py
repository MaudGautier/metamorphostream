import pickle
import socket
import time
from hashlib import sha256
from typing import Optional


class ProducerRecord:
    Key = bytes
    Value = bytes

    def __init__(self, key: Key or None, value: Value or None, timestamp: Optional[float] = None):
        self.key = key
        self.value = value
        self.timestamp = timestamp if timestamp else time.time()


class KafkaProducer:
    def __init__(self, brokers_addresses, key_serializer, value_serializer):
        self.brokers_addresses = brokers_addresses
        self.key_serializer = key_serializer
        self.value_serializer = value_serializer

        # Assuming one partition per broker for simplicity
        self.partitions = {partitionId: broker_address
                           for partitionId, broker_address in enumerate(self.brokers_addresses)}
        self.buffers = {partition: [] for partition in self.partitions}
        self._max_buffer_size = 3

    def _get_broker_address(self, partition_id):
        return self.partitions[partition_id]

    def _serialize(self, record: ProducerRecord):
        """Creates a serialized message complying with the protocol between producers and brokers.
        """
        serialized_key = self.key_serializer(record.key)
        serialized_value = self.value_serializer(record.value)
        message = {'timestamp': record.timestamp, 'key': serialized_key, 'value': serialized_value}
        serialized_message = pickle.dumps(message)
        return serialized_key, serialized_message

    def _choose_partition(self, serialized_key: bytes):
        """Choose a partition based on the hash of the key (default method)."""
        hash_value = sha256(serialized_key).digest()
        return int.from_bytes(hash_value, byteorder='big') % len(self.partitions)

    def _should_flush(self, partition):
        return len(self.buffers[partition]) >= self._max_buffer_size

    def _flush(self, partition):
        """Send buffered messages in partition to the broker designated for this partition."""
        data = b''.join(self.buffers[partition])
        broker_address = self._get_broker_address(partition)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(broker_address)
            sock.sendall(data)
            print(f"Sent to {broker_address}: {data}")
        self.buffers[partition] = []

    def _send_to_buffer(self, partition, message):
        """Adds message to the correct buffer and sends the full buffer.
        """
        self.buffers[partition].append(message)
        if self._should_flush(partition):
            self._flush(partition)

    def send(self, topic, record: ProducerRecord):
        """Simulate sending a message to a Kafka broker."""
        serialized_key, serialized_message = self._serialize(record)
        partition = self._choose_partition(serialized_key)
        self._send_to_buffer(partition, serialized_message)

    def close(self):
        for partition in self.partitions:
            self._flush(partition)
