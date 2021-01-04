#!/usr/bin/python

'''
Write a function that takes in two numbers from the user via input(), 
call the numbers a and b, and then returns the value of squared a divided by b,
construct a try-except block which raises an exception if the two values given by
the input function were not numbers, and if value b was zero(cannot divide by zero).    
'''

def return_square_division(a, b):
    return a**2 / b

if __name__ == "__main__":
    while True:
        try:
            a, b = (int(input("Enter first number: ")), int(input("Enter second number: ")))
            print(f'{return_square_division(a, b):.2f}')
            break
        except ValueError:
            print('Invalid enter, not integer. Try again!')
        except ZeroDivisionError:
            print('Invalid enter, cannot divide by zero. Try again!')
    
