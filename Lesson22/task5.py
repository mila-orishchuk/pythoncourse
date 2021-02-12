def sum_of_digits_recursive(digit_string: str) -> int:
    if not digit_string.isdigit():
        raise ValueError("Input string must be digit string")
    
    digits = map(int, list(digit_string))
    return int(digit_string) if len(digit_string) == 1 else sum_of_digits_recursive(str(sum(digits)))


if __name__ == "__main__":
    try:
        assert sum_of_digits_recursive('26') == 8
        assert sum_of_digits_recursive('123') == 6
        assert sum_of_digits_recursive('1234') == 1
        assert sum_of_digits_recursive('12345') == 6
        sum_of_digits_recursive('test')
    except ValueError as error:
        print(error)
