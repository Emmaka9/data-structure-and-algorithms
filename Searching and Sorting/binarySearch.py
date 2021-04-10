"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

'''
The Golden Rule of coding: Say what you mean simply and directly.
ref: The Elements of Programming Style
'''


def binary_search_v1(input_array, value):
    """Your code goes here."""
    #  0 1 2 3  4  5  6
    # [1,3,9,11,15,19,29] -> Find 25

    start, end = 0, len(input_array)-1

    # @loop_invariant: if input_array[mid]==value for any mid, then 0<=start<=mid<=end<=len(input_array)-1.
    while start <= end:
        mid = start + (end - start) // 2
        assert start <= mid <= end

        if input_array[mid] == value:
            return mid
        elif value > input_array[mid]:
            start = mid + 1

        elif value < input_array[mid]:
            end = mid - 1

    return -1

# ask someone to look into it for me.


def binary_search_check_someone(arr, value):
    upper = len(arr)
    lower = 0
    mid1 = 0
    while(lower < upper):
        #print('loop')
        mid = lower + (upper - lower)//2

        if arr[mid] == value:
            return mid
        elif value > arr[mid]:
            lower = mid
        elif value < arr[mid]:
            upper = mid

        if mid1 == mid:
            return -1
        mid1 = mid
    return -1


def binary_search_v2(arr, value):
    upper = len(arr)
    lower = 0

    while(lower <= upper):
        #print('loop')
        mid = lower + (upper - lower)//2

        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            lower = mid+1
        elif value < arr[mid]:
            upper = mid-1
    return -1


def binary_search_v3(arr, value):
    upper = len(arr)
    lower = 0

    while(lower < upper):
        #print('loop')
        mid = lower + (upper - lower)//2

        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            lower = mid+1
        elif value < arr[mid]:
            upper = mid
    return -1


'''
    Implementation -- version 4.
--Doesn't works while saught_value doesn't exist in the array.
'''


def binary_search_v4(arr, value):
    upper = len(arr)
    lower = 0

    while lower < upper:
        i = lower + (upper - lower)//2

        if arr[i] == value:
            return i
        if arr[i] < value:
            lower = i
        if arr[i] > value:
            upper = i
    return -1


'''
-----------Implementation Binary Search-----------
Recursive Binary Search: 
'''
# [1,3,9,11,15,19,29]


def binary_search(arr, value, start, end):

    i = start + (end - start)//2
    if start > end:
        return -1
    if arr[i] == value:
        return i
    if arr[i] > value:
        return binary_search(arr, value, start, end=i - 1)
    if arr[i] < value:
        return binary_search(arr, value, start=i+1, end=end)


test_list = [1, 3, 9, 11, 15, 19, 29]
# test_val1 = 25
# test_val2 = 15

# # prints -1 #v4 deosn't work
# print(binary_search(test_list, test_val1, 0, len(test_list)))
# print(binary_search(test_list, test_val2, 0, len(test_list)))  # prints 4 # works
# print(binary_search(test_list, 29, 0, len(test_list)))  # prints 6 #works
# print(binary_search(test_list, 2, 0, len(test_list)))  # prints -1 #doesn't work
# print(binary_search(test_list, 9, 0, len(test_list)))  # prints 2 # works
# # prints -1 # doesn't work
# print(binary_search(test_list, 10, 0, len(test_list)))
# print(binary_search_check_someone(test_list, 10))