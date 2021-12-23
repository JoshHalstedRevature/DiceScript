#probably has to do with the function, maybe just fixing the return for it or something 

#pog

import random
import logging
#import os

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def printDice(num):
  """Working on this (Displays every pip as of now)..."""
  halfNum = int(num/2)
  print(f"%s"%"_ "*(num))
  for n in range(0, halfNum, 1):
    print("| ", "• "*halfNum, "|")
  print("¯ "*num)


def MaxChoice():
  """Will decide the ..."""
  curious = input("What dice size would you like? (6/8/10/12/20/100): ")
  curious = int(curious)
  Sides = 0
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
  elif curious == 100:
    Sides = 100
  printDice(Sides) # Testing
  return Sides

DiceCheck = "yes"
NumSides = 20
if DiceCheck == "yes" or DiceCheck == "y" or DiceCheck == "Yes" or DiceCheck == "Y":
  NumSides = MaxChoice()
check = "yes"

while check == "yes" or check == "y" or check == "Yes" or check == "Y":
    print("Rolling the dice...")
    print("The values are....")
    print(round(random.random()*NumSides + 1))
    print(round(random.random()*NumSides + 1))
    

    check = input("Roll the dice again?:")
    if check == "yes" or check == "y" or check == "Yes" or check == "Y":
      DiceCheck = input("Would you like to select different dice?:")
      if DiceCheck == "yes" or DiceCheck == "y" or DiceCheck == "Yes" or DiceCheck == "Y":
        NumSides = MaxChoice()


def main():
  pass
        
if __name__ == "__main__":
  main()