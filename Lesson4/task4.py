
'''
The math quiz program

'''
import random
import operator

def random_math(success = 5): 

    while success > 0:  
        a = random.randint(1,20)
        b = random.randint(1,20) 
        a,b = (b,a) if a < b else (a,b)
        random_operator = random.choice(['+', '-', '*'])

        print(a, random_operator, b, '= ?')

        userInput = input()

        if random_operator == "+":
            result = a + b
        elif random_operator == "-":
            result = a - b
        elif random_operator == "*":
            result = a * b
        if str(result) == userInput:
            success += 1
        else:
            success = 0
            print('try again')

if __name__ == '__main__':
    random_math()