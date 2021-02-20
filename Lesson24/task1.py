'''
Extend UnorderedList

Implement append, index, pop, insert methods for UnorderedList. Also implement
a slice method, which will take two parameters `start` and `stop`,
and return a copy of the list starting at the position and going up
to but not including the stop position.
'''

from node import Node


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def append(self, item):
        if not self._head:
            return self.add(item)
        current = self._head
        while current.get_next() is not None:
            current = current.get_next()
        temp = Node(item)
        temp.set_next(current.get_next())
        current.set_next(temp)

    def get_index(self, item):
        index = 0
        current = self._head
        found = False
        while current is not None:
            if current.get_data() == item:
                found = True
                break
            else:
                current = current.get_next()
                index += 1
        if not found:
            index = None
        return index

    def get_item(self, index):
        current = self._head
        for i in range(index):
            current = current.get_next()
            
        if current is not None:
            return current.get_data()
        else:
            raise IndexError("index out of range")

    def pop(self, index):
        self.remove(self.get_item(index))
        
    def get_slice(self, start, stop):
        if start > stop:
            raise ValueError("Start should be less then stop")
        current = self._head
        index = 0
        in_range = False
        slised = UnorderedList()
        while current is not None:
            if start == index:
                in_range = True
            if stop == index:
                in_range = False
            if in_range:
                slised.append(current.get_data())
            
            index += 1
            current = current.get_next()
        
        return slised

    def insert(self, index, item):
        current = self._head
        for i in range(index):
            current = current.get_next()

        if current is not None:
            temp = Node(item)
            temp.set_next(current.get_next())
            current.set_next(temp)
        else:
            raise IndexError("index out of range")

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    my_list.append(33)
    my_list.append(56)
    my_list.insert(5, 6)
    my_list.insert(2, 41)
    print(my_list.get_index(54))
    print(my_list.get_item(4))
    print('1', my_list.get_slice(2, 6))
        
    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    my_list.pop(4)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))
