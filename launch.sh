#!/bin/bash

echo "Vérification de l'environnement virtuel..."
if [ ! -d "venv" ]; then
    echo "Création de l'environnement virtuel..."
    python3 -m venv venv
fi

echo "Activation de l'environnement virtuel..."
source venv/bin/activate

echo "Installation des dépendances..."
pip install -r requirements.txt

echo "Démarrage de l'application..."
python3 index.py
