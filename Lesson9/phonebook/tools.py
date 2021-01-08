from os import system, name 
import phonebook

def clear(): 
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear') 

def render_menu(menu: list, entry_msg = 'Enter: '):
    clear()

    for i, item in enumerate(menu):
        print(i + 1, item["menu_item"])
    
    entry = int(input(entry_msg)) - 1

    if 0 <= entry < len(menu):
        menu[entry]['callback'](entry)
    else:
        print('invalid input')
