'''
Files

Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
Then write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from the system command line. 
Does the new file show up in the directory where you ran your scripts? 
What if you add a different directory path to the filename passed to open?
Note: file write methods do not add newline characters to your strings; add an explicit ‘\n’ at the end of the string if you want to 
fully terminate the line in the file.

'''
import os
import json

my_details = 'Hello file world!\n'

path = './Lesson9/tmp/'
add_file = path + 'myfile.txt'

if not os.path.exists(path):
    try:
        os.mkdir(path)
    except OSError as error:
        print (error)
    else:
        print ("You add directory")

try:
    with open(add_file, 'w+') as my_file:
        json.dump(my_details, my_file)
        my_file.seek(0)
        print(my_file.read())
except Exception as e:
    print(e)
