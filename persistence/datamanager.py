import json

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            # Crée un nouveau fichier si le fichier n'existe pas encore
            self.save_data()

    def save_data(self):
        with open(self.file_path, 'w') as file:
            # Convertit les clés en chaînes pour assurer la sérialisation JSON
            serialized_data = {str(key): value for key, value in self.data.items()}
            json.dump(serialized_data, file, indent=4)

    def create(self, entity):
        key = f"{entity.id}_{type(entity).__name__}"  # Utiliser une chaîne pour représenter la clé
        self.data[key] = entity.to_dict()
        self.save_data()

    def read(self, entity_id, entity_class):
        key = f"{entity_id}_{entity_class.__name__}"
        data = self.data.get(key)
        if data:
            return entity_class.from_dict(data)
        return None

    def update(self, entity):
        key = f"{entity.id}_{type(entity).__name__}"
        if key in self.data:
            self.data[key] = entity.to_dict()
            self.save_data()
        else:
            raise ValueError(f"Entity with key '{key}' does not exist in the data store.")

    def delete(self, entity_id, entity_class):
        key = f"{entity_id}_{entity_class.__name__}"
        if key in self.data:
            del self.data[key]
            self.save_data()
        else:
            raise ValueError(f"Entity with key '{key}' does not exist in the data store.")
