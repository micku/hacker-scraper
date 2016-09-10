# -*- coding: utf-8 -*-

from hacker_scraper import only_numbers

import unittest


class TestOutput(unittest.TestCase):
    def test_cases(self):
        cases = {
            '123': 123,
            'asd45': 45,
            'dsa12asd': 12,
            'aa1b1gg': 11,
            u'ùni65à': 65,
            u' 8  8  ': 88,
            u'': 0,
            u'gni': 0,
        }

        for k, v in cases.iteritems():
            self.assertEqual(only_numbers(k), v)
