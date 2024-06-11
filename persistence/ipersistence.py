import json
import os

class IPersistenceManager:
    def create(self, entity):
        raise NotImplementedError

    def read(self, entity_id):
        raise NotImplementedError

    def update(self, entity_id, data):
        raise NotImplementedError

    def delete(self, entity_id):
        raise NotImplementedError
