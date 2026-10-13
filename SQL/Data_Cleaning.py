import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = sns.load_dataset("penguins")

print("FIRST 10 Rows:")
print(df.head(10))

print("Checking missing Values:")
print(df.isnull().any())
print(df.isnull().sum())

#Heat map
plt.figure(figsize=(20,15))
sns.heatmap(df.isnull(),cmap='coolwarm')
plt.title("Heat Map")
plt.xlabel("Dataset Columns")
plt.ylabel("Penguin Records")
plt.show()

#Removing rows
print("Removing rows with dropna")
print(df.dropna(how='all'))
print(df.head())

#Categorical columns Handling
print("Categorical Columns")
categorical_columns = ["species","sex","island"]

for column in categorical_columns:
    most_common_value = df[column].mode()[0]
    df[column]=df[column].fillna(
        most_common_value
    )

#Numerical values handling
print("Numerical Columns")
numerical_values =["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]

df[numerical_values]=(df[numerical_values].interpolate())
df[numerical_values]=(df[numerical_values].bfill().ffill())

print("Datset:")
print(df.isnull().sum())

print("Cleaned Rows:")
print(df.head(10))

#Number of rows left after completely cleaning:
penguins= df.dropna()

print("number of complete penguin records:")
print(len(penguins))
















