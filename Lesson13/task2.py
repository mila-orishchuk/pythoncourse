'''
Write a Python program to access a function inside a function
(Tips: use function, which returns another function)

'''


def area(a):

    def rectangle(b):
        tri = a * b
        return f'Triangle area = {tri}'
    return rectangle

    # return lambda b: f'Triangle area = {a * b}'


if __name__ == '__main__':
    print('Finding the area of the diffrent shapes')
    area_rect = area(3)
    print(area_rect(3))
