'''
Extend Phonebook application

Functionality of Phonebook application:

    Add new entries 
    Search by first name 
    Search by last name 
    Search by full name
    Search by telephone number
    Search by city or state
    Delete a record for a given telephone number
    Update a record for a given telephone number
    An option to exit the program

The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with application,
else raise an error. After the user exits, all data should be saved to loaded JSON.
'''
import os
import json
import data
import tools


def add_contact():
    name = input('Name: ').capitalize()
    lastname = input("Last name: ").capitalize()
    phone = input("Phone: ")
    city = input("City: ")
    contact = {
        'firstName': name,
        "lastName": lastname,
        "fullName": name + " " + lastname,
        "phone": phone,
        "city": city
    }
    data.create(contact)

def search_contact(phonebook):
    pass

def delete_by_phone(phone):
    pass

def update_by_phone(phone):
    pass

def exit_program():
    exit()

if __name__ == '__main__':
    main_menu = [
    {
        'callback': add_contact,
        'menu_item': 'Create new contact'
    },
    {
        'callback': search_contact,
        'menu_item': 'Search contact'
    },
    {
        'callback': update_by_phone,
        'menu_item': 'Update an record'
    },
    {
        'callback': delete_by_phone,
        'menu_item': 'Delete an record'
    },
    {
        'callback': exit_program,
        'menu_item': 'Exit'
    },
]

    print(tools.render_menu(main_menu))
