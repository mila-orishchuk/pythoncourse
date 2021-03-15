'''
Practice asynchronous code

Create a separate asynchronous code to calculate Fibonacci, factorial, squares
and cubic for an input n. Schedule the execution of this code using
asyncio.gather for a list of integers from 1 to 10. You need to get four lists
of results from corresponding functions.

Rewrite the code to use simple functions to get the same results but using a
multiprocessing library. Time the execution of both realizations, explore the results,
what realization is more effective, why did you get a result like this.
'''

import asyncio
from multiprocessing import Process
import time

async def fibonacci(n):
    index = n - 2
    fib1 = fib2 = 1

    while index > 0:
        fib1, fib2 = fib2, fib1 + fib2
        index -= 1

    return fib2


async def factorial(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1

    return factorial


async def squares(n):
    return n**2


async def cubic(n):
    return n**3


def fibonacci_math(n):
    result = []
    n1 = 0
    n2 = 1
    for i in range(1, n + 1):
        result.append(n1)
        n1, n2 = n2, n1 + n2
    return result


def factorial_math(n):
    result = []
    a = 1
    for i in range(1, n + 1):
        a *= i
        result.append(a)

    return result


def square_math(n):
    result = []
    for i in range(1, n + 1):
        a = i ** 2
        result.append(a)

    return result


def cubic_math(n):
    result = []
    for i in range(1, n + 1):
        a = i ** 3
        result.append(a)

    return result


async def gather_all(n):
    await asyncio.gather(
        factorial(n),
        fibonacci(n),
        squares(n),
        cubic(n))


if __name__ == '__main__':
    math_functions = [cubic_math, square_math, fibonacci_math, factorial_math]
    n = 10
    
    start_time = time.time()
    loop = asyncio.get_event_loop()
    for i in range(n):
        asyncio.run(gather_all(i))
    end_time = time.time()
    print(f'Total time: {(end_time - start_time):.5f}ms.')

    
    start_time = time.time()
    for func in math_functions:
        new_process = Process(target=func, args=(n, ))
        new_process.start()
        new_process.join()
    end_time = time.time()
    print(f'Total time: {(end_time - start_time):.5f}ms.')
