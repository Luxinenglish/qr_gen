# Générateur de QR Code

Ce projet est un **générateur de QR Code** en Python avec une interface HTML simple. Il permet de créer des QR Codes à partir de textes ou d'URLs.

## Fonctionnalités

- **Générer des QR Codes** : Créez des QR Codes à partir de texte ou d'URLs.
- **Interface HTML** : Une interface web simple pour faciliter l'utilisation du générateur.
- **Multi-plateforme** : Fonctionne sur Linux, Mac et Windows.

## Prérequis

Avant d'exécuter le projet, assurez-vous que Python 3.x est installé sur votre machine. Vous aurez également besoin des bibliothèques suivantes :

- `qrcode` : pour la génération des QR Codes.
- `flask` : pour héberger l'interface HTML via un serveur web local.

Installez les dépendances avec la commande suivante :

<pre><code>pip install -r requirements.txt</code></pre>

## Installation

### Cloner le repository

Clonez ce repository ou téléchargez-le sur votre machine locale :

<pre><code>git clone https://github.com/Luxinenglish/qrcode-generator.git
cd qrcode-generator</code></pre>

### Lancer le projet

#### Pour Linux/Mac

Exécutez le script `launch.sh` pour démarrer le projet :

<pre><code>./launch.sh</code></pre>

#### Pour Windows

Exécutez le fichier `launch.bat` pour démarrer le projet :

<pre><code>launch.bat</code></pre>

## Utilisation

Une fois le serveur démarré, ouvrez votre navigateur web et accédez à l'URL suivante :

<pre><code>http://127.0.0.1:5000</code></pre>

Dans l'interface, vous pourrez entrer du texte ou une URL pour générer un QR Code.

## Exemple d'utilisation

### Générer un QR Code

1. Entrez un texte ou une URL dans l'interface.
2. Cliquez sur "Générer" pour afficher le QR Code.
3. Vous pouvez télécharger le QR Code généré.

## Code du projet

Voici un aperçu du code utilisé pour générer et gérer les QR Codes.

### Fonctions principales

- `generate_qr_code(data)` : Génère un QR Code à partir de données fournies.
- `save_qr_code(qr_code, filename)` : Sauvegarde un QR Code généré dans un fichier image.
- `load_qr_code(filename)` : Charge un QR Code à partir d'un fichier.

**projet sous license MIT**
