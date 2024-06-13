from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from models.city import City
from persistence.datamanager import DataManager

app = Flask(__name__)
api = Api(app, version='1.0', title='City API', description='API for managing cities')

city_model = api.model('City', {
    'name': fields.String(required=True, description='The city name'),
    'country_code': fields.String(required=True, description='The ISO 3166-1 alpha-2 country code of the city')
})

city_data_manager = DataManager('city_data.json', countries_file_path='persistence/countries.json')

@api.route('/cities')
class CityList(Resource):
    @api.doc('list_cities')
    def get(self):
        '''List all cities'''
        cities = [city_data_manager.read_city(city_id) for city_id in city_data_manager.data]
        cities = [city.to_dict() for city in cities if city]
        return jsonify(cities), 200

    @api.doc('create_city')
    @api.expect(city_model)
    def post(self):
        '''Create a new city'''
        data = request.json
        if 'name' not in data or 'country_code' not in data:
            return {'message': 'City name and country_code are required'}, 400
        
        try:
            new_city = City(name=data['name'], country_code=data['country_code'])
            city_data_manager.create_city(new_city)
            return new_city.to_dict(), 201
        except (TypeError, ValueError) as e:
            return {'message': str(e)}, 400

@api.route('/cities/<string:city_id>')
@api.response(404, 'City not found')
class SingleCity(Resource):
    @api.doc('get_city')
    def get(self, city_id):
        '''Fetch a city given its identifier'''
        city = city_data_manager.read_city(city_id)
        if city:
            return city.to_dict()
        return {'message': 'City not found'}, 404

    @api.doc('delete_city')
    @api.response(204, 'City deleted')
    def delete(self, city_id):
        '''Delete a city given its identifier'''
        city = city_data_manager.read_city(city_id)
        if city:
            city_data_manager.delete_city(city_id)
            return '', 204
        return {'message': 'City not found'}, 404

    @api.expect(city_model)
    @api.response(400, 'Invalid data')
    @api.doc('update_city')
    def put(self, city_id):
        '''Update a city given its identifier'''
        city = city_data_manager.read_city(city_id)
        if not city:
            return {'message': 'City not found'}, 404

        data = request.json
        if 'country_code' in data:
            return {'message': 'Country code cannot be updated'}, 400
        
        if 'name' in data:
            city.name = data['name']
        
        try:
            city_data_manager.update_city(city)
            return city.to_dict()
        except (TypeError, ValueError) as e:
            return {'message': str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)
