'''
Read about the Fibonacci search and implement it using python.
Explore its complexity and compare it to sequential, binary searches.
'''


def fibonacci_generator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    return fibonacci_generator(n - 1) + fibonacci_generator(n - 2)


def fibonacci_search(arr, x):
    m = 0
    while fibonacci_generator(m) < len(arr):
        m += 1 
    
    offset = -1    
    while fibonacci_generator(m) > 1:
        i = min( offset + fibonacci_generator(m - 2) , len(arr) - 1)
        print('Current Element : ',arr[i])
        
        if (x > arr[i]):
            m = m - 1
            offset = i
        elif (x < arr[i]):
            m = m - 2
        else:
            return i        
    
    if fibonacci_generator(m - 1) and arr[offset + 1] == x:
        return offset + 1
    return -1


if __name__ == "__main__":
    arr = [10, 22, 30, 44, 56, 58, 60, 70, 100, 110, 130]
    x = 60
    print('Number found at index : ', fibonacci_search(arr, x))
