#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertEqual(self.user.email, '')
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertEqual(self.user.password, '')
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertEqual(self.user.first_name, '')
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.last_name, '')

    def test_inheritance(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_str(self):
        string = str(self.user)
        self.assertIsInstance(string, str)

    def test_save(self):
        self.user.save()
        self.assertIsNotNone(self.user.updated_at)

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsNotNone(user_dict['created_at'])
        self.assertIsNotNone(user_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
