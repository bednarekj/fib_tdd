import unittest

from main import fib_nums


class FibNumsTests(unittest.TestCase):

    def test_1_number(self):
        number_gen = fib_nums()
        self.assertEqual(1, next(number_gen))

    def test_2_numbers(self):
        number_gen = fib_nums()
        self.assertEqual(1, next(number_gen))
        self.assertEqual(1, next(number_gen))

    def test_10_numbers(self):
        number_gen = fib_nums()
        numbers = [next(number_gen) for _ in range(10)]
        expected_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual(expected_numbers, numbers)
