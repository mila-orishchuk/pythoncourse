#!/usr/bin/python

'''
TASK4

'''

'''
Phone number

'''

def validNumber(phone):

    operators = ['063', '093', '050']
    
    if not phone.isnumeric():
        return('Phone number must contian only numbers')

    elif len(phone) != 10: 
        return('Wrong length number')

    elif phone[0:3] not in operators:
        return('Unknown operator')

    else:
        return('Number is correct')

phone_number = input('Enter your phone number:')
phone_number = phone_number.replace(' ', '').replace('+38', '')

    
if __name__ == '__main__':
    print(validNumber(phone_number))





'''
random ariphmetic

'''

import random
import operator

def random_math(success = 5): 

    while success > 0:  

        a = random.randint(1,20)
        b = random.randint(1,20) 
        a,b = (b,a) if a < b else (a,b)
        random_operator = random.choice(['+', '-', '*'])

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

    string = str(input()).lower().strip()
    rev_string = string[::-1]

    if string == rev_string:
        print("palindrome")

    else:
        print("isn`t palindrome")

if __name__ == '__main__':
    IsPalindrome()













