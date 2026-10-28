import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("USA_Housing.csv")

df.head()

#Dataset info
df.info()

#Statistical Summary
df.describe()

#Column Names
df.columns

sns.pairplot(df)
plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include=[np.number])

sns.heatmap(
    numeric_df.corr(),
    annot = True,
    cmap='coolwarm',
    linewidth = 0.5
)

plt.title("Correlation Map")
plt.show()

