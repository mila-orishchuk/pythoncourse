#!/usr/bin/python

'''
TASK2

'''


def phone_number():

    number = input('Enter your phone number: ')

    if not number.isnumeric():
        print('Phone number must contian only numbers')

    elif len(number) != 10:
        print('Please check your phone number')
    
    else:
        print('Thank you! Number is valid')


if __name__ == '__main__':
    phone_number()