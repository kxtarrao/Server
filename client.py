import socket

class Client():
    HEADER = 64
    FORMAT = "utf-8"
    DISCONNECT_MESSAGE = "!DISCONNECT"
    ADDR = ("192.168.0.2",5050)

    @classmethod
    def send(cls,msg):
        msg_enc = str(msg).encode(cls.FORMAT)
        msg_length = len(msg_enc)
        msg_length_enc = str(msg_length).encode(cls.FORMAT)
        msg_length_enc += b' ' * (cls.HEADER - len(msg_length_enc))
        cls.client.send(msg_length_enc)
        cls.client.send(msg_enc)

    @classmethod
    def receive(cls):
        ans_length = cls.client.recv(cls.HEADER).decode(cls.FORMAT)
        if ans_length:
            ans_length = int(ans_length)
            # Receive Message
            ans = cls.client.recv(ans_length).decode(cls.FORMAT)
            return ans

    @classmethod
    def start(cls):
        cls.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.client.connect(cls.ADDR)
        print(f"[CONNECTION ESTABLISHED] to {cls.ADDR}")

    @classmethod
    def stop(cls):
        cls.send(cls.DISCONNECT_MESSAGE)
        print(f"[CONNECTION SEVERED] to {cls.ADDR}")

    @classmethod
    def query(cls, qry):
        cls.send(qry)
        ans = cls.receive()
        print(f"[QUERY] Asked: {qry} / Received: {ans}")


