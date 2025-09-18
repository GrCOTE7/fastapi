import numpy as np
import pandas as pd
import math, os, platform
from tabulate import tabulate
import urllib.request

from subs.get_json import get_movies

if __name__ == "__main__":

    w = 178

    # print("\n" * 99, "\b" + "─" * 70 + ">")
    print("\n" * 99)

    movie = get_movies()
    # print(movie.fillna('').head())

    l = movie.genres.str.split("|", expand=True)
    print(l[0].value_counts().describe())
    print("─" * w)

    movie["nb_genres"] = movie["genres"].fillna("").str.count(r"\|") + 1

    max_genres = movie["nb_genres"].max()  # - 7

    films_max_genres = movie[movie["nb_genres"] == max_genres]

    print(f"Films avec le max de genres ({max_genres}):")
    print(
        tabulate(
            films_max_genres[["movie_title", "genres"]],
            headers="keys",
            tablefmt="pretty",
        )
    )

    nb_films = len(films_max_genres)
    cases = {0: "Aucun film n'a", 1: "1 film a"}
    phrase = cases.get(nb_films, f"{nb_films} films ont")
    print(f"{phrase} {max_genres} genre{'s' if max_genres > 1 else ''}.")
