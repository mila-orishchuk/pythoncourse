'''
Implement a binary heap as a max heap
'''


class MaxHeap:
    def __init__(self, alist=None):
        self.heap = [0]
        self.current_size = 0
        if alist is not None:
            self.create_max_heap(alist)
            self.heap = alist
            self.current_size = len(alist)

    def create_max_heap(self, alist):
        n = len(alist)

        for i in range(int(n / 2), -1, -1):
            self.max_heapify(i, alist, n)

    def max_heapify(self, indx, alist, size):
        left_child = indx * 2 + 1
        right_child = indx * 2 + 2

        largest = indx

        if left_child < size:
            if alist[left_child] > alist[largest]:
                largest = left_child

        if right_child < size:
            if alist[right_child] > alist[largest]:
                largest = right_child

        if largest != indx:
            alist[indx], alist[largest] = alist[largest], alist[indx]
            self.max_heapify(largest, alist, size)

    def insert(self, value):
        self.heap.append(value)
        self.current_size += 1

        indx = self.current_size - 1
        parent = int(indx / 2 - 1)

        while parent >= 0 and self.heap[indx] > self.heap[parent]:
            self.heap[indx], self.heap[parent] = self.heap[parent], self.heap[indx]
            indx = parent
            parent = int(indx / 2 - 1)

    def delete(self, indx):
        if self.current_size == 0:
            return

        self.heap[-1], self.heap[indx] = self.heap[indx], self.heap[-1]
        self.current_size -= 1
        self.max_heapify(indx, self.heap, self.current_size)

        return self.heap.pop()

    def extract_max(self):
        return self.delete(0)

    def __str__(self):
        return ', '.join(map(str, self.heap))


if __name__ == "__main__":
    heap = MaxHeap([7, 10, 2, 8, 5, 9, 11])
    print(heap)
    heap.insert(1)
    print(heap)
    print('del 2nd is', heap.delete(2))
    heap.extract_max()
    print(heap)
