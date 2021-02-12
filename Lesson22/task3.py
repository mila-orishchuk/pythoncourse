def mult_recursive(a: int, n: int) -> int:
    if n < 0:
        raise ValueError(
            f'{mult_recursive.__name__} works only with postive integers')
    return 0 if n == 0 else a + mult_recursive(a, n-1)


if __name__ == "__main__":
    try:
        assert mult_recursive(2, 4) == 8
        assert mult_recursive(2, 0) == 0
        assert mult_recursive(2, -4) == 0
    except ValueError as error:
        print(error)
