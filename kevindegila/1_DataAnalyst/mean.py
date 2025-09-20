import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    w = 178
    print("-" * w)

    titanic = sns.load_dataset("titanic")
    print(titanic.shape)
    # sns.histplot(titanic.age, kde=True)
    # # sns.kdeplot(titanic.age)
    # # sns.displot(titanic.age)
    # # sns.histplot(titanic.age, kde=True, bins=5)
    # # sns.histplot(
    # #     titanic.age, kde=True, bins=5, stat="density", element="step", fill=False
    # # )
    # # plt.show()

    # grid = sns.FacetGrid(titanic, row="sex", col="survived")
    # grid.map(plt.hist, "age")
    # # plt.show()

    print(titanic.head())

    # scatter avec ligne
    # sns.regplot(data=titanic, x="age", y="fare", scatter_kws={"alpha": 0.5})
    # plt.title("sns.regplot()")
    # plt.show()

    # Distribution of ages for those who survived vs those who did not
    # sns.stripplot(data=titanic, x="survived", y="age")
    # Distribution plus large
    sns.swarmplot(data=titanic, x="survived", y="age")
    
    # sns.pairplot(data=titanic, hue="survived")
    plt.show()

    # Doc Seaborn: https://seaborn.pydata.org/tutorial.html
