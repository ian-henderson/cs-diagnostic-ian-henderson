# Problem 18: Rolling the Dice

from random import randint
import sys

def roll_die(sides=6):
    return randint(0, sides)

if len(sys.argv) == 2:
    print(roll_die(int(sys.argv[1])))
else:
    print(roll_die())
