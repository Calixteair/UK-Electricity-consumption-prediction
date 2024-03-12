import seaborn as sns
import matplotlib.pyplot as plt

from Archiloader2 import loaderData

# Calculer la matrice de corrélation

dfs = loaderData()
df2009_2024 = dfs[0]
df2019_2024 = dfs[1]
df2023_2024 = dfs[2]




corr = df2009_2024.corr()

# Créer une heatmap
plt.figure(figsize=(12,10))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

# Calculer la matrice de corrélation

