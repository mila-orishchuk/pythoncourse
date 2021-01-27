"""
Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
"""


class MyIterable:

    def __init__(self, list):
        self.__list = list
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index == len(self.__list):
            raise StopIteration
        return self.__list[self.__index]

    def __getitem__(self, index):
        return self.__list[index]

if __name__ == '__main__':
    my_iterable = MyIterable([1, 2, 3, "432", 433, {1,2,3}])
    for i in my_iterable:
        print(i)
    
    print(my_iterable[3])
