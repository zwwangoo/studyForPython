# coding: utf-8

import unittest

from .bubble import *
from .insert import insert_sort
from .quick import quick_sort
from .select import select_sort
from .shell import shell_sort


class SortTest(unittest.TestCase):
    def setUp(self):
        self.data = [1, 12, 78, 5, 8, 11, 2]
        self.result = [1, 2, 5, 8, 11, 12, 78]

    def test_insert(self):
        self.assertEqual(self.result, insert_sort(self.data))

    def test_bubble(self):
        self.assertEqual(self.result, bubble_sort_1(self.data))

    def test_select(self):
        self.assertEqual(self.result, select_sort(self.data))

    def test_quick(self):
        self.assertEqual(self.result, quick_sort(self.data))

    def test_shell(self):
        self.assertEqual(self.result, shell_sort(self.data))


class BubbleSortTest(unittest.TestCase):
    def setUp(self):
        self.data = [1, 12, 78, 5, 8, 11, 2]
        self.result = [1, 2, 5, 8, 11, 12, 78]

    def test_sort_1(self):
        self.assertEqual(self.result, bubble_sort_1(self.data))

    def test_sort_2(self):
        self.assertEqual(self.result, bubble_sort_2(self.data))

    def test_sort_3(self):
        self.assertEqual(self.result, bubble_sort_3(self.data))


if __name__ == "__main__":
    unittest.main()
