''' This is my first time writing test for a program in Python.
-----------------------------------------------------------------
ref: RealPython, https://docs.python-guide.org/writing/tests/
     https://pymbook.readthedocs.io/en/latest/testing.html
     https://codereview.stackexchange.com/questions/209387/bubble-sort-algorithms-and-unittest-in-python
-----------------------------------------------------------------

This program is to test all the search algorithms implemented in this directory.
Search Algorithms, namely:
1. Linear Search
2. Binary Search

'''

import unittest
from linear_search import linear_search
from binarySearch import binary_search


class TesSearchAlgorithm(unittest.TestCase):

     test_array_1 = [1, 3, 9, 11, 15,19,29]

     def _test_search_algorithm(self, search_func: 'function', input_array: list, saught_value: int, expected_output: int):
         self.assertEqual(search_func(input_array, saught_value), expected_output)

     def _test_all_search_funcs(self, input_array, saught_value):
          try:
               expected_output = input_array.index(saught_value)
          except ValueError:
               expected_output = -1

          self._test_search_algorithm(linear_search, input_array, saught_value, expected_output)
          self._test_search_algorithm(binary_search, input_array, saught_value, expected_output)

     def test_1(self):
          self._test_all_search_funcs([1, 3, 9, 11, 15,19,29], 25)

     def test_first_element(self):
          
          self._test_all_search_funcs([1, 3, 9, 11, 15,19,29], 1)
     
     def test_last_element(self):
          
          self._test_all_search_funcs(test_array_1, 29)
     
     def test_2(self):
          self._test_all_search_funcs(test_array_1, 15)




if __name__ == "__main__":
    unittest.main()
