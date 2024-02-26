#Module 4-Lab 4
#Sarah Sung
#2/26/24
#Calculates company and employee bonuses

#declare local variables

#monthly sales amount
monthlySales = 0

#store bonus amount
storeAmount = 0

#employee bonus amount
empAmount = 0

#percent of sales increase
salesIncrease = 0

#prompt will be a string literal
prompt = 'Enter monthly sales amount: '

#this code gets the monthly sales
monthlySales = float(input(prompt))

#this code determines the storeAmount bonus
if monthlySales >= 110000:
  storeAmount = 6000
elif monthlySales >= 100000:
  storeAmount = 5000
elif monthlySales >= 90000:
  storeAmount = 4000
elif monthlySales >= 80000:
  storeAmount = 3000
else:
  storeAmount = 0

#this code gets the percent of increase in sales
salesIncrease = float(input('Enter sales increase: ')
salesIncrease = salesIncrease / 100

#this code determines the empAmount bonus
if salesIncrease >= .05:
  empAmount = 75
elif salesIncrease >= .04:
  empAmount = 50
elif salesIncrease >= .03:
  empAmount = 40
else:
  empAmount = 0

#this code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000) and (empAmount == 75):
  print("Congrats! You have reached the highest bonus amounts possible!")
