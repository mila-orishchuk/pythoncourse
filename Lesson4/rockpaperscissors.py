
'''
tasks 

'''

import random

print(input('Welcome to Rock, Paper, Scissors!'))
user_wins = 0
computer_wins = 0

choices = ['rock', 'paper', 'scissors']
random_index = random.randint(0,2)
comp_choice = choices[random_index]
while True:
    user_choice = input('Select rock, paper or scissors? ').lower()
    if user_choice == comp_choice:
        print('Tie!')
    elif user_choice == 'rock':
        if comp_choice == 'paper':
            print('You lose!', comp_choice, 'covers', user_choice)
        else:
            print('You win!', user_choice, 'smashes', comp_choice)
    elif user_choice == 'paper':
        if comp_choice == 'scissors':
            print('You lose!', comp_choice, 'cut', user_choice)
        else:
            print('You win!', user_choice, 'covers', comp_choice)
    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            print('You lose...', comp_choice, 'smashes', user_choice)
        else:
            print('You win!', user_choice, 'cut', comp_choice)
    else:
        print('That is invalid enter. Try again!')

    repeat = input('Play again? (Y/N) ').lower()
    while repeat not in ['y', 'n']:
        repeat = input('That isn`t valid. Try again: ').lower()
    
    if repeat == 'n':
        break
print('Game over')