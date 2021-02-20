'''
Implement a queue using a singly linked list.
'''

from node import Node


class Queue(object):
    def __init__(self, data=None):
        self._head = None
        self._tail = None

    def enqueue(self, item):        
        new_node = Node(item)
        
        if self._tail is None:
            self._head = self._tail = new_node
        self._tail.set_next(new_node)
        self._tail = new_node

    def dequeue(self):
        node = self._head
        self._head = node.get_next()
  
        if self.is_empty: 
            self._tail = None

    @property
    def is_empty(self):
        return not self._head

    def __repr__(self):
        representation = "<Queue: "
        current = self._head
        last = self._tail
        if current is not None and last is not None:
            while current != last:
                representation += f"{current.get_data()} "
                current = current.get_next()
            representation += f'{last.get_data()}'
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue("first")
    my_queue.enqueue("second")
    my_queue.enqueue("third")
    print(my_queue)
    my_queue.dequeue()
    print(my_queue)
    my_queue.dequeue()
    print(my_queue)
    my_queue.dequeue()
    print(my_queue)
