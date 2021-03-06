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
#from Lesson3.task4 import validNumber

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
    filtered_contacts = list(filter(
        lambda contact: contact[fields[user_input]].lower() == enter.lower(), contacts))
    for item in filtered_contacts:
        print(*item.values())


def get_contact_id_by_phone(all_contacts, phone):
    filtered_contacts = list(filter(
        lambda contact: contact['phone'] == phone,
        all_contacts
    ))
    contact = None
    if len(filtered_contacts) == 1:
        contact = filtered_contacts.pop()
    elif len(filtered_contacts) == 0:
        raise Exception('Contact not found')
    else:
        available_contacts = []
        for contact in filtered_contacts:
            available_contacts.append({
                'menu_item': f"{contact['name']} {contact['last_name']} {contact['city']}"
            })
        index = tools.render_menu(available_contacts, 'Specify contact: ')
        contact = filtered_contacts[index]

    return all_contacts.index(contact)


def delete_by_phone(user_input):
    phone = input("Enter phone to delete: ")
    all_contacts = data.getAll()
    contact_id = get_contact_id_by_phone(all_contacts, phone)
    data.delete(contact_id)


def update_by_phone(user_input):
    phone = input("Enter phone to update: ")
    all_contacts = data.getAll()
    contact_id = get_contact_id_by_phone(all_contacts, phone)
    new_contact = all_contacts[contact_id]

    update_contact_menu = []
    for key, value in new_contact.items():
        update_contact_menu.append({'menu_item': f'{key}: {value}'})

    field_id = tools.render_menu(
        update_contact_menu, 'Choose field to update: ')

    field = fields[field_id]
    print(field)
    user_input = input(f"Enter new {field} update: ")
    new_contact[field] = user_input
    data.update(contact_id, new_contact)

if __name__ == '__main__':
    while True:
        try:
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
        except Exception as e:
            print(e)
        input('Press any key: ')
