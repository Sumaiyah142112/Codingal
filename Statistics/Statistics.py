import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as stats

df = pd.read_csv("Titanic Dataset.csv")

df.head(5)

df.select_dtypes(include=['number'])

df.isnull().sum()

#Mean value of age and fare
mean_age = np.mean(df['Age'])
print("Mean age of passenger is: ",mean_age)

#Mean value of fare
mean_fare = np.mean(df['Fare'])
print('Mean fare is: ',mean_fare)

#Median value of age and fare

median_age = np.median(df['Age'])
print("Median value of age: ",median_age )

median_fare = np.median(df['Fare'])
print("Median value of fare: ",median_fare )

#Mode value of age and pclass for QUANTATIVE Variables
mode_age = stats.mode(df['Age'])
print("Mode Value of Age: ",mode_age)

mode_class = stats.mode(df['Pclass'])
print("Mode Value of Pclass: ",mode_class)


#Mode value of Categorical Feature - Gender

mode_gender = df['Gender'].value_counts().index[0]
print("Mode of Feature Gender: ",mode_gender)





