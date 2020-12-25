#!/usr/bin/python

'''
Exclusive common numbers

'''
from task1 import generate_random_list
def common_numbers(list1, list2):
    list3 = []
    i = 0

    while i < len(list1): 
        if list1[i] in list2 and list1[i] not in list3:
            list3.append(list1[i])
        i += 1

    return list3  

if __name__ == '__main__':
    list1 = generate_random_list(end = 10)
    list2 = generate_random_list(end = 10)
    print(list1, list2)
    print(common_numbers(list1, list2))

