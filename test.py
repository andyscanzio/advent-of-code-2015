import unittest

import day01
import day02
import day03
import day04


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


class TestDay02(unittest.TestCase):
    def setUp(self):
        self.text_list = ["2x3x4", "1x1x10"]
        self.result_part1_list = [58, 43]
        self.result_part2_list = [34, 14]

    def test_part1(self):
        for text, result in zip(self.text_list, self.result_part1_list):
            self.assertEqual(day02.part1(text), result)

    def test_part2(self):
        for text, result in zip(self.text_list, self.result_part2_list):
            self.assertEqual(day02.part2(text), result)


class TestDay03(unittest.TestCase):
    def setUp(self):
        self.text_part1_list = [">", "^>v<", "^v^v^v^v^v"]
        self.text_part2_list = ["^v", "^>v<", "^v^v^v^v^v"]
        self.result_part1_list = [2, 4, 2]
        self.result_part2_list = [3, 3, 11]

    def test_part1(self):
        for text, result in zip(self.text_part1_list, self.result_part1_list):
            self.assertEqual(day03.part1(text), result)

    def test_part2(self):
        for text, result in zip(self.text_part2_list, self.result_part2_list):
            self.assertEqual(day03.part2(text), result)


class TestDay04(unittest.TestCase):
    def setUp(self):
        self.text_list = ["abcdef", "pqrstuv"]
        self.result_list = [609043, 1048970]

    def test_part1(self):
        for text, result in zip(self.text_list, self.result_list):
            self.assertEqual(day04.part1(text), result)
