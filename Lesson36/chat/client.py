import socket
import select
import sys
import signal

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = "localhost"
PORT = 42069

HEADER_LENGTH = 10

client_socket.connect((IP, PORT))


def sigint_handler(signum, frame):
    print('\n Disconnecting from server')
    sys.exit()


signal.signal(signal.SIGINT, sigint_handler)

my_username = input("Username: ")


def send_username_to_server(my_username):
    username = my_username.encode('utf-8')
    username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
    client_socket.send(username_header + username)


send_username_to_server(my_username)

sockets_list = [sys.stdin, client_socket]


while True:
    read_sockets, write_socket, error_socket = select.select(
        sockets_list, [], [])

    for socket in read_sockets:
        if socket == client_socket:
            message = socket.recv(2048)
            if not len(message):
                print("Connection closed by server")
                sys.exit()

            print(message.decode('utf-8'))

        else:
            message = sys.stdin.readline()
            message = message.encode('utf-8')
            client_socket.send(message)
            sys.stdout.write(str(my_username) + " > ")
            sys.stdout.write(message.decode('utf-8'))
            sys.stdout.flush()


client_socket.close()
