''' 
This is my first time writing test for a program in Python.
-----------------------------------------------------------------
ref: RealPython, https://docs.python-guide.org/writing/tests/
     https://pymbook.readthedocs.io/en/latest/testing.html
     https://codereview.stackexchange.com/questions/209387/bubble-sort-algorithms-and-unittest-in-python
-----------------------------------------------------------------

This program is to test all the search algorithms implemented in this directory.
Search Algorithms, namely:
1. Linear Search
2. Linear Search recursive implementation
2. Binary Search -> v1, v2, v3, v4, check_someone(need more test cases.)
3. Binary Search recursive implementation

'''

import unittest
from linear_search import linear_search
from binarySearch import *
from linear_search_recursive import linear_search_recursive


class TestSearchAlgorithms(unittest.TestCase):

     test_array_1 = [1, 3, 9, 11, 15,19,29]

     def _test_search_algorithm(self, search_func: 'function', input_array: list, saught_value: int, expected_output: int):
         self.assertEqual(search_func(input_array, saught_value), expected_output)

     def _test_all_search_funcs(self, input_array, saught_value):
          try:
               expected_output = input_array.index(saught_value)
          except ValueError:
               expected_output = -1

          self._test_search_algorithm(linear_search, input_array, saught_value, expected_output)
          self._test_search_algorithm(linear_search_recursive, input_array, saught_value, expected_output)
          self._test_search_algorithm(binary_search_v1, input_array, saught_value, expected_output)
          self._test_search_algorithm(binary_search_v2, input_array, saught_value, expected_output)
          self._test_search_algorithm(binary_search_v3, input_array, saught_value, expected_output)
          self._test_search_algorithm(binary_search_v4, input_array, saught_value, expected_output)
          self._test_search_algorithm(binary_search_check_someone, input_array, saught_value, expected_output)
          


     def test_1(self):
          self._test_all_search_funcs(TestSearchAlgorithms.test_array_1, 25)

     def test_first_element(self):
          self._test_all_search_funcs(TestSearchAlgorithms.test_array_1, 1)
     
     def test_last_element(self):
          
          self._test_all_search_funcs(TestSearchAlgorithms.test_array_1, 29)
     
     def test_2(self):
          self._test_all_search_funcs(TestSearchAlgorithms.test_array_1, 15)
     
     def test_3(self):
          self._test_all_search_funcs(TestSearchAlgorithms.test_array_1, 10)

     def test_4(self):
          self._test_all_search_funcs(TestSearchAlgorithms.test_array_1, 9)




if __name__ == "__main__":
    unittest.main()
