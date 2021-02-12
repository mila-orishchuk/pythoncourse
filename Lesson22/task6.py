'''
доп задачку сдвига числа уточню можно сдвигать влево и вправо.
как будет удобнее. Но принцип такой что крайнее переходит назад, ведущий ноль
не выводится но если сдвигаем дальше то он не теряется.
сдвиг - единицы стают на десятки, десятки на сотни, сотни на тысячи, тысячи на единицы
'''
from math import log10


def shift_digits(inval, count=1):
    last_digits = inval % (10**count)
    rest = inval // (10**count)
    rest_len = int(log10(rest) + 1)
    return last_digits * (10**rest_len) + rest


if __name__ == "__main__":
    assert shift_digits(123) == 312
    assert shift_digits(120) == 12
    assert shift_digits(120, 2) == 201
    assert shift_digits(543210, 3) == 210543
