# Parker George
# IS 403 Section 4
# Chapter 7 Homework Part 1

# Write a program that will continue to generate two random numbers until they are not equal. Then display the two numbers.

# Clear Console
import os
def clear_console():
    os.system('cls')
clear_console()

import random
iRanNumInput = int(input("Enter the maximum number for your random number generator: "))

iRnd1 = 0
iRnd2 = 0
iCount = 0

while iRnd1 == iRnd2:
    iRnd1 = random.randrange(0, iRanNumInput)
    iRnd2 = random.randrange(0, iRanNumInput)
    iCount = iCount + 1

print(f"It took {iCount} tries")