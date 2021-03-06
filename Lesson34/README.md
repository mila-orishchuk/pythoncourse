# Мультипроцесорність


![Peek recording Client Window functionality](https://raw.githubusercontent.com/mila-orishchuk/pythoncourse/master/Lesson34/echo_server/img/client_window.gif)


### Links:  
https://docs.python.org/3.7/library/multiprocessing.html  
https://realpython.com/python-concurrency/  
https://www.geeksforgeeks.org/multiprocessing-python-set-1/  
https://www.geeksforgeeks.org/multiprocessing-python-set-2/  
https://www.geeksforgeeks.org/synchronization-pooling-processes-python/  
https://pymotw.com/3/multiprocessing/basics.html  


#### Homework
[Task 1](https://github.com/mila-orishchuk/pythoncourse/blob/master/Lesson34/task1.py)

##### Primes
```
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
```
We have the following input list of numbers, some of them are prime. You need to create a utility function that takes as input a number and returns a bool, whether it is prime or not.

Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS. 
Compare the results and performance of each of them.

[Task 2](https://github.com/mila-orishchuk/pythoncourse/blob/master/Lesson34/task2.py)

##### Requests using concurrent and multiprocessing libraries

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 
As a result, store all comments in chronological order in JSON and dump it to a file. For this task use concurrent and multiprocessing libraries for making requests to Reddit API.

[Task 3](https://github.com/mila-orishchuk/pythoncourse/blob/master/Lesson34/echo_server)

##### Echo server with threading

Create a socket echo server that handles each connection using the multiprocessing library.


