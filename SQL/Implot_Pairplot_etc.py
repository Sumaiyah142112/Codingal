import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df = df.dropna()

df.info()
df.head()

#Barplot
sns.barplot(data =df,x='day',y='total_bill',hue='sex')
plt.title("Bar Plot")
plt.xlabel("Days")
plt.ylabel("Total_bill")
plt.show()


#Countplot
sns.countplot(data =df,x='day',hue='sex')
plt.title("Count Plot",y=1.05)
plt.xlabel("Days")
plt.ylabel("Count")
plt.show()

#Boxplot
sns.boxplot(data =df,x='day',y='total_bill',hue='sex')
plt.title("Box Plot")
plt.xlabel("Days")
plt.ylabel("Total_bill")
plt.show()
#Striplot
sns.stripplot(data =df,x='day',y='total_bill',jitter= True)
plt.title("Strip Plot")
plt.xlabel("Days")
plt.ylabel("Total_bill")
plt.show()
#Swarmplot
sns.swarmplot(data =df,x='day',y='total_bill')
plt.title("Swarm Plot")
plt.xlabel("Days")
plt.ylabel("Total_bill")
plt.show()

#Jointplot
sns.jointplot(data =df,x='total_bill',y='tip')
plt.title("Joint Plot")
plt.xlabel("Total_bill")
plt.ylabel("tip")
plt.show()

#Jointplot with kde
sns.jointplot(data =df,x='total_bill',y='tip', kind = 'kde')
plt.title("Joint Plot With KDE")
plt.xlabel("Total_Bill")
plt.ylabel("Tip")
plt.show()

#Pairplot
sns.pairplot(df[['total_bill','tip','size']])
plt.suptitle("Pair Plot",y=1.02)
plt.show()

#Implot
sns.lmplot(data =df,x='total_bill',y='tip')
plt.suptitle("Implot",y=1.05)
plt.xlabel("Total_Bill")
plt.ylabel("Tip")
plt.show()

#Pointplot
sns.pointplot(data =df,x='day',y='total_bill',hue='sex')
plt.suptitle("Pointplot",y=1.05)#y is like padding
plt.ylabel("Total_Bill")
plt.xlabel("Day")
plt.show()