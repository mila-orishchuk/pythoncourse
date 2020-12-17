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
    print(symbol, symbol, sep = '\t', end = '\n\n')

letters()

'''Use loop'''

def litera():

    '''Letter O'''

    i = 0
    while i < 5:
        if 0 < i < 4:
            print("#","#", sep="\t")
        else:
            print(9*"#")
        i += 1
    print(end = "\n")
    
    '''Letter H'''
    i = 0
    while i < 5:
        if i == 2:
            print (9*"#")
        else:
            print("#","#", sep="\t")
        i += 1

litera()   