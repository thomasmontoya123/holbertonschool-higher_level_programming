#!/usr/bin/python3
"""Unitest module -> max_integer

    max_integer = finds the biggest value
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Intranet cases'''

    def test_intranet_0(self):
        values = [1, 2, 3, 4]
        self.assertEqual(max_integer(values), 4)

    def test_intranet_1(self):
        values = [1, 3, 4, 2]
        self.assertEqual(max_integer(values), 4)

    '''Edge cases'''

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_floats(self):
        values = [1.5, 3.5, 4.5, 2.5]
        self.assertEqual(max_integer(values), 4.5)

    def test_one_value(self):
        self.assertEqual(max_integer([98]), 98)

    def test_negative_values(self):
        values = [-1, -3, -4, -2]
        self.assertEqual(max_integer(values), -1)

    def test_character(self):
        values = ["a", "b", "c"]
        self.assertEqual(max_integer(values), 'c')

    def test_words(self):
        values = ["aloja", "buuuu", "change"]
        self.assertEqual(max_integer(values), 'change')
