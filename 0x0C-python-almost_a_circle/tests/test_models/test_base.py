#!/usr/bin/python3 
"""Module: Base Module unittesting"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0


    def tearDown(self):
        pass


    def test_default_id(self):
        """ Test if the id is assigned correctly when not provided"""
        obj1 = Base()
        obj2 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_custome_id(self):
        """Test if the id is assined correctly when provided"""
        obj1 = Base(12)
        obj2 = Base(90)

        self.assertEqual(obj1.id, 12)
        self.assertEqual(obj2.id, 90)


    def test_nb_objects_increment(self):
        """Test if __nb_objects is incremented correctly"""
        obj1 = Base()
        obj2 = Base()

        self.assertEqual(obj2.id, 2)
