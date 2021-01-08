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

fields = {
    0: 'name',
    1: 'lastname',
    2: 'fullname',
    3: 'phone',
    4: 'city'
}

def add_contact(user_input):
    name = input('Name: ').capitalize()
    lastname = input("Last name: ").capitalize()
    phone = input("Phone: ")
    city = input("City: ")
    contact = {
        'name': name,
        "last_name": lastname,
        "fullname": name + lastname,
        "phone": phone,
        "city": city
    }
    data.create(contact)


def search_contact(user_input):
    search_menu = []  
    for i in fields:
        search_menu.append({
            'callback': search_by_param,
            'menu_item': f"Search by {fields[i]}"
        })
    tools.render_menu(search_menu)

def search_by_param(user_input):
    contacts = data.getAll()
    enter = input(f"Enter {fields[user_input]} to search: ")
    filtered_contacts = list(filter(lambda contact: contact[fields[user_input]].lower() == enter.lower(), contacts))
    for item in filtered_contacts:
        print(*item.values())
    # print(filtered_contacts)

def delete_by_phone(user_input):
    phone = input("Enter phone to delete: ")
    contacts = data.getAll()
    filtered_contacts = list(
        filter(lambda contact: contact['phone'] == phone, contacts))
    while True:
        if len(filtered_contacts) == 1:
            id = contacts.index(filtered_contacts.pop())
            print(id)
            data.delete(id)
        elif len(filtered_contacts) == 0:
            print('Contact not found')
        else:
            del_contacts = []
            for contact in filtered_contacts:
                del_contacts.append({
                    'callback': lambda user_input:
                        data.delete(
                            contacts.index(filtered_contacts[user_input])
                        ),
                    'menu_item': f"{contact['name']} {contact['last_name']}"
                })
            tools.render_menu(del_contacts, 'Choose contact to delete: ')
            # for i, contact in enumerate(filtered_contacts):
            #     print(i, contact['name'], contact['last_name'])
            # user_input = int(input())
            # if not 0 <= user_input < len(filtered_contacts):
            #     print('Invalid input')
            # continue
            # id = contacts.index(filtered_contacts[user_input])
            # data.delete(id)
        break


def update_by_phone(user_input):
    pass


# def exit_program(user_input):
#     exit()


if __name__ == '__main__':
 #   while True:
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
            'menu_item': 'Update a record'
        },
        {
            'callback': delete_by_phone,
            'menu_item': 'Delete a record',
        },
        {
            'callback': exit,
            'menu_item': 'Exit\n'
        },
    ]

    tools.render_menu(main_menu)
