#CIS129_SarahSung_Lab12.py
#Sarah Sung
#May 15, 2024
#This program defines a class named Pet with methods that store and return values indicating the name, type, and age of the pet.

def main():
    inputName = input("Enter your pet's name:\n")
    inputType = input("Enter your pet's type:\n")
    inputAge = input("Enter your pet's age:\n")

    Animal = Pet()
    
    Animal.setName(inputName)
    Animal.setType(inputType)
    Animal.setAge(inputAge)

    print("Your pet's name is", Animal.getName())
    print("Your pet's type is", Animal.getType())
    print("Your pet's age is", Animal.getAge())

class Pet:

    def __init__(self, n="", t="", a=0):

        self.name = n
        self.type = t
        self.age = a

    def setName(self, n):

        self.name = n

    def setType(self, t):

        self.type = t

    def setAge(self, a):

        self.age = a

    def getName(self):

        return self.name

    def getType(self):

        return self.type

    def getAge(self):

        return self.age
    
if __name__ == "__main__":
    main()