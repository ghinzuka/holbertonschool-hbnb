import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User
from persistence.datamanager import DataManager

class TestUser(unittest.TestCase):
    def setUp(self):
        # Créer une instance de DataManager avec un chemin de fichier spécifique pour le stockage des données JSON
        self.file_path = "test_users.json"  # Chemin de fichier pour stocker les données JSON
        self.datamanager = DataManager(self.file_path)

    def tearDown(self):
        # Supprimer le fichier JSON après chaque test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_user_crud(self):
        # Création d'un utilisateur
        user = User('email@example.com', 'password', 'John', 'Doe')
        self.datamanager.create(user)

        # Récupération de l'utilisateur
        retrieved_user = self.datamanager.read(user.id, User)
        self.assertEqual(retrieved_user.email, 'email@example.com')
        self.assertEqual(retrieved_user.password, 'password')
        self.assertEqual(retrieved_user.first_name, 'John')
        self.assertEqual(retrieved_user.last_name, 'Doe')

        # Mise à jour de l'utilisateur
        user.first_name = 'Jane'
        self.datamanager.update(user)
        updated_user = self.datamanager.read(user.id, User)
        self.assertEqual(updated_user.first_name, 'Jane')

        # Suppression de l'utilisateur
        self.datamanager.delete(user.id, User)
        deleted_user = self.datamanager.read(user.id, User)
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()
