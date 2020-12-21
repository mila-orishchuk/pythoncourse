#!/usr/bin/python

'''
TASK2

'''


def phone_number():

    number = input('Enter your phone number: ')

    if number.isnumeric():

        if len(number) != 10:
            print('Please check your phone number')
        
        else:
            print('Thank you! Number is valid')
    else:
        print('You enter invalid number')

if __name__ == '__main__':
    phone_number()