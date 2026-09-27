import seaborn as sns
import matplotlib.pyplot as plt

ds = sns.load_dataset('planets')

ds = ds.dropna()

print("First five rows:")
print(ds.head())

print(ds.info())

print(ds.describe())
print("Unique:",ds['year'].unique())

sns.histplot(data = ds,x = 'orbital_period',color= 'blue',bins = 30)
plt.title('Orbital_Period Distribution')
plt.xlabel("Orbital_Period")
plt.show()

sns.kdeplot(data = ds,x = 'distance',fill= True)
plt.title('KDE')
plt.xlabel("Distance")
plt.show()

sns.histplot(data = ds,x = 'orbital_period',color= 'blue',bins = 15,kde = True)
plt.title('Orbital_Period Distribution')
plt.xlabel("Orbital_Period")
plt.show()

sns.scatterplot(data = ds,x = 'orbital_period',y='distance',hue= 'year')
plt.title('Comparision')
plt.xlabel("Orbital-period")
plt.ylabel("Distance")
plt.show()

corr = ds.corr(numeric_only = True)
print(corr)
sns.heatmap(corr,annot = True,cmap= 'coolwarm')
plt.title("Correlation_Heatmap")
plt.show()
