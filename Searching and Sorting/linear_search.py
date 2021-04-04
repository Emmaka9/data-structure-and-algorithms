''' 
Implementation of Linear Search algorithm.
---------------------------------------------------
1. Function 'linear_search(input_array, value) implements the array'
    -> Find the value in the input_array.
    -> While the value is found, index of the value is returned.
    -> When the value is not found, -1 is returned.
2. The test cases are in the main function.

'''

def linear_search(input_array, value):
    
    for i in range(len(input_array)):
        if input_array[i] == value:
            return i
    return -1



if __name__ == "__main__":
    ''' Test Cases '''
    test_list = [1,3,9,11,15,19,29]
    test_val1 = 25
    test_val2 = 15

    print(linear_search(test_list, test_val1))
    print(linear_search(test_list, test_val2))
