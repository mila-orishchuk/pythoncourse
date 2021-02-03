'''
Imports practice

Make a directory with 2 modules; make a function in one of them;
then import this function in the other module and use that in your script of choice.

'''

import modul1

modul1.some_list.append(14)

if __name__ == "__main__":
    print(modul1.some_list)
