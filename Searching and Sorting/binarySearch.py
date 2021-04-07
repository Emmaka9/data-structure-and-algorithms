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



def binary_search(input_array, value):
    """Your code goes here."""
    #  0 1 2 3  4  5  6
    # [1,3,9,11,15,19,29] -> Find 25

    start, end = 0, len(input_array)-1

    # @loop_invariant: if input_array[mid]==value for any mid, then 0<=start<=mid<=end<=len(input_array)-1.
    while start <= end:
        mid = start + (end - start) //2
        assert start<= mid <= end

        if input_array[mid] == value:
            return mid
        elif value > input_array[mid]:
            start = mid + 1
        
        elif value < input_array[mid]:
            end = mid -1

    return -1

# test_list = [1,3,9,11,15,19,29]
# test_val1 = 25
# test_val2 = 15

# print(binary_search(test_list, test_val1)) #prints -1
# print(binary_search(test_list, test_val2)) #prints 4
# print(binary_search(test_list, 29)) #prints 6
# print(binary_search(test_list, 2)) #prints 6
