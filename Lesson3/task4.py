#!/usr/bin/python

'''
TASK4

'''

'''
Phone number

'''

def validNumber():

    phone_number = input('Enter your phone number:')
    phone_number = phone_number.replace(' ', '').replace('+38', '')
    operators = ['063', '093', '050']
    
    if not phone_number.isnumeric():
        print('Phone number must contian only numbers')

    elif len(phone_number) != 10: 
        print('Wrong length number')

    elif phone_number[0:3] not in operators:
        print('Unknown operator')

    else:
        print('Number is correct')
        
if __name__ == '__main__':
    validNumber()






'''
random ariphmetic

'''

import random
import operator

def random_math():   

    a = random.randint(1,20)
    b = random.randint(1,20) 

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
        print("palindrome")

    else:
        print("isn`t palindrome")

if __name__ == '__main__':
    IsPalindrome()













