import os
import json
import phonebook

path = './Lesson9/phonebook/'
file_name = path + 'phonebook.txt'

if not os.path.exists(path):
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)
    else:
        print("You add directory")


mod = 'r+' if os.path.isfile(file_name) else 'w+'   
my_file = open(file_name, mod)

def getAll():
    my_file.seek(0)
    return json.load(my_file)


def create(contact: dict):
    data = json.load(my_file)
    data.append(contact)
    my_file.truncate(0)
    my_file.seek(0)
    json.dump(data, my_file)

def update(id, new_contact):
    data = json.load(my_file)
    data[id] = new_contact
    json.dump(data, my_file)


def delete(id):
    my_file.seek(0)
    data = json.load(my_file)
    if not data[id]:
        raise IndexError("Id not found")
    del(data[id])
    my_file.truncate(0)
    my_file.seek(0)
    json.dump(data, my_file)

#my_file = close(file_name)
