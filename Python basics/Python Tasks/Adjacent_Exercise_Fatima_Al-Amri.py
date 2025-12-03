"""Write a Python program that repeatedly asks
the user to enter numbers and prints This number
is repeated!" when the user enters
the same number consecutively.
"""

numbers = input("Enter number: ")
previous = numbers

while numbers != "":
    numbers = input("Enter number: ") #new input
    if numbers == previous and numbers != "":
        print("This number is repeated!")
    previous = numbers