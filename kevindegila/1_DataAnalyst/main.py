import numpy as np
import pandas as pd
import math, os
from tabulate import tabulate
import urllib.request

from subs.get_json import get_movies


print("-" * 111)


if __name__ == "__main__":
    movie = get_movies()
    print(
        "Un des films avec K. SPACEY:",
        movie[movie["actor_1_name"] == "Kevin Spacey"]["movie_title"][4:5],
    )
