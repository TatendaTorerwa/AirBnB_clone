#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up necessary objects before each test"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.save()
        self.storage.new(self.model)

    def tearDown(self):
        """Clean up after each test"""
        self.storage = None
        self.model = None

    def test_all(self):
        """Test the 'all' method"""
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {'BaseModel.{}'.format(self.model.id): self.model})

    def test_new(self):
        """Test the 'new' method"""
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {'BaseModel.{}'.format(self.model.id): self.model,
                                       'BaseModel.{}'.format(new_model.id): new_model})

    def test_save(self):
        """Test the 'save' method"""
        with open(FileStorage._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertEqual(data, '{}')

        self.storage.save()

        with open(FileStorage._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertNotEqual(data, '{}')

    def test_reload(self):
        """Test the 'reload' method"""
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {'BaseModel.{}'.format(self.model.id): self.model})

if __name__ == '__main__':
    unittest.main()
