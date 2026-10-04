import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('SQL/IMDB.csv')

# Printing Rows
print('head',df.head(3))
print('tail',df.tail(3))

#Info of dataset
print('info:',df.info())
print('describe:',df.describe())
print('shape:',df.shape)

print('null values:',df.isnull().sum())

#subset creation of dataset
subset = df.iloc[41:75]

sns.scatterplot(data=df,x='IMDB_Rating',y='Runtime')
plt.title("Relationship between IMBD_RATING AND RUNTIME USING Scatterplot")
plt.ylabel("Runtime")
plt.xlabel("IMBD_Rating")
plt.show()

sns.boxplot(data=df,x='IMDB_Rating',y='Runtime')
plt.title("Boxplot")
plt.ylabel("Runtime")
plt.xlabel("IMBD_Rating")

plt.show()


sns.countplot(data=df,x='IMDB_Rating')
plt.title("Countplot")
plt.ylabel("Count")
plt.xlabel("IMBD_Rating")

plt.show()

#Distribution of features using jointplot

sns.jointplot(data= df,x='IMDB_Rating',y='Runtime',kind='kde',cmap='coolwarm')
plt.suptitle("Jointplot",y=1.04)
plt.ylabel("Runtime")
plt.xlabel("IMBD_Rating")

plt.show()




