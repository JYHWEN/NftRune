# test_nftrune.py
"""
Tests for NftRune module.
"""

import unittest
from nftrune import NftRune

class TestNftRune(unittest.TestCase):
    """Test cases for NftRune class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftRune()
        self.assertIsInstance(instance, NftRune)

    def test_run_method(self):
        """Test the run method."""
        instance = NftRune()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
