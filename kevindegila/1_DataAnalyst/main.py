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

    print('ok')
