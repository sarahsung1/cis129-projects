# CIS129_Sarah Sung_Lab 7
# Sarah Sung
# 3/31/2024
# Lab 7-3 The Dice Game

#add libraries needed
import random

#the main function
def main():
    print()

    #initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'

    #call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    #while loop to run program again
    while endProgram == 'no':

        #populate variables
        winnerName = 'NO NAME'
        p1number = 0
        p2number = 0

        #call to rollDice
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)

        #call to display info
        displayInfo(winnerName)
        endProgram = input('Do you want to end program? (yes/no): ')

#this function gets the players names
def inputNames(playerOne, playerTwo):
    playerOne = input("Player One's name: ")
    playerTwo = input("Player Two's name: ")
    return playerOne, playerTwo

#this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    if p1number == p2number:
        winnerName = "TIE"
    elif p1number > p2number:
        winnerName = playerOne
    elif p1number < p2number:
        winnerName = playerTwo
    return winnerName

#this function displays the winner
def displayInfo(winnerName):
    print(winnerName, "wins")

#calls main
main()