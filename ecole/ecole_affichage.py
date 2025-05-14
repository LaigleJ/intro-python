import pandas as pd
import os
from ecole.ecole_classes import Etudiant, Professeur

def charger_donnees(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        lignes = f.readlines()

    lignes = [ligne.strip().split() for ligne in lignes if ligne.strip()]
    return lignes


def parser_donnees(lignes):
    personnes = []

    for valeurs in lignes:
        if len(valeurs) == 5:
            nom, prenom, age, filiere, niveau = valeurs
            personnes.append(Etudiant(nom, prenom, int(age), filiere, int(niveau)))
        elif len(valeurs) == 6:
            nom, prenom, age, specialite, annee_exp, annee_etude = valeurs
            personnes.append(Professeur(nom, prenom, int(age), specialite, int(annee_exp), int(annee_etude)))

    return personnes


def afficher_groupes_par_filiere(etudiants):
    from collections import defaultdict
    groupes = defaultdict(list)

    for etu in etudiants:
        groupes[etu.filiere].append(etu)

    for filiere, membres in groupes.items():
        print(f"\nFilière : {filiere}")
        for etu in membres:
            print(f"  - {etu}")  # ✅ Ici, {etu} déclenche l'appel à __repr__()

