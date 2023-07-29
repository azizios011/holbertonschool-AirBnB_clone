#!/usr/bin/python3
"""Unittest module for the amenity."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, '')

    def test_inheritance(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_str(self):
        string = str(self.amenity)
        self.assertIsInstance(string, str)

    def test_save(self):
        self.amenity.save()
        self.assertIsNotNone(self.amenity.updated_at)

    def test_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsNotNone(amenity_dict['created_at'])
        self.assertIsNotNone(amenity_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
