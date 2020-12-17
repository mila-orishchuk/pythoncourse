#!/usr/bin/python

def letters(symbol = "#"):

    '''Letter O'''

    print(symbol*9, end = '\n')
    print(symbol, symbol, sep = '\t', end = '\n')
    print(symbol, symbol, sep = '\t', end = '\n')
    print(symbol, symbol, sep = '\t', end = '\n')
    print(symbol*9, end = '\n\n')

    '''Letter H'''

    print(symbol, symbol, sep = '\t', end = '\n')
    print(symbol, symbol, sep = '\t', end = '\n')
    print(symbol*9, end = '\n')
    print(symbol, symbol, sep = '\t', end = '\n')
    print(symbol, symbol, sep = '\t', end = '\n')

letters()

'''

