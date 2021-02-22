'''
Read about the Fibonacci search and implement it using python.
Explore its complexity and compare it to sequential, binary searches.
'''


# def fibonacci_generator(n):
#     a,b = 0,1
#     while True:
#         yield a
#         a, b = b, a + b


def fibonacci_search(seq, x):
    if type(seq) == dict:
        seq = list(seq.values())
    fib_m2 = 0
    fib_m1 = 1
    fib_m = fib_m1 + fib_m2
    
    while fib_m < len(seq):
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m1 + fib_m2
    index = -1
    
    while fib_m > 1:
        i = min(index + fib_m2, (len(seq)-1))
        if (seq[i] < x):
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            index = i
        elif seq[i] > x:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else :
            return i
        
    if(fib_m1 and index < (len(seq)-1) and seq[index+1] == x):
        return index+1
    return -1


if __name__ == "__main__":
    arr = [10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130]
    x = 60
    print('Number found at index : ', fibonacci_search(arr, x))
