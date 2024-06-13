from flask import Flask, request
from flask_restx import Api, Resource, fields, abort
from models.city import City
from persistence.city_manager import CityManager

app = Flask(__name__)
api = Api(app, version='1.0', title='City API', description='API for managing cities')

# Initialize CityManager with the JSON file path
city_manager = CityManager('cities.json')

# Define the City model for serialization and validation
city_model = api.model('City', {
    'name': fields.String(required=True, description='The city name'),
    'country_code': fields.String(required=True, description='The country code (ISO 3166-1 alpha-2)')
})

# Endpoint to create a new city
@api.route('/cities')
class CityList(Resource):
    @api.doc('create_city')
    @api.expect(city_model)
    @api.response(201, 'City successfully created', model=city_model)
    @api.response(400, 'Invalid data')
    @api.response(409, 'City name already exists in the country')
    def post(self):
        '''Create a new city'''
        data = request.json
        try:
            new_city = City(name=data['name'], country_code=data['country_code'])
            city_manager.create_city(new_city)
            return new_city.to_dict(), 201
        except (TypeError, ValueError) as e:
            return {'message': str(e)}, 400
        except KeyError:
            abort(409, message=f"City name '{data['name']}' already exists in country '{data['country_code']}'")

# Endpoint to retrieve all cities
@api.route('/cities')
class AllCities(Resource):
    @api.doc('list_all_cities')
    @api.marshal_list_with(city_model)
    def get(self):
        '''List all cities'''
        return [city.to_dict() for city in city_manager.get_all_cities()]

# Endpoint to retrieve details of a specific city by its ID
@api.route('/cities/<string:city_id>')
@api.response(404, 'City not found')
class SingleCity(Resource):
    @api.doc('get_city')
    @api.marshal_with(city_model)
    def get(self, city_id):
        '''Fetch a city given its ID'''
        city = city_manager.read_city(city_id)
        if city:
            return city.to_dict()
        else:
            abort(404, message='City not found')

# Endpoint to update an existing city's information
@api.route('/cities/<string:city_id>')
@api.response(404, 'City not found')
class UpdateCity(Resource):
    @api.doc('update_city')
    @api.expect(city_model)
    @api.marshal_with(city_model)
    def put(self, city_id):
        '''Update a city given its ID'''
        data = request.json
        city = city_manager.read_city(city_id)
        if not city:
            abort(404, message='City not found')

        try:
            city.name = data['name']
            city.country_code = data['country_code']
            city_manager.update_city(city)
            return city.to_dict()
        except (TypeError, ValueError) as e:
            return {'message': str(e)}, 400
        except KeyError:
            abort(409, message=f"City name '{data['name']}' already exists in country '{data['country_code']}'")

# Endpoint to delete a specific city by its ID
@api.route('/cities/<string:city_id>')
@api.response(404, 'City not found')
class DeleteCity(Resource):
    @api.doc('delete_city')
    @api.response(204, 'City successfully deleted')
    def delete(self, city_id):
        '''Delete a city given its ID'''
        if city_manager.delete_city(city_id):
            return '', 204
        else:
            abort(404, message='City not found')

if __name__ == '__main__':
    app.run(debug=True)