import numpy as np
from sklearn.ensemble import RandomForestClassifier
import random
import pandas as pd
import os
from datetime import datetime
import pickle

class PierrePapierCiseaux:
    def __init__(self):
        self.choix = ['pierre', 'papier', 'ciseaux']
        self.historique_joueur = []
        self.historique_ia = []
        self.modele = RandomForestClassifier(n_estimators=100)
        self.entraine = False
        self.fichier_historique = 'historique_parties.csv'
        self.fichier_modele = 'model.pkl'
        self.charger_historique()
        self.charger_modele()
        
    def charger_historique(self):
        if os.path.exists(self.fichier_historique):
            df = pd.read_csv(self.fichier_historique)
            self.historique_joueur = df['choix_joueur'].tolist()
            self.historique_ia = df['choix_ia'].tolist()
            if len(self.historique_joueur) >= 5:
                self.entrainer_modele()
    
    def charger_modele(self):
        if os.path.exists(self.fichier_modele):
            try:
                with open(self.fichier_modele, 'rb') as f:
                    self.modele = pickle.load(f)
                self.entraine = True
                print("Modèle précédent chargé avec succès!")
            except Exception as e:
                print(f"Erreur lors du chargement du modèle: {e}")
                self.modele = RandomForestClassifier(n_estimators=100)
    
    def sauvegarder_partie(self, choix_joueur, choix_ia, resultat):
        nouvelle_partie = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'choix_joueur': choix_joueur,
            'choix_ia': choix_ia,
            'resultat': resultat
        }
        
        if os.path.exists(self.fichier_historique):
            df = pd.read_csv(self.fichier_historique)
            df = pd.concat([df, pd.DataFrame([nouvelle_partie])], ignore_index=True)
        else:
            df = pd.DataFrame([nouvelle_partie])
        
        df.to_csv(self.fichier_historique, index=False)
    
    def jouer_tour(self, choix_joueur):
        if choix_joueur not in self.choix:
            return "Choix invalide. Veuillez choisir 'pierre', 'papier' ou 'ciseaux'."
        
        self.historique_joueur.append(choix_joueur)
        
        # Si nous avons assez de données, entraîner le modèle
        if len(self.historique_joueur) >= 5:
            self.entrainer_modele()
            choix_ia = self.predire_choix()
        else:
            # Au début, jouer aléatoirement
            choix_ia = random.choice(self.choix)
            
        self.historique_ia.append(choix_ia)
        
        resultat = self.determiner_gagnant(choix_joueur, choix_ia)
        self.sauvegarder_partie(choix_joueur, choix_ia, resultat)
        return f"IA a choisi: {choix_ia}\n{resultat}"
    
    def entrainer_modele(self):
        if len(self.historique_joueur) < 5:
            return
        
        # Préparer les données d'entraînement
        X = []
        y = []
        
        for i in range(len(self.historique_joueur) - 1):
            # Utiliser les 3 derniers coups comme features
            if i >= 2:
                features = [
                    self.choix.index(self.historique_joueur[i-2]),
                    self.choix.index(self.historique_joueur[i-1]),
                    self.choix.index(self.historique_joueur[i])
                ]
                X.append(features)
                y.append(self.choix.index(self.historique_joueur[i+1]))
        
        if len(X) > 0:
            X = np.array(X)
            y = np.array(y)
            self.modele.fit(X, y)
            self.entraine = True
            self.sauvegarder_modele()
    
    def predire_choix(self):
        if not self.entraine:
            return random.choice(self.choix)
        
        # Utiliser les 3 derniers coups pour prédire le prochain
        derniers_coups = [
            self.choix.index(self.historique_joueur[-3]),
            self.choix.index(self.historique_joueur[-2]),
            self.choix.index(self.historique_joueur[-1])
        ]
        
        prediction = self.modele.predict([derniers_coups])[0]
        # Choisir le coup qui bat la prédiction
        return self.choix[(prediction + 1) % 3]
    
    def determiner_gagnant(self, choix_joueur, choix_ia):
        if choix_joueur == choix_ia:
            return "Égalité!"
        
        gagnant = {
            'pierre': 'ciseaux',
            'papier': 'pierre',
            'ciseaux': 'papier'
        }
        
        if gagnant[choix_joueur] == choix_ia:
            return "Vous avez gagné!"
        return "L'IA a gagné!"
    
    def afficher_statistiques(self):
        if not os.path.exists(self.fichier_historique):
            return "Aucune partie n'a été jouée."
        
        df = pd.read_csv(self.fichier_historique)
        total_parties = len(df)
        victoires_joueur = len(df[df['resultat'] == "Vous avez gagné!"])
        victoires_ia = len(df[df['resultat'] == "L'IA a gagné!"])
        egalites = len(df[df['resultat'] == "Égalité!"])
        
        return f"""
Statistiques des parties:
Total des parties: {total_parties}
Vos victoires: {victoires_joueur} ({victoires_joueur/total_parties*100:.1f}%)
Victoires de l'IA: {victoires_ia} ({victoires_ia/total_parties*100:.1f}%)
Égalités: {egalites} ({egalites/total_parties*100:.1f}%)
"""
    
    def sauvegarder_modele(self):
        try:
            with open(self.fichier_modele, 'wb') as f:
                pickle.dump(self.modele, f)
            print("Modèle sauvegardé avec succès!")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du modèle: {e}")

def main():
    jeu = PierrePapierCiseaux()
    print("Bienvenue au jeu Pierre-Papier-Ciseaux!")
    print("Entrez 'q' pour quitter")
    print("Entrez 's' pour voir les statistiques")
    
    while True:
        choix = input("\nVotre choix (pierre/papier/ciseaux): ").lower()
        if choix == 'q':
            break
        elif choix == 's':
            print(jeu.afficher_statistiques())
            continue
            
        resultat = jeu.jouer_tour(choix)
        print(resultat)

if __name__ == "__main__":
    main()
