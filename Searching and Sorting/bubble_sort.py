

'''
This program implements bubble_sort(input_array)
'''
#[1, 3, 4, 6, 9, 14, 20, 21, 21, 25]
def bubble_sort(input_array):
    size = len(input_array)-1
    
    for i in range(size):
        for j in range(size):
            if input_array[j] > input_array[j+1]:
                input_array = swap(input_array, j, j+1)
            #print(input_array, 'i:',i, 'j:', j)
        if is_sorted(input_array): break
            
    
    return input_array
        


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
    return a
    
def is_sorted(input_array):
    size = len(input_array) - 1
    for i in range(size):
        if input_array[i] > input_array[i + 1]:
            return False
    return True
    


test_array1 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(bubble_sort(test_array1))
# a = [4, 6, 9]
# print(swap(a, 1,1-1))