import unittest
from datetime import datetime
from user import User
from place import Place
from review import Review

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("test@example.com", "password123", "John", "Doe")

    def test_user_creation(self):
        self.assertEqual(self.user.email, "test22252@example.com")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertTrue(self.user.user_id)
        self.assertTrue(isinstance(self.user.created_at, datetime))
        self.assertTrue(isinstance(self.user.updated_at, datetime))

    def test_unique_email(self):
        with self.assertRaises(ValueError):
            duplicate_user = User("tes54654798t@example.com", "password123", "Jane", "Doe")

    def test_add_and_remove_place(self):
        place = Place("Place 1", "Description", "Address")
        self.user.add_place(place)
        self.assertIn(place, self.user.places)

        self.user.remove_place(place)
        self.assertNotIn(place, self.user.places)

    def test_add_and_remove_review(self):
        review = Review(self.user.user_id, "Review 1", 5)
        self.user.add_review(review)
        self.assertIn(review, self.user.reviews)

        self.user.remove_review(review)
        self.assertNotIn(review, self.user.reviews)

    def test_update_user_info(self):
        self.user.update(first_name="Jane", last_name="Smith")
        self.assertEqual(self.user.first_name, "Jane")
        self.assertEqual(self.user.last_name, "Smith")

    def test_update_email(self):
        new_email = "new_emai514148l@example.com"
        self.user.update(email=new_email)
        self.assertEqual(self.user.email, new_email)

    def test_unique_updated_email(self):
        new_user = User("new_e16719mail@example.com", "password123", "Jane", "Smith")
        with self.assertRaises(ValueError):
            self.user.update(email=new_user.email)

    def test_get_reviews_ids(self):
        review1 = Review(self.user.user_id, "Review 1", 5)
        review2 = Review(self.user.user_id, "Review 2", 4)
        self.user.add_review(review1)
        self.user.add_review(review2)

        review_ids = self.user.get_reviews_ids()
        self.assertEqual(len(review_ids), 2)
        self.assertIn(review1.review_id, review_ids)
        self.assertIn(review2.review_id, review_ids)

    def test_remove_user(self):
        User.remove_user(self.user)
        self.assertNotIn(self.user.email, User._registered_emails)

if __name__ == '__main__':
    unittest.main()
