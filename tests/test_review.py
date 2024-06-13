import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.review import Review
from persistence.datamanager import DataManager

class TestReview(unittest.TestCase):
	def setUp(self):
		"""
		Set up the test case.
		Create an instance of DataManager with a specific file path for storing JSON data.
		"""
		self.file_path = "test_reviews.json" 
		self.datamanager = DataManager(self.file_path)

	def tearDown(self):
		"""
		Clean up after the test case.
		Remove the JSON file after each test.
		"""
		if os.path.exists(self.file_path):
			os.remove(self.file_path)

	def test_review_crud(self):
		"""
		Test the CRUD operations for Review objects.
		"""
		review = Review('Great place!', 5)
		self.datamanager.create(review)

		retrieved_review = self.datamanager.read(review.id, Review)
		self.assertEqual(retrieved_review.text, 'Great place!')
		self.assertEqual(retrieved_review.rating, 5)

		review.text = 'Updated review'
		self.datamanager.update(review)
		updated_review = self.datamanager.read(review.id, Review)
		self.assertEqual(updated_review.text, 'Updated review')

		self.datamanager.delete(review.id, Review)
		deleted_review = self.datamanager.read(review.id, Review)
		self.assertIsNone(deleted_review)

if __name__ == '__main__':
	unittest.main()
