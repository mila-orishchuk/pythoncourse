#!/usr/bin/python

'''
Extracting numbers

'''

def extracting_numbers(list):
    i = 0
    list2 = []

    while i < len(list):
        if not list[i] % 7 and list[i] % 5:
            list2.append(list[i])
        i += 1

    return list2

if __name__ == '__main__':
    list = []
    for i in range(1, 100):
        list.append(i)
    # list = [*range(1, 100)]
    print(list)
    print(extracting_numbers(list))
    
