from hacker_scraper import hacker_scraper

import unittest
import click
from click.testing import CliRunner


class TestCli(unittest.TestCase):
    def test_input_param(self):
        runner = CliRunner()

        result = runner.invoke(hacker_scraper, ['--posts', ])
        self.assertGreaterEqual(result.exit_code, 0)

        result = runner.invoke(hacker_scraper, ['--no', ])
        self.assertEqual(result.exit_code, 2)

        result = runner.invoke(hacker_scraper, [0, ])
        self.assertEqual(result.exit_code, -1)


    def test_input_posts_int(self):
        runner = CliRunner()

        result = runner.invoke(hacker_scraper, ['--posts', ])
        self.assertEqual(result.exit_code, 2)

        result = runner.invoke(hacker_scraper, ['--posts', 'err', ])
        self.assertEqual(result.exit_code, 2)

        result = runner.invoke(hacker_scraper, ['--posts', '1', ])
        self.assertEqual(result.exit_code, 0)


    def test_input_posts_range(self):
        runner = CliRunner()

        result = runner.invoke(hacker_scraper, ['--posts', '-1', ])
        self.assertEqual(result.exit_code, 2)

        result = runner.invoke(hacker_scraper, ['--posts', '101', ])
        self.assertEqual(result.exit_code, 2)

        result = runner.invoke(hacker_scraper, ['--posts', '50.2', ])
        self.assertEqual(result.exit_code, 2)

        result = runner.invoke(hacker_scraper, ['--posts', '50', ])
        self.assertEqual(result.exit_code, 0)
