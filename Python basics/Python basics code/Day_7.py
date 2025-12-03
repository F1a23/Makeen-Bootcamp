# ======================================================================
# Boolean Logic, While Loops, and Calculator Practice
# ======================================================================

# ----------------------------------------------------------------------
# Example 1 — Boolean basics and equality operators
# ----------------------------------------------------------------------
flag = False
age = 20
print(age == 2)
print(age != 2)

if age == 20:
    print("flag is True")
else:
    print("flag is False")

flag = False
grade = 90
flag = 90 <= grade <= 100
if flag:
    print("you are excellent")
else:
    print("you did good")

f = True == 1
print(f)

f = False == 0
print(f)

# ----------------------------------------------------------------------
# Example 2 — Check if a number is positive
# ----------------------------------------------------------------------
number = int(input("Enter number: "))
is_positive = number >= 0
print(is_positive)
if is_positive:
    print("number is positive")
else:
    print("number is negative")

# ----------------------------------------------------------------------
# Example 3 — Temperature check (liquid range)
# ----------------------------------------------------------------------
temp = float(input("Enter temperature: "))
if temp > 0 and temp < 100:
    print("Liquid")
elif temp <= 0 or temp >= 100:
    print("Not Liquid")

# ----------------------------------------------------------------------
# Example 4 — While loop printing
# ----------------------------------------------------------------------
counter = 1
while counter < 10:
    counter = counter + 1
    print("Hi")

# ----------------------------------------------------------------------
# Example 5 — Compound interest while loop
# ----------------------------------------------------------------------
rate = 0.05
target = 20000
balance = 10000
year = 0
while balance < target:
    year = year + 1
    interest = balance * rate
    balance = balance + interest
print("Investment reached target after", year, "years")

# ----------------------------------------------------------------------
# Example 6 — While loop example with break condition
# ----------------------------------------------------------------------
i = 0
total = 0
while total >= 0:
    i = i + 1
    total = total + i
print(i, total)

# ----------------------------------------------------------------------
# Example 7 — Calculate average salary
# ----------------------------------------------------------------------
salary = 0.0
total = 0.0
count = 0.0
while salary >= 0:
    salary = float(input("Enter a salary or -1 to finish: "))
    if salary >= 0.0:
        total = total + salary
        count = count + 1
avg = total / count
print("Average salary is:", avg)

# ----------------------------------------------------------------------
# Q0 — Loop-based Calculator
# ----------------------------------------------------------------------
print("------------------------Q0------------------")
print("Modify the calculator to loop until user decides to exit.")
print("Answer:")

while True:
    a = input("Type 'exit' to end or press Enter to continue: ")
    if a.lower() == "exit":
        print("Exiting calculator...")
        break

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Addition result:", num1 + num2)
    elif operator == "-":
        print("Subtraction result:", num1 - num2)
    elif operator == "*":
        print("Multiplication result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Division result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero")
    else:
        print("Invalid operator!")
print("-------------------------------------------------------------")

# ----------------------------------------------------------------------
# Q1 — Sum of digits in a number
# ----------------------------------------------------------------------
print("------------------------Q1------------------")
print("Write a program that takes a number as input and finds the sum of its digits.")
num = input("Enter a number: ")
i = 0
total = 0
while i < len(num):
    total = total + int(num[i])
    i = i + 1
print("The sum of digits is:", total)

# ----------------------------------------------------------------------
# Q2 — Username and Password check using Boolean operators
# ----------------------------------------------------------------------
print("-------------------------------------------------------------")
print("Boolean operators practice: username and password check")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Access granted")
else:
    print("Access denied")

# ----------------------------------------------------------------------
# Q3 — Divisible by 3 or 5
# ----------------------------------------------------------------------
print("------------------------Q3------------------")
print("Write a program that checks if the number is divisible by 3 or 5.")
number = int(input("Enter a number: "))
if number % 3 == 0 or number % 5 == 0:
    print("The number is divisible by 3 or 5")
else:
    print("The number is not divisible by 3 or 5")
