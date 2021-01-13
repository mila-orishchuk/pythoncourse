'''
Custom exception

Create your custom exception named `CustomException`, you can inherit from base Exception class, but extend its functionality
to log every error message to a file named `logs.txt`. Tips: Use __init__ method to extend functionality for saving messages to file

'''
import os
from datetime import datetime


class CustomException(Exception):
    log_file_name = 'logs.txt'
    date_str = str(datetime.now().replace(microsecond=0))

    def __init__(self, message):
        super().__init__(message)
        mod = "a" if os.path.isfile(self.log_file_name) else "w"
        with open(self.log_file_name, mod) as err_file:
            err_file.write(self.date_str + ' ' + message + '\n')


raise CustomException('asdasfd')
