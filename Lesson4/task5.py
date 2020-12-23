
'''
tasks 

'''
import math

'''

'''
print('Solving quadratic equation')
a = float(input('a = ' ))
b = float(input('b = '))
c = float(input('c = '))

discriminant = b**2 + 4*a*c

if discriminant < 0:
    print ('This equation has no real solution')

elif discriminant == 0:
    x = (-b / (2*a))
    print ('Discriminant = 0', f'This equation has one solutions: {x:.2f}')

else:
    x1 =  (-b + math.sqrt(discriminant)) / (2*a)
    x2 =  (-b - math.sqrt(discriminant)) / (2*a)
    print ('Discriminant =', discriminant)
    print (f'This equation has two solutions: {x1:.2f} and {x2:.2f}')