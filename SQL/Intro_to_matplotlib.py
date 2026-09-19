import matplotlib.pyplot as plt

y = ["Sunday","Monday","Tuesday","Wednesday","Thursday"]
x = [38,34,50,31,55]

plt.plot(y,x,color="blue",linewidth = 3,linestyle = "dotted",marker = "o")

plt.title("Weather")

plt.xlabel("Days of the week")
plt.ylabel("Celsius")
plt.ylim(10)
plt.show()


y = ["Sunday","Monday","Tuesday","Wednesday","Thursday"]
x = [38,34,50,31,55]

plt.bar(y,x,color="Orange",linewidth = 1)

plt.title("Weather")

plt.xlabel("Days of the week")
plt.ylabel("Celsius")
plt.ylim(10)
plt.show()

