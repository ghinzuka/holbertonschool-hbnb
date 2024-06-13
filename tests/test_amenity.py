import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from persistence.datamanager import DataManager
from models.amenity import Amenities

class TestAmenities(unittest.TestCase):
    def setUp(self):
        # Créer une instance de DataManager avec un chemin de fichier spécifique pour le stockage des données JSON
        self.file_path = "test_amenities.json"  # Chemin de fichier pour stocker les données JSON
        self.datamanager = DataManager(self.file_path)

    def tearDown(self):
        # Supprimer le fichier JSON après chaque test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_amenities_crud(self):
        # Création d'une commodité
        amenities = Amenities(name='Swimming Pool')
        self.datamanager.create(amenities)

        # Récupération de la commodité
        retrieved_amenities = self.datamanager.read(amenities.id, Amenities)
        self.assertEqual(retrieved_amenities.name, 'Swimming Pool')
        self.assertIsNotNone(retrieved_amenities.id)  # Vérifier que l'ID a été correctement défini

        # Mise à jour de la commodité
        amenities.name = 'Gym'
        self.datamanager.update(amenities)
        updated_amenities = self.datamanager.read(amenities.id, Amenities)
        self.assertEqual(updated_amenities.name, 'Gym')

        # Suppression de la commodité
        self.datamanager.delete(amenities.id, Amenities)
        deleted_amenities = self.datamanager.read(amenities.id, Amenities)
        self.assertIsNone(deleted_amenities)

if __name__ == '__main__':
    unittest.main()
