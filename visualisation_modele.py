import pickle
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import numpy as np
import os

def visualiser_modele():
    # Vérifier si le modèle existe
    if not os.path.exists('model.pkl'):
        print("Erreur: Le fichier model.pkl n'existe pas.")
        return

    # Charger le modèle
    try:
        with open('model.pkl', 'rb') as f:
            modele = pickle.load(f)
    except Exception as e:
        print(f"Erreur lors du chargement du modèle: {e}")
        return

    # Créer un dossier pour les visualisations
    if not os.path.exists('visualisations'):
        os.makedirs('visualisations')

    # Visualiser les 5 premiers arbres de la forêt
    for i in range(min(5, len(modele.estimators_))):
        plt.figure(figsize=(20, 10))
        plot_tree(modele.estimators_[i], 
                 feature_names=['Coup-3', 'Coup-2', 'Coup-1'],
                 class_names=['Pierre', 'Papier', 'Ciseaux'],
                 filled=True,
                 rounded=True)
        plt.title(f'Arbre de décision {i+1}')
        plt.savefig(f'visualisations/arbre_{i+1}.png')
        plt.close()

    # Créer un résumé des features importantes
    importances = modele.feature_importances_
    features = ['Coup-3', 'Coup-2', 'Coup-1']
    
    plt.figure(figsize=(10, 6))
    plt.bar(features, importances)
    plt.title('Importance des features dans le modèle')
    plt.ylabel('Importance')
    plt.savefig('visualisations/importance_features.png')
    plt.close()

    print("Visualisations créées dans le dossier 'visualisations'")
    print("Vous pouvez trouver :")
    print("- Les 5 premiers arbres de décision (arbre_1.png à arbre_5.png)")
    print("- Un graphique montrant l'importance des features (importance_features.png)")

if __name__ == "__main__":
    visualiser_modele() 