# Sarah Sung
# 3/15/24
# Counts number of bottles collected
# Lab 5 The Bottle Return Program

# Declare variables
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = "y"

# Loop to run program again
while keepGoing == "y":
    for counter in range(7):
        counter += 1
        todayBottles = int(input(f'Enter number of bottles for day #{counter}: '))
        totalBottles += todayBottles
        totalPayout = totalBottles * 0.10

# Code to print final results
print(f'The total number of bottles collected is: {totalBottles:.2f}')
print(f'The total paid out is: $ {totalPayout:.2f}')

# Reset variables
counter = 1
totalBottles = 0
totalPayout = 0

# Ask user for more data
keepGoing = input('Do you want to enter another week worth of data?" (Enter y or n): ')