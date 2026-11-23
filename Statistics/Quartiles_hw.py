import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv("Bestsellers.csv")

print("Head",df.head(5))

print("Info",df.info())

df.isnull().sum()

quartile_10 = np.quantile(df['Price'],0.10)

quartile_1 = np.quantile(df['Price'],0.25)
quartile_2 = np.quantile(df['Price'],0.50)
quartile_3 = np.quantile(df['Price'],0.75)

IQ_range_price = quartile_1 - quartile_3
print("Quartile 10: ",quartile_10)
print("Quartile 1: ",quartile_1)
print("Quartile 2: ",quartile_2)
print("Quartile 3: ",quartile_3)

print("IQR of Price: ",IQ_range_price)


quartile_1_U = np.quantile(df['User Rating'],0.25)
quartile_2_U = np.quantile(df['User Rating'],0.50)
quartile_3_U = np.quantile(df['User Rating'],0.75)

IQR_User = quartile_1_U - quartile_3_U
print("Quartile 10: ",quartile_10)
print("Quartile 1: ",quartile_1_U)
print("Quartile 2: ",quartile_2_U)
print("Quartile 3: ",quartile_3_U)

print("IQR of Price: ",IQR_User)


plt.boxplot(df['Price'])
plt.title("Box plot of Price")
plt.xlabel('Count')
plt.ylabel("Price")
plt.show()


plt.boxplot(df['User Rating'])
plt.title("Box plot of User rating")
plt.xlabel('Count')
plt.ylabel("User Rating")
plt.show()



