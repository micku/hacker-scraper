# -*- coding: utf-8 -*-

from hacker_scraper import is_valid

import unittest


class TestIsValid(unittest.TestCase):
    def test_title(self):
        base = {
            'uri': 'http://test.com/',
            'author': 'test author',
            'points': 1,
            'comments': 1,
            'rank': 1,
        }
        cases = [
            ({'title': 'It\'s ok'}, True),
            ({'title': ''}, False),
            ({'title': 'x'*257}, False),
        ]

        for (k, v) in cases:
            test_case = base.copy()
            test_case.update(k)
            self.assertEqual(is_valid(test_case), v, '{} failed'.format(k))

    def test_author(self):
        base = {
            'title': 'test title',
            'uri': 'http://test.com/',
            'points': 1,
            'comments': 1,
            'rank': 1,
        }
        cases = [
            ({'author': 'It\'s ok'}, True),
            ({'author': ''}, False),
            ({'author': 'x'*257}, False),
        ]

        for (k, v) in cases:
            test_case = base.copy()
            test_case.update(k)
            self.assertEqual(is_valid(test_case), v, '{} failed'.format(k))

    def test_uri(self):
        base = {
            'title': 'test title',
            'author': 'test author',
            'points': 1,
            'comments': 1,
            'rank': 1,
        }
        cases = [
            ({'uri': 'http://this.is.a.valid.url/'}, True),
            ({'uri': ''}, False),
            ({'uri': 'è@so.valid'}, True),
            ({'uri': 'mailto:this@is.valid'}, True),
            ({'uri': 'tel:+39-123-4567'}, True),
        ]

        for (k, v) in cases:
            test_case = base.copy()
            test_case.update(k)
            self.assertEqual(is_valid(test_case), v, '{} failed'.format(k))

    def test_points_comments_rank(self):
        base = {
            'title': 'test title',
            'author': 'test author',
            'uri': 'http://test.com/',
        }
        cases = [
            ({ 'points': -1, 'comments': 1, 'rank': 1}, False),
            ({ 'points': 1, 'comments': -1, 'rank': 1}, False),
            ({ 'points': 1, 'comments': 1, 'rank': -1}, False),
            ({ 'points': 1.2, 'comments': 1, 'rank': 1}, False),
            ({ 'points': 1, 'comments': 1.2, 'rank': 1}, False),
            ({ 'points': 1, 'comments': 1, 'rank': 1.2}, False),
            ({ 'points': '1', 'comments': 1, 'rank': 1}, False),
            ({ 'points': 1, 'comments': '1', 'rank': 1}, False),
            ({ 'points': 1, 'comments': 1, 'rank': '1'}, False),
            ({ 'points': 0, 'comments': 1, 'rank': 1}, True),
            ({ 'points': 1, 'comments': 0, 'rank': 1}, True),
            ({ 'points': 1, 'comments': 1, 'rank': 0}, True),
        ]

        for (k, v) in cases:
            test_case = base.copy()
            test_case.update(k)
            self.assertEqual(is_valid(test_case), v, '{} failed'.format(k))

