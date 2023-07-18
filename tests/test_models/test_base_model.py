#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str_method(self):
        my_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], "BaseModel")
        self.assertIsInstance(my_model_dict['id'], str)
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertEqual(my_model_dict['name'], "My_First_Model")
        self.assertEqual(my_model_dict['my_number'], 89)

    def test_from_dict_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()

        new_model = BaseModel(**my_model_dict)

        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(my_model.id, new_model.id)
        self.assertEqual(my_model.created_at, new_model.created_at)
        self.assertEqual(my_model.updated_at, new_model.updated_at)
        self.assertEqual(my_model.name, new_model.name)
        self.assertEqual(my_model.my_number, new_model.my_number)

if __name__ == "__main__":
    unittest.main()
