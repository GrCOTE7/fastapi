import numpy as np
from tabulate import tabulate


n = np.arange(1, 10)
print(np.vstack([n, n**2, n**3]))
print("-" * 55)

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

moyennes = np.mean(x, axis=1)
for i, m in enumerate(moyennes, 1):
    print(f"Élève {i} : {m:.2f}")
print("-" * 55)

moyennes = np.mean(x, axis=1)
table = [[f"Élève {i+1}", f"{m:.2f}"] for i, m in enumerate(moyennes)]
print(tabulate(table, headers=["Étudiant", "Moyenne"], tablefmt="grid"))
print("-" * 55)

print(x[x > 10])
print("-" * 55)
indices = np.argwhere(x > 10)
for i, j in indices:
    print(f"Élève {i+1}, Matière {j+1} : {x[i, j]}")
print("-" * 55)

print(*[f"\bÉlève {i+1}, Matière {j+1} : {x[i, j]}\n" for i, j in indices])
