'''
Implement binary search using recursion.
'''


def recursive_binary_search(alist, item):

    if len(alist) == 0:
        return False

    mid = len(alist)//2

    if item == alist[mid]:
        return True

    new_list = alist[:mid] if item < alist[mid] else alist[mid+1:]

    return recursive_binary_search(new_list, item)


if __name__ == "__main__":
    a_list = [1, 2, 3, 5, 8, 10, 12, 16]
    
    assert recursive_binary_search(a_list, 1) == True
    assert recursive_binary_search(a_list, 8) == True
    assert recursive_binary_search(a_list, 9) == False
