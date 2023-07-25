#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertEqual(self.review.place_id, '')
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertEqual(self.review.user_id, '')
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.text, '')

    def test_inheritance(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_str(self):
        string = str(self.review)
        self.assertIsInstance(string, str)

    def test_save(self):
        self.review.save()
        self.assertIsNotNone(self.review.updated_at)

    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsNotNone(review_dict['created_at'])
        self.assertIsNotNone(review_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
