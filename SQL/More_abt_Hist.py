import matplotlib.pyplot as plt

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women =[67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

type = [blood_sugar_men,blood_sugar_women]
colors = ['g','r']
bins = 10
xlabel = ("Blood Sugar Range")
ylabel = ("No. of Women")
label = ['men','women']

plt.hist(type,bins = bins,color=colors,rwidth = 0.80,label =label,orientation = "vertical")

plt.title("Blood Sugar Level Charts")
plt.show()