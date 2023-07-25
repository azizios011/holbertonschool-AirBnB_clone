#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, '')

    def test_inheritance(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_str(self):
        string = str(self.state)
        self.assertIsInstance(string, str)

    def test_save(self):
        self.state.save()
        self.assertIsNotNone(self.state.updated_at)

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsNotNone(state_dict['created_at'])
        self.assertIsNotNone(state_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
