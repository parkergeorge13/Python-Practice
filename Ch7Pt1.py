# Parker George
# IS 403 Section 4
# Chapter 7 Homework Part 1

# Write a program that prompts the user to enter the maximum number used in generating a random number. Then generate the random number. 
# Start the timer as the user tries to guess the number. Display whether the guess is "Too High" or "Too Low". 
# Once the number is guessed, display how many seconds it took to guess the number.

# Clear Console
import os
def clear_console():
    os.system('cls')
clear_console()

# Library imports
import random
from datetime import datetime
# Initial user input
iRanNumInput = int(input("Enter the maximum number for your random number generator: "))

# Start program for guesses with a timer
iRandom = random.randrange(1, iRanNumInput)
print(f"Your timer has started. Guess what the random number is between 1 and {iRanNumInput}!")
dBegin = datetime.now()

# Do while loop to retreive all guesses
iCount = 1
iGuess = int(input(f"Enter guess #{iCount}: "))
while iRandom != iGuess:
    iCount = iCount + 1
    if iGuess > iRandom:
        print("Too High!")
    else:
        print("Too Low!")
    iGuess = int(input(f"Enter guess #{iCount}: "))

# Ending output
dEnd = datetime.now()
dResult = dEnd - dBegin
print(f"Correct! It took you {dResult.seconds} seconds to find the random number!")