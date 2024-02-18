print ("Welcome to My Coffee and Muffin Shop")

name = input("What is your name? ")

print("Hello " + name + ", thank you for coming in today! Here is our menu.\n")

menu = {"Coffee": 5.00,
        "Muffin": 4.00}

print("------ MENU ------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------\n")

print("Are you ready to order?")

input()

print("How many coffee(s) would you like?")

input1 = int(input('quantity: '))

print("How many muffin(s) would you like?")

input2 = int(input('quantity: '))

print("Sounds good, we will have your order ready for you soon.\n\n")

print("My Coffee and Muffin Shop Receipt")
print("1 Coffee(s) at $5 each: $5.00\n",
       "2 Muffin(s) at $4 each: $8.00\n",
       "6% tax: $.78\n",
      "------\n",
      "Total: $13.78\n")
print("*********************************")
