import matplotlib.pyplot as plt

x= [4,6,8,10,15,17,19]
y= [8,5,9,4,7,11,15]
y1=[6,7,10,12,13,15,19]
plt.plot(x,y,marker='o',linestyle='dashed',label='Line 1')
plt.plot(x,y1,marker='o',linestyle='dashed',label='Line 2')
plt.xlim(4,20)
plt.ylim(4,20)
plt.ylabel("y")
plt.xlabel("x")
plt.title("Line graph")
plt.fill_between(x,y,y1,color='green',alpha=0.1)
plt.legend(loc='upper left')
plt.show()


