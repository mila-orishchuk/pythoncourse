#!/usr/bin/python

'''
Words combination

'''
import random

def get_word():
    word = input('Enter word: ')
    for i in range(5):
        shuffled = ''.join(random.sample(word,len(word)))
        print(shuffled)
if __name__ == '__main__':
    get_word()

