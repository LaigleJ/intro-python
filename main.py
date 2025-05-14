from ecole.ecole_affichage import charger_donnees, parser_donnees, afficher_groupes_par_filiere
from ecole.ecole_calcul import meme_cours, peut_enseigner
from ecole.ecole_classes import Etudiant, Professeur

# Charger les données depuis le fichier
df = charger_donnees("data/personnes.txt")
personnes = parser_donnees(df)

# Séparer étudiants et professeurs
etudiants = [p for p in personnes if isinstance(p, Etudiant)]
professeurs = [p for p in personnes if isinstance(p, Professeur)]

# Afficher les groupes
afficher_groupes_par_filiere(etudiants)

# Exemple de comparaison
if len(etudiants) >= 2:
    print("\nLes deux premiers étudiants peuvent-ils être dans le même cours ?")
    print(meme_cours(etudiants[0], etudiants[1]))

if professeurs and etudiants:
    print("\nLe premier professeur peut-il enseigner au premier étudiant ?")
    print(peut_enseigner(professeurs[0], etudiants[0]))
