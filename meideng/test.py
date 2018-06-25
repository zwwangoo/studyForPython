import unittest
from tt import get_order_days, get_deadline


class Test(unittest.TestCase):
    def test_fun1(self):
        self.assertEqual(get_order_days(2018, 1, 31), 28)
    def test_func2(self):
        self.assertEqual(get_deadline(2011, 3, 1, 12), (2012, 3, 1))
    def test_func3(self):
        self.assertEqual(get_deadline(2011, 2, 28, 13), (2012, 3, 28))
    def test_func4(self):
        self.assertEqual(get_deadline(2008, 2, 29, 12), (2009, 2, 28))
    def test_func5(self):
        self.assertEqual(get_deadline(2011, 11, 29, 2), (2012, 1, 29))

if __name__ == "__main__":
    unittest.main()

