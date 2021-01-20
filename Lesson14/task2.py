'''
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

'''
from functools import wraps


def stop_words(words: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            for word in words:
                result = result.replace(word, "*")
            return result
        return wrapper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == '__main__':
    assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
