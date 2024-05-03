from typing import BinaryIO


class RecordsFile:
    def __init__(self, path: str, file: BinaryIO):
        self.path = path
        self.file = file
        # TODO: add index ??

    @classmethod
    def create(cls, path: str):
        file = open(path, "wb")

        return cls(path=path, file=file)

    def close(self):
        self.file.close()

    def write(self, data: bytes):
        self.file.write(data)
