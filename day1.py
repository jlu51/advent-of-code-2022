# Advent of Code 2022
# Day 1 
# 12/12/2022

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