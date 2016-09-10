from hacker_scraper import hacker_scraper

import unittest
import click
import json
from click.testing import CliRunner


class TestOutput(unittest.TestCase):
    def test_format(self):
        runner = CliRunner()

        result = runner.invoke(hacker_scraper, [])
        self.assertGreaterEqual(result.exit_code, 0,
            'Output is: {}'.format(result.output))
        try:
            js = json.loads(result.output)
        except ValueError:
            self.fail('Output is not a valid JSON')


    def test_quantity(self):
        runner = CliRunner()

        result = runner.invoke(hacker_scraper, [])
        self.assertGreaterEqual(result.exit_code, 0,
            'Output is: {}'.format(result.output))
        try:
            js = json.loads(result.output)
        except ValueError:
            self.fail('Output is not a valid JSON')
        self.assertEqual(len(js), 10)

        result = runner.invoke(hacker_scraper, ['--posts', '13'])
        self.assertGreaterEqual(result.exit_code, 0,
            'Output is: {}'.format(result.output))
        try:
            js = json.loads(result.output)
        except ValueError:
            self.fail('Output is not a valid JSON')
        self.assertEqual(len(js), 13,
            'Output is: {}'.format(result.output))
