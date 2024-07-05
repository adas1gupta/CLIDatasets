# tests/test_cli.py
import unittest
from click.testing import CliRunner
from data_analyzer.cli import cli

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_load(self):
        result = self.runner.invoke(cli, ['load', 'path/to/dataset.csv'])
        self.assertIn('Loading dataset from', result.output)

if __name__ == "__main__":
    unittest.main()
