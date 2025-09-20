import numpy as np
import pandas as pd
import math, os
from tabulate import tabulate
import urllib.request

from subs.get_json import get_movies


print("-" * 111)


if __name__ == "__main__":
    movie = get_movies()

    # print(
    #     movie.loc[4:8, ["duration", "gross", "actor_2_name", "director_facebook_likes"]]
    # )

    # print(movie[movie["director_name"] == "Doug Walker"]['movie_title'])
    print(
        "Le 4ème film avec K. SPACEY:",
        movie[movie["actor_1_name"] == "Kevin Spacey"]["movie_title"][4:5],
    )
    print("-" * 111)

    d = movie["duration"]
    print("Moyenne:", f"{d.mean():.2f}", "\n\bÉcart-type:", f"{d.std():.2f}")
    # exit()
    import matplotlib.pyplot as plt

    # # ✅ Histogramme & Nuage de points (côte à côte)
    # fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # 1 ligne, 2 colonnes
    # fig.canvas.manager.set_window_title("✅ Analyse des durées de films")

    # plt.suptitle("Histogramme & Nuage de points (côte à côte)", fontsize=16)

    # axes[0].hist(movie["duration"], bins=50, color="skyblue", edgecolor="black")
    # axes[0].set_xlabel("Durée (min)")
    # axes[0].set_ylabel("Nombre de films")
    # axes[0].set_title("Distribution des durées")

    # axes[1].scatter(
    #     range(len(movie["duration"])), movie["duration"], alpha=0.2, color="darkorange"
    # )
    # axes[1].set_xlabel("Index du film")
    # axes[1].set_ylabel("Durée (minutes)")
    # axes[1].set_title("Durée des films (nuage de points)")
    # axes[1].grid(True)
    # plt.tight_layout()
    # plt.show()

    # 🧠 Explication rapide
    # fig, axes = plt.subplots(1, 2) → crée une figure avec 2 sous-graphes côte à côte
    # axes[0] → histogramme
    # axes[1] → scatter plot
    # figsize=(12, 5) → ajuste la taille globale
    # tight_layout() → évite que les titres ou labels se chevauchent

    # ✅ Version Superposée (scatter plot + courbe de densité (même axe Y))

    import seaborn as sns

    sns.set_theme(style="whitegrid", palette="pastel")

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.canvas.manager.set_window_title("Durée des films")

    # Moyenne
    mean_duration = movie["duration"].mean()
    ax.axhline(
        mean_duration,
        color="red",
        linestyle="-",
        linewidth=2,
        label=f"Moyenne: {mean_duration:.2f} min",
    )

    # Médiane (Valeur au centre d’un tri)
    median_duration = movie["duration"].dropna().median()
    # dropna() pour éviter les NaN
    ax.axhline(
        median_duration,
        color="purple",
        linestyle=":",
        linewidth=2,
        label=f"Médiane: {median_duration:.2f} min",
    )

    # Écart-type (au-dessus et en-dessous de la moyenne)
    std_duration = movie["duration"].std()
    ax.axhline(
        std_duration,
        color="blue",
        linestyle="--",
        linewidth=2,
        label=f"Écart-type: {std_duration:.2f} min",
    )

    # Légende
    ax.legend()

    # Nuage de points vertical (index vs durée)
    ax.scatter(
        range(len(movie["duration"])), movie["duration"], alpha=0.2, color="skyblue"
    )
    ax.set_xlabel("Index du film")
    ax.set_ylabel("Durée (minutes)")
    ax.set_title("Durée des films")

    # Axe secondaire pour histogramme horizontal
    ax_hist = ax.twinx()

    # Histogramme horizontal (durée sur Y, fréquence sur X)
    ax_hist.hist(
        movie["duration"],
        bins=50,
        orientation="horizontal",
        color="darkorange",
        alpha=0.7,
    )
    ax_hist.set_ylabel("Durée (minutes)")
    ax_hist.set_xlabel("Fréquence")
    ax_hist.grid(False)  # pour éviter double grille

    plt.tight_layout()
    plt.show()
