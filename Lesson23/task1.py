'''
Write a program that reads in a sequence of characters and
prints them in reverse order, using your implementation of Stack.

Extend the Stack to include a method called get_from_stack that searches and returns an element
e from a stack. Any other element must remain on the stack respecting their order. Consider the
case in which the element is not found - raise ValueError with proper info Message
'''

from typing import List, Any


class Stack:

    def __init__(self):
        self._items: List[Any] = []

    def is_empty(self):
        return not self._items

    def push(self, item: Any):
        self._items.append(item)

    def pop(self) -> Any:
        return self._items.pop()

    def peek(self):
        if not self.is_empty():
            return self._items[len(self._items)-1]

    def size(self):
        return len(self._items)

    def get_from_stack(self, search_element):
        if not search_element in self._items:
            raise ValueError(
                f'{search_element} not found')
        return search_element

    def __str__(self):
        return f'{self._items[::-1]}'


if __name__ == "__main__":
    stack = Stack()
    stack.push('1')
    stack.push('2')
    stack.push('3')
    print(stack.size())
    stack.pop()
    print(stack)
    try:
        stack.get_from_stack('2')
        stack.get_from_stack('n')
    except ValueError as error:
        print(error)
