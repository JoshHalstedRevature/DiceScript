#probably has to do with the function, maybe just fixing the return for it or something 

#max is a keyword, so I changed it to Sides. So is min, so it was removed.
#pog

import random
import logging
import os

def printDice(num):
  print("-----------")


def MaxChoice():
  """Will decide the ..."""
  curious = input("What dice size would you like? (6/8/10/12/20/100)")
  if curious == 6:
    Sides = 6
  elif curious == 8:
    Sides = 8
  elif curious == 10:
    Sides = 10 
  elif curious == 12:
    Sides = 12 
  elif curious == 20:
    Sides = 20
  else:
    Sides = 100
  return Sides

DiceCheck = "yes"
numSides = 0
if DiceCheck == "yes" or DiceCheck == "y" or DiceCheck == "Yes" or DiceCheck == "Y":
  NumSides = MaxChoice()

check = "yes"

# Are the results supposed to be 86 and 35?

while check == "yes" or check == "y" or check == "Yes" or check == "Y":
    print("Rolling the dices...")
    print("The values are....")
    print(round(random.random()*numSides + 1))
    print(round(random.random()*numSides + 1))
    

    check = input("Roll the dices again?:")
    if check == "yes" or check == "y" or check == "Yes" or check == "Y":
      DiceCheck = input("Would you like to select different dice?:")
      if DiceCheck == "yes" or DiceCheck == "y" or DiceCheck == "Yes" or DiceCheck == "Y":
        NumSides = MaxChoice()


def main():
  pass
        
if __name__ == "__main__":
  main()