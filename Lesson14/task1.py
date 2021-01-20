'''
Write a decorator that prints a function with arguments passed to it.
! It should print the function, not the result of its execution!

For example:

 "add called with 4, 5"
'''
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args):
        print(func.__name__, 'called with', ', '.join(map(str, args)))
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


if __name__ == '__main__':
    print(add.__name__)
    add(1, 2)
    square_all(1, 3, 5)
