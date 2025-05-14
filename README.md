# intro-python

Exercice Python J3
Créez :
une classe "Personne" avec pour attributs "nom":str, "prenom":str et "age":int
;
2 classes filles qui seront "Etudiant" et "Professeur", avec des attributs
supplémentaires :
Etudiant : attribut "Filiere":str, attribut "Niveau d'étude":int
Professeur : attribut "Specialite":str, attribut "Annee d'experience":int,
attribut “Annee d’etude”:int


une fonction de calcul pour “Etudiant” qui va regarder les années d’étude et la
filiere de deux éléments et nous sortir si oui ou non ces 2 élements peuvent
être dans le même cours

une fonction de calcul qui va regarder le nombre d’années d’expérience fois 2
sommé au niveau d’étude d’un professeur et comparer au niveau d’étude d’un
étudiant. Si le professeur a ce nombre d’années supérieures ou égales au
nombre d’années d’étude de l’étudiant, la fonction retournera True
une méthode de représentation d'élément pour les classes Personnes,
Etudiant et Professeur qui affichera sous forme de phrase chacun des attributs
des classes correspondantes.

une fonction de lecture/affichage qui prendre un fichier csv ou txt (les deux
cas doivent être gérés) sous la forme :
Victor BONELLY 24 Programmation_Objet 3
Adrian ROSARI 30 Analyse_de_données 4 5
Ludovic Nan 23 Développement_Web 4
…

Pour le csv, ce sera non pas des espaces mais des “;” qui serviront de
séparateurs

Exercice Python J3 1

Et créer un dataframe avec ces données en attribuant les colonnes
nécessaires.

Il faudra également utiliser ces données en utilisant les méthodes et fonctions
utilisées pour regrouper les élèves par groupe/Filière.

Il faudra regrouper les classes dans un module ecole_classes, les méthodes de
calcul dans un module ecole_calcul, les méthodes d’affichage dans un module
ecole_affichage et tout cela dans le package ecole.

Il ne faudra pas oublier __ init __.py (sans espace) à placer dans les packages que
l'on veut créer (le contenu de __ init __.py (sans espace) n'importe pas).

Au même niveau que le package, un fichier ipynb ou py où on exécutera les
différentes sorties des fonctions de calcul et d'affichage. 