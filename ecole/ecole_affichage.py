import pandas as pd
import os
from ecole.ecole_classes import Etudiant, Professeur
from collections import defaultdict

# Fonction pour charger les données depuis un fichier
def charger_donnees(fichier):
    try:
        # Vérifier si le fichier existe
        if not os.path.exists(fichier):
            raise FileNotFoundError(f"Le fichier '{fichier}' n'existe pas.")
        
        with open(fichier, 'r', encoding='utf-8') as f:
            lignes = f.readlines()

        # Nettoyage et découpage des lignes
        lignes = [ligne.strip().split() for ligne in lignes if ligne.strip()]
        return lignes
    except FileNotFoundError as e:
        print(f"Erreur : {e}")
        return None
    except Exception as e:
        print(f"Erreur inattendue lors du chargement du fichier : {e}")
        return None


# Fonction pour parser les données et créer des objets Etudiant et Professeur
def parser_donnees(lignes):
    personnes = []
    
    try:
        for valeurs in lignes:
            if len(valeurs) == 5:  # Si c'est un étudiant
                if len(valeurs) != 5:
                    raise ValueError(f"Les données de l'étudiant {valeurs} sont mal formées.")
                nom, prenom, age, filiere, niveau = valeurs
                personnes.append(Etudiant(nom, prenom, int(age), filiere, int(niveau)))
            elif len(valeurs) == 6:  # Si c'est un professeur
                if len(valeurs) != 6:
                    raise ValueError(f"Les données du professeur {valeurs} sont mal formées.")
                nom, prenom, age, specialite, annee_exp, annee_etude = valeurs
                personnes.append(Professeur(nom, prenom, int(age), specialite, int(annee_exp), int(annee_etude)))
            else:
                print(f"Erreur de format dans les données : {valeurs}. Ce format n'est pas reconnu.")
                continue
        return personnes
    except ValueError as e:
        print(f"Erreur de validation des données : {e}")
        return []
    except Exception as e:
        print(f"Erreur inattendue lors du parsing des données : {e}")
        return []


# Fonction pour afficher les groupes par filière
def afficher_groupes_par_filiere(etudiants):
    try:
        groupes = defaultdict(list)

        for etu in etudiants:
            if not isinstance(etu, Etudiant):
                raise TypeError("Tous les éléments de la liste doivent être des objets de type Etudiant.")
            groupes[etu.filiere].append(etu)

        for filiere, membres in groupes.items():
            print(f"\nFilière : {filiere}")
            for etu in membres:
                print(f"  - {etu}")  # ✅ Ici, {etu} déclenche l'appel à __repr__()

    except TypeError as e:
        print(f"Erreur de type : {e}")
    except Exception as e:
        print(f"Erreur inattendue dans l'affichage des groupes : {e}")
