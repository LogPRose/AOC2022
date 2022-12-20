import numpy as np
import sys

args = sys.argv
inputFile = args[1]
#Part 1
with open(inputFile, 'r') as file:
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