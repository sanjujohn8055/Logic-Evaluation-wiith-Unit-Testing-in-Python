import sys
import os
import unittest

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from loader import load_train_data, load_ideal_data, load_test_data, get_data_paths


class TestLoader(unittest.TestCase):

    def test_load_train_data(self):
        df = load_train_data()
        self.assertFalse(df.empty)
        self.assertIn("x", df.columns)

    def test_load_ideal_data(self):
        df = load_ideal_data()
        self.assertFalse(df.empty)
        self.assertIn("x", df.columns)
        self.assertEqual(len(df.columns), 51)  # 50 ideal + 1 x

    def test_load_test_data(self):
        df = load_test_data()
        self.assertFalse(df.empty)
        self.assertIn("x", df.columns)
        self.assertIn("y", df.columns)

    def test_data_paths_exist(self):
        paths = get_data_paths()
        for path in paths.values():
            self.assertTrue(os.path.exists(path))


if __name__ == '__main__':
    unittest.main()
