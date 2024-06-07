import unittest
from uuid import UUID
from datetime import datetime
from amenity import Amenities

class TestAmenities(unittest.TestCase):

    def test_unique_amenities(self):
        amenities = Amenities(["piscine", "wifi", "salle de sport"])
        print("Résultat après avoir passé des noms d'aménités uniques :")
        print(amenities.get_all_amenities())
        self.assertEqual(len(amenities.get_all_amenities()), 3)

    def test_duplicate_amenities(self):
        amenities = Amenities(["piscine", "wifi", "piscine"])
        print("Résultat après avoir passé des noms d'aménités avec des duplications :")
        print(amenities.get_all_amenities())
        self.assertEqual(len(amenities.get_all_amenities()), 2)
    
    def test_non_string_arguments(self):
        with self.assertRaises(TypeError) as context:
            amenities = Amenities(["piscine", 123, True])
        self.assertEqual(
            str(context.exception),
            "Tous les noms doivent être des chaînes de caractères"
        )

    def test_get_amenities_by_name(self):
        names = ["Pool", "Gym", "WiFi"]
        amenities = Amenities(names)
        pool_amenities = Amenities.get_amenities_by_name("Pool")
        self.assertEqual(len(pool_amenities), 1)
        self.assertEqual(pool_amenities[0]['name'], "Pool")

    def test_add_duplicate_names(self):
        names = ["Pool", "Gym", "Pool"]
        amenities = Amenities(names)
        self.assertEqual(len(Amenities._amenities), 2)

    def test_add_existing_amenity_name(self):
        Amenities(["Pool", "Gym"])
        Amenities(["Pool", "WiFi"])
        self.assertEqual(len(Amenities._amenities), 3)
        existing_amenity = next((amenity for amenity in Amenities._amenities if amenity['name'] == "Pool"), None)
        self.assertIsNotNone(existing_amenity)
        self.assertEqual(existing_amenity['name'], "Pool")

if __name__ == '__main__':
    unittest.main()
