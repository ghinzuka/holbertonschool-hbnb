# persistence/place_manager.py
from models.place import Place
from models.city import City
from models.amenity import Amenities
from persistence.datamanager import DataManager
from persistence.city_manager import CityManager

class PlaceManager(DataManager, CityManager):
    def __init__(self, file_path, city_file_path):
        DataManager.__init__(self, file_path)
        CityManager.__init__(self, city_file_path)


    def create_place(self, place):
        if not isinstance(place, Place):
            raise TypeError("Expected Place instance")

        # Validate city_id
        if not self.read_city(place.city_id):
            raise ValueError(f"City with ID '{place.city_id}' does not exist")

        # Validate amenities
        for amenity_id in place.amenities:
            if not self.amenity_manager.read(amenity_id, Amenities):
                raise ValueError(f"Amenity with ID '{amenity_id}' does not exist")

        self.create(place)
        print(f"Place with ID {place.id} created.")

    def update_place(self, place):
        if not isinstance(place, Place):
            raise TypeError("Expected Place instance")

        # Validate city_id
        if not self.read_city(place.city_id):
            raise ValueError(f"City with ID '{place.city_id}' does not exist")

        # Validate amenities
        for amenity_id in place.amenities:
            if not self.amenity_manager.read(amenity_id, Amenities):
                raise ValueError(f"Amenity with ID '{amenity_id}' does not exist")

        self.update(place)
        print(f"Place with ID {place.id} updated.")

    def read_place(self, place_id):
        return self.read(place_id, Place)

    def delete_place(self, place_id):
        self.delete(place_id, Place)
        print(f"Place with ID {place_id} deleted.")

    def get_all_places(self):
        return self.get_all(Place)
