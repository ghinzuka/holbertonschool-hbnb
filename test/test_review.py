import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.review import Review
from persistence.datamanager import DataManager

class TestReview(unittest.TestCase):
    def setUp(self):
        # Créer une instance de DataManager avec un chemin de fichier spécifique pour le stockage des données JSON
        self.file_path = "test_reviews.json"  # Chemin de fichier pour stocker les données JSON
        self.datamanager = DataManager(self.file_path)

    def tearDown(self):
        # Supprimer le fichier JSON après chaque test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_review_crud(self):
        # Création d'une critique
        review = Review('Great place!', 5)
        self.datamanager.create(review)

        # Récupération de la critique
        retrieved_review = self.datamanager.read(review.id, Review)
        self.assertEqual(retrieved_review.text, 'Great place!')
        self.assertEqual(retrieved_review.rating, 5)

        # Mise à jour de la critique
        review.text = 'Updated review'
        self.datamanager.update(review)
        updated_review = self.datamanager.read(review.id, Review)
        self.assertEqual(updated_review.text, 'Updated review')

        # Suppression de la critique
        self.datamanager.delete(review.id, Review)
        deleted_review = self.datamanager.read(review.id, Review)
        self.assertIsNone(deleted_review)

if __name__ == '__main__':
    unittest.main()
