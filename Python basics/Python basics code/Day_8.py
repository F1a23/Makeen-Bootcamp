# ======================================================================
# While Loop Practice — Input Until Blank
# ======================================================================

# ----------------------------------------------------------------------
# Q1 — Sum of Numbers
# Question: Continuously ask the user to enter a value until they press Enter (blank line).
# Compute the total sum of all entered numbers.
# ----------------------------------------------------------------------
print("---------Q1-------")

total = 0.0
inputStr = input("Enter value: ")
while inputStr != "":
    value = float(inputStr)
    total = total + value
    inputStr = input("Enter value: ")
print("The total is:", total)


# ----------------------------------------------------------------------
# Q2 — Count Negative Numbers
# Question: Ask the user for numbers until they press Enter.
# Count how many of the entered numbers are negative.
# ----------------------------------------------------------------------
print("---------Q2-------")

count = 0
inputStr = input("Enter value: ")
while inputStr != "":
    value = int(inputStr)
    if value < 0:
        count = count + 1
    inputStr = input("Enter value: ")
print("The count of negative numbers is:", count)


# ----------------------------------------------------------------------
# Q3 — Find Maximum Number
# Question: Ask the user to enter numbers until a blank line.
# Find and display the largest number entered.
# ----------------------------------------------------------------------
print("---------Q3-------")

num = input("Enter value: ")
largest = int(num)

while num != "":
    num = input("Enter value: ")
    if num != "":
        if int(num) > largest:
            largest = int(num)
print("The largest number is:", largest)


# ----------------------------------------------------------------------
# Q4 — Find Minimum Number
# Question: Ask the user to enter numbers until a blank line.
# Find and display the smallest number entered.
# ----------------------------------------------------------------------
print("---------Q4-------")

num = input("Enter value: ")
smallest = int(num)

while num != "":
    num = input("Enter value: ")
    if num != "":
        if int(num) < smallest:
            smallest = int(num)
print("The smallest number is:", smallest)
