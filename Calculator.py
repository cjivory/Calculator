from math import sqrt
#Calculator program in python

#addition function
def add(x, y):
    return x +y 

#subtraction function
def subtract(x, y):
    return x - y

#multiplication function
def multiply(x, y):
    return x * y 

#division function
def divide(x, y):
    return x / y

#Square root function
def sqroot(x):
    return sqrt(x)

print("Select an operation.")
print("1.Add")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Square Root")

while True:
    #Get user input
    operationchoice = input("Enter operation(1,2,3,4,5)")

    #Loop to check if the choice is one of the operations
    if operationchoice in ('1','2','3','4','5'):
        firstnumber = float(int(input("Enter first number: ")))
        secondnumber = float(int(input("Enter second number: ")))

        if operationchoice == '1': 
            print(firstnumber, "+", secondnumber, "=", add(firstnumber, secondnumber))
        elif operationchoice == '2': 
            print(firstnumber, "-", secondnumber, "=", subtract(firstnumber, secondnumber))
        elif operationchoice == '3': 
            print(firstnumber, "*", secondnumber, "=", multiply(firstnumber, secondnumber))
        elif operationchoice == '4': 
            print(firstnumber, "/", secondnumber, "=", divide(firstnumber, secondnumber))
        elif operationchoice == '5': 
            print("Square root of", firstnumber, "is", "=", sqroot(firstnumber))

        #Checking to see if the user wants to do another calculation 
        nextcalc = input("Do you wish to do another calculation? (yes/no)")
        if nextcalc == "no":
            break
    else:
        print("Please enter a valid input.")