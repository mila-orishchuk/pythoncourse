import socket
import threading

SERVER = "127.0.0.1"
PORT = 14000
HEADER = 100
FORMAT = "utf-8"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER, PORT))  

def receive_msg():
    while True:
        username_header = client_socket.recv(HEADER)
        username_length = int(username_header.decode(FORMAT))
        username = client_socket.recv(username_length).decode(FORMAT)

        msg_header = client_socket.recv(HEADER)
        if msg_header:
            msg_length = int(msg_header.decode(FORMAT))
            message = client_socket.recv(msg_length).decode(FORMAT)
            print(f"{username} > {message}")
        else:
            print("Nothing received")


def send_msg():
    while True:
        user = str(input("Enter Username: "))
        if user:
            username = user.encode(FORMAT)
            username_length = str(len(user)).encode(FORMAT)
            username_length += b" " * (HEADER - len(username_length))
            client_socket.send(username_length + username)
            break
        else:
            continue

    while True:
        _input = str(input())
        if _input:
            message = _input.encode(FORMAT)
            message_length = str(len(_input)).encode(FORMAT)
            message_length += b" " * (HEADER - len(message_length))
            client_socket.send(message_length + message)


send_thread = threading.Thread(target = send_msg)
send_thread.start()

recv_thread = threading.Thread(target = receive_msg)
recv_thread.start()