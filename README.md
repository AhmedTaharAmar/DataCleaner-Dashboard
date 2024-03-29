# data-cleaner

Collecter des données de qualité, constituer sa BDD analytique et réaliser le tableau de bord de l’application pour son client.

## Contexte du projet
On vous a confié la tâche de réaliser un proof of concept (PoC) dans le cadre d’un projet de dashboard d’aide à la décision pour un client exigeant. Vous avez accès à un fichier de données brutes, matérialisant un export depuis leurs bases de données opérationnelles.
Ce fichier CSV alimentera votre base analytique et tient lieu de situation initiale. Les CSV des mois suivants vous seront régulièrement transmis.

Avec le PoC du futur dashboard que vous réaliserez, le client doit pouvoir lancer un ETL (Extract Transform Load) dédié pour collecter des données de qualité. Celles ci pourront être illustrées sous forme de graphiques.

## Installation :

- Installer un environnement virtuel : `py -m venv .env`
- Lancer l'environnement virtuel : `.env\Scripts\activate.bat`
- Installer les différents packages (Django, ...) : `pip install -r requirements.txt`
- Effectuer les premières migrations : `cd src` puis `py manage.py migrate`

## Lancer le serveur Django :

- Vérifier que l'environnement virtuel est lancé et que vous êtes bien dans le dossier 'src' : `py manage.py runserver`
