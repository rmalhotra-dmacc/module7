import unittest
from fun_with_collections import sort_and_search_array
import array as arr


class MyTestCase(unittest.TestCase):
    def test_search_array_found(self):
        self.assertEqual(sort_and_search_array.search_array([1, 2, 3, 4, 5, 6, 7], 2), 1)

    def test_search_array_not_found(self):
        self.assertEqual(sort_and_search_array.search_array([1, 2, 3, 4, 5, 6, 7], 9), -1)

    def test_sort(self):
        self.assertEqual(sort_and_search_array.sort_array([2, 3, 1, 5, 4]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
