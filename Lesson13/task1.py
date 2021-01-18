'''
Write a Python program to detect the number of local variables declared in a function.

'''

def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    print("Площадь: %.2f" % (a*b))


if __name__ == '__main__':
    print("Number of local variables:",
          rectangle.__code__.co_nlocals)
