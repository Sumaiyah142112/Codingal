import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,13)

#Saving plan using equations
y = 500* x
y1 = 700 * x

#Plotting
plt.plot(x,y,linestyle='dashed',color='r',marker='o',linewidth=1,label='Regular_Plan')

plt.plot(x,y1,linestyle='solid',color='b',marker='D',linewidth=1,label='Goal_plan')

#Filling space
plt.fill_between(x,y,y1,alpha=0.2,label="Savings difference",color="teal")

plt.title("Savings Double Line Chart")
plt.xlabel("Month")
plt.ylabel("Total Savings")

#Set the limits of x and y axis
plt.xlim(1,12)
plt.ylim(0,9000)

#Displaying all numbers on the x-axis
plt.xticks(x)

#Show the labels
plt.legend()

plt.show()

