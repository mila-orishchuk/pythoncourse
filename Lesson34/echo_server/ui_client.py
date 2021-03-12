# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Client(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Client")
        MainWindow.resize(320, 505)
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 "    background-color: #FFE293;\n"
                                 "    border-radius:7px;\n"
                                 "    font: 57 8pt \\\"Poppins Medium\\\";\n"
                                 "    color: rgb(0, 0, 0)\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setGeometry(QtCore.QRect(10, 465, 300, 28))
        self.pushButton_send.setStyleSheet("QpushButton{\n"
                                           "    background-color: #333;\n"
                                           "    border-radius:7px;\n"
                                           "    color: white;\\n\n"
                                           "}\n"
                                           "QPushButton:pressed {\n"
                                           "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                           "stop: 0 #BEBEBE​, stop: 1 #D7D7D7​);\n"
                                           "}")
        self.pushButton_send.setObjectName("pushButton_send")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 370, 300, 87))
        self.textEdit.setStyleSheet("QTextEdit{\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "    border-radius:7px;\n"
                                    "}")
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 300, 350))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    border-radius:7px;\n"
                                       "}")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Client", "Client"))
        self.pushButton_send.setText(_translate("Client", "Send"))
