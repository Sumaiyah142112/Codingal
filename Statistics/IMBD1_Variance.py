import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("IMDB.csv")

df.head(5)

df.isnull().sum()


plt.hist(df['Runtime'])
plt.ylabel("Count of Movies")
plt.xlabel("Runtime")

plt.hist(df['IMDB_Rating'])
plt.ylabel("Count of Movies")
plt.xlabel("IMDB Rating")

df['Runtime'].unique()

bins_time = np.arange(80,230,10)
plt.hist(df['Runtime'],edgecolor='black',bins=bins_time,color='g')
plt.ylabel("Count of Movies")
plt.xlabel("Runtime")


df["IMDB_Rating"].unique()

bins_rating = np.arange(8,10,0.20)
plt.hist(df['IMDB_Rating'],edgecolor='black',bins=bins_rating,color='g')
plt.ylabel("Count of Movies")
plt.xlabel("IMDB Rating")
plt.xticks(bins_rating)

