import unittest
import os
from data_analyzer.process_data import load_data, process_data, save_data

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        # Path to the test data
        self.source = os.path.join(os.path.dirname(__file__), 'test_data.csv')
        self.output = os.path.join(os.path.dirname(__file__), 'processed_test_data.csv')
        # Ensure the global dataframe is reset before each test
        from data_analyzer.process_data import dataframe
        self._set_global_dataframe(None)

    def _set_global_dataframe(self, value):
        global dataframe
        dataframe = value

    def test_load_data(self):
        self._set_global_dataframe(None)
        load_data(self.source)
        from data_analyzer.process_data import dataframe
        print(f"Dataframe after loading: {dataframe}")
        self.assertIsNotNone(dataframe, "Dataframe should be loaded")

    def test_process_data(self):
        self._set_global_dataframe(None)
        load_data(self.source)
        process_data()
        from data_analyzer.process_data import dataframe
        print(f"Dataframe after processing: {dataframe}")
        self.assertIn('mean_salary', dataframe.columns, "Dataframe should have 'mean_salary' column after processing")

    def test_save_data(self):
        self._set_global_dataframe(None)
        load_data(self.source)
        process_data()
        save_data(self.output)
        self.assertTrue(os.path.exists(self.output), "Processed data should be saved to output file")
        os.remove(self.output)  # Clean up after test

if __name__ == '__main__':
    unittest.main()
