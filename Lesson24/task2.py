'''
Implement a stack using a singly linked list.
'''
from node import Node


class Stack:
    def __init__(self):
        self._head = None

    @property
    def is_empty(self):
        return self._head is None

    @property
    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def push(self, item):
        node = Node(item)
        if self.is_empty:
            self._head = node
        else:
            node.set_next(self._head)
            self._head = node

    def pop(self):
        if self._head is None:
            raise Exception("Pop from empty stack")
        
        pop_node = self._head
        self._head = self._head.get_next()
        pop_node.set_next(None)

        return pop_node.get_data()

    def peek(self):
        return None if self.is_empty else self._head.get_data()

    def __repr__(self):
        current = self._head
        l = []
        while current is not None:
            l.append(str(current.get_data()))
            # representation += f'{current.get_data()} '
            current = current.get_next()
        representation = " ".join(l)
        return f"<Stack: {representation}>"

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    my_stack = Stack()

    print(my_stack.is_empty)
    my_stack.push(31)
    my_stack.push(77)
    my_stack.push(17)
    
    print(my_stack)
    print(my_stack.peek())
    print(my_stack)
    print(my_stack.pop())
    print(my_stack)
    print(my_stack.size)
