from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from datetime import datetime

app = Flask(__name__)
api = Api(app, version='1.0', title='User API', description='A simple User API')

ns = api.namespace('users', description='User operations')

user_model = api.model('User', {
    'email': fields.String(required=True, description='The user email'),
    'first_name': fields.String(required=True, description='The user first name'),
    'last_name': fields.String(required=True, description='The user last name')
})

users = []

def find_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None

def validate_email(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    def get(self):
        '''List all users'''
        return jsonify(users)

    @ns.doc('create_user')
    @ns.expect(user_model)
    def post(self):
        '''Create a new user'''
        data = request.json
        if not validate_email(data.get('email')):
            return {'message': 'Invalid email format'}, 400

        if any(u['email'] == data['email'] for u in users):
            return {'message': 'Email already exists'}, 409

        new_user = {
            'id': len(users) + 1,
            'email': data['email'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'created_at': datetime.utcnow().isoformat(),
            'updated_at': datetime.utcnow().isoformat()
        }
        users.append(new_user)
        return new_user, 201

@ns.route('/<int:user_id>')
@ns.response(404, 'User not found')
class User(Resource):
    @ns.doc('get_user')
    def get(self, user_id):
        '''Fetch a user given its identifier'''
        user = find_user(user_id)
        if user:
            return user
        return {'message': 'User not found'}, 404

    @ns.doc('delete_user')
    @ns.response(204, 'User deleted')
    def delete(self, user_id):
        '''Delete a user given its identifier'''
        global users
        user = find_user(user_id)
        if user:
            users = [u for u in users if u['id'] != user_id]
            return '', 204
        return {'message': 'User not found'}, 404

    @ns.expect(user_model)
    @ns.response(400, 'Invalid data')
    @ns.doc('update_user')
    def put(self, user_id):
        '''Update a user given its identifier'''
        user = find_user(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        data = request.json
        if not validate_email(data.get('email')):
            return {'message': 'Invalid email format'}, 400

        if any(u['email'] == data['email'] and u['id'] != user_id for u in users):
            return {'message': 'Email already exists'}, 409

        user['email'] = data['email']
        user['first_name'] = data['first_name']
        user['last_name'] = data['last_name']
        user['updated_at'] = datetime.utcnow().isoformat()
        return user

if __name__ == '__main__':
    app.run(debug=True, port=5001)