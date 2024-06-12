# Utiliser une image de base Python
FROM python:3.9-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires pour les applications Flask
COPY api/ ./api
COPY models/ ./models
COPY persistence/ ./persistence
COPY test/ ./test
COPY requirements.txt .

# Installer les dépendances des applications Flask
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port pour l'application Flask
EXPOSE 5000

# Démarrer l'application Flask combinée avec Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "api.app_combined:app"]