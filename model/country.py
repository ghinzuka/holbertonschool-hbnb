from basemodel import BaseModel

class Country(BaseModel):
    def __init__(self, name: str, cities: list = None):
        self.name = name
        self.cities = cities or []

    def add_city(self, city):
        if city in self.cities:
            raise ValueError(f"City {city.name} is already added to this country")
        self.cities.append(city)

    def get_all_cities(self):
        return [city.name for city in self.cities]