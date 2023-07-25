import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import models
import os


class FileStorageTestCase(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_file_path(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        # obj = FileStorage()
        # self.assertEqual(obj.all(), obj._FileStorage__objects)
        obj = User()
        models.storage.save()
        all_objects = models.storage.all()
        self.assertEqual(all_objects, {"User.{}".format(obj.id): obj})

    def test_new(self):
        obj = User()
        variable = models.storage._FileStorage__objects
        self.assertIn("User.{}".format(obj.id), variable)

    def test_save(self):
        obj = User()
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        obj = User()
        self.storage.save()
        self.assertEqual(os.path.exists("file.json"), True)
        os.remove("file.json")
        self.assertEqual(os.path.exists("file.json"), False)

        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertEqual(all_objects, {"User.{}".format(obj.id)


if __name__ == '__main__':
    unittest.main()
