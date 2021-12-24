import random
import logging

logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
logging.info("Logging activity for DiceRoll...")

def getSidesInt():
    tries = 0
    logging.info("Requesting input for # of sides per die")
    while tries < 3:
        curious = input("We're rolling two dice.\nWhat size would you like? (no. of sides): ")
        try:
            int(curious)
        except ValueError:
            tries += 1
            logging.error(f"Invalid input = {curious}; attempts: {tries}/3")
            print(f"Input invalid (attempts: {tries}/3)")
        else:
            logging.info(f"Valid input = {curious}")
            print(f"Okay, we're rolling two d{curious}s")
            return int(curious)

def rollDice(NumSides):
    try:
        dieA = round(random.random()*NumSides + 1)
        dieB = round(random.random()*NumSides + 1)
        #logging.debug(f"dieA * 5 = {dieA * 5}")
    except TypeError:
        logging.error(f"NumSides is not a number: NumSides = {NumSides}")
    else:
        logging.info("Rolling dice...")
        print(f"The values are...\n{dieA}\n{dieB}")

check = "yes"
diceCheck = "yes"  
numSides = getSidesInt()
while check == "yes" or check == "y" or check == "Yes" or check == "Y":
    rollDice(numSides)
    check = input("Roll the dice again?:")
    if check == "yes" or check == "y" or check == "Yes" or check == "Y":
        logging.info("User chose to reroll")
        diceCheck = input("Would you like to select different dice?:")
        if diceCheck == "yes" or diceCheck == "y" or diceCheck == "Yes" or diceCheck == "Y":
            logging.info("User wants new dice")
            numSides = getSidesInt()
    else:
        logging.info("User chose not to reroll")