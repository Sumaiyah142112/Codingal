import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("IMDB.csv")

df .head(10)

df.isnull().sum()

plt.hist(df['Runtime'])
plt.xlabel("Count of movies")
plt.ylabel("Runtime")
plt.show()


plt.hist(df['IMDB_Rating'])
plt.xlabel("Count of movies")
plt.ylabel("IMBD_Rating")
plt.title("IMDB Rating")
plt.show()

df['Runtime'].unique

bins_time = np.arange(80,230,10)
plt.hist(df["Runtime"],bins= bins_time,edgecolor='black',color='g')
plt.xlabel("Runtime")
plt.ylabel("Count of Movies")
plt.show()

df['IMDB_Rating'].unique

bins_rating = np.arange(8,10,0.20)
plt.hist(df["IMDB_Rating"],bins= bins_rating,edgecolor='black',color='g')
plt.xlabel("IMDB_Rating")
plt.ylabel("Count of Movies")
plt.xticks('IMDB Rating')
plt.show()