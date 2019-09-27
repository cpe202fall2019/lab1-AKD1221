import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([5, 5, 3]), 5)
        self.assertEqual(max_list_iter([5]), 5)
        self.assertEqual(max_list_iter([1, 3, 5, 5, 6, 7, 8, 10, 3]), 10)
        self.assertEqual(max_list_iter([1, 8, 3]), 8)
        self.assertEqual(max_list_iter([1, 5, 5]), 5)
        self.assertEqual(max_list_iter([]), None)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([3, 2, 1]), [1, 2, 3])
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(None)
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([1, 3]), [3, 1])
        self.assertEqual(reverse_rec([1, 3, 2, 4, 7]), [7, 4, 2, 3, 1])

    def test_bin_search(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]

        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        self.assertEqual(bin_search(3, 0, 3, []), None)
        with self.assertRaises(ValueError):
            bin_search(2, 0, 3, None)
        self.assertEqual(bin_search(1, 0, 1, [1, 5]), 0)
        self.assertEqual(bin_search(5, 0, 1, [2, 5]), 1)
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        self.assertEqual(bin_search(12, 0, len(list_val) - 1, list_val), None)
        self.assertEqual(bin_search(2, 0, len(list_val) - 1, list_val), 2)
        self.assertEqual(bin_search(7, 0, len(list_val) - 1, list_val), 5)

if __name__ == "__main__":
    unittest.main()
