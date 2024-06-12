from flask import Flask
from api.app_user import user_bp  # Importez le Blueprint user_bp
from api.app_amenity import amenity_bp  # Importez le Blueprint amenity_bp

app = Flask(__name__)

# Enregistrez les Blueprints pour les API utilisateur et amenity avec des préfixes de chemin
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(amenity_bp, url_prefix='/amenities')