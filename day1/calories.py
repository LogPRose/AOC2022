import numpy as np

#Part 1
with open('input.txt', 'r') as file:
    elfMeals = []
    elfBags = file.read().split("\n\n")
    for bag in elfBags:
        calories = sum(map(int, bag.splitlines()))
        elfMeals.append(calories)
print(max(elfMeals))

totalCals = 0
#Part 2
for i in range(3):
    totalCals += elfMeals.pop(np.argmax(elfMeals))

print(totalCals)