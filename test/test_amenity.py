import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.amenity import Amenities
from persistence.datamanager import DataManager

class TestAmenities(unittest.TestCase):
    def test_amenities_init(self):
        # Création d'une instance d'Amenities
        amenities = Amenities(name="WiFi")

        # Vérification des attributs
        self.assertEqual(amenities.name, "WiFi")
        self.assertIsNotNone(amenities.id)  # Vérification que l'ID est défini

    def test_amenities_to_dict(self):
        # Création d'une instance d'Amenities
        amenities = Amenities(name="Pool")

        # Conversion en dictionnaire
        amenities_dict = amenities.to_dict()

        # Vérification des clés du dictionnaire
        self.assertIn("name", amenities_dict)
        self.assertIn("id", amenities_dict)

        # Vérification des valeurs du dictionnaire
        self.assertEqual(amenities_dict["name"], "Pool")
        self.assertIsNotNone(amenities_dict["id"])  # Vérification que l'ID est inclus dans le dictionnaire

    def test_amenities_from_dict(self):
        # Création d'un dictionnaire représentant Amenities
        amenities_data = {
            "name": "Gym"
        }

        # Création d'une instance d'Amenities à partir du dictionnaire
        amenities = Amenities.from_dict(amenities_data)

        # Vérification des attributs de l'instance
        self.assertEqual(amenities.name, "Gym")

if __name__ == '__main__':
    unittest.main()
