import numpy as np
import math
from tabulate import tabulate

x = np.array([[1, 2, 3], [4, 5, 6]])
xmean = x.mean(axis=0)
xstd = x.std(axis=0) # Ecart-type par colonne
# xvar = a.var(axis=0)

print(x.mean(), x.std())
# print(np.mean(a), xmean, xstd, xvar)
print(xmean, xstd)
# print(np.median(a), np.median(a, axis=0)) # Ignore les extrêmes
x_centre_et_reduit = (x - xmean) / xstd
print(x_centre_et_reduit, "Moyenne = ", x_centre_et_reduit.mean(), x.std(), xstd)
