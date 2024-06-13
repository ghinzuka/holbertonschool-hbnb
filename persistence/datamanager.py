import json
from models.city import City
from models.country import Country

class DataManager:
    """
    A class to manage data persistence for various entities, such as cities and countries.

    Attributes:
        file_path (str): Path to the data file.
        countries_file_path (str, optional): Path to the countries file.
        data (dict): Dictionary to store entity data.
        countries (list): List to store country data.
    """
    
    def __init__(self, file_path, countries_file_path=None):
        """
        Initialize the DataManager with paths to data and countries files.

        Args:
            file_path (str): Path to the data file.
            countries_file_path (str, optional): Path to the countries file. Defaults to None.
        """
        self.file_path = file_path
        self.countries_file_path = countries_file_path
        self.data = {}
        self.countries = []
        self.load_data()
        self.load_countries()

    def load_data(self):
        """
        Load data from the file specified by file_path.

        If the file does not exist, it initializes an empty data dictionary and creates the file.
        """
        try:
            with open(self.file_path, 'r') as file:
                content = file.read().strip()
                if content:
                    self.data = json.loads(content)
                else:
                    self.data = {}
        except FileNotFoundError:
            self.data = {}
            self.save_data()  # Create a new file if it does not exist

    def load_countries(self):
        """
        Load country data from the file specified by countries_file_path.

        Raises:
            FileNotFoundError: If the countries file is not found.
        """
        if self.countries_file_path:
            try:
                with open(self.countries_file_path, 'r') as file:
                    self.countries = json.load(file)
            except FileNotFoundError:
                raise FileNotFoundError(f"Countries file '{self.countries_file_path}' not found.")

    def save_data(self):
        """
        Save the current state of the data dictionary to the file specified by file_path.
        """
        with open(self.file_path, 'w') as file:
            serialized_data = {str(key): value for key, value in self.data.items()}
            json.dump(serialized_data, file, indent=4)

    def create(self, entity):
        """
        Create a new entity in the data dictionary.

        Args:
            entity: An instance of an entity with an 'id' attribute and a 'to_dict' method.

        Raises:
            AttributeError: If the entity does not have an 'id' attribute.
        """
        if not hasattr(entity, 'id'):
            raise AttributeError("Entity must have an 'id' attribute.")

        key = f"{entity.id}_{type(entity).__name__}"
        self.data[key] = entity.to_dict()
        self.save_data()
        print(f"Entity {type(entity).__name__} with ID {entity.id} created.")

    def read(self, entity_id, entity_class):
        """
        Read an entity from the data dictionary by its ID and class.

        Args:
            entity_id: The ID of the entity.
            entity_class: The class of the entity.

        Returns:
            An instance of entity_class created from the stored data, or None if not found.
        """
        key = f"{entity_id}_{entity_class.__name__}"
        data = self.data.get(key)
        if data:
            print(f"Entity {entity_class.__name__} with ID {entity_id} retrieved.")
            return entity_class.from_dict(data)
        else:
            print(f"Entity {entity_class.__name__} with ID {entity_id} not found.")
            return None

    def update(self, entity):
        """
        Update an existing entity in the data dictionary.

        Args:
            entity: An instance of an entity with an 'id' attribute and a 'to_dict' method.

        Raises:
            ValueError: If the entity does not exist in the data store.
        """
        key = f"{entity.id}_{type(entity).__name__}"
        if key in self.data:
            self.data[key] = entity.to_dict()
            self.save_data()
            print(f"Entity {type(entity).__name__} with ID {entity.id} updated.")
        else:
            raise ValueError(f"Entity with key '{key}' does not exist in the data store.")

    def delete(self, entity_id, entity_class):
        """
        Delete an entity from the data dictionary by its ID and class.

        Args:
            entity_id: The ID of the entity.
            entity_class: The class of the entity.
        """
        key = f"{entity_id}_{entity_class.__name__}"
        if key in self.data:
            del self.data[key]
            self.save_data()
            print(f"Entity {entity_class.__name__} with ID {entity_id} deleted.")
        else:
            print(f"Entity {entity_class.__name__} with ID {entity_id} not found. Deletion failed.")

    def create_city(self, city):
        """
        Create a new city entity in the data dictionary.

        Args:
            city: An instance of the City class.

        Raises:
            TypeError: If the provided object is not a City instance.
            ValueError: If the city's country code is invalid.
        """
        if not isinstance(city, City):
            raise TypeError("Expected City instance")
        
        if not self.is_valid_country_code(city.country_code):
            raise ValueError(f"Invalid country_code '{city.country_code}'")

        key = f"{city.id}_City"
        self.data[key] = city.to_dict()
        self.save_data()
        print(f"City with ID {city.id} created.")

    def read_city(self, city_id):
        """
        Read a city entity from the data dictionary by its ID.

        Args:
            city_id: The ID of the city.

        Returns:
            An instance of the City class created from the stored data, or None if not found.
        """
        key = f"{city_id}_City"
        data = self.data.get(key)
        if data:
            print(f"City with ID {city_id} retrieved.")
            return City.from_dict(data)
        else:
            print(f"City with ID {city_id} not found.")
            return None

    def update_city(self, city):
        """
        Update an existing city entity in the data dictionary.

        Args:
            city: An instance of the City class.

        Raises:
            ValueError: If the city does not exist in the data store or has an invalid country code.
        """
        key = f"{city.id}_City"
        if key in self.data:
            if not self.is_valid_country_code(city.country_code):
                raise ValueError(f"Invalid country_code '{city.country_code}'")
            
            self.data[key] = city.to_dict()
            self.save_data()
            print(f"City with ID {city.id} updated.")
        else:
            raise ValueError(f"City with ID '{city.id}' does not exist in the data store.")

    def delete_city(self, city_id):
        """
        Delete a city entity from the data dictionary by its ID.

        Args:
            city_id: The ID of the city.
        """
        key = f"{city_id}_City"
        if key in self.data:
            del self.data[key]
            self.save_data()
            print(f"City with ID {city_id} deleted.")
        else:
            print(f"City with ID {city_id} not found. Deletion failed.")

    def create_country(self, country):
        """
        Create a new country entity in the data dictionary.

        Args:
            country: An instance of the Country class.

        Raises:
            TypeError: If the provided object is not a Country instance.
        """
        if not isinstance(country, Country):
            raise TypeError("Expected Country instance")
        
        key = f"{country.code}_Country"
        self.data[key] = country.to_dict()
        self.save_data()
        print(f"Country with code {country.code} created.")

    def read_country(self, country_code):
        """
        Read a country entity from the data dictionary by its code.

        Args:
            country_code: The code of the country.

        Returns:
            An instance of the Country class created from the stored data, or None if not found.
        """
        key = f"{country_code}_Country"
        data = self.data.get(key)
        if data:
            print(f"Country with code {country_code} retrieved.")
            return Country.from_dict(data)
        else:
            print(f"Country with code {country_code} not found.")
            return None

    def update_country(self, country):
        """
        Update an existing country entity in the data dictionary.

        Args:
            country: An instance of the Country class.

        Raises:
            ValueError: If the country does not exist in the data store.
        """
        key = f"{country.code}_Country"
        if key in self.data:
            self.data[key] = country.to_dict()
            self.save_data()
            print(f"Country with code {country.code} updated.")
        else:
            raise ValueError(f"Country with code '{country.code}' does not exist in the data store.")

    def delete_country(self, country_code):
        """
        Delete a country entity from the data dictionary by its code.

        Args:
            country_code: The code of the country.
        """
        key = f"{country_code}_Country"
        if key in self.data:
            del self.data[key]
            self.save_data()
            print(f"Country with code {country_code} deleted.")
        else:
            print(f"Country with code {country_code} not found. Deletion failed.")

    def is_valid_country_code(self, country_code):
        """
        Validate a country code against the loaded list of countries.

        Args:
            country_code: The code of the country.

        Returns:
            bool: True if the country code is valid, False otherwise.
        """
        return country_code in [country['code'] for country in self.countries]
