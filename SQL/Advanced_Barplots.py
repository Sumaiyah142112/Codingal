import matplotlib.pyplot as plt
import pandas as pd

df =pd.read_csv('Countrie_Data.csv')
print(df.head(3))

c_52 = df.loc[df['year'] == 1952]
print(c_52.head())

c_07 = df.loc[df['year'] == 2007]
print(c_07.head())

type(c_52)

#Merge
c_merge = c_52.merge(c_07,left_on = 'country',right_on='country')
print(c_merge.head())

#Dropping certain columns
c_merge= c_merge.drop(['year_x','year_y'],axis = 1)
print(c_merge.head())

#Creating new column
c_merge['population_growth']= (c_merge['population_y']-c_merge['population_x'])
print(c_merge.head())

print("Shape: ",c_merge.shape,type(c_merge))

#Sort Values 
c_merge =c_merge.sort_values('population_growth',ascending=False).head(10)

print(c_merge.head(10))


#Dropping an index column
#c_merge =c_merge.drop('index',axis=1)
#c_merge
c_merge.shape


#Plotting data
name =[
    'China',
    'India',
    'United States',
    'Indonesia',
    'Brazil',
    'Pakistan',
    'Bangladesh',
    'Nigeria',
    'Mexico',
    'Philippines'
]

pop_growth = c_merge['population_growth']/ 10**6

plt.figure(figsize= (15,9))

plt.bar(name,pop_growth,width= 0.4)

plt.xlabel("Country")
plt.ylabel("Population_Growth(Million)")
plt.title("Top 10 Countries w/the Biggest Population Growth from 1952 to 2007")
plt.xticks(rotation= 50)

for x,y in zip(name,pop_growth):
    label= "{:.2f}".format(y)

    plt.annotate(label,(x,y),textcoords='offset points',xytext= (0,10),ha='center')

plt.show()