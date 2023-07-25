#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.state_id, '')
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.name, '')

    def test_inheritance(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_str(self):
        string = str(self.city)
        self.assertIsInstance(string, str)

    def test_save(self):
        self.city.save()
        self.assertIsNotNone(self.city.updated_at)

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsNotNone(city_dict['created_at'])
        self.assertIsNotNone(city_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
