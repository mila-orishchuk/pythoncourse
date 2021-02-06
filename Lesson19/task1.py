'''
File Context Manager class

Create your own class, which can behave like a built-in function `open`.
Also, you need to extend its functionality with counter and logging. Pay special
attention to the implementation of `__exit__` method, which has to cover all the
requirements to context managers mentioned here:

https://docs.python.org/3.7/library/stdtypes.html#typecontextmanager

https://docs.python.org/3.7/reference/compound_stmts.html#with

'''
import os

class OpenFile:
    counter = 0

    def __init__(self, file_name, mode):
        self.filename = file_name
        self.__modes = ('r', 'r+', 'rb', 'w', 'w+', 'wb',
                        'wb+', 'a', 'a+', 'ab', 'ab+')
        self.mode = mode
        if self.mode not in self.__modes:
            raise ValueError(f'Invalid mode: {self.mode}')

    def __enter__(self):
        OpenFile.counter += 1
        OpenFile._log(
            f'File {self.filename} open with mode {self.mode}\nCounter: {self.counter}')
        self.file_obj = open(self.filename, self.mode)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            OpenFile._log(
                f'Exeption {exc_type.__name__}, {exc_val}, {exc_tb.tb_lineno}')
        OpenFile._log(f'File {self.filename} close')
        self.file_obj.close()
        return True

    @staticmethod
    def _log(data):
        print(data)


if __name__ == '__main__':
    content = "Message to write on file"
    try:
        with OpenFile('text.txt', 'w') as text_file:
            text_file.write(content)

        with OpenFile('text.txt', 'a') as text_file:
            text_file.write(content)

        with OpenFile('text.txt', 'r') as text_file:
            print(text_file.read())

        with OpenFile('text.txt', 'z') as text_file:
            print(text_file.read())
    except ValueError as error:
        print(error)
