import unittest
from fun_with_collections import sort_and_search_list


class MyTestCase(unittest.TestCase):
    def test_search_list_found(self):
        self.assertEqual(sort_and_search_list.search_list(['z', 'e', 'i', 'o', 'u'], 'e'), 1)

    def test_search_list_not_found(self):
        self.assertEqual(sort_and_search_list.search_list(['z', 'e', 'i', 'o', 'u'], 'x'), -1)

    def test_sort(self):
        self.assertEqual(sort_and_search_list.sort_list(['z', 'e', 'i', 'o', 'u']), ['e', 'i', 'o', 'u', 'z'])


if __name__ == '__main__':
    unittest.main()
