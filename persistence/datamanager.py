import json
from models.city import City
from models.country import Country

class DataManager:
    def __init__(self, file_path, countries_file_path):
        self.file_path = file_path
        self.countries_file_path = countries_file_path
        self.data = {}
        self.countries = []
        self.load_data()
        self.load_countries()  # Nouvelle méthode pour charger les pays

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.save_data()  # Crée un nouveau fichier si inexistant

    def load_countries(self):
        try:
            with open(self.countries_file_path, 'r') as file:
                self.countries = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Countries file '{self.countries_file_path}' not found.")

    def save_data(self):
        with open(self.file_path, 'w') as file:
            serialized_data = {str(key): value for key, value in self.data.items()}
            json.dump(serialized_data, file, indent=4)

    def create(self, entity):
        if not hasattr(entity, 'id'):
            raise AttributeError("Entity must have an 'id' attribute.")

        key = f"{entity.id}_{type(entity).__name__}"
        self.data[key] = entity.to_dict()
        self.save_data()
        print(f"Entity {type(entity).__name__} with ID {entity.id} created.")

    def read(self, entity_id, entity_class):
        key = f"{entity_id}_{entity_class.__name__}"
        data = self.data.get(key)
        if data:
            print(f"Entity {entity_class.__name__} with ID {entity_id} retrieved.")
            return entity_class.from_dict(data)
        else:
            print(f"Entity {entity_class.__name__} with ID {entity_id} not found.")
            return None

    def update(self, entity):
        key = f"{entity.id}_{type(entity).__name__}"
        if key in self.data:
            self.data[key] = entity.to_dict()
            self.save_data()
            print(f"Entity {type(entity).__name__} with ID {entity.id} updated.")
        else:
            raise ValueError(f"Entity with key '{key}' does not exist in the data store.")

    def delete(self, entity_id, entity_class):
        key = f"{entity_id}_{entity_class.__name__}"
        if key in self.data:
            del self.data[key]
            self.save_data()
            print(f"Entity {entity_class.__name__} with ID {entity_id} deleted.")
        else:
            print(f"Entity {entity_class.__name__} with ID {entity_id} not found. Deletion failed.")

    def create_city(self, city):
        if not isinstance(city, City):
            raise TypeError("Expected City instance")
        
        # Validate country_code against preloaded countries
        if not self.is_valid_country_code(city.country_code):
            raise ValueError(f"Invalid country_code '{city.country_code}'")

        key = f"{city.id}_City"
        self.data[key] = city.to_dict()
        self.save_data()
        print(f"City with ID {city.id} created.")

    def read_city(self, city_id):
        key = f"{city_id}_City"
        data = self.data.get(key)
        if data:
            print(f"City with ID {city_id} retrieved.")
            return City.from_dict(data)
        else:
            print(f"City with ID {city_id} not found.")
            return None

    def update_city(self, city):
        key = f"{city.id}_City"
        if key in self.data:
            # Validate country_code against preloaded countries
            if not self.is_valid_country_code(city.country_code):
                raise ValueError(f"Invalid country_code '{city.country_code}'")
            
            self.data[key] = city.to_dict()
            self.save_data()
            print(f"City with ID {city.id} updated.")
        else:
            raise ValueError(f"City with ID '{city.id}' does not exist in the data store.")

    def delete_city(self, city_id):
        key = f"{city_id}_City"
        if key in self.data:
            del self.data[key]
            self.save_data()
            print(f"City with ID {city_id} deleted.")
        else:
            print(f"City with ID {city_id} not found. Deletion failed.")

    def create_country(self, country):
        if not isinstance(country, Country):
            raise TypeError("Expected Country instance")
        
        key = f"{country.code}_Country"
        self.data[key] = country.to_dict()
        self.save_data()
        print(f"Country with code {country.code} created.")

    def read_country(self, country_code):
        key = f"{country_code}_Country"
        data = self.data.get(key)
        if data:
            print(f"Country with code {country_code} retrieved.")
            return Country.from_dict(data)
        else:
            print(f"Country with code {country_code} not found.")
            return None

    def update_country(self, country):
        key = f"{country.code}_Country"
        if key in self.data:
            self.data[key] = country.to_dict()
            self.save_data()
            print(f"Country with code {country.code} updated.")
        else:
            raise ValueError(f"Country with code '{country.code}' does not exist in the data store.")

    def delete_country(self, country_code):
        key = f"{country_code}_Country"
        if key in self.data:
            del self.data[key]
            self.save_data()
            print(f"Country with code {country_code} deleted.")
        else:
            print(f"Country with code {country_code} not found. Deletion failed.")

    def is_valid_country_code(self, country_code):
        # Implement your validation logic here
        # For example, check if the country_code exists in your pre-loaded data
        return country_code in [country['code'] for country in self.countries]
