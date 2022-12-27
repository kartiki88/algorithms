import unittest

from src.sorting.InsertSort import insertSort


class MyTestCase(unittest.TestCase):
    def test_case_baseCase(self):
        array = [4, 3, 2, 1]
        self.assertEqual(insertSort(array), [1, 2, 3, 4])
    def test_case_with_char(self):
        array = ['x','b','c','a']
        self.assertEqual(insertSort(array), ['a','b','c','x'])


if __name__ == '__main__':
    unittest.main()
