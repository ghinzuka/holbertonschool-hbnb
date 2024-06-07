import unittest
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

if __name__ == '__main__':
    unittest.main()
