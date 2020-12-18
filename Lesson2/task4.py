#!/usr/bin/python

'''
TASK4

'''

print('{0:06} {1} {2:06b} {3:.2f}'.format(12, "Василий", 54, 32.1))


'''
Change word

'''

word = "python"
word = (word.upper() + word.lower() + word.replace('', ' '))
print(word)

s1 = "Корован"
s1 = s1.replace('К', 'в')
s1 = s1[:4] + 'н' + s1[5:6]
print(s1)

