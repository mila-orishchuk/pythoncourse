'''
Write a class TypeDecorators which has several methods for converting results
of functions to a specified type (if it's possible):

methods:
to_int
to_str
to_bool
to_float

Don't forget to use @wraps

'''
from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except:
                return result
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except:
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return str(func(*args, **kwargs))
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == 'False':
                return False
            elif result == 'True':
                return True
            else:
                return result
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def do_something_else(string: str):
    return string


@TypeDecorators.to_str
def count_letters(string: str):
    return len(string)


if __name__ == '__main__':
    assert do_nothing('25') == 25
    assert do_something('True') is True
    assert do_something_else('12.34') == 12.34
    assert count_letters('qwe') == '3'
