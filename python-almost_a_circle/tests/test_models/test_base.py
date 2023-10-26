"""
Unittest for Base module
"""
import unittest
from models.base import Base
import io
import sys
import os

class TestBase(unittest.TestCase):
    """
    Tests for Base Class
    """
    def test_base_arguments(self):
        """
        Testing for missing arguments
        """
        base_1 = Base()
        base_2 = Base()
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 2)
        self.assertNotEqual(base_1.id, base_2.id)
        base_3 = Base(45)
        self.assertEqual(base_3.id, 45)
