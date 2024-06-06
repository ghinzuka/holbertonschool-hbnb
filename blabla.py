import re

class AddressValidator:
    def __init__(self, address):
        self.address = address

    def validate(self):
        if not isinstance(self.address, str) or not self.address:
            raise TypeError("Address must be a non-empty string")
        
        address_pattern = re.compile(
            r'^\d+\s[A-Za-z0-9\s]+,\s*[A-Za-z\s]+,\s*[A-Za-z\s]+,\s*[A-Za-z]{2}\s*\d{5}$'
        )
        
        if not address_pattern.match(self.address):
            raise ValueError("Address must follow the format '1234 Main St, City, State, 12345'")
        
        return True

# Exemple d'utilisation :
address = "1234 Main St, City, State, 12345"
validator = AddressValidator(address)
try:
    validator.validate()
    print("L'adresse est valide.")
except (TypeError, ValueError) as e:
    print("Erreur de validation:", e)
