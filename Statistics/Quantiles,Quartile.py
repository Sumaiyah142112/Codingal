import pandas as pd
import numpy as np
import statistics as stats
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("Titanic Dataset.csv")

df.head(5)

df.info()

df.isnull().sum()

age_q1 = np.quantile(df['Age'],0.25)
age_q2 = np.quantile(df['Age'],0.50)
age_q3 = np.quantile(df['Age'],0.75)

print("Age Quartiles- ")
print('Q1: ',age_q1)
print("Q2: ",age_q2)
print('Q3: ',age_q3)

IQR_age = age_q3 - age_q1
print("Interquartile Range: ",IQR_age)

plt.hist(df['Age'])
plt.xlabel('Age')
plt.ylabel("Count of Passengers")
plt.show()

fare_q1 = np.quantile(df['Fare'],0.25)
fare_q2 = np.quantile(df['Fare'],0.50)
fare_q3 = np.quantile(df['Fare'],0.75)

print("Fare Quartiles- ")
print('Q1: ',fare_q1)
print("Q2: ",fare_q2)
print('Q3: ',fare_q3)

IQR_Fare = fare_q3 - fare_q1
print("Interquartile Range: ",IQR_Fare)

bin = np.arange(0,250,20)
plt.hist(df['Fare'],bins=np.arange(1,250,20),color='g',edgecolor= 'black')
plt.xlabel('Fare')
plt.ylabel("Count of Passengers")
plt.xticks(bin)
plt.show()






