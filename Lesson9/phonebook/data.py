'''

'''
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

my_file = open(file_name, 'w+')

def getAll():
    my_file.seek(0)
    return json.load(my_file)

def create(contact: dict):
    my_file.seek(0)
    data = json.load(my_file)
    data.append(contact)
    json.dump(data, my_file)

def update(id, new_row):
    my_file.seek(0)
    data = json.load(my_file)
    data[id] = new_row
    json.dump(data, my_file)

def delete(id):
    my_file.seek(0)
    data = json.load(my_file)
    del(data[id])
    json.dump(data, my_file)