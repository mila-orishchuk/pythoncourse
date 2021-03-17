import socket
import threading

SERVER = "127.0.0.1"
PORT = 14000
HEADER = 100
FORMAT = "utf-8"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER, PORT))
server_socket.listen()

#client_sockets_list = []
clients = {}
print("! Server Online !")


def receive_msg(conn):
    username_header = conn.recv(HEADER)
    username_length = int(username_header.decode(FORMAT))
    username = connection.recv(username_length).decode(FORMAT)

    while True:
        try:
            msg_header = conn.recv(HEADER)
            if msg_header:
                msg_length = int(msg_header.decode(FORMAT))
                message = conn.recv(msg_length).decode(FORMAT)

                print(f"{username} > {message}")
                clients[conn] = {username: message}

                send_thread = threading.Thread(
                    target=send_msg, args=(conn, username, message))
                send_thread.start()

        except ConnectionResetError:
            try:
                del(clients[conn])

                send_msg(conn, username, "!DISCONNECTED!")

            except RuntimeError:
                print("A 'RuntimeError' occurred!")
                continue

            print(f"{username} DISCONNECTED!")
            break


def send_msg(socket, user_name, message):
    if message == "!DISCONNECTED!":
        for client in clients:
            username2 = user_name.encode(FORMAT)
            user2_length = str(len(user_name)).encode(FORMAT)
            user2_length += b" " * (HEADER - len(user2_length))

            msg2 = message.encode(FORMAT)
            message2_header = str(len(message)).encode(FORMAT)
            message2_header += b" " * (HEADER - len(message2_header))

            client.send(user2_length + username2 + message2_header + msg2)

    else:
        for client in clients:
            try:
                if client != socket:
                    username = user_name.encode(FORMAT)
                    user_length = str(len(user_name)).encode(FORMAT)
                    user_length += b" " * (HEADER - len(user_length))

                    msg = message.encode(FORMAT)
                    message_header = str(len(message)).encode(FORMAT)
                    message_header += b" " * (HEADER - len(message_header))

                    client.send(user_length + username + message_header + msg)

            except ConnectionResetError:
                print("!CLIENT DISCONNECTED!")


while True:
    connection, address = server_socket.accept()
    recv_thread = threading.Thread(target=receive_msg, args=(connection, ))
    recv_thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
