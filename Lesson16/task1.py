'''
Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
`iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function


'''
from typing import Iterable


def with_index(iterable: Iterable, start=0):
    if not isinstance(iterable, Iterable):
        raise ValueError(f'Not iterable {iterable}')
    
    for elem in iterable:
        yield start, elem
        start += 1
    # return [(start + i, iterable[i]) for i in range(len(iterable))]


if __name__ == '__main__':
   
    try:
        seasons = ["Spring", "Summer", "Fall", "Winter"]
        seasons_list = list(with_index(seasons, start=1))
        assert seasons_list == list(enumerate(seasons, start=1))
        values = 123
        values_list = list(with_index(values))
    except ValueError as error:
        print(error)  