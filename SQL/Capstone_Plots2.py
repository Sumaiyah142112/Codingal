import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv("heart.csv")

df.shape

df.head()

df.info()

df.columns

df.describe()

df.isnull().sum()

print(df.info())

df.hist(figsize =(15,15),layout=(5,3))
plt.tight_layout()
plt.show()


df.plot(kind='box',subplots=True,figsize=(12,12),layout=(5,3))
plt.tight_layout() 
plt.show()


sns.barplot(data = df,x='sex',y='chol',hue='target',palette='spring')
plt.tight_layout() 
plt.show()

df['sex'].value_counts()

df['thal'].value_counts()

df['target'].value_counts()


plt.figure(figsize=(20,10))
sns.heatmap(df.corr(),annot=True,cmap='terrain')
plt.show()

sns.countplot(data=df,x='sex',palette='husl',hue='target')
plt.show()

sns.countplot(data=df,x='target',palette='BuGn')
plt.show()

sns.countplot(data=df,x='ca',hue='target')
plt.show()

