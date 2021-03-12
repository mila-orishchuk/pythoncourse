'''
Echo server with threading

Create a socket echo server that handles each
connection using the multiprocessing library.
'''
import sys
import socket
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication
from ui_client import Ui_Client
from ui_connect import Ui_Connect
import time

class ReceiveThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super(ReceiveThread, self).__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            self.receive_message()

    def receive_message(self):
        message = self.client_socket.recv(1024)
        message = message.decode()

        self.signal.emit(message)


class ClientWindow(QtWidgets.QMainWindow):

    host = 'localhost'
    port = 8888

    def __init__(self):
        super().__init__()
        self.ui_connect = Ui_Connect()
        self.ui_connect.setupUi(self)
        self.show()

        self.ui_connect.pushButton.clicked.connect(self.btn_connect_clicked)

        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def btn_connect_clicked(self):

        user_name = self.ui_connect.nameTextEdit.toPlainText()

        if len(user_name) < 1:
            return

        if not self.connect(self.host, self.port, user_name):
            return

        self.recv_thread = ReceiveThread(self.tcp_client)
        self.recv_thread.signal.connect(self.show_message)
        self.recv_thread.start()
        print("[INFO] recv thread started")

        self.client_chat = Ui_Client()
        self.client_chat.setupUi(self)
        self.client_chat.pushButton_send.clicked.connect(self.send_message)
        self.show()

    def connect(self, host, port, user_name):
        try:
            self.tcp_client.connect((host, port))
            self.tcp_client.send(user_name.encode())

            print("[INFO] Connected to server")

            return True
        except Exception as e:
            error = f"Unable to connect to server \n'{str(e)}'"
            print("[INFO]", error)
            self.show_error("Connection Error", error)

            return False

    def show_message(self, message):
        self.client_chat.textBrowser.append(message)

    def send_message(self):
        message = self.client_chat.textEdit.toPlainText()     
        print("sent: " + message)

        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = f"Unable to send message '{str(e)}'"
            print("[INFO]", error)
            self.show_error("Server Error", error)
            
        self.client_chat.textEdit.clear()

    def show_error(self, error_type, message):
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setText(message)
        error_dialog.setWindowTitle(error_type)
        error_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        error_dialog.exec_()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    client = ClientWindow()
    sys.exit(app.exec_())
