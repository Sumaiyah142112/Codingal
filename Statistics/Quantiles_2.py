import pandas as pd
import numpy as np
import statistics as stats
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("Titanic Dataset.csv")

df.head(5)

df.isnull().sum()

plt.boxplot(df['Age'])
plt.title("Age Distribution")
plt.show()

plt.boxplot(df['Pclass'])
plt.title("Pclass Distribution")
plt.show()