'''
Writing tests for context manager

Take your implementation of the context manager class from Task 1
and write tests for it. Try to cover as many use cases as you can, positive
ones when a file exists and everything works as designed. And also, write tests
when your class raises errors or you have errors in the runtime context suite.
'''
from task1 import OpenFile
import unittest
# from unittest.mock import patch, mock_open


class TestOpenFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.filename = 'test.txt'
        self.data = "Message to write on file to be written"

    def tearDown(self):
        pass

    def testOpenNonExistingFile(self):
        try:
            with OpenFile('text123.txt', 'r') as text_file:
                text_file.read()
        except FileNotFoundError as e:
            self.assertEqual(type(e), FileNotFoundError)

    def testWriteToFile(self):
        test_counter = OpenFile.counter
        with OpenFile(self.filename, 'w') as text_file:
            text_file.truncate()
            text_file.write(self.data)
        self.assertEqual(test_counter + 1, OpenFile.counter)

    def testReadFile(self):
        with OpenFile(self.filename, 'r') as text_file:
            read_file = text_file.read()
        self.assertEqual(read_file, self.data)

    def testIncorrectMode(self):
        try:
            with OpenFile('text.txt', 'z') as text_file:
                print(text_file.read())
        except ValueError as e:
            self.assertEqual(type(e), ValueError)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOpenFile)
    unittest.TextTestRunner(verbosity=2).run(suite)
