import random
import logging
import os
#import unittest

os.system('cls' if os.name == 'nt' else 'clear')

# style notes: indents are standard 4 spaces (PEP8)
#   except for hanging indents for lists, etc,
#   which are 2 spaces

logging.basicConfig(
  filename='app.log', 
  filemode='w', 
  level=logging.DEBUG, 
  format='%(asctime)s %(levelname)s: %(message)s', 
  datefmt='%m/%d/%Y %I:%M:%S')
logging.info("Logging activity for DiceRoll...")

def getSidesInt():
    tries = 0
    logging.info("Requesting input for # of sides per die")
    while tries < 3:
        curious = input("We're rolling two dice.\nWhat size would you like? (no. of sides): ")
        try:
            int(curious)
            logging.info("Valid input = %s", curious)
            print(f"Okay, we're rolling two d{curious}s")
            if(int(curious) <= 100 and int(curious) > 1):
              return int(curious)
            else:
              print("Invalid size. Default size (6) is being used. ")
              return 6
        except ValueError:
            tries += 1
            logging.error("Invalid input = %s; attempts: %s/3", curious, tries)
            print(f"Input invalid (attempts: {tries}/3)")
        if(tries == 3):
            print("Three invalid entries. The default size (6) is being used.")
            return 6

def rollDice(NumSides):
    try:
        dieA = round(random.random()*NumSides + 1)
        dieB = round(random.random()*NumSides + 1)
        logging.info("Rolling dice...")
        print(f"The values are...\n{dieA}\n{dieB}")
    except TypeError:
        logging.error("NumSides is not a number: NumSides = %s", NumSides)

class main():
    check = "yes"
    diceCheck = "yes"  
    numSides = getSidesInt()
    while check in ('yes', 'y', 'Yes', 'Y'):
        if numSides:
            rollDice(numSides)
            check = input("Roll the dice again?:")
            if check in ('yes', 'y', 'Yes', 'Y'):
                logging.info("User chose to reroll")
                diceCheck = input("Would you like to select different dice? ")
                if diceCheck in ('yes', 'y', 'Yes', 'Y'):
                    logging.info("User wants new dice")
                    numSides = getSidesInt()
            else:
                logging.info("User chose not to reroll")
        else:
            check = "no"

if __name__ == '__main__':
    main()
    #unittest.main()