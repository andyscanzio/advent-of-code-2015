import unittest

import day01


class TestDay01(unittest.TestCase):
    def setUp(self):
        self.text_part1_list = [
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
        self.result_part1_list = [0, 0, 3, 3, 3, -1, -1, -3, -3]
        self.text_part2_list = [")", "()())"]
        self.result_part2_list = [1, 5]

    def test_part1(self):
        for text, result in zip(self.text_part1_list, self.result_part1_list):
            self.assertEqual(day01.part1(text), result)

    def test_part2(self):
        for text, result in zip(self.text_part2_list, self.result_part2_list):
            self.assertEqual(day01.part2(text), result)
