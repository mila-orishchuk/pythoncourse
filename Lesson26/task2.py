'''
Implement the mergeSort function without using the slice operator.
'''


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = 0
    right_list_index = 0
    left_list_length = len(left_list)
    right_list_length = len(right_list)

    while left_list_index + right_list_index < left_list_length + right_list_length:
        if left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
            
        elif left_list[left_list_index] <= right_list[right_list_index]:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
        else:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        
    input(sorted_list)
    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)


if __name__ == "__main__":
    random_list_of_nums = [5, 7, 9, 1, 2, 55, 22, 89, 18, 21]
    random_list_of_nums = merge_sort(random_list_of_nums)
    print(random_list_of_nums)
