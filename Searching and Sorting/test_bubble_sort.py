from bubble_sort import bubble_sort, bubble_sort_v2

import unittest

class TestBubbleSortAlgorithm(unittest.TestCase):

    def _test_sort_single_func(self, sorting_func, input_list):
        expected_list = sorted(input_list)
        self.assertEqual(sorting_func(input_list), expected_list)

    def _test_sort_all_funcs(self, input_list):
        self._test_sort_single_func(bubble_sort, input_list)
        self._test_sort_single_func(bubble_sort_v2, input_list)

    def test_bubble_sort_empty_list(self):
        input_list = []
        self._test_sort_all_funcs(input_list)

    def test_bubble_sort_one_element(self):
        input_list = [0]
        self._test_sort_all_funcs(input_list)

    def test_bubble_sort_same_numbers(self):
        input_list = [1, 1, 1, 1]
        self._test_sort_all_funcs(input_list)

    def test_bubble_sort_already_sorted(self):
        input_list = [1, 2, 3, 4]
        self._test_sort_all_funcs(input_list)

    def test_bubble_sort_reversed(self):
        input_list = [4, 3, 2, 1]
        self._test_sort_all_funcs(input_list)

    def test_bubble_sort_disorder_with_repetitions(self):
        input_list = [3, 5, 3, 2, 4, 2, 1, 1]
        self._test_sort_all_funcs(input_list)


#__________________________________________________________________________--



if __name__=='__main__':
    unittest.main()