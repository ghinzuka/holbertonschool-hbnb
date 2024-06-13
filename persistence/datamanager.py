import json
from models.city import City
from models.country import Country

class DataManager:
    def __init__(self, file_path=None, city_file_path=None, countries_file_path=None):
        self.file_path = file_path
        self.city_file_path = city_file_path
        self.countries_file_path = countries_file_path
        self.data = {}
        self.cities = {}
        self.countries = []
        self.load_data()
        self.load_cities_data()
        self.load_countries()

    def load_data(self):
        if self.file_path:
            try:
                with open(self.file_path, 'r') as file:
                    self.data = json.load(file)
            except FileNotFoundError:
                self.data = {}
                self.save_data()
        else:
            self.data = {}

    def save_data(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                json.dump(self.data, file, indent=4)

    def load_cities_data(self):
        if self.city_file_path:
            try:
                with open(self.city_file_path, 'r') as file:
                    self.cities = json.load(file)
            except FileNotFoundError:
                self.cities = {}
                self.save_cities_data()
        else:
            self.cities = {}

    def save_cities_data(self):
        if self.city_file_path:
            with open(self.city_file_path, 'w') as file:
                json.dump(self.cities, file, indent=4)

    def load_countries(self):
        if self.countries_file_path:
            try:
                with open(self.countries_file_path, 'r') as file:
                    self.countries = json.load(file)
            except FileNotFoundError:
                self.countries = []
                self.save_countries_data()
        else:
            self.countries = []

    def save_countries_data(self):
        if self.countries_file_path:
            with open(self.countries_file_path, 'w') as file:
                json.dump(self.countries, file, indent=4)

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
        
        key = f"{city.id}_City"
        self.cities[key] = city.to_dict()
        self.save_cities_data()
        print(f"City with ID {city.id} created.")

    def read_city(self, city_id):
        key = f"{city_id}_City"
        data = self.cities.get(key)
        if data:
            print(f"City with ID {city_id} retrieved.")
            return City.from_dict(data)
        else:
            print(f"City with ID {city_id} not found.")
            return None

    def update_city(self, city):
        key = f"{city.id}_City"
        if key in self.cities:
            self.cities[key] = city.to_dict()
            self.save_cities_data()
            print(f"City with ID {city.id} updated.")
        else:
            raise ValueError(f"City with ID '{city.id}' does not exist in the data store.")

    def delete_city(self, city_id):
        key = f"{city_id}_City"
        if key in self.cities:
            del self.cities[key]
            self.save_cities_data()
            print(f"City with ID {city_id} deleted.")
        else:
            print(f"City with ID {city_id} not found. Deletion failed.")

    def create_country(self, country):
        if not isinstance(country, Country):
            raise TypeError("Expected Country instance")
        
        self.countries.append(country.to_dict())
        self.save_countries_data()
        print(f"Country with code {country.code} created.")

    def read_country(self, country_code):
        for country_data in self.countries:
            if country_data.get('code') == country_code:
                print(f"Country with code {country_code} retrieved.")
                return Country.from_dict(country_data)
        print(f"Country with code {country_code} not found.")
        return None

    def update_country(self, country):
        updated = False
        for idx, country_data in enumerate(self.countries):
            if country_data.get('code') == country.code:
                self.countries[idx] = country.to_dict()
                updated = True
                break
        
        if updated:
            self.save_countries_data()
            print(f"Country with code {country.code} updated.")
        else:
            raise ValueError(f"Country with code '{country.code}' does not exist in the data store.")

    def delete_country(self, country_code):
        deleted = False
        for idx, country_data in enumerate(self.countries):
            if country_data.get('code') == country_code:
                del self.countries[idx]
                deleted = True
                break
        
        if deleted:
            self.save_countries_data()
            print(f"Country with code {country_code} deleted.")
        else:
            print(f"Country with code {country_code} not found. Deletion failed.")

    def is_valid_country_code(self, country_code):
        return any(country_data.get('code') == country_code for country_data in self.countries)
