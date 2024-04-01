#CIS129_Sarah Sung_Lab6.py

import math

def main():
    #Declare variables
    total = getTotalHotDogs()

    #Hot dogs in package
    hotDogs = 10
    #Hot dog buns in package
    hotDogBuns = 8

    #Leftover hot dogs
    dogsLeft = 0
    #Leftover buns
    bunsLeft = 0

    #Calculate the number of leftover hotdogs
    dogsLeft = (hotDogs - total % hotDogs) % hotDogs

    #Calculate the min number of packages of hot dogs
    minDogs = math.ceil(total / hotDogs)

    #Calculate the number of leftover hot dog buns
    bunsLeft = (hotDogBuns - total % hotDogBuns) % hotDogBuns

    #Calculate the min number of packages of hot dogs buns
    minBuns = math.ceil(total / hotDogBuns)

    #Display results
    showResults(dogsLeft, minDogs, bunsLeft, minBuns)

def getTotalHotDogs():
    #Find out number of people attending the cookout
    people = int(input("Enter the number of people attending the cookout: "))

    #Get the number of hot dogs for each person
    hotDogs = int(input("Enter the number of hot dogs for each person: "))

    #Calculate the total number of hot dogs that need to be purchased
    total = people * hotDogs
    return total

def showResults(dogsLeft, minDogs, bunsLeft, minBuns):
    #Display the min packages of hot dogs needed
    print("Minimum number of packages of hot dogs required:", minDogs)

    #Display the min packages of hot dog buns needed
    print("Minimum number of packages of hot dog buns required:", minBuns)

    #Display how many hot dogs are left over
    print("Hot dogs left over:", dogsLeft)

    #Display how many hot dog buns are left over
    print("Hot dog buns left over:", bunsLeft)

if __name__=="__main__":
    main()