import numpy as np
import math
from tabulate import tabulate


print("-" * 55)
# Math, Physique, SVT
x = np.array(
    [
        [6, 8, 4],
        [12, 10, 7],
        [8, 13, 11],
        [5, 7, 6],
        [10, 2, 11],
    ]
)

res = np.median(np.mean(x, axis=1))
print(res)


# notes_sup_5 = np.sum(x > 5)
# notes_sup_8_students = np.sum(x > 8, axis=1)
# nb_student_with_2_notes_sup_8 = np.sum(notes_sup_8_students >= 2)

# tous_les_etudiants_ont_note_sup_7 = np.all(np.any(x > 7, axis=1))

# Est-ce qu'il y au moins un élève ayant au moins une note supérieur à 12 ?
au_moins_un_etudiant_avec_note_sup_12 = np.any(x > 12)

# Quelle est la moyenne en Math et Physique de la classe si on considère uniquement les 3 élèves dont les notes apparaissent en premier ?
moyenne_math_physique_premiers_eleves = np.mean(x[:3, :2])

# print("Notes > 5 :", notes_sup_5)
# print("Notes > 8 par étudiant :", notes_sup_8_students)
# print("Nombre d'étudiants avec 2 notes > 8 :", nb_student_with_2_notes_sup_8)

# print("Tous ont au moins une note > 7 :", tous_les_etudiants_ont_note_sup_7)
# print("Au moins un étudiant a une note > 12 :", au_moins_un_etudiant_avec_note_sup_12)

# print("Moyenne Math et Physique des 3 premiers élèves :", moyenne_math_physique_premiers_eleves)

# la médiane des moyennes (elèves)
mediane_moyennes_eleves = np.median(np.mean(x, axis=1))

# Combien d'élèves ont au moins 2 notes supérieurs à la médiane des moyennes (élèves) de la classe ?
notes_sup_mediane = np.sum(x > mediane_moyennes_eleves, axis=1)
nb_eleves_avec_2_notes_sup_mediane = np.sum(notes_sup_mediane >= 2)
print(nb_eleves_avec_2_notes_sup_mediane)
