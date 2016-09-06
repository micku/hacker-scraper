from hacker_scraper import hacker_scraper

import unittest
import click
from click.testing import CliRunner


class TestCli(unittest.TestCase):
    def test_input_param(self):
        runner = CliRunner()

        result = runner.invoke(hacker_scraper, ['--posts', ])
        assert result.exit_code >= 0

        result = runner.invoke(hacker_scraper, ['--no', ])
        assert result.exit_code == 2

        result = runner.invoke(hacker_scraper, [0, ])
        assert result.exit_code == -1


    def test_input_posts_int(self):
        runner = CliRunner()

        result = runner.invoke(hacker_scraper, ['--posts', ])
        assert result.exit_code == 2

        result = runner.invoke(hacker_scraper, ['--posts', 'err', ])
        assert result.exit_code == 2

        result = runner.invoke(hacker_scraper, ['--posts', '1', ])
        assert result.exit_code == 0


    def test_input_posts_range(self):
        runner = CliRunner()

        result = runner.invoke(hacker_scraper, ['--posts', '-1', ])
        assert result.exit_code == 2

        result = runner.invoke(hacker_scraper, ['--posts', '101', ])
        assert result.exit_code == 2

        result = runner.invoke(hacker_scraper, ['--posts', '50.2', ])
        assert result.exit_code == 2

        result = runner.invoke(hacker_scraper, ['--posts', '50', ])
        assert result.exit_code == 0
