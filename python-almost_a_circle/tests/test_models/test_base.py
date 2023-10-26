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

    def test_to_json_string(self):
        """
        Testing for returning JSON string representation
        """
        """
        Test with an empty list
        """
        base_data_1 = []
        json_string_1 = Base.to_json_string(base_data_1)
        self.assertEqual(json_string_1, "[]")
        """
        Test for correct output of JSON string representation
        """
        base_data_2 = [{"Mina": "1"}, {"Nayeon": "2"}, {"Jihyo": "3"}]
        json_string_2 = Base.to_json_string(base_data_2)
        self.assertEqual(json_string_2
                         , '[{"Mina": "1"}, {"Nayeon": "2"}, {"Jihyo": "3"}]')
        """
        Test for correct output of JSON string representation if the input
        is 'None'
        """
        base_data_3 = None
        json_string_3 = Base.to_json_string(base_data_3)
        self.assertEqual(json_string_3, '[]')

    def test_from_json_string(self):
        """
        Testing for inputing JSON string representation
        """
        """
        Test for string input
        """
        json_string_1 = '[{"Mina": "1"}, {"Nayeon": "2"}, {"Jihyo": "3"}]'
        base_data_1 = Base.from_json_string(json_string_1)
        self.assertEqual(base_data_1
                        , [{"Mina": "1"}, {"Nayeon": "2"}, {"Jihyo": "3"}])
        """
        Test for empty string input
        """
        json_string_2 = ''
        base_data_2 = Base.from_json_string(json_string_2)
        self.assertEqual(base_data_2, [])
        """
        Test for None string input
        """
        json_string_3 = None
        base_data_3 = Base.from_json_string(json_string_3)
        self.assertEqual(base_data_3, [])
