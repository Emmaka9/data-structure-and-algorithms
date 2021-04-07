#________________________________________________________________________--

import unittest

class TestBubbleSortAlgorithm(unittest.TestCase):

    def _test_sort(self, sorting_func, input_list, expected_list):
        self.assertEqual(sorting_func(input_list), expected_list)

    def test_bubble_sort_v1_with_positive_numbers(self):
        self._test_sort(bubble_sort, [5, 5, 7, 8, 2, 4, 1], [1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_v1_negative_numbers_only(self):
        self._test_sort(bubble_sort, [-1, -3, -5, -7, -9, -5], [-9, -7, -5, -5, -3, -1])

    def test_bubble_sort_v1_with_negative_and_positive_numbers(self):
        self._test_sort(bubble_sort, [-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1], [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_v1_same_numbers(self):
        self._test_sort(bubble_sort, [1, 1, 1, 1], [1, 1, 1, 1])

    def test_bubble_sort_v1_empty_list(self):
        self._test_sort(bubble_sort, [], [])

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



if __name__=='__main__':
    unittest.main()