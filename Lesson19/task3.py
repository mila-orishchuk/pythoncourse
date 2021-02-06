'''
Pytest fixtures with context manager

Create a simple function, which performs any logic of your choice with text data,
which it obtains from a file object, passed to this function ( def test(file_obj) ). 

Create a test case for this function using pytest library
(https://docs.pytest.org/en/latest/contents.html). 

Create pytest fixture, which uses your implementation of the context manager to return
a file object, which could be used inside your function.
'''
import pytest
import unittest


class FixtureFileObj:
    def read(self):
        return 'qwerty'

@pytest.fixture
def file_obj():
    return FixtureFileObj()


def revert_string(file_obj):
    string = file_obj.read()
    return string[::-1]


@pytest.mark.usefixtures
def test_revert_string(file_obj):
    assert revert_string(file_obj) == 'ytrewq'


@pytest.fixture(autouse=True, scope='module')
def module_setup_teardown():
    print("MODULE SETUP!!!")
    yield
    print("MODULE TEARDOWN!!!")

def test1():
    print("TEST1!!!")



class MyTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def initdir(self, tmpdir):
        tmpdir.chdir()
        tmpdir.join("text.txt").write("testdata")

    def test_method(self):
        with open("text.txt") as text_file:
            s = text_file.read()
        self.assertIn("testdata", s)


if __name__ == '__main__':
    pass
