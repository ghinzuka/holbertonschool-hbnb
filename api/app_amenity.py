from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from models.amenity import Amenities
from persistence.datamanager import DataManager

app = Flask(__name__)
api = Api(app, version='1.0', title='Amenity API', description='A simple Amenity API')

ns = api.namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='The amenity name')
})

# Initialize the DataManager
amenity_data_manager = DataManager('amenity_data.json')

@ns.route('/')
class AmenityList(Resource):
    @ns.doc('list_amenities')
    def get(self):
        '''List all amenities'''
        amenities = [amenity_data_manager.read(amenity_id, Amenities) for amenity_id in amenity_data_manager.data]
        amenities = [amenity.to_dict() for amenity in amenities if amenity]
        return jsonify(amenities)

    @ns.doc('create_amenity')
    @ns.expect(amenity_model)
    def post(self):
        '''Create a new amenity'''
        data = request.json
        if 'name' not in data or not data['name'].strip():
            return {'message': 'Amenity name is required'}, 400

        if any(a.name == data['name'] for a in [amenity_data_manager.read(amenity_id, Amenities) for amenity_id in amenity_data_manager.data if amenity_data_manager.read(amenity_id, Amenities) is not None]):
            return {'message': 'Amenity already exists'}, 409

        new_amenity = Amenities(name=data['name'])
        amenity_data_manager.create(new_amenity)
        return new_amenity.to_dict(), 201

@ns.route('/<string:amenity_id>')
@ns.response(404, 'Amenity not found')
class SingleAmenity(Resource):
    @ns.doc('get_amenity')
    def get(self, amenity_id):
        '''Fetch an amenity given its identifier'''
        amenity = amenity_data_manager.read(amenity_id, Amenities)
        if amenity:
            return amenity.to_dict()
        return {'message': 'Amenity not found'}, 404

    @ns.doc('delete_amenity')
    @ns.response(204, 'Amenity deleted')
    def delete(self, amenity_id):
        '''Delete an amenity given its identifier'''
        amenity = amenity_data_manager.read(amenity_id, Amenities)
        if amenity:
            amenity_data_manager.delete(amenity_id, Amenities)
            return '', 204
        return {'message': 'Amenity not found'}, 404

    @ns.expect(amenity_model)
    @ns.response(400, 'Invalid data')
    @ns.doc('update_amenity')
    def put(self, amenity_id):
        '''Update an amenity given its identifier'''
        amenity = amenity_data_manager.read(amenity_id, Amenities)
        if not amenity:
            return {'message': 'Amenity not found'}, 404

        data = request.json
        if 'name' not in data or not data['name'].strip():
            return {'message': 'Amenity name is required'}, 400

        if any(a and a.name == data['name'] and a.id != amenity_id for a in [amenity_data_manager.read(amenity_id, Amenities) for amenity_id in amenity_data_manager.data]):
            return {'message': 'Amenity name already exists'}, 409

        amenity.name = data['name']
        amenity_data_manager.update(amenity)
        return amenity.to_dict()

if __name__ == '__main__':
    app.run(debug=True, port=5002)