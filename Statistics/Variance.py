import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Weather Dataset.csv")

df.head(5)

df.info()

df.isnull().sum()


mean = np.mean(df['Temperature (C)'])
print("Mean Temp is: ",mean)

var = np.var(df['Temperature (C)'])
print("Variance of Temp is: ",var)

standard_deviation = np.std(df['Temperature (C)'])
print("Standard Deviation of temp is: ",standard_deviation)


for i in range(1,13):
    temp = df.loc[df['month'] == i ]["Temperature (C)"]
    print("For month: "+ str(i))
    print("Mean temp is: "+ str(np.mean(temp)))
    print("Standard Deviation: " + str(np.std(temp))+'\n')
