from ipersistence import IPersistenceManager
import json
import os

class DataManager(IPersistenceManager):
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump([], file)

    def _read_file(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def _write_file(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def create(self, entity):
        data = self._read_file()
        data.append(entity.__dict__)
        self._write_file(data)

    def read(self, entity_id):
        data = self._read_file()
        for item in data:
            if item['id'] == str(entity_id):
                return item
        return None

    def update(self, entity_id, new_data):
        data = self._read_file()
        for index, item in enumerate(data):
            if item['id'] == str(entity_id):
                data[index].update(new_data)
                self._write_file(data)
                return True
        return False

    def delete(self, entity_id):
        data = self._read_file()
        for index, item in enumerate(data):
            if item['id'] == str(entity_id):
                data.pop(index)
                self._write_file(data)
                return True
        return False
