# test_angelwing.py
"""
Tests for AngelWing module.
"""

import unittest
from angelwing import AngelWing

class TestAngelWing(unittest.TestCase):
    """Test cases for AngelWing class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AngelWing()
        self.assertIsInstance(instance, AngelWing)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AngelWing()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
