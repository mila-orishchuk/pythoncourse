'''
Imports practice

Make a directory with 2 modules; make a function in one of them;
then import this function in the other module and use that in your script of choice.

'''


def myfunc(*args):
    return [num for num in range(*args) if num % 2 == 0]


some_list = myfunc(13)
if __name__ == "__main__":
    print(some_list)
