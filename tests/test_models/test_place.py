#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertEqual(self.place.city_id, '')
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertEqual(self.place.user_id, '')
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertEqual(self.place.name, '')
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertEqual(self.place.description, '')
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertEqual(self.place.number_rooms, 0)
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertEqual(self.place.max_guest, 0)
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertEqual(self.place.price_by_night, 0)
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertEqual(self.place.latitude, 0.0)
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertEqual(self.place.longitude, 0.0)
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_inheritance(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_str(self):
        string = str(self.place)
        self.assertIsInstance(string, str)

    def test_save(self):
        self.place.save()
        self.assertIsNotNone(self.place.updated_at)

    def test_to_dict(self):
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIsNotNone(place_dict['created_at'])
        self.assertIsNotNone(place_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
