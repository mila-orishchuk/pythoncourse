#!/usr/bin/python

'''
TASK1

'''

def given_string():

    string = input()

    if len(string) < 2:
        return ''
    
    else:
        print(string[:2] + string[-2:])

if __name__ == '__main__':
    given_string()