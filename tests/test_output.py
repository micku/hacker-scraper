from hacker_scraper import hacker_scraper

import unittest
import click
import json
from click.testing import CliRunner


class TestOutput(unittest.TestCase):
    def test_format(self):
        runner = CliRunner()

        result = runner.invoke(hacker_scraper, [])
        self.assertGreaterEqual(result.exit_code, 0)
        js = json.loads(result.output)


    def test_quantity(self):
        runner = CliRunner()

        result = runner.invoke(hacker_scraper, [])
        self.assertGreaterEqual(result.exit_code, 0)
        js = json.loads(result.output)
        self.assertEqual(len(js), 10)

        result = runner.invoke(hacker_scraper, ['--posts', '13'])
        self.assertGreaterEqual(result.exit_code, 0)
        js = json.loads(result.output)
        self.assertEqual(len(js), 13)
