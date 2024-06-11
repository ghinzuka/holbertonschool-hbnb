import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.amenity import Amenities
from persistence.datamanager import DataManager

class TestAmenity(unittest.TestCase):
    def setUp(self):
        # Créer une instance de DataManager avec un chemin de fichier spécifique pour le stockage des données JSON
        self.file_path = "test_amenities.json"  # Chemin de fichier pour stocker les données JSON
        self.datamanager = DataManager(self.file_path)

    def tearDown(self):
        # Supprimer le fichier JSON après chaque test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_amenity_crud(self):
        # Création d'un équipement
        amenity = Amenities('Pool')
        self.datamanager.create(amenity)

        # Récupération de l'équipement
        retrieved_amenity = self.datamanager.read(amenity.id, Amenities)
        self.assertEqual(retrieved_amenity.name, 'Pool')

        # Mise à jour de l'équipement
        amenity.name = 'Updated Pool'
        self.datamanager.update(amenity)
        updated_amenity = self.datamanager.read(amenity.id, Amenities)
        self.assertEqual(updated_amenity.name, 'Updated Pool')

        # Suppression de l'équipement
        self.datamanager.delete(amenity.id, Amenities)
        deleted_amenity = self.datamanager.read(amenity.id, Amenities)
        self.assertIsNone(deleted_amenity)

if __name__ == '__main__':
    unittest.main()