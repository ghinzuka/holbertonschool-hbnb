from flask_testing import TestCase
from flask import url_for
from api.app import app
from persistence.datamanager import DataManager
from models.user import User

class TestUserAPI(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def setUp(self):
        # Préparer l'environnement pour chaque test
        self.data_manager = DataManager('test_data.json')
        self.data_manager.data = {}  # Réinitialiser les données pour chaque test

    def tearDown(self):
        # Nettoyer l'environnement après chaque test
        self.data_manager.data = {}

    def test_create_user(self):
        response = self.client.post(url_for('users_user_list'), json={
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'Test',
            'last_name': 'User'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('email', response.json)
        self.assertEqual(response.json['email'], 'test@example.com')
        self.assertIn('id', response.json)  # Vérifie si l'UUID de l'utilisateur est présent dans la réponse JSON

    def test_get_user(self):
        # Créer un utilisateur de test
        test_user = User(
            email='test@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )
        self.data_manager.create(test_user)

        # Récupérer l'identifiant UUID de l'utilisateur créé
        user_id = test_user.id

        # Effectuer une requête GET pour récupérer les détails de l'utilisateur
        response = self.client.get(url_for('users_single_user', user_id=user_id))
        
        # Vérifier si la réponse est réussie et si les détails de l'utilisateur sont corrects
        self.assertEqual(response.status_code, 200)
        self.assertIn('email', response.json)
        self.assertEqual(response.json['email'], 'test@example.com')
        self.assertIn('id', response.json)
        self.assertEqual(response.json['id'], str(user_id))  # Vérifie si l'identifiant UUID est présent et correct

    def test_update_user(self):
        # Créer un utilisateur de test
        test_user = User(
            email='test@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )
        self.data_manager.create(test_user)

        # Récupérer l'identifiant UUID de l'utilisateur créé
        user_id = test_user.id

        # Effectuer une requête PUT pour mettre à jour les détails de l'utilisateur
        response = self.client.put(url_for('users_single_user', user_id=user_id), json={
            'email': 'updated_test@example.com',
            'password': 'newpassword123',
            'first_name': 'Updated',
            'last_name': 'User'
        })

        # Vérifier si la mise à jour s'est faite avec succès
        self.assertEqual(response.status_code, 200)

        # Récupérer les détails mis à jour de l'utilisateur
        updated_user = self.data_manager.read(user_id, User)

        # Vérifier si les détails ont été correctement mis à jour dans la base de données
        self.assertEqual(updated_user.email, 'updated_test@example.com')
        self.assertEqual(updated_user.first_name, 'Updated')
        self.assertEqual(updated_user.last_name, 'User')

    def test_delete_user(self):
        # Créer un utilisateur de test
        test_user = User(
            email='test@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )
        self.data_manager.create(test_user)

        # Récupérer l'identifiant UUID de l'utilisateur créé
        user_id = test_user.id

        # Effectuer une requête DELETE pour supprimer l'utilisateur
        response = self.client.delete(url_for('users_single_user', user_id=user_id))

        # Vérifier si la suppression s'est faite avec succès
        self.assertEqual(response.status_code, 204)

        # Vérifier si l'utilisateur a été correctement supprimé de la base de données
        deleted_user = self.data_manager.read(user_id, User)
        self.assertIsNone(deleted_user)  # L'utilisateur ne doit pas être trouvé dans la base de données


if __name__ == '__main__':
    import unittest
    unittest.main()