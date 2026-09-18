import numpy as np

numbers = np.array([0,1,2,3,4,5,6,7,8,9])

print(numbers)

print(numbers.reshape(2,5))

sum = 0
for number in numbers:
    if number % 2 == 0:
      sum= sum+number
print(sum)
    

new = numbers.copy()

for number in new:
   if new[number] % 2 != 0:
      new[number] = -1
    

print(new)