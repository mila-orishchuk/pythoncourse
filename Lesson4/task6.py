
'''
tasks 

'''

number = int(input('Enter number: '))
for i in range(number):
    if not i % 18 == 0 and not (50 <= i <= 80):
        if i == 42:
            print('Потому что')
        else:
            print(i)

'''

'''
attempts = 0
max_number = None
while attempts != 5:
    user_input = input('Enter numbers: ')
    if user_input.isnumeric():
        if not max_number or max_number < int(user_input):
            max_number = int(user_input)
        attempts += 1
    elif user_input.lower() == 'q':
        break
    else:
        print('Invalid enter. Try again.')
        continue
print(max_number)

'''

'''
def math_equ():
    arguments = ['operand1', 'operator', 'operator2']
    
    while True:
        expression = []
        for i in arguments:
            userInput = (input (f'Enter {i}: '))
            expression.append(userInput)
            if userInput.lower() == 'q':
                return
        if expression[1] == '+':
            print(int(expression[0]) + int(expression[2]))   
        elif expression[1] == '-':
            print(int(expression[0]) - int(expression[2]))
        else:
            print('invalid operator')
    
math_equ()