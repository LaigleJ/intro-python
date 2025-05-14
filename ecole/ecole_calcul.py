# Ce fichier contient les calculs de base pour le projet d'école.

def meme_cours(etud1, etud2):
    return etud1.filiere == etud2.filiere and etud1.niveau_etude == etud2.niveau_etude

def peut_enseigner(prof, etud):
    score_prof = prof.annee_experience * 2 + prof.annee_etude
    return score_prof >= etud.niveau_etude