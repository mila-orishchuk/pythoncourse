def reverse_recursive(input_str: str) -> str:
    return input_str if len(input_str) <= 1 else reverse_recursive(input_str[1:]) + input_str[0]


if __name__ == "__main__":
    assert reverse_recursive('hello') == 'olleh'
    assert reverse_recursive('o') == 'o'
    assert reverse_recursive('1234') == '4321'
