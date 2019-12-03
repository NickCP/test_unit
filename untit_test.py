from  main import sorting
import unittest


class My_List_Test(unittest.TestCase):
    def test_normal(self):
        res = sorting([9, 8, 6, 5, 4])
        self.assertEqual(res, [4, 5, 6, 8, 9])
        self.assertEqual(sorting([3, 2, 1]), [1, 2, 3])

    def test_empty(self):
        res = sorting([])
        self.assertEqual(res, [])
