import sys
import os
import unittest
import pandas as pd

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from processor import FunctionMapper, TestDataMapper
from loader import load_train_data, load_ideal_data, load_test_data
from exceptions import MappingException


class TestProcessor(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.train_df = load_train_data()
        cls.ideal_df = load_ideal_data()
        cls.test_df = load_test_data()

    def test_find_best_fit_returns_four(self):
        mapper = FunctionMapper(self.train_df, self.ideal_df)
        matches = mapper.find_best_fit()
        self.assertEqual(len(matches), 4)
        for key, val in matches.items():
            self.assertTrue(key.startswith("y"))
            self.assertTrue(val.startswith("y"))

    def test_test_mapper_mapping_format(self):
        fm = FunctionMapper(self.train_df, self.ideal_df)
        matches = fm.find_best_fit()

        test_mapper = TestDataMapper(matches, self.train_df)
        result_df = test_mapper.map(self.test_df, self.ideal_df)

        self.assertFalse(result_df.empty)
        self.assertIn("ideal_function", result_df.columns)
        self.assertIn("deviation", result_df.columns)


if __name__ == '__main__':
    unittest.main()
