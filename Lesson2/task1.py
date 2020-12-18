#!/usr/bin/python

'''
TASK1

'''

from datetime import datetime

def message(name = "Mila Orishchuk"):
    
    day = datetime.today().strftime('%A')    
    print(f'Good day {name}! {day} is a perfect day to learn some python.')

message()
