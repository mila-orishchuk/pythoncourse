#!/usr/bin/python

'''
Guess number between 1 and 100

'''

import random

def guess_number(
    numberGuess = random.randint(1,100),
    userGuess = 0):

    while userGuess != numberGuess:

        userGuess = int(input("Guess number between 1 and 100: ")) 

        if userGuess > numberGuess:
            print(f'The Number smaller than {userGuess}')

        elif userGuess < numberGuess: 
            print(f'The Number greater than {userGuess}') 

        else: 
            print(f'You win! The guessed number is {numberGuess}')
            break

if __name__ == '__main__':
    guess_number()
