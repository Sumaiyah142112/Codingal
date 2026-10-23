import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\DELL\Documents\Zoom\Coding\SQL\Penguins Data.csv")

Length = (df['Culmen Length (mm)'] - df['Culmen Length (mm)'].mean()) / df['Culmen Length (mm)'].std()
Depth = (df['Culmen Depth (mm)']-df['Culmen Depth (mm)'].mean())/ df['Culmen Depth (mm)'].std()
Flipper_Lenght = (df['Flipper Length (mm)']-df['Flipper Length (mm)'].mean())/df['Flipper Length (mm)'].std()
Body = (df['Body Mass (g)']-df['Body Mass (g)'].mean())/df['Body Mass (g)'].std()

bins = 15

plt.hist(Length,bins = bins,label= 'Culmen Length (mm)',color = 'r',rwidth = 0.80,histtype='barstacked',alpha = 0.5)
plt.hist(Depth,bins = bins,label= 'Culmen Depth (mm)',color = 'g',rwidth = 0.80,histtype='barstacked',alpha = 0.5)
plt.hist(Flipper_Lenght,bins = bins,label= 'Flipper Length (mm)',color ='b',rwidth = 0.80,histtype='barstacked',alpha = 0.5)
plt.hist(Body,bins = bins,label= 'Body Mass (g)',color = 'pink',rwidth = 0.80,histtype='stepfilled',alpha = 0.7)


plt.xlabel("Range")
plt.ylabel("Count")
plt.title("Penguins Features Ranges")
plt.legend()
plt.show()