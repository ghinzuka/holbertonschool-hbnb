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
            print("Data loaded successfully from file.")
        except FileNotFoundError:
            print("Data file not found. Initializing with empty data.")
            self.save_data()

    def save_data(self):
        with open(self.file_path, 'w') as file:
            # Convertit les clés en chaînes pour assurer la sérialisation JSON
            serialized_data = {str(key): value for key, value in self.data.items()}
            json.dump(serialized_data, file, indent=4)
        print("Data saved successfully to file.")

    def create(self, entity):
        key = f"{entity.id}_{type(entity).__name__}"  # Utiliser une chaîne pour représenter la clé
        self.data[key] = entity.to_dict()
        self.save_data()
        print(f"Entity {type(entity).__name__} with ID {entity.id} created. Name: {entity.first_name} {entity.last_name}")

    def read(self, entity_id, entity_class):
        key = f"{entity_id}_{entity_class.__name__}"
        data = self.data.get(key)
        if data:
            print(f"Entity {type(entity_class).__name__} with ID {entity_id} retrieved.")
            return entity_class.from_dict(data)
        else:
            print(f"Entity {type(entity_class).__name__} with ID {entity_id} not found.")
            return None

    def update(self, entity):
        key = f"{entity.id}_{type(entity).__name__}"
        if key in self.data:
            self.data[key] = entity.to_dict()
            self.save_data()
            print(f"Entity {type(entity).__name__} with ID {entity.id} updated. Name: {entity.first_name} {entity.last_name}")
        else:
            print(f"Entity {type(entity).__name__} with ID {entity.id} not found. Update failed.")

    def delete(self, entity_id, entity_class):
        key = f"{entity_id}_{entity_class.__name__}"
        if key in self.data:
            del self.data[key]
            self.save_data()
            print(f"Entity {type(entity_class).__name__} with ID {entity_id} deleted.")
        else:
            print(f"Entity {type(entity_class).__name__} with ID {entity_id} not found. Deletion failed.")
