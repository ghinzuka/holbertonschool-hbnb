# Utiliser une image de base Python
FROM python:3.9-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires pour les applications Flask
COPY api/ ./api
COPY models/ ./models
COPY persistence/ ./persistence
COPY tests/ ./tests
COPY requirements.txt .

# Installer les dépendances des applications Flask
RUN pip install --no-cache-dir -r requirements.txt

# Exposer les ports pour les applications Flask
EXPOSE 5001
EXPOSE 5002

# Démarrer les applications Flask avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "api.app_user:app"]
CMD ["gunicorn", "--bind", "0.0.0.0:5002", "api.app_amenity:app"]
