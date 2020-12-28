#!/usr/bin/python

'''
Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock.
'''
def total_price(stock, prices):
    total_price = 0
    
    for key in stock:
        if key in prices:
            total_price += stock[key] * prices[key]
            
    return total_price

if __name__ == '__main__':
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

    total_stock_price = total_price(stock, prices)
    print(total_stock_price)

    