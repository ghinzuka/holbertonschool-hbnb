from models.city import City

class CityManager:
    def __init__(self):
        self.cities = {}

    def create_city(self, city):
        if not isinstance(city, City):
            raise TypeError("Expected City instance")

        key = f"{city.id}_City"
        self.cities[key] = city.to_dict()
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
            print(f"City with ID {city.id} updated.")
        else:
            raise ValueError(f"City with ID '{city.id}' does not exist in the data store.")

    def delete_city(self, city_id):
        key = f"{city_id}_City"
        if key in self.cities:
            del self.cities[key]
            print(f"City with ID {city_id} deleted.")
        else:
            print(f"City with ID {city_id} not found. Deletion failed.")
