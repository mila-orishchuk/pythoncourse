'''
Extend the Stack to include a method called get_from_stack that searches and returns an element
e from a stack. Any other element must remain on the stack respecting their order. Consider the
case in which the element is not found - raise ValueError with proper info Message

Extend the Queue to include a method called get_from_stack that searches and returns an element
e from a queue. Any other element must remain in the queue respecting their order. Consider the
case in which the element is not found - raise ValueError with proper info Message
'''

from typing import List, Any


class Queue:

    def __init__(self):
        self._items: List[Any] = []

    def is_empty(self):
        return not self._items

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def get_from_stack(self, search_element):
        if not search_element in self._items:
            raise ValueError(
                f'{search_element} not found')
        return search_element

    def __str__(self):
        return f'{self._items}'


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    print(q.is_empty())
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    print('size:', q.size())
    print(q)
    try:
        q.get_from_stack(2)
        q.get_from_stack('n')
    except ValueError as error:
        print(error)
