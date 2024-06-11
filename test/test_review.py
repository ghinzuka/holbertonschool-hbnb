import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.datamanager import DataManager
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        # Créer une instance de DataManager avec un stockage fictif pour les tests
        self.datamanager = DataManager(MockStorage())

    def test_review_crud(self):
        # Création d'un avis
        review = Review('Great place!', 5)
        self.datamanager.create(review)

        # Récupération de l'avis
        retrieved_review = self.datamanager.read(review.id, Review)
        self.assertEqual(retrieved_review.text, 'Great place!')
        self.assertEqual(retrieved_review.rating, 5)

        # Mise à jour de l'avis
        review.text = 'Updated review'
        self.datamanager.update(review)
        updated_review = self.datamanager.read(review.id, Review)
        self.assertEqual(updated_review.text, 'Updated review')

        # Suppression de l'avis
        self.datamanager.delete(review.id, Review)
        deleted_review = self.datamanager.read(review.id, Review)
        self.assertIsNone(deleted_review)

class MockStorage:
    def __init__(self):
        self.data = {}

    def create(self, entity):
        self.data[(entity.id, type(entity))] = entity

    def read(self, entity_id, entity_type):
        return self.data.get((entity_id, entity_type))

    def update(self, entity):
        self.data[(entity.id, type(entity))] = entity

    def delete(self, entity_id, entity_type):
        del self.data[(entity_id, entity_type)]

if __name__ == '__main__':
    unittest.main()
