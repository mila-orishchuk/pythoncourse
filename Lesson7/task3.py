#!/usr/bin/python

'''
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
(to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

    the call make_operation(‘+’, 7, 7, 2) should return 16
    the call make_operation(‘-’, 5, 5, -10, -20) should return 30
    the call make_operation(‘*’, 7, 6) should return 42 
'''
from math import prod

calc = {
    '+': lambda *args: sum(args),
    '-': lambda *args: args[0] - sum(args[1:]),
    "*": lambda *args: prod(args)
}

def make_operation(operator, *args, **kwargs):
    return calc[operator](*args)

if __name__ == '__main__':
    print(make_operation('+', 7, 7, 2, 5, 7, 98, 23))
    print(make_operation('-', 5, 5, -10, -20))
    print(make_operation('*', 7, 6, 9, -8))