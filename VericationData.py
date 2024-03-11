
import seaborn as sns
import matplotlib.pyplot as plt

from ArchiveLoader import loaderData

dfs = loaderData()
df2009_2024 = dfs[0]
df2019_2024 = dfs[1]
df2023_2024 = dfs[2]



print(df2009_2024['settlement_date'].head(5))