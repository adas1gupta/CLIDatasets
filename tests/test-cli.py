import unittest
import os
from click.testing import CliRunner
from data_analyzer.cli import cli

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()
        self.source = 'test_data.csv'
        self.output = 'processed_test_data.csv'

    def test_process_command(self):
        result = self.runner.invoke(cli, ['process', self.source, '--output', self.output])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Data processed and saved to", result.output)
        self.assertTrue(os.path.exists(self.output))
        os.remove(self.output)  # Clean up after test

if __name__ == '__main__':
    unittest.main()
