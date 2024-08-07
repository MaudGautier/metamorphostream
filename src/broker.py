import pickle
import socket
from io import BytesIO

from src.id_generator import BrokerIdGenerator


class Broker:
    Host = str
    Port = str

    def __init__(self, host: Host, port: Port):
        self.host = host
        self.port = port
        self.ID = next(BrokerIdGenerator(0))

    def start(self):
        """
        Starts the broker and makes it listen for messages indefinitely.
        """

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Broker {self.ID} listening on {self.host}:{self.port}")

            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    data = conn.recv(1024)

                    byte_stream = BytesIO(data)
                    while True:
                        try:
                            # Each call to pickle.load() reads one object from the stream
                            message = pickle.load(byte_stream)
                            print(f"Received message on {self.host}:{self.port} (Broker {self.ID}): {message}")
                        except EOFError:
                            # No more objects in the stream
                            break
