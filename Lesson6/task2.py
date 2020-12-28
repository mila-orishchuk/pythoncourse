#!/usr/bin/python

'''
Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock.
'''

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = {}

for key, value in stock.items():
    total_price[key] = stock[key] * prices[key]
    total_price_stock = sum(total_price.values())
    
print(f'Total price of each fruit is: {total_price} and total price of stock: {total_price_stock}')