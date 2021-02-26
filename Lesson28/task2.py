'''
Using the BinaryHeap class, implement a new class called PriorityQueue.
Your PriorityQueue class should implement the constructor, plus the enqueue and dequeue methods.
'''
from task1 import MaxHeap


class PriorityQueue:
    def __init__(self):
        self.queue = MaxHeap()

    def enqueue(self, value):
        self.queue.insert(value)

    def dequeue(self, indx):
        return self.queue.delete(indx)

    def __len__(self):
        return self.queue.current_size

    def __str__(self):
        return self.queue.__str__()


if __name__ == "__main__":
    my_lst = [7, 10, 2, 8, 5, 9, 11]

    mq = PriorityQueue()
    mq.enqueue(7)
    mq.enqueue(10)
    mq.enqueue(2)
    mq.enqueue(8)
    mq.enqueue(5)
    mq.enqueue(9)
    mq.enqueue(11)
    print(mq)
    print(mq.dequeue(3))
    print(mq.dequeue(5))
    print(mq)
