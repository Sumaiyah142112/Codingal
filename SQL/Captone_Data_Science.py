import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

ds = sns.load_dataset('penguins')

print("First ten rows:",ds.head(10))
print("First five rows:",ds.tail())

print("Types of columns:",ds.dtypes)

print("Dataset information:",ds.info())

print("Statistical info:",ds.describe())

print(ds['species'].unique())
print(ds['island'].unique())
print(ds['sex'].unique())

print(ds['species'].value_counts())
print(ds['island'].value_counts())
print(ds['sex'].value_counts())

corr = ds.corr(numeric_only=True)
print(corr)

sns.heatmap(corr,annot=True,cmap= 'coolwarm')
plt.title("Heatmap")
plt.show()

sns.histplot(corr,x='body_mass_g',bins= 10,color= 'skyblue')
plt.title("Histogram")
plt.xlabel("Body_Mass")
plt.show()

sns.boxplot(data = ds,x="flipper_length_mm",y="body_mass_g",color = 'maroon')
plt.title("Boxplot")
plt.xlabel("Flipper_length")
plt.ylabel("Body_Mass")
plt.show()

sns.countplot(data = ds,x="species",color = 'maroon')
plt.title("Countplot")
plt.xlabel("Species")
plt.show()

sns.countplot(data = ds,x="sex",color = 'lightgreen')
plt.title("Countplot")
plt.xlabel("Species")
plt.show()

sns.countplot(data = ds,x="island",color = 'lightblue')
plt.title("Countplot")
plt.xlabel("Island")
plt.show()

sns.scatterplot(data = ds,x="flipper_length_mm",y="body_mass_g",hue= 'species')
plt.title("Scatterplot")
plt.xlabel("Flipper_length")
plt.ylabel("Body_Mass")
plt.show()

sns.scatterplot(data = ds,x="bill_length_mm",y="bill_depth_mm",hue= 'species')
plt.title("Scatterplot")
plt.xlabel("bill_length")
plt.ylabel("bil_depth")
plt.show()

sns.pairplot(ds[['flipper_length_mm','body_mass_g','bill_depth_mm']])
plt.title("Pairplot")
plt.show()