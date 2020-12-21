#!/usr/bin/python

'''
TASK3

'''

def check_name(name = 'mila'):

    enterName = (input('Please enter your name: ')).lower()

    if enterName == name:
        return True            

    else:
        print('You enter wrong name!')

if __name__ == '__main__':
    check_name()