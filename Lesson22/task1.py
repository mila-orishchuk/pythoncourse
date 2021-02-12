'''
Returns  x ^ exp
'''

from typing import Union


def to_power_recursive(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp < 0:
        raise ValueError(
            f'{to_power_recursive.__name__} works only with exp >= 0')
    return 1 if exp == 0 else x * to_power_recursive(x, exp - 1)


if __name__ == "__main__":
    try:
        assert to_power_recursive(2, 3) == 8
        assert to_power_recursive(3.5, 2) == 12.25
        assert to_power_recursive(3.5, 1) == 3.5
        assert to_power_recursive(2, -1) == 0.37
    except ValueError as error:
        print(error)
