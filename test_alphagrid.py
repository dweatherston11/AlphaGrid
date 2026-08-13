# test_alphagrid.py
"""
Tests for AlphaGrid module.
"""

import unittest
from alphagrid import AlphaGrid

class TestAlphaGrid(unittest.TestCase):
    """Test cases for AlphaGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AlphaGrid()
        self.assertIsInstance(instance, AlphaGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AlphaGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
