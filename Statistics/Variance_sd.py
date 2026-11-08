import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Weather Dataset.csv")

df.head(5)

df.info()

df.isnull().sum()

mean_temp = np.mean(df['Temperature (C)'])
print("Mean temp is: ",mean_temp)

var_temp = np.var(df['Temperature (C)'])
print("Variation of temp is: ",var_temp)

sd_temp = np.std(df['Temperature (C)'])
print("Standard Deviation of temp is: ",sd_temp)

for i in range(1,13):
    month = df.loc[df['month']==i]["Temperature (C)"]
    print("for month "+str(i))
    print("Mean temp is: "+str(np.mean(month)))
    print("Standard deviation is: ",str(np.std(month))+'\n')