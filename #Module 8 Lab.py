#Module 8 Lab

def is_palindrome(string):
    string = string.lower()

    if string == string[::-1]:
        return True
    else:
        return False
    
string = str(input("Enter a word: "))

if is_palindrome(string) == True:
        print("Yes, it is palindrome")
else:
        print("No, is not palindrome")