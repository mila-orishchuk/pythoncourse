import os
import json
import phonebook

path = './Lesson9/phonebook/'
file_name = path + 'phonebook.txt'

if not os.path.exists(path):
    try:
        os.mkdir(path)
    except OSError as error:
        print (error)
    else:
        print ("You add directory")




my_file = open(file_name, 'r+')
if not os.path.isfile(file_name):
    with open(file_name, "r+") as my_file:
        json.dump([], my_file)

def getAll():
    return json.load(my_file)

def create(contact: dict):
    data = json.load(my_file)
    data.append(contact)
    json.dump(data, my_file)
    print()

def update(id, new_contact):
    data = json.load(my_file)
    data[id] = new_contact
    json.dump(data, my_file)

def delete(phone):
    data = json.load(my_file)
    del(data[phone])
    json.dump(data, my_file)

#my_file = close(file_name)