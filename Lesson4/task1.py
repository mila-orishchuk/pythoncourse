#!/usr/bin/python

'''
The Guessing Game

'''
import random

def get_user_number(msg = 'enter number'):
    while True:
        user_msg = input(msg)
        if  user_msg.isdigit():
            return int(user_msg)
        print('Must contian only numbers') 
        

def guess_number(number):
    numberGuess = random.randint(1,10)
    while True: 
        userGuess = number("Guess number between 1 and 10: ")

        if userGuess == numberGuess:
            print(f'You win! The guessed number is {userGuess}')
            break
        elif userGuess < numberGuess: 
            print(f'The Number greater than {userGuess}') 
        else: 
            print(f'The Number smaller than {userGuess}')

if __name__ == '__main__':
    guess_number(get_user_number)