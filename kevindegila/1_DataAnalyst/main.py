import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":

    w = 178

    print("-" * w)

    titanic = sns.load_dataset("titanic")
    sns.kdeplot(titanic.age)
    # sns.distplot(titanic.age)
    # sns.displot(titanic.age)
    # sns.histplot(titanic.age)
    plt.show()
