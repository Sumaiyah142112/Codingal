import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Bestsellers.csv")

df.head(5)

df.isnull().sum()

var = np.var(df['Price'])
print("Variance of Price is: ",var)

standard_deviation = np.std(df['Price'])
print("Standard Deviation of Price is: ",standard_deviation)

var_1 = np.var(df['User Rating'])
print("Variance of User Rating is: ",var_1)

standard_deviation_1 = np.std(df['User Rating'])
print("Standard Deviation of User Rating is: ",standard_deviation_1)

bins = np.arange(10,250,20)
plt.hist(df['Price'],bins = bins,color='blue')
plt.title("Price HistPlot")
plt.xlabel("Price")
plt.ylabel("Count")
plt.xticks(bins)
plt.show()


plt.hist(df['User Rating'],bins = 10,color='blue')
plt.title("User Rating HistPlot")
plt.xlabel("User Rating")
plt.ylabel("Count")
plt.xticks()
plt.show()