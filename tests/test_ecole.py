# Ce fichier contient les tests unitaires pour le projet d'école.

import unittest
from ecole.ecole_classes import Etudiant, Professeur
from ecole.ecole_affichage import parser_donnees
from ecole.ecole_calcul import meme_cours, peut_enseigner

class TestEcole(unittest.TestCase):

    def setUp(self):
        self.etud1 = Etudiant("Doe", "John", 20, "Informatique", 3)
        self.etud2 = Etudiant("Smith", "Alice", 22, "Informatique", 3)
        self.etud3 = Etudiant("Lee", "Kevin", 21, "Maths", 4)
        self.prof1 = Professeur("Brown", "Tom", 45, "Informatique", 10, 6)
        self.prof2 = Professeur("Miller", "Sara", 35, "Maths", 2, 2)

    def test_meme_cours_true(self):
        self.assertTrue(meme_cours(self.etud1, self.etud2))

    def test_meme_cours_false(self):
        self.assertFalse(meme_cours(self.etud1, self.etud3))

    def test_peut_enseigner_true(self):
        self.assertTrue(peut_enseigner(self.prof1, self.etud1))  # 10*2 + 6 = 26 >= 3

    def test_peut_enseigner_false(self):
        prof = Professeur("Test", "Mini", 30, "Info", 1, 1)  # 1*2 + 1 = 3
        etud = Etudiant("Petit", "Paul", 18, "Info", 5)      # niveau 5
        self.assertFalse(peut_enseigner(prof, etud))


    def test_parser_donnees(self):
        lignes = [
            ["Doe", "John", "20", "Informatique", "3"],
            ["Smith", "Alice", "22", "Maths", "4"],
            ["Brown", "Tom", "45", "Dev_Web", "15", "8"]
        ]
        personnes = parser_donnees(lignes)
        self.assertEqual(len(personnes), 3)
        self.assertIsInstance(personnes[0], Etudiant)
        self.assertIsInstance(personnes[2], Professeur)

if __name__ == "__main__":
    unittest.main()