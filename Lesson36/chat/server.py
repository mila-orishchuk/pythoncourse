'''
Echo server with threading

Create a socket echo server that handles each
connection using the multiprocessing library.
'''

import socket
import threading
import multiprocessing
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(format="%(asctime)s:\n{%(process)d} - %(message)s", datefmt = '%Y-%m-%d %H:%M:%S')



class Server:
    def __init__(self, host, port):
        self.clients = {}
        self.host = host
        self.port = port

    def run(self):
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.tcp_server.bind((host, port))
        self.tcp_server.listen(5)

        logger.info(f"Server running on {host}: {port}")

        while True:
            connection, address = self.tcp_server.accept()
            user_name = connection.recv(1024)
            user_name = user_name.decode()
            self.clients[user_name] = connection

            # start a thread for the client
            threading.Thread(target=self.receive_message, args=(
                connection, user_name), daemon=True).start()

            logger.info(
                f"Connection from {address[0]}: {address[1]} name {user_name}")

    def receive_message(self, connection, user_name):
        while True:
            try:
                msg = connection.recv(1024)
                # print(type(msg), msg.decode())
                if (not msg):
                    break
                
                self.send_message(msg, user_name)
                logging.info(f"{user_name}: {msg.decode()}")
            except Exception as e:
                print(e)
                break

        connection.close()
        # remove user from users list
        del(self.clients[user_name])
        logger.info(f"{user_name} disconnected")
        self.send_message('@went to sleep'.encode(), user_name)

    def send_message(self, message, sender):
        if len(self.clients) > 0:
            for user_name in self.clients:
                msg = f"{sender}: {message.decode()}"
                self.clients[user_name].send(msg.encode())


if __name__ == "__main__":
    port = 8888
    host = "localhost"

    chat_server = Server(host, port)
    
    try:
        chat_server.run()
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt')
    
