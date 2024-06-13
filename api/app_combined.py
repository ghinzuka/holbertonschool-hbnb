from flask import Flask, jsonify
from api.app_user import user_bp  
from api.app_amenity import amenity_bp
from api.app_country import country_bp
from api.app_city import city_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(amenity_bp, url_prefix='/amenities')
app.register_blueprint(country_bp, url_prefix='/countries')
app.register_blueprint(city_bp, url_prefix='/cities')

@app.route('/', methods=['GET'])
def root():
    return jsonify(message='Welcome to the combined API!',
                   links={
                       'users': '/users',
                       'amenities': '/amenities',
                       'countries': '/countries',
                       'cities': '/cities'
                   })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
