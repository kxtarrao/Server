import socket
import threading
import pymongo

class Server():
    # Add MongoDB COLLECTION
    COLLECTION = pymongo.MongoClient(
        "mongodb+srv://user:password0@cluster0.pa3o1.mongodb.net/project0?retryWrites=true&w=majority")\
        ['database0']\
        ['collection0']
    HEADER = 64
    FORMAT = "utf-8"
    DISCONNECT_MESSAGE = "!DISCONNECT"
    ADDR = ("192.168.0.2",5050)

    @classmethod
    def send(cls, conn, msg):
        message = str(msg).encode(cls.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(cls.FORMAT)
        send_length += b' ' * (cls.HEADER - len(send_length))
        conn.send(send_length)
        conn.send(message)

    @classmethod
    def receive_client(cls, conn, addr):
        cls.CONNECTION_COUNT+=1
        print(f"[NEW CONNECTION] {addr} now connected. [ACTIVE CONNECTIONS] {cls.CONNECTION_COUNT}")
        while True:
            # Receive Message Length Header
            msg_length = conn.recv(cls.HEADER).decode(cls.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                # Receive Message
                msg = conn.recv(msg_length).decode(cls.FORMAT)
                # Disconnect Line
                if msg == cls.DISCONNECT_MESSAGE:
                    print(f"[CONNECTION SEVERED] {addr}")
                    break
                else:
                    # Query COLLECTION
                    ans = cls.COLLECTION.find_one({"key": msg})["value"]
                    cls.send(conn, ans)
        cls.CONNECTION_COUNT-=1
        conn.close()

    @classmethod
    def start(cls):
        cls.CONNECTION_COUNT=0
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(cls.ADDR)

        server.listen()
        print(f"[STARTING] Server is listening on {cls.ADDR}")
        while (True):
            conn, addr = server.accept()
            threading.Thread(target=cls.receive_client, args=(conn,addr)).start()

# Operation
Server.start()
