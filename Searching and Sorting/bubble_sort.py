
'''
This program implements bubble_sort(input_array)
'''
import unittest

#[1, 3, 4, 6, 9, 14, 20, 21, 21, 25]

# implementation
def bubble_sort(input_array:list) -> list:
    size = len(input_array)-1
    numItr = 0 # to count the number of iteration needed.
    sorted = False

    while not sorted:
        sorted = True
        for i in range(size):
            if input_array[i] > input_array[i + 1]:
                input_array[i], input_array[i + 1] = input_array[i + 1], input_array[i]
                sorted = False
            print(input_array, 'numItr: %d size: %d, i:%d'%(numItr, size, i))
            numItr += 1
        size -= 1
    print('Number of iteration needed in bubbleSort: %d' %numItr)
    return input_array


#--------------------------------------------------------
# An wikipedia version of Bubble Sort

def bubble_sort_Optimized(A:list) -> list:
    n = len(A)
    numItr = 0 # to count the number of iteration needed.
    
    while n > 1:
        
        newn = 0
        for i in range(1, n):
            if A[i-1] > A[i]:
                A[i - 1], A[i] = A[i], A[i - 1]
                newn = i
            numItr += 1
            print(A,'numItr: %d n: %d, newn:%d, i:%d'%(numItr, n, newn, i))
        n = newn

    print('Number of iteration needed in bubble_sort_Optimized: %d' %numItr)
    return A


                
        



    




   




#________________________________________________________________________--

class TestBubbleSortAlgorithm(unittest.TestCase):

    def _test_sort(self, sorting_func, bubble_sort, expected_list):
        self.assertEqual(sorting_func(input_list), expected_list)

    def test_bubble_sort_v1_with_positive_numbers(self):
        self._test_sort(bubble_sort_v1, [5, 5, 7, 8, 2, 4, 1], [1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_v1_negative_numbers_only(self):
        self._test_sort(bubble_sort_v1, [-1, -3, -5, -7, -9, -5], [-9, -7, -5, -5, -3, -1])

    def test_bubble_sort_v1_with_negative_and_positive_numbers(self):
        self._test_sort(bubble_sort_v1, [-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1], [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_v1_same_numbers(self):
        self._test_sort(bubble_sort_v1, [1, 1, 1, 1], [1, 1, 1, 1])

    def test_bubble_sort_v1_empty_list(self):
        self._test_sort(bubble_sort_v1, [], [])

    def test_bubble_sort_v2_with_positive_numbers(self):
        self._test_sort(bubble_sort_v2, [5, 5, 7, 8, 2, 4, 1], [1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_v2_negative_numbers_only(self):
        self._test_sort(bubble_sort_v2, [-1, -3, -5, -7, -9, -5], [-9, -7, -5, -5, -3, -1])

    def test_bubble_sort_v2_with_negative_and_positive_numbers(self):
        self._test_sort(bubble_sort_v2, [-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1], [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_v2_same_numbers(self):
        self._test_sort(bubble_sort_v2, [1, 1, 1, 1], [1, 1, 1, 1])

    def test_bubble_sort_v2_empty_list(self):
        self._test_sort(bubble_sort_v2, [], [])

#__________________________________________________________________________--











# # Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]
   
# print(bubbleSort(arr))
   
# print ("Sorted array :")


#-------------------------------------------------------------




test_array1 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test_array1_O = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print(bubble_sort(test_array1))

print('-'*60)
# Test Optimized bubble sort

print(bubble_sort_Optimized(test_array1_O))

# print(bubble_sort(test_array1))
# # a = [4, 6, 9]
# # print(swap(a, 1,1-1))
