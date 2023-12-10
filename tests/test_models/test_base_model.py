#!/usr/bin/python3
"""
This is the module for BaseModel unittest.
"""
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage



class TestBasemodel(unittest.TestCase):
    """
    Unittest for the BaseModel.
    """

    def setUp(self):
        """
        Setup for temporary file path.
        """
        try:
            os.rename("file.json", "temp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down for temporary file path.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("temp.json", "file.json")
        except FileNotFoundError:
            pass
    def test_init(self):
        """
        The test for the init.
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        The test for the save method.
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at

        current_updated_at = my_model.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        The test for the to_dict method.
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.created_at.isoformat())


    def test_str(self):
        """
        The test for the string representation.
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
=======
"""Test cases for base_model.py"""

import unittest
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base = BaseModel()

    def tearDown(self):
        del self.base

    def test_init(self):
        self.assertIsNotNone(self.base.id)
        self.assertIsNotNone(self.base.created_at)
        self.assertIsNotNone(self.base.updated_at)
        self.assertEqual(self.base._class, BaseModel)
        self.assertIn(self.base, storage.all())

    def test_str(self):
        expected = "[{}] ({}) {}".format(self.base.class.__name, self.base.id, self.base.__dict_)
        self.assertEqual(str(self.base), expected)

    def test_save(self):
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(self.base.updated_at, old_updated_at)
        self.assertIn(self.base, storage.all())

    def test_to_dict(self):
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["class"], self.base._class.__name_)
        self.assertEqual(base_dict["id"], self.base.id)
        self.assertEqual(base_dict["created_at"], self.base.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"], self.base.updated_at.isoformat())

    def test_init_kwargs(self):
        kwargs = {
            "_class": "Test",
            "id": "1234",
            "created_at": "2023-12-09T18:06:20.000000",
            "updated_at": "2023-12-09T18:06:20.000000",
            "name": "Alice"
        }
        base = BaseModel(**kwargs)
        self.assertEqual(base.id, kwargs["id"])
        self.assertEqual(base.created_at, datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base.updated_at, datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base.name, kwargs["name"])
        self.assertEqual(base._class, BaseModel)
        self.assertIn(base, storage.all())

    def test_init_empty_kwargs(self):
        base = BaseModel(**{})
        self.assertIsNotNone(base.id)
        self.assertIsNotNone(base.created_at)
        self.assertIsNotNone(base.updated_at)
        self.assertEqual(base._class, BaseModel)
        self.assertIn(base, storage.all())

    def test_init_invalid_kwargs(self):
        kwargs = {
            "id": 1234,
            "created_at": 2023,
            "updated_at": "invalid"
        }
        base = BaseModel(**kwargs)
        self.assertIsNotNone(base.id)
        self.assertIsNotNone(base.created_at)
        self.assertIsNotNone(base.updated_at)
        self.assertEqual(base._class, BaseModel)
        self.assertIn(base, storage.all())

if _name_ == "_main_":
    unittest.main()
