from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from datetime import datetime
from models.user import User
from persistence.datamanager import DataManager

app = Flask(__name__)
api = Api(app, version='1.0', title='User API', description='A simple User API')

ns = api.namespace('users', description='User operations')

user_model = api.model('User', {
    'email': fields.String(required=True, description='The user email'),
    'password': fields.String(required=True, description='The user password'),
    'first_name': fields.String(required=True, description='The user first name'),
    'last_name': fields.String(required=True, description='The user last name')
})

# Initialize the DataManager
data_manager = DataManager('data.json')

def validate_email(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    def get(self):
        '''List all users'''
        users = [data_manager.read(user_id, User) for user_id in data_manager.data]
        users = [user.to_dict() for user in users if user]
        return jsonify(users)

    @ns.doc('create_user')
    @ns.expect(user_model)
    def post(self):
        '''Create a new user'''
        data = request.json
        if not validate_email(data.get('email')):
            return {'message': 'Invalid email format'}, 400

        if any(u.email == data['email'] for u in [data_manager.read(user_id, User) for user_id in data_manager.data]):
            return {'message': 'Email already exists'}, 409

        new_user = User(
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        data_manager.create(new_user)
        user_dict = new_user.to_dict()
        user_dict['id'] = new_user.id  # Ajouter l'ID à l'objet JSON
        return user_dict, 201

@ns.route('/<string:user_id>')  # Utilisation de string car les IDs sont des UUIDs
@ns.response(404, 'User not found')
class SingleUser(Resource):
    @ns.doc('get_user')
    def get(self, user_id):
        '''Fetch a user given its identifier'''
        user = data_manager.read(user_id, User)
        if user:
            return user.to_dict()
        return {'message': 'User not found'}, 404

    @ns.doc('delete_user')
    @ns.response(204, 'User deleted')
    def delete(self, user_id):
        '''Delete a user given its identifier'''
        user = data_manager.read(user_id, User)
        if user:
            data_manager.delete(user_id, User)
            return '', 204
        return {'message': 'User not found'}, 404

    @ns.expect(user_model)
    @ns.response(400, 'Invalid data')
    @ns.doc('update_user')
    def put(self, user_id):
        '''Update a user given its identifier'''
        user = data_manager.read(user_id, User)
        if not user:
            return {'message': 'User not found'}, 404

        data = request.json
        if not validate_email(data.get('email')):
            return {'message': 'Invalid email format'}, 400

        if any(u.email == data['email'] and u.id != user_id for u in [data_manager.read(uid, User) for uid in data_manager.data]):
            return {'message': 'Email already exists'}, 409

        user.email = data['email']
        user.password = data['password']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        data_manager.update(user)
        return user.to_dict()

if __name__ == '__main__':
    app.run(debug=True, port=5001)