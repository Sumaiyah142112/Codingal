import pandas as pd
import numpy as np
import statistics as stats
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("Bestsellers.csv")

print(df.head(),'\n')
print(df.info(),'\n')
print(df.describe(),'\n')

print(df.isnull().sum(),'\n')


Mean = np.mean(df['User Rating'])
Mean0 = df['User Rating'].mean()
Mean1 = np.mean(df['Price'])
Mean2 = np.mean(df['Reviews'])

print("Mean of User rating: ",Mean)
print("Mean of Price: ",Mean1)
print("Mean of Reviews: ",Mean2)
print("Mean0 of user ratings(Using pandas): ",Mean0,'\n')

median = np.median(df['User Rating'])
median0 = df['User Rating'].median()
median1 = np.median(df['Price'])
median2 = np.median(df['Reviews'])

print("Median of User Ratings: ",median)
print("Median of Price: ",median1)
print("Median of Reviews: ",median2)
print("Median0 of user ratings(Using pandas): ",median0,"\n")

Mode = stats.mode(df['User Rating'])
Mode0 = df['Price'].mode()[0]
Mode1 = stats.mode(df['Price'])
Mode2 = stats.mode(df['Reviews'])

print("Mode of User Ratings: ",Mode)
print("Mode of Price: ",Mode1)
print("Mode of Reviews: ",Mode2)
print("Mode0 of price(Using pandas): ",Mode0)

