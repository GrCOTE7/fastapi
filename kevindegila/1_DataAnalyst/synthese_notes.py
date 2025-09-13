import numpy as np
from tabulate import tabulate

notes = np.random.randint(21, size=(3, 5))

row_means = np.mean(notes, axis=1)
col_means = np.mean(notes, axis=0)
global_mean = np.mean(notes)

# Préparation du tableau avec les moyennes par ligne (en gras)
table = []
for i, row in enumerate(notes):
    table.append(
        [f"Élève {i+1}"] + list(row) + [f"\033[1m{round(row_means[i], 2)}\033[0m"]
    )

# Ajout de la ligne des moyennes par colonne (en gras) et la moyenne générale en bas à droite
table.append(
    ["Moyenne colonnes"]
    + [f"\033[1m{round(m, 2)}\033[0m" for m in col_means]
    + [f"\033[1m{round(global_mean, 2)}\033[0m"]
)

# Création des entêtes
headers = (
    ["Classe 1"] + [f"Col {j+1}" for j in range(notes.shape[1])] + ["Moyenne lignes"]
)

print(tabulate(table, headers=headers, tablefmt="grid"))
