import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

if __name__ == "__main__":

    w = 178

    auto = pd.read_csv(
        "https://raw.githubusercontent.com/kevindegila/data-analyst/refs/heads/main/datasets/Automobile_data.csv"
    )

    print(auto)
    print("-" * w)
    print(auto.describe().T)
    print(auto["body-style"].value_counts())
    print("-" * w)
    print(auto.groupby("body-style").groups)
    print(auto.groupby("body-style").groups.keys())
    # print(auto.groupby('body-style').groups.values())

    style = auto.groupby("body-style")
    print(style.get_group("convertible"))

    print(auto["drive-wheels"].value_counts())
    print("-" * w)

    double_groupin = auto.groupby(["body-style", "drive-wheels"])
    print(double_groupin.size())

    print("-" * w)

    print("\ngroups", "─" * (w - 7))
    print(double_groupin.groups)

    print("-" * w)
    print(double_groupin.first())  # 1ère combinaison de chaque groupe

    print("\n\nsize()", "─" * (w - 7) + "\n")
    print(style.size())

    print("\n\nsum()", "─" * (w - 6) + "\n")
    print(style.sum())

    print("\n\nget_group", "─" * (w - 10) + "\n")
    print(style.get_group("convertible"))

    print("\n\nfirst", "─" * (w - 6) + "\n")
    print(style.first())

    # print("\n\nfirst", "─" * (w - 6) + "\n")
    # print(style.info())

    # print(style["city-mpg"].mean().plot(kind="bar"))


    print("\n\nstyle['city-mpg'].mean()", "─" * (w - 25) + "\n")
    mean_val = style["city-mpg"].mean()
    print(mean_val)
    
    mean_val.plot(kind="bar")

    plt.title("Moyenne city-mpg")
    plt.ylabel("mpg")
    plt.tight_layout()
    plt.show()
