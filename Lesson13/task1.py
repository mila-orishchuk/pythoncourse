'''
Write a Python program to detect the number of local variables declared in a function.

'''

def rectangle():
    a = float(input('Width: '))
    b = float(input('Height: '))
    print('Area: %.2f' % (a*b))


if __name__ == '__main__':
    rectangle()
    print('Number of local variables:',
          rectangle.__code__.co_nlocals)
