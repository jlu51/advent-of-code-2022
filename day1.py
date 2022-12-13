# Advent of Code 2022
# Day 1 
# 12/12/2022

# TODO: Turn into functions are define with a main!

# First Half
f = open("./input/day1_input.txt", "r")
mySum = 0
lines = f.readlines()
calorieDict = {}

print(lines)
runningSum = 0
index = 0

for line in lines:
   if not line.isspace():
      runningSum += int(line.strip())
   else:
      print("space")
      calorieDict[index] = runningSum
      runningSum = 0
      index += 1
      
print(calorieDict)
print(max(calorieDict, key=calorieDict.get))
print(calorieDict[max(calorieDict, key=calorieDict.get)])

# Second Half
# Unlike first half, a dictionary is not necessary for this WHOLE problem at all.
# We are just accessing the values and do not need indication of who

f = open("./input/day1_input.txt", "r")
mySum = 0
lines = f.readlines()
calorieArr = []

print(lines)
runningSum = 0
index = 0

for line in lines:
   if not line.isspace():
      runningSum += int(line.strip())
   else:
      print("space")
      calorieArr.append(runningSum)
      runningSum = 0
      index += 1
      
print(calorieArr)
print(sorted(calorieArr)[-3:]) # returns the last three items in list (highest 3 calories elf)
print(sum(sorted(calorieArr)[-3:])) 
