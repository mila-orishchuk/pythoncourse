'''
Checks if input string is Palindrome
'''
from typing import Optional


def is_palindrome_recursive(looking_str: str, index: int = 0) -> bool:
    return len(looking_str) < 2 or looking_str[index] == looking_str[index-1] and is_palindrome_recursive(looking_str[1:-1])


if __name__ == "__main__":
    assert is_palindrome_recursive('mom') == True
    assert is_palindrome_recursive('sassas') == True
    assert is_palindrome_recursive('o') == True
    assert is_palindrome_recursive('so') == False
    assert is_palindrome_recursive('sova') == False
