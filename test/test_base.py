import unittest
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.base import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_base_model_init(self):
        # Création d'une instance de BaseModel
        base_model = BaseModel()
        
        # Vérification des attributs initialisés
        self.assertIsNotNone(base_model.id)  # Vérifie si l'id n'est pas None
        self.assertIsInstance(base_model.created_at, datetime)  # Vérifie si created_at est une instance de datetime
        self.assertIsInstance(base_model.updated_at, datetime)  # Vérifie si updated_at est une instance de datetime
        

    def test_base_model_save(self):
        # Création d'une instance de BaseModel
        base_model = BaseModel()
        
        # Stockage de la valeur de updated_at avant l'appel de save()
        updated_at_before_save = base_model.updated_at
        
        # Appel de la méthode save() pour mettre à jour updated_at
        base_model.save()
        
        # Stockage de la valeur de updated_at après l'appel de save()
        updated_at_after_save = base_model.updated_at
        
        # Vérification que updated_at a été mise à jour après l'appel de save()
        self.assertGreater(updated_at_after_save, updated_at_before_save)

if __name__ == '__main__':
    unittest.main()