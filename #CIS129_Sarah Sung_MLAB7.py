#CIS129_Sarah Sung_MLAB7

#main
def main():
    
    #constants for price in seating section
    seat_cost_A = 20
    seat_cost_B = 15
    seat_cost_C = 10
    
    #constants for max number of seats
    seat_max_A = 300
    seat_max_B = 500
    seat_max_C = 200
    
    #constants for min number of seats
    seat_min_ABC = 0
    
    #initialize varibles
    validA = 0
    validB = 0
    validC = 0
    
    #totalincome
    totalIncome = 0
    
#welcome message
    print("Welcome to the theater!")

    name = input("What is your name? ")
    print("Hello " + name + ", thank you for coming in!\n")

    #section A ticket number
    while validA == 0:
        try:
            ticketsSoldA = int(input('Enter number of Section A seating tickets sold: '))
            if (ticketsSoldA < seat_min_ABC) or (ticketsSoldA > seat_max_A):
                print("Error in entry for Section A seating")
            else:
                validA = 1
        except ValueError:
            print("Valid in entry for Section A seating")

    #section B ticket number
    while validB == 0:
        try:
            ticketsSoldB = int(input('Enter number of Section B seating tickets sold: '))
            if (ticketsSoldB < seat_min_ABC) or (ticketsSoldA > seat_max_A):
                print("Error in entry for Section B seating") 
            else:
                validB = 1
        except ValueError:
            print("Valid in entry for Section B seating")
    
    #section C ticket number
    while validC == 0:
        try:
            ticketsSoldC = int(input('Enter number of Section B seating tickets sold: '))
            if (ticketsSoldC < seat_min_ABC) or (ticketsSoldA > seat_max_A):
                print("Error in entry for Section C seating")
            else:
                validC = 1
        except ValueError:
            print("Valid in entry for Section B seating")
    
    #calculate total
    totalIncome = (seat_cost_A * ticketsSoldA) + (seat_cost_B * ticketsSoldB) + (seat_cost_C * ticketsSoldC)
    print("The total income of ticket sales is ${value:.2f}".format(totalIncome))

#loop
while endProgram == 'yes':
    #call main
    main()
    #ask user if they want to end program
    endProgram = input("Do you want to end the program? (yes/no): ")