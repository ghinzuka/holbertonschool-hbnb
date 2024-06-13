from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from models.country import Country
from persistence.datamanager import DataManager

app = Flask(__name__)
api = Api(app, version='1.0', title='Country API', description='API for managing countries')

country_model = api.model('Country', {
    'code': fields.String(required=True, description='The country code (ISO 3166-1 alpha-2)'),
    'name': fields.String(required=True, description='The country name')
})

country_data_manager = DataManager('country_data.json')

@api.route('/countries')
class CountryList(Resource):
    @api.doc('list_countries')
    def get(self):
        '''List all countries'''
        countries = [country_data_manager.read_country(country['code']) for country in country_data_manager.countries]
        countries = [country.to_dict() for country in countries if country]
        return jsonify(countries)

    @api.doc('create_country')
    @api.expect(country_model)
    def post(self):
        '''Create a new country'''
        data = request.json
        if 'code' not in data or 'name' not in data:
            return {'message': 'Country code and name are required'}, 400
        
        try:
            new_country = Country(code=data['code'], name=data['name'])
            country_data_manager.create_country(new_country)
            return new_country.to_dict(), 201
        except (TypeError, ValueError) as e:
            return {'message': str(e)}, 400

@api.route('/countries/<string:country_code>')
@api.response(404, 'Country not found')
class SingleCountry(Resource):
    @api.doc('get_country')
    def get(self, country_code):
        '''Fetch a country given its code'''
        country = country_data_manager.read_country(country_code)
        if country:
            return country.to_dict()
        return {'message': 'Country not found'}, 404

    @api.doc('delete_country')
    @api.response(204, 'Country deleted')
    def delete(self, country_code):
        '''Delete a country given its code'''
        country = country_data_manager.read_country(country_code)
        if country:
            country_data_manager.delete_country(country_code)
            return '', 204
        return {'message': 'Country not found'}, 404

    @api.expect(country_model)
    @api.response(400, 'Invalid data')
    @api.doc('update_country')
    def put(self, country_code):
        '''Update a country given its code'''
        country = country_data_manager.read_country(country_code)
        if not country:
            return {'message': 'Country not found'}, 404

        data = request.json
        if 'code' in data:
            return {'message': 'Country code cannot be updated'}, 400
        
        if 'name' in data:
            country.name = data['name']
        
        try:
            country_data_manager.update_country(country)
            return country.to_dict()
        except (TypeError, ValueError) as e:
            return {'message': str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)
