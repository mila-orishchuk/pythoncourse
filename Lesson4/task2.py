#!/usr/bin/python

'''
The birthday greeting program

'''

def birthday_greeting():
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    print(f'Hello {name}, on your next birthday you’ll be {age+1} years')
if __name__ == '__main__':
    birthday_greeting()