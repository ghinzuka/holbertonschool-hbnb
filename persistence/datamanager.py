from persistence import IPersistenceManager

class DataManager(IPersistenceManager):
    def save(self, entity):
        # Logique pour sauvegarder l'entité dans le stockage
        pass

    def get(self, entity_id, entity_type):
        # Logique pour récupérer une entité basée sur l'ID et le type
        pass

    def update(self, entity):
        # Logique pour mettre à jour une entité dans le stockage
        pass

    def delete(self, entity_id, entity_type):
        # Logique pour supprimer une entité du stockage
        pass
