from base import BaseModel

class Amenities:
    def __init__(self, names: str):
        super().__init__()
        self.names = names 

    @property
    def names(self):
        return self.__names

    @names.setter
    def names(self, value):
        print("Checking names:", value)  # Ajouter cette ligne pour voir les noms vérifiés
        if not all(isinstance(name, str) for name in value):
            raise TypeError("Tous les noms doivent être des chaînes de caractères")
        self.__names = list(set(value))  # Convertir en ensemble pour éliminer les doublons, puis reconvertir en liste
