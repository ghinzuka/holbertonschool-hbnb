import unittest
from datetime import datetime
from uuid import UUID, uuid4
from review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        # Create a mock list of places with their creator IDs
        self.places_list = [
            {'place_id': uuid4(), 'creator_id': uuid4()},
            {'place_id': uuid4(), 'creator_id': uuid4()},
            {'place_id': uuid4(), 'creator_id': uuid4()}
        ]

    def test_review_creation_non_creator(self):
        # Test review creation where user has created the associated place
        user_id = uuid4()
        place_creator_id = self.places_list[0]['creator_id']
        place_id = self.places_list[0]['place_id']
        review_text = "Great place!"
        review_rating = 5

        print("User ID:", user_id)
        print("Place Creator ID:", place_creator_id)
        print("Place ID:", place_id)

        # Assert that creating a review with a user who created the place raises PermissionError
        with self.assertRaises(PermissionError):
            review = Review(user_id, place_id, review_text, review_rating, self.places_list)

    def test_review_creation_creator(self):
        # Test review creation where user has not created the associated place
        user_id = uuid4()
        place_id = self.places_list[0]['place_id']
        review_text = "Great place!"
        review_rating = 5

        # Assert that creating a review with a user who hasn't created the place does not raise PermissionError
        try:
            review = Review(user_id, place_id, review_text, review_rating, self.places_list)
        except PermissionError:
            self.fail("Review creation failed unexpectedly")

        # Check if review attributes are set correctly
        self.assertEqual(review.user_id, user_id)
        self.assertEqual(review.place_id, place_id)
        self.assertEqual(review.text, review_text)
        self.assertEqual(review.rating, review_rating)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
