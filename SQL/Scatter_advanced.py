import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("C:/Users/DELL/Documents/Zoom/Coding/SQL/Penguins Data.csv")

print(df.head())
print(df.info())
print(df.describe())

sns.scatterplot(x="Culmen Length (mm)",data = df,y='Body Mass (g)',cmap='coolwarm')
plt.title("Features")
plt.xlabel("Culmen Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()

sns.scatterplot(x="Culmen Depth (mm)",data = df,y='Body Mass (g)',cmap='virgilis',markers='s')
plt.title("Features")
plt.xlabel("Culmen Depth (mm)")
plt.ylabel("Body Mass (g)")
plt.show()

sns.pairplot(data = df)
plt.xticks(rotation = 60)
plt.show()

cleaned_df = df.drop(columns=['Body Mass (g)', 'Sample Number'])
cleaned_df.plot(kind='area',figsize=(15,12),alpha=0.5)
plt.title("Penguin Features")
plt.ylabel("Scale")
plt.show()
