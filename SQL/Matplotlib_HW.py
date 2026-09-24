import matplotlib.pyplot as plt

week = [1,2,3,4,5,6]
savings = [300,400,150,0,260,700]

plt.plot(week,savings,color= 'crimson' ,marker='o',markeredgecolor='red',linestyle = 'dashed',linewidth=2)

plt.title("Savings")
plt.xlabel("Saving Done")
plt.ylabel("Week")

plt.grid(True)

plt.ylim(0,800)
plt.show()




plt.bar(week,savings,color= 'lightblue')

plt.title("Savings")
plt.xlabel("Savings Done")
plt.ylabel("Week")

plt.ylim(0,800)
plt.show()