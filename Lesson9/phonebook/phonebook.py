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

main_menu = [
    {
        'callback': phonebook_tools.add_contact,
        'menu_item': 'Create new contact'
    },
    {
        'callback': phonebook_tools.search_contact,
        'menu_item': 'Search contact'
    },
    {
        'callback': phonebook_tools.update_by_phone,
        'menu_item': 'Update an record'
    },
    {
        'callback': phonebook_tools.delete_by_phone,
        'menu_item': 'Delete an record'
    },
    {
        'callback': phonebook_tools.exit_program,
        'menu_item': 'Exit'
    },
]

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
    query = input('Enter name to search: ')
    if type(query)==str:
        query = query.capitalize()
        disp(query)         
    elif type(query)==int:
        print(contacts.values())

def delete_by_phone(phone):
    phone = str(input('Enter phone of the contact to delete').capitalize())
    confirm = input('Delete this contact? Y/N: ')
    if confirm.upper() == 'Y':
        contacts.pop(phone)

def update_by_phone(phone):
    phone = str(input('Enter phone of the contact to update').capitalize())
    confirm = input('Update this contact? Y/N: ')
    if confirm.upper() == 'Y':
        contacts.pop(phone)

def exit_program():
    exit()

if __name__ == '__main__':
