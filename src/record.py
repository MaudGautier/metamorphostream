import struct
import time
from typing import Tuple, Optional


class Record:
    Key = bytes
    Value = bytes

    def __init__(self, key: Key or None, value: Value or None, offset: int, timestamp: Optional[float] = None):
        self.key = key
        self.value = value
        self.timestamp = timestamp if timestamp else time.time()
        self.offset = offset

    def __eq__(self, other):
        if not isinstance(other, Record):
            return NotImplemented
        return (self.key == other.key and
                self.value == other.value and
                self.offset == other.offset and
                self.timestamp == other.timestamp)

    @property
    def key_size(self) -> int or None:
        return len(self.key) if self.key is not None else -1

    @property
    def value_size(self) -> int or None:
        return len(self.value) if self.value is not None else -1

    @property
    def size(self) -> int:
        return len(self.serialize())

    def serialize(self) -> bytes:
        serialized_key_size = struct.pack("i", self.key_size)
        serialized_value_size = struct.pack("i", self.value_size)
        serialized_timestamp = struct.pack("d", self.timestamp)
        serialized_offset = struct.pack("I", self.offset)
        return serialized_offset + serialized_timestamp + serialized_key_size + self.key + serialized_value_size + self.value

    @staticmethod
    def deserialize_variable_length_part(offset: int, data: bytes) -> Tuple[Key or None, int]:
        key_size_start, key_size_end = offset, offset + 4
        key_size = struct.unpack("i", data[key_size_start:key_size_end])[0]

        if key_size == -1:
            return None, key_size_end

        key_start, key_end = key_size_end, key_size_end + key_size
        key = data[key_start:key_end]

        return key, key_end

    @classmethod
    def deserialize(cls, data: bytes):
        offset_start, offset_end = 0, 4
        offset = struct.unpack("I", data[offset_start:offset_end])[0]
        timestamp_start, timestamp_end = offset_end, offset_end + 8
        timestamp = struct.unpack("d", data[timestamp_start:timestamp_end])[0]
        key, key_end = cls.deserialize_variable_length_part(data=data, offset=timestamp_end)
        value, _ = cls.deserialize_variable_length_part(data=data, offset=key_end)

        return cls(offset=offset, timestamp=timestamp, key=key, value=value)
