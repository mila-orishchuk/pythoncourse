from os import system, name 
import phonebook

def clear(): 
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear') 

def render_menu(main_menu: list):
    clear()

    for i, item in enumerate(menu):
        print(i + 1, item["menu_item"])
    
    entry = int(input('Enter: ')) - 1

    if 0 <= entry < len(menu):
        menu[entry]['callback']()
    else:
        print('invalid input')
