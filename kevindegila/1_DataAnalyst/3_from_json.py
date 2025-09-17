import numpy as np
import pandas as pd
import math, os
from tabulate import tabulate
import urllib.request

print("-" * 55)

dossier = "data"
fichier = os.path.join(dossier, "movie.csv")

url = (
    "https://raw.githubusercontent.com/kevindegila/data-analyst/main/datasets/movie.csv"
)

# Créer le dossier si nécessaire
os.makedirs(dossier, exist_ok=True)

# Télécharger le fichier seulement s'il n'existe pas
if not os.path.exists(fichier):
    urllib.request.urlretrieve(url, fichier)

# Lecture robuste du CSV
try:
    movie = pd.read_csv(fichier, sep=",")
except pd.errors.ParserError:
    # movie = pd.read_csv(fichier, sep=",", engine="python", on_bad_lines="skip")
    movie = pd.read_csv(fichier, sep=",", engine="python", on_bad_lines="ignore")
    print("Avertissement: certaines lignes mal formées ont été ignorées.")

print(movie.info())
print(movie.head(3))
print(movie.tail(3))
print(movie)
print(movie.ndim, movie.shape, movie.size)

# movie_reduced = movie.drop(0, inplace=True)
movie_reduced = movie.drop(0)

percentages = movie_reduced["language"].value_counts(normalize=True) * 100
percentages = percentages.apply(lambda x: f"{x:.2f} %")
print(percentages)

print(movie.movie_title)
print(movie.gross.describe())
