#!/usr/bin/python3

import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    def test_id_assignment(self):
        instance1 = Base()
        instance2 = Base()

        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)

    def test_custom_id(self):
        instance = Base(id=45)
        self.assertEqual(instance.id, 45)

if __name__ == '__main__':
    unittest.main()
