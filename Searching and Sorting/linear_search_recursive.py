


def linear_search_recursive(arr, value, start, end):

    if start >= end: return -1
    if arr[start] == value:
        return start
    if arr[end] == value: return end
    else:
        return linear_search_recursive(arr, value, start+1, end-1)

test_list = [1,3,9,11,15,19,29]



print(linear_search_recursive(test_list, 15, 0, len(test_list)-1)) #prints 4 
print(linear_search_recursive(test_list, 29, 0, len(test_list)-1)) #prints 4
print(linear_search_recursive(test_list, 25, 0, len(test_list)-1)) #prints -1
