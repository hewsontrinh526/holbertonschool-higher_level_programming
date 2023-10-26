#!/usr/bin/python3
"""
Unittest for Rectangle module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import io
import sys
import os


class TestRectangle(unittest.TestCase):
    """
    Tests for Rectangle Class
    """
    def test_rectangle_correct_arguments(self):
        """
        Test for correct input
        """
        rectangle_1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle_1.width, 1)
        self.assertEqual(rectangle_1.height, 2)
        self.assertEqual(rectangle_1.x, 3)
        self.assertEqual(rectangle_1.y, 4)
        self.assertEqual(rectangle_1.id, 5)

    def test_rectangle_missing_arguments(self):
        """
        Test for missing arguments
        """
        rectangle_1 = Rectangle(1, 2, 3)
        self.assertEqual(rectangle_1.width, 1)
        self.assertEqual(rectangle_1.height, 2)
        self.assertEqual(rectangle_1.x, 3)
        self.assertEqual(rectangle_1.y, 0)

    def test_rectangle_adding_arguments(self):
        """
        Test for modifying and adding arguments after initalisation
        """
        rectangle_1 = Rectangle(1, 2, 3)
        self.assertEqual(rectangle_1.width, 1)
        self.assertEqual(rectangle_1.height, 2)
        self.assertEqual(rectangle_1.x, 3)
        self.assertEqual(rectangle_1.y, 0)
        self.assertEqual(rectangle_1.id, 1)
        rectangle_1.y = 4
        rectangle_1.id = 5
        self.assertEqual(rectangle_1.y, 4)
        self.assertEqual(rectangle_1.id, 5)

    def test_rectangle_area(self):
        """
        Test for correct area calculation
        """
        rectangle_1 = Rectangle(1, 2)
        self.assertEqual(rectangle_1.area(), 2)

    def test_rectangle_display(self):
        """
        Test for correct rectangle display
        """
        rectangle_1 = Rectangle(2, 2)
        display_1 = "##\n##\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        rectangle_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), display_1)
