# Rock Paper Machine

Ce projet est une implémentation d'un jeu de Pierre-Papier-Ciseaux avec une composante d'apprentissage automatique.

## Fonctionnement du Projet

### Architecture Générale

Le projet utilise une approche hybride combinant :
- Un système de jeu classique Pierre-Papier-Ciseaux
- Un modèle d'apprentissage automatique (Random Forest) pour prédire les choix du joueur
- Un système de persistance des données pour l'historique des parties et le modèle entraîné

### Système d'Apprentissage

Le modèle utilise un Random Forest Classifier avec les caractéristiques suivantes :
- Apprentissage basé sur les 3 derniers coups du joueur
- Prédiction du prochain coup probable
- Adaptation continue au style de jeu du joueur
- Sauvegarde automatique du modèle après chaque entraînement

### Processus de Jeu

1. **Phase Initiale** :
   - Les 5 premiers coups sont joués de manière aléatoire
   - Les données sont collectées pour l'entraînement initial

2. **Phase d'Apprentissage** :
   - Après 5 coups, le modèle commence à s'entraîner
   - Utilise les 3 derniers coups comme features
   - Prédit le prochain coup probable du joueur
   - Choisit le coup qui bat la prédiction

3. **Persistance des Données** :
   - Chaque partie est enregistrée dans `historique_parties.csv`
   - Le modèle est sauvegardé dans `model.pkl`
   - Les statistiques sont calculées en temps réel

### Analyse des Données

Le projet inclut deux outils d'analyse :

1. **Notebook Jupyter** (`analyse.ipynb`) :
   - Visualisation des tendances de jeu
   - Analyse des performances du modèle
   - Étude des patterns de jeu du joueur

2. **Outil de Visualisation du Modèle** (`visualisation_modele.py`) :
   - Visualisation des 5 premiers arbres de décision
   - Graphique d'importance des features
   - Génère des images dans le dossier `visualisations/`

Pour utiliser l'outil de visualisation :
```bash
python visualisation_modele.py
```

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/Primica/Rock-paper-machine
cd Rock-paper-machine
```

2. Créez un environnement virtuel :
```bash
python -m venv .venv
```

3. Activez l'environnement virtuel :
- Sur macOS/Linux :
```bash
source .venv/bin/activate
```
- Sur Windows :
```bash
.venv\Scripts\activate
```

4. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Structure du Projet

- `main.py` : Programme principal du jeu
- `model.pkl` : Modèle d'apprentissage automatique entraîné
- `historique_parties.csv` : Historique des parties jouées
- `analyse.ipynb` : Notebook Jupyter pour l'analyse des données
- `requirements.txt` : Liste des dépendances Python

## Dépendances Principales

- numpy >= 1.21.0
- scikit-learn >= 1.0.0
- pandas >= 1.3.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- jupyter >= 1.0.0

## Utilisation

1. Assurez-vous que votre environnement virtuel est activé
2. Lancez le jeu :
```bash
python main.py
```

## Analyse des Données

Pour explorer les analyses et visualisations :
1. Lancez Jupyter Notebook :
```bash
jupyter notebook
```
2. Ouvrez `analyse.ipynb`

## Fichiers Ignorés

Les fichiers suivants sont ignorés par Git :
- `.cursor/`
- `.venv/`
- `historique_parties.csv`
- `model.pkl`

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

[À compléter selon votre licence] 