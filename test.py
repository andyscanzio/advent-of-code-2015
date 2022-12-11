import unittest

import day01


class TestDay01(unittest.TestCase):
    def setUp(self):
        self.text_list = [
            "(())",
            "()()",
            "(((",
            "(()(()(",
            "))(((((",
            "())",
            "))(",
            ")))",
            ")())())",
        ]
        self.result_list = [0, 0, 3, 3, 3, -1, -1, -3, -3]

    def test_part1(self):
        for text, result in zip(self.text_list, self.result_list):
            self.assertEqual(day01.part1(text), result)
