#!/usr/bin/python

'''
TASK4

'''

'''
random 

'''

import random
import operator

def random_math(
    a = random.randint(1,20),
    b = random.randint(1,20)):    

    operators = [operator.add, operator.sub, operator.mul, operator.truediv]
    random_operator = random.choice(operators)

    result = random_operator(a, b)

    print(a, random_operator, b, '=', result)

if __name__ == '__main__':
    random_math()





'''
Palindrome

'''

def IsPalindrome():

    string = str(input())
    rev_string = string[::-1]

    if string == rev_string:
        print("yes")

    else:
        print("no")

if __name__ == '__main__':
    IsPalindrome()













