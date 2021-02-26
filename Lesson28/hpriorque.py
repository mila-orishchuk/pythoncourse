class _Item:
    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __lt__(self, other):
        return self._key < other._key
    
    def __str__(self):
        return f'{self._key}: {self._value}'

class HeapPriorityQueue:
    
    def __init__(self):
        self._data = []
    
    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j: int):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def __len__(self):
        return len(self._data)

    def enqueue(self, key, value):
        self._data.append(_Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        item = self._data[0]
        return item._key, item._value

    def dequeue(self):
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return item._key, item._value

    def __str__(self):
        return ', '.join(map(str, self._data))


if __name__ == "__main__":
    pq = HeapPriorityQueue()
    pq.enqueue(key=4, value="C")
    pq.enqueue(key=3, value="B")
    pq.enqueue(key=5, value="D")
    pq.enqueue(17, "W")
    pq.enqueue(11, "S")
    print(pq)
    print(pq.min())
    print(len(pq))
    pq.dequeue()
    print(pq)
