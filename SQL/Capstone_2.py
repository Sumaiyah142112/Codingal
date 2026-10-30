import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Penguins Data.csv')

print("Info: ",df.info())
print("Head:" ,df.head())
print("Describe: ",df.describe())

print(df.isnull().sum())


numerical_df = df.select_dtypes(include=['number'])
#Plotting null values for numeric data
numerical_df.plot(kind='box',figsize=(12,12),color='skyblue')
plt.xticks(rotation=25,ha='right')
plt.show()

sns.pairplot(data =df)
plt.title("Pairplot")
plt.xticks(rotation=25,ha='right')
plt.show()


sns.heatmap(data=numerical_df.corr(),annot=True,cmap='coolwarm')
plt.title('Heatmap')
plt.xticks(rotation=25,ha='right')
plt.tight_layout() 
plt.show()

numerical_dfs = df.select_dtypes(include=['number'])
numerical_dfs.boxplot(data=df)
plt.title('Boxplot')
plt.xticks(rotation=25,ha='right')
plt.tight_layout() 
plt.show()

sns.countplot(data=df,x='Species',hue="Gender")
plt.title('Countplot')
plt.xticks(rotation=25,ha='right')
plt.tight_layout() 
plt.show()

