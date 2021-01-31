'''
Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
Tips: See the documentation for `range` function

'''


def in_range(start: int, end=None, step=1):
    if end is None:
        start, end = 0, start
   
    if not all(isinstance(arg, int) for arg in (start, end, step)):
        raise TypeError('All arguments must be integer.')

    if step == 0:
        raise ValueError('Does not accept step = 0')

    current = start
    while (step > 0 and current < end) or (step < 0 and current > end):
        yield current
        current += step


if __name__ == '__main__':
    data_sets = [
        (10,),
        (21, 10),
        (10, -1, -2),
        (-10, 10, 2),
        (1, 20, 0),
        (2, 10, 2.5),
        (2, 10, True)
    ]
    for data_set in data_sets:
        try:
            assert list(in_range(*data_set)) == list(range(*data_set))
        except ValueError as error:
            print(data_set)
            print(error)
        except TypeError as error:
            print(data_set)
            print(error)
