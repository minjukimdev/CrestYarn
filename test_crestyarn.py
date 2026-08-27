# test_crestyarn.py
"""
Tests for CrestYarn module.
"""

import unittest
from crestyarn import CrestYarn

class TestCrestYarn(unittest.TestCase):
    """Test cases for CrestYarn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrestYarn()
        self.assertIsInstance(instance, CrestYarn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrestYarn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
