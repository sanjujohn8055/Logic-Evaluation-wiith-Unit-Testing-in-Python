import sys
import os
import unittest

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from exceptions import MappingException


class TestExceptions(unittest.TestCase):

    def test_mapping_exception_raised(self):
        with self.assertRaises(MappingException):
            raise MappingException("Test error")
        
        try:
            raise MappingException("Test error")
        except MappingException as e:
            self.assertEqual(str(e), "Test error")


if __name__ == '__main__':
    unittest.main()
