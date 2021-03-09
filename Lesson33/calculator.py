from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    first_number = None
    typing_number = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        buttons = range(0, 10)
        for button in buttons:
            getattr(self, f'pushButton_{button}').clicked.connect(self.button_pressed)

        self.pushButton_module.clicked.connect(self.unary_button_pressed)
        self.pushButton_percent.clicked.connect(self.unary_button_pressed)

        self.pushButton_add.clicked.connect(self.binary_button_pressed)
        self.pushButton_substract.clicked.connect(self.binary_button_pressed)
        self.pushButton_multiply.clicked.connect(self.binary_button_pressed)
        self.pushButton_divide.clicked.connect(self.binary_button_pressed)

        self.pushButton_decimal.clicked.connect(self.decimal_pressed)

        self.pushButton_clear.clicked.connect(self.clear_button_pressed)

        self.pushButton_equals.clicked.connect(self.equal_pressed)

        self.pushButton_add.setCheckable(True)
        self.pushButton_substract.setCheckable(True)
        self.pushButton_multiply.setCheckable(True)
        self.pushButton_divide.setCheckable(True)

    def button_pressed(self):
        button = self.sender()

        if ((self.pushButton_add.isChecked() or self.pushButton_substract.isChecked() or
                self.pushButton_multiply.isChecked() or self.pushButton_divide.isChecked())
                and (not self.typing_number)):
            new_label = format(float(button.text()), '.15g')
            self.typing_number = True
        else:
            if float(self.label.text()) > 10000000000:
                return

            if '.' in self.label.text() and button.text() == '0':
                new_label = format(self.label.text() + button.text(), '.15')
            else:
                new_label = format(
                    float(self.label.text() + button.text()), '.15g')

        self.label.setText(new_label)

    def unary_button_pressed(self):
        button = self.sender()
        lable_number = float(self.label.text())

        if button.text() == '+/-':
            lable_number *= -1
        else:
            lable_number *= 0.01

        new_label = format(lable_number, '.15g')
        self.label.setText(new_label)

    def binary_button_pressed(self):
        button = self.sender()
        self.first_number = float(self.label.text())

        button.setChecked(True)

    def decimal_pressed(self):
        if '.' not in self.label.text():
            new_label = self.label.setText(self.label.text() + '.')

    def clear_button_pressed(self):
        self.pushButton_add.setChecked(False)
        self.pushButton_substract.setChecked(False)
        self.pushButton_divide.setChecked(False)
        self.pushButton_multiply.setChecked(False)

        self.typing_number = False
        self.label.setText('0')

    def equal_pressed(self):
        typing_number = float(self.label.text())
        if self.pushButton_add.isChecked():
            labelNumber = self.first_number + typing_number
            new_label = format(labelNumber, '.15g')
            self.label.setText(new_label)
            self.pushButton_add.setChecked(False)

        elif self.pushButton_substract.isChecked():
            labelNumber = self.first_number - typing_number
            new_label = format(labelNumber, '.15g')
            self.label.setText(new_label)
            self.pushButton_substract.setChecked(False)

        elif self.pushButton_divide.isChecked():
            try:
                labelNumber = self.first_number / typing_number
                new_label = format(labelNumber, '.15g')
                self.label.setText(new_label)
                self.pushButton_divide.setChecked(False)
            except ZeroDivisionError:
                self.label.setText('Error')

        elif self.pushButton_multiply.isChecked():
            labelNumber = self.first_number * typing_number
            new_label = format(labelNumber, '.15g')
            self.label.setText(new_label)
            self.pushButton_multiply.setChecked(False)

        self.typing_number = False
