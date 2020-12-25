#!/usr/bin/python

'''
The greatest number

'''
import random

def generate_random_list(length = 10, start = 1, end = 100):
    random_list = []

    for i in range(0, length):
        number = random.randint(start,end)
        random_list.append(number)

    return random_list

def get_max_number(list):

    i = 1
    max_number = list[0]

    while i < len(list): 
        if list[i] > max_number:
            max_number = list[i]
        i += 1

    return max_number  

if __name__ == '__main__':
    list = generate_random_list()
    print(list)
    print(get_max_number(list))
