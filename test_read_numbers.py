import unittest

from read_numbers.read_numbers import read_numbers


class ReadNumbersTestCase(unittest.TestCase):

    def setUp(self):
        self.list_1 = [1]
        self.list_2 = [1, 3]
        self.list_3 = [1, 2, 3]
        self.list_4 = [1, 2, 3, 6, 8, 9, 10]
        self.list_5 = [13, 14, 15, 16, 20, 23, 24, 25, 100]

    def test_read_numbers(self):
        self.assertEqual(read_numbers(self.list_1), "1")
        self.assertEqual(read_numbers(self.list_2), "1, 3")
        self.assertEqual(read_numbers(self.list_3), "1~3")
        self.assertEqual(read_numbers(self.list_4), "1~3, 6, 8~10")
        self.assertEqual(read_numbers(self.list_5), "13~16, 20, 23~25, 100")
