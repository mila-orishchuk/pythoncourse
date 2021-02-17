'''
Write a program that reads in a sequence of chararacters, and determines
whether it's parentheses, braces, and curly brackets are "balanced."
'''
from task1 import Stack


def is_balanced_brackets(test_string: str):
    stack = Stack()
    open_brackets = ["(", "{", "["]
    closing_brackets = [")", "}", "]"]

    for char in test_string:
        if char in open_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty() or open_brackets[closing_brackets.index(char)] != stack.peek():
                return False
            stack.pop()

    return stack.is_empty()


if __name__ == "__main__":
    test_balanced_strings = [
        "()", "(())", "{(([]))}", "{{}}[]", "[](){}", "{{}}{}()[]"
    ]
    test_unbalanced_strings = [
        ")(", "{()", "}}}}", "((()", "[{](){}", "{(})"
    ]
    test_strings = [*test_balanced_strings, *test_unbalanced_strings]

    for test_no, test_string in enumerate(test_strings):
        print(
            f"Test {test_no} - {test_string} \nIs balanced: {is_balanced_brackets(test_string)} \n")
