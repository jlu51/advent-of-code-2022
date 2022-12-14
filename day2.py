# Advent of Code 2022
# Day 2
# 12/13/2022

# Could improve using a map!

def main():
   print(calcTotalScore())
   print(calcTotalScore2())

def calcTotalScore():
   f = open("./input/day2_input.txt", "r")
   mySum = 0
   lines = f.readlines()
   totalScore = 0
   for line in lines:
      totalScore += getSelectedShapeScore(line.split()[1]) + calcRoundOutcome(line.split()[1], line.split()[0])
   return totalScore

def calcTotalScore2():
   f = open("./input/day2_input.txt", "r")
   mySum = 0
   lines = f.readlines()
   totalScore = 0
   for line in lines:
      playerChoice = findPlayerShape(line.split()[0], line.split()[1])
      totalScore += getSelectedShapeScore(playerChoice) + calcRoundOutcome(playerChoice, line.split()[0])
   return totalScore
def getSelectedShapeScore(playerChoice):
   if playerChoice == 'X':
      return 1
   elif playerChoice == 'Y':
      return 2
   elif playerChoice == 'Z':
      return 3

# calcRoundOutcome: Takes in opponent choice and player choice and outputs players result in points
def calcRoundOutcome(playerChoice, opponentChoice):
   # Player choses rock...
   if playerChoice == 'X':
      if opponentChoice == 'A':
         return 3
      elif opponentChoice == 'B':
         return 0
      elif opponentChoice == "C":
         return 6
   # Player chooses paper
   elif playerChoice == 'Y':
      if opponentChoice == 'A':
         return 6
      elif opponentChoice == 'B':
         return 3
      elif opponentChoice == "C":
         return 0
   # Player chooses scissors
   elif playerChoice == 'Z':
      if opponentChoice == 'A':
         return 0
      elif opponentChoice == 'B':
         return 6
      elif opponentChoice == "C":
         return 3

def findPlayerShape(opponentChoice, roundCondition):
   # Opponent chooses rock
   if opponentChoice == 'A':
      if roundCondition == 'X':
         # Here we return scisccors because we need to lose
         return 'Z'
      elif roundCondition == 'Y':
         return 'X'
      elif roundCondition == 'Z':
         return 'Y'
   # Opponent chooses paper
   elif opponentChoice == 'B':
      # Lose
      if roundCondition == 'X':
         return 'X'
      # Tie
      elif roundCondition == 'Y':
         return 'Y'
      # Win
      elif roundCondition == 'Z':
         return 'Z'
   # Opponent chooses scissors
   elif opponentChoice == 'C':
      # Lose
      if roundCondition == 'X':
         return 'Y'
      # Tie
      elif roundCondition == 'Y':
         return 'Z'
      # Win
      elif roundCondition == 'Z':
         return 'X'

if __name__ == "__main__":
    main()
