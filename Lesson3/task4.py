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

def random_math(success = 5): 

    while success > 0:  

        a = random.randint(1,20)
        b = random.randint(1,20) 

        random_operator = random.choice(['+', '-', '*'])

 #       result = random_operator(a, b)

        print(a, random_operator, b, '= ?')

        userInput = input()
        if random_operator == "+":
            result = a + b
        elif random_operator == "-":
            result = a - b
        elif random_operator == "*":
            result = a * b
        if str(result) == userInput:
            success += 1
        else:
            success = 0
        print('try again')


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













