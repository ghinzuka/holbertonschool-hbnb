from flask import Flask, jsonify
from api.app_user import user_bp  
from api.app_amenity import amenity_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(amenity_bp, url_prefix='/amenities')

@app.route('/', methods=['GET'])
def root():
    return jsonify(message='Welcome to the combined API!',
                   links={
                       'users': '/users',
                       'amenities': '/amenities'
                   })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
