import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("Bestsellers.csv")

print(df.isnull().sum())

#Variances
var_Ratings = np.var(df['User Rating'])
var_price = np.var(df['Price'])
print("Variance of User Rating: ",var_Ratings)
print("Variance of Price: ",var_price)

#Standard deviation
sd_Ratings= np.std(df['User Rating'])
sd_price = np.std(df['Price'])
print("Standard Deviation of User Rating: ",sd_Ratings)
print("Standard Deviation of Price: ",sd_price)

df['User Rating'].unique()

plt.hist(df['User Rating'],color='b',edgecolor = 'cyan',bins = 20)
plt.title("Hist plot of User Ratings")
plt.ylabel("No.of Books")
plt.xlabel("User Ratings")
plt.show()

df['Price'].unique()
plt.hist(df['Price'],color='r',edgecolor = 'black',bins = 20)
plt.title("Hist plot of Price")
plt.ylabel("No.of Books")
plt.xlabel("Price")
plt.show()