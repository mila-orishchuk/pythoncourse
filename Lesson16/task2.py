'''
Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
Tips: See the documentation for `range` function

'''


def in_range(start, end=None, step=1):
    if end is None:
        start, end = 0, start

    if start > end:
        return

    current = start
    while current < end:
        yield current
        current += step


if __name__ == '__main__':
    data_sets = [
        (10,),
        (21, 11),
        (-10, 10, 2)
    ]
    for data_set in data_sets:
        assert list(in_range(*data_set)) == list(range(*data_set))
