
import seaborn as sns
import matplotlib.pyplot as plt

from Archiloader2 import loaderData

dfs = loaderData()
df2009_2024 = dfs[0]
df2019_2024 = dfs[1]
df2023_2024 = dfs[2]

print("demarage de la verification")


for value in df2009_2024['non_bm_stor']:
    if value != 0:
        print("La valeur est différente de 0", value)

print(df2009_2024.shape)


