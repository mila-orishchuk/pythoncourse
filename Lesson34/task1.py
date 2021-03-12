'''
NUMBERS

We have the following input list of numbers, some of them are prime. You need
to create a utility function that takes as input a number and returns a bool,
whether it is prime or not.

Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent
implementations for filtering NUMBERS. 

Compare the results and performance of each of them.
'''

from contextlib import contextmanager
from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor
import math
from time import process_time

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]


def is_prime(n):
   if n == 2:
      return True
   
   if n < 2 and n % 2 == 0:
      return False

   sqrt_n = int(math.floor(math.sqrt(n)))
   for i in range(3, sqrt_n + 1, 2):
      if n % i == 0:
         return False
   return True


def execute_serial(numbers):
   for number in numbers:
      print(f'{number} {is_prime(number)}')


def execute_map(numbers):
   with ProcessPoolExecutor() as executor:
      for number, result in zip(numbers, executor.map(is_prime, numbers, timeout=60)):
         print(f'{number} {result}')


def execute_submit(numbers):
   with ThreadPoolExecutor() as executor:
      futures = {executor.submit(
         is_prime, number): number for number in numbers}
      for future in as_completed(futures, timeout=90):
         print(f'{futures[future]} {future.result()}')


def show_execution_time(func):
   @contextmanager
   def timer():
      try:
         start = process_time()
         yield
      finally:
         end = process_time()
         print(f'Time spent=>{1000.0*(end - start):>10.3f}ms.')

   print(func.__name__)
   with timer():
      func(NUMBERS)


if __name__ == '__main__':
   functions = [execute_submit, execute_map, execute_serial]

   for func in functions:
      show_execution_time(func)
