# Le projet consiste à modeliser une architecture simple pour gérer les contact des utiliasteurs :

# Fonctionnalités :
- créer un contact : nom , numéro phone
- lister des contacts

# Affichage via CMD

# architecture du projet avec venv
en utilisant list dict 
models/  contient les données (ex: utilisateur)
services/ contient la logique (ex: ajouter utilisateur)
tests/ contient les tests automatiques
main.py (point d’entrée du programme)

# lancer le test
python -m unittest -v

# lancer l'app 
main.py

cd git_contact
python -m app.tests.test_contact_service

python -m unittest tests.test_contact_service -v

# créer le fichier "requirements.txt"
pip freeze > requirements.txt