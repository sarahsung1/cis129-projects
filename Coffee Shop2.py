print("Welcome to My Coffee and Muffin Shop!")

name = input("What is your name? ")
print("Hello " + name + ", thank you for coming in today! Here is our menu.\n")

menu = {"Coffee": 5.00,
        "Muffin": 4.00,
        "Cupcake": 6.00,
        "Cookie": 3.00}

print("------ MENU ------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------\n")

print("Are you ready to order?")
input()

#Variables
number0fCoffeesPurchased = 0
number0fMuffinsPurchased = 0
number0fCupcakesPurchased = 0
number0fCookiesPurchased = 0
price0fcoffee = 5.0
price0fmuffin = 4.0
price0fcupcake = 6.0
price0fcookie = 3.0
taxRate = 0.06

#Input
number0fCoffeesPurchased = int(input("How many coffees would you like?: "))
number0fMuffinsPurchased = int(input("How many muffins would you like?: "))
number0fCupcakesPurchased = int(input("How many cupcakes would you like?: "))
number0fCookiesPurchased = int(input("How many cookies would you like?: "))

print("\nSounds good, we will have your order ready soon.\n\n")

#Total
total_Coffee_Cost = number0fCoffeesPurchased * price0fcoffee
total_Muffin_Cost = number0fMuffinsPurchased * price0fmuffin
total_Cupcake_Cost = number0fCupcakesPurchased * price0fcupcake
total_Cookie_Cost = number0fCookiesPurchased * price0fcookie

#Subtotal
subTotal = number0fCoffeesPurchased * price0fcoffee + number0fMuffinsPurchased * price0fmuffin + number0fCupcakesPurchased * price0fcupcake + number0fCookiesPurchased * price0fcookie

#Tax
taxCost = subTotal * taxRate

#Total Cost
totalCost = subTotal + taxCost

#Receipt
print("********************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{number0fCoffeesPurchased} coffees at $5 each: ${total_Coffee_Cost}")
print(f"{number0fMuffinsPurchased} muffins at $4 each: ${total_Muffin_Cost}")
print(f"{number0fCupcakesPurchased} cupcakes at $6 each: ${total_Cupcake_Cost}")
print(f"{number0fCookiesPurchased} cookies at $3 each: ${total_Cookie_Cost}")
print(f"Subtotal: ${subTotal}")
print(f"Tax: ${taxCost}")
print("------")
print(f"Total: ${totalCost}")
print("*********************************")
print("Thank you for ordering, come back soon!")


