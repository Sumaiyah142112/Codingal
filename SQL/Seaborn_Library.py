import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

clean = df.dropna()
print(clean)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

print(df['species'].unique())
print(df['island'].unique())

sns.histplot(data = df,x = 'flipper_length_mm',color = 'blue',bins = 10)
plt.title('Species')
plt.xlabel('Flipper_length')
plt.ylabel('Count')
plt.show()

sns.kdeplot(data = df,x = 'flipper_length_mm',hue = 'island',fill = True)
plt.title("Islands")
plt.xlabel("Flipper_Length")
plt.ylabel("Islands")
plt.show()

sns.histplot(data = df,x = 'flipper_length_mm',color = 'blue',bins = 10,kde = True)
plt.title('Species')
plt.xlabel('Flipper_length')
plt.ylabel('Count')
plt.show()

corr = df.corr(numeric_only = True)
sns.heatmap(corr,annot = True)
plt.title("Length")
plt.show()

sns.scatterplot(data = df,x = "body_mass_g",y="flipper_length_mm",hue='species',color = "skyblue")
plt.title("Dots")
plt.xlabel("Body_mass_g")
plt.ylabel("Flipper_Length")
plt.show()