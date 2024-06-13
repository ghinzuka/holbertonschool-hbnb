from models.base import BaseModel
import unittest
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestBaseModel(unittest.TestCase):
    def test_base_model_init(self):
        """
        Test the initialization of a BaseModel instance.
        """
        base_model = BaseModel()

        self.assertIsNotNone(base_model.id)

        self.assertIsInstance(base_model.created_at, datetime)

        self.assertIsInstance(base_model.updated_at, datetime)

    def test_base_model_save(self):
        """
        Test the save method of a BaseModel instance.
        """
        base_model = BaseModel()

        updated_at_before_save = base_model.updated_at

        base_model.save()

        updated_at_after_save = base_model.updated_at

        self.assertGreater(updated_at_after_save, updated_at_before_save)


if __name__ == '__main__':
    unittest.main()
