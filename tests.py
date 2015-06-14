import unittest

from main import fib_nums, find_term


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


class FindTermsTests(unittest.TestCase):

    def test_0_number(self):
        self.assertEqual('F1', find_term(0))

    def test_1_number(self):
        self.assertEqual('F1', find_term(1))

    def test_2_number(self):
        self.assertEqual('F7', find_term(2))

    def test_3_number(self):
        self.assertEqual('F1', find_term(1))

    def test_4_number(self):
        self.assertEqual('F7', find_term(2))

    def test_5_number(self):
        self.assertEqual('F12', find_term(3))

    def test_6_number(self):
        self.assertEqual('F17', find_term(4))

    def test_7_number(self):
        self.assertEqual('F21', find_term(5))

    def test_8_number(self):
        self.assertEqual('F26', find_term(6))

    def test_9_number(self):
        self.assertEqual('F31', find_term(7))

    def test_10_number(self):
        self.assertEqual('F36', find_term(8))
