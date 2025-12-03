
# ===============================
# 1) Strings & Basic Operations
# ===============================

# 1.1 Count length and concatenate number as text
word = "Hi I am Fatima #"
count = 5
word_length = len(word)
change_count_type = str(count)
print(word_length)               # prints length of word
print(word + change_count_type)  # concatenates string + "5"
#--------------------------------------------------------------------------------------------------
# 1.2 Indexing strings and lists
name = "fatima"
numbers = [1, 2, 3, 4]
n = len(name)
print(name[n-1])                 # last char via len-1
print(name[2], name[3], name[4]) # 't', 'i', 'm'
print(numbers[2], numbers[3])    # 3, 4
#----------------------------------------------------------------------------------------------------
# 1.3 String building + casting
string = "Py"
age = 20
string = string + "thon"         # "Python"
print(string, "hi", age)         # space-separated print
print(string + "hi" + str(age))  # full concatenation
#--------------------------------------------------------------------------------------------------------
# 1.4 Escape sequences
print("Hi//world \n")           # prints literal backslash-n
print("F")


# ===============================
# 2) Input, Arithmetic, Comparisons
# ===============================

# 2.1 Simple multiply of two inputs
# (Uncomment to run interactively)
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = x * y
print(z)
#---------------------------------------------------------------------------------------------
# 2.2 Hello message
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old.")
#-----------------------------------------------------------------------------------------------
# 2.3 Sum two ints
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
sumv = number1 + number2
print("The sum is", sumv)
#--------------------------------------------------------------------------------------------------
# 2.4 Compare two numbers
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print("Is the first number greater?", number1 > number2)
#-----------------------------------------------------------------------------------------
# 2.5 Voting eligibility
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")
if age >= 18 and nationality.lower() == "omani":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#--------------------------------------------------------------------------------------
# 2.6 Positive/Negative check
num = int(input("Enter number: "))
if num > 0:
    print("number is positive")
else:
    print("number is negative")
#_------------------------------------------------------------------------------------------
# 2.7 Even/Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
#_----------------------------------------------------------------------------------------------------
# 2.8 Grade to text
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Excellent")
elif 70 <= marks < 90:
    print("Good")
elif 50 <= marks < 70:
    print("Pass")
else:
    print("Fail")
#------------------------------------------------------------------------------------------------------
# 2.9 Driving
age = int(input("Enter your age: "))
driving_license = input("Do you have a driving license? (yes/no): ")
if age >= 18 and driving_license.lower() == "yes":
    print("You can drive.")
else:
    print("You need a license to drive.")


# ===============================
# 3) while Loops
# ===============================

# 3.1 Count 1..5
num = 1
while num <= 5:
    print(num)
    num = num + 1
#----------------------------------------------------------
# 3.2 Print all even numbers up to n
n = int(input("Enter number: "))
count = 0
while count <= n:
    if count % 2 == 0:
        print(count)
        count += 1
#----------------------------------------------------------
# 3.3 Average salary until -1 sentinel
def average_salary():
    total = 0.0
    count = 0
    while True:
        s = float(input("Enter a salary or -1 to finish: "))
        if s < 0:
            break
        total += s
        count += 1
    if count == 0:
        print("No data.")
    else:
        print("Average salary is:", total / count)
#----------------------------------------------------------
# 3.4 Sum of digits of a given number string
def sum_of_digits():
    num = input("Enter a number: ")
    total = 0
    i = 0
    while i < len(num):
        total += int(num[i])
        i += 1
    print("The sum of digits is:", total)


# ===============================
# 4) Time Comparison
# ===============================

def compare_times_strptime():
    import time
    t1 = input("Enter first time (HH:MM): ")
    t2 = input("Enter second time (HH:MM): ")
    time1 = time.strptime(t1, "%H:%M")
    time2 = time.strptime(t2, "%H:%M")
    if time1 < time2:
        print("Time 1 comes before Time 2")
    elif time1 > time2:
        print("Time 2 comes before Time 1")
    else:
        print("Both times are the same")
#----------------------------------------------------------
def compare_times_manual():
    # Format: HH:MM:SS
    time1 = input("Enter first time (HH:MM:SS): ")
    time2 = input("Enter second time (HH:MM:SS): ")

    h1, m1, s1 = time1.split(":")
    h2, m2, s2 = time2.split(":")  # fixed bug: originally split from time1

    # cast to int
    h1, m1, s1 = int(h1), int(m1), int(s1)
    h2, m2, s2 = int(h2), int(m2), int(s2)

    if (h1, m1, s1) < (h2, m2, s2):
        print("Time 1 comes before Time 2")
    elif (h1, m1, s1) > (h2, m2, s2):
        print("Time 2 comes before Time 1")
    else:
        print("Both times are the same")


# ===============================
# 5) Boolean / Flags
# ===============================

def positive_flag():
    number = int(input("Enter number: "))
    is_positive = number >= 0
    print(is_positive)
    if is_positive:
        print("number is positive")
    else:
        print("number is negative")
#----------------------------------------------------------
def liquid_or_not():
    temp = float(input("Enter temp: "))
    if 0 < temp < 100:
        print("Liquid")
    else:
        print("Not Liquid")


# ===============================
# 6) for Loops & Patterns
# ===============================

# 6.1 Iterating text
for ch in "Ali":
    print(ch, end="")
print(" and my age is 20")
#----------------------------------------------------------
# 6.2 Powers table
for i in range(1, 5):
    for j in range(1, 5):
        print(i ** j)
    print()
#----------------------------------------------------------
# 6.3 Right triangle of stars
for i in range(4):
    # print leading spaces
    for _ in range(4 - i - 1):
        print(" ", end="")
    # print stars
    for _ in range(i + 1):
        print("*", end="")
    print()
#----------------------------------------------------------
# 6.4 Diamond-ish triangle up and down
for i in range(3):
    for _ in range(i + 1):
        print("*", end="")
    print()
for i in range(3, -1, -1):
    for _ in range(i + 1):
        print("*", end="")
    print()


# ===============================
# 7) Functions
# ===============================

def cube_volume(side_length: float) -> float:
    return side_length ** 3
#----------------------------------------------------------
def factorial_while(n: int) -> int:
    result = 1
    if n == 0:
        return 1
    while n >= 1:
        result *= n
        n -= 1
    return result
#----------------------------------------------------------
def factorial_for(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
#----------------------------------------------------------
# NOTE: The following version is WRONG because it ignores n
def factorial_wrong(n: int) -> int:
    result = 1
    for i in range(5, 1, -1):  # ignores n entirely
        result *= i
        return result


# ===============================
# 8) Globals (Bank example)
# ===============================

balance = 10000  # global

def withdraw(amount: float) -> None:
    global balance
    if balance >= amount:
        balance -= amount

def deposit(amount: float) -> None:
    global balance
    balance += amount

def check_balance() -> float:
    return balance

# Example:
withdraw(350)
deposit(500)
withdraw(200)
print("balance after operations =", check_balance())


# ===============================
# 9) Lists & Methods
# ===============================

trainees_in_ai = ["Azam", "Noor", "Muradi", "Muna"]
print(len(trainees_in_ai))

# iterate by value
for t in trainees_in_ai:
    print(t)

# iterate by index
for i in range(len(trainees_in_ai)):
    print(i, trainees_in_ai[i])

# largest in list
numbers = [19, 2, 3, 4, 5]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("The largest number is:", largest)

# smallest in list
numbers = [19, 2, -1, 4, 5]
small = numbers[0]
for n in numbers:
    if n < small:
        small = n
print("The smallest number is:", small)
#---------------------------------------------------------
# even/odd for each number
numbers = [3, 2, 5, 6]
for val in numbers:
    if val % 2 == 0:
        print("number", val, "is even")
    else:
        print("number", val, "is odd")
#-----------------------------------------------------
# push inputs into list with isdigit & negatives handling
def collect_numbers():
    result = []
    while True:
        new_no = input("You must enter a number or q to stop: ")
        if new_no == "q":
            break
        if new_no.lstrip("-").isdigit():
            result.append(int(new_no))
        else:
            print("Invalid input, skipping:", new_no)
    print("The list of numbers is:", result)
#------------------------------------------
# list insert, index, remove, pop
new_list = ["ali", 2, "noor"]
new_list.insert(2, "4")
print(new_list)

friends = ["Harry", "Bob", "Cari", "Emily"]
if "Emily" in friends:
    idx = friends.index("Emily")
    print(idx)
friends.remove("Emily")
print(friends)
friends.pop()  # removes last

friends = ["Harry", "Bob", "Cari", "Emily"]
friends.pop(2)  # removes index 2
print(friends)

# list concatenation and repetition
myFriends = ["Fritz", "Cindy"]
yourFriends = ["Lee", "Pat", "Phuong"]
ourFriends = myFriends + yourFriends
print(ourFriends)

monthInQuarter = [1, 2, 3] * 4
print(monthInQuarter)


# ===============================
# 10) Formatting & String Methods
# ===============================

price = 1.2199967
discount = 588
print("The price is %.4f" % (price))
print("The price is: %10.2f" % (price))
print("The price is%.4f And the discount is %d" % (price, discount))
print("The price is %.4f And the discount is %10d" % (price, discount))
print("The price is %.4f And the discount is %-10d" % (price, discount))

price2 = 3.989889
print("The price is %.4f" % (price2))
greet = "Hello"
greet2 = "Good morning"
num = 4
print("%-10s %10s" % (greet, greet2))
print("%%%20d" % (num))
print("%20d%%" % (num))

title = "Python For everyone python for everyone"
print(title.upper())
print(title.lower())
print('Python'.center(10, '-'))
print(title.title())
print(title.isidentifier())
print(title.replace("everyone", "program"))
print(title.replace("everyone", "program", 1))
print(title.find("y"))
print(title.find("y", 4, 18))
print(title.rfind("y"))
print(title.count("y"))
print(title.count("y", 4))


# ===============================
# 11) Simple Discount Example
# ===============================

def discount_example():
    price = float(input("Enter the price: "))
    if price > 200:
        d = price * 0.05
        final = price - d
        print("The price after discount is:", final)
        print("The discount is", d)
    else:
        print("The price without discount is", price)


# ===============================
# 12) Calculators
# ===============================

def calculator_print_all():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Addition (+): ", num1 + num2)
    print("Subtraction (-): ", num1 - num2)
    print("Multiplication (*): ", num1 * num2)
    print("Division (/): ", num1 / num2)
#-----------------------------------------
def calculator_choose_op():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero")
    else:
        print("Invalid operator")
#-----------------------------------------
def calculator_loop():
    while True:
        a = input("Type 'exit' to end or press Enter to continue: ")
        if a.lower() == "exit":
            print("Exiting calculator...")
            break
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        if operator == "+":
            print("Result:", num1 + num2)
        elif operator == "-":
            print("Result:", num1 - num2)
        elif operator == "*":
            print("Result:", num1 * num2)
        elif operator == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero")
        else:
            print("Invalid operator! Please use +, -, *, or /")
        print()  # spacing


# ===============================
# 13) Misc Math Examples
# ===============================

# rectangle area
w = 20
l = 50
area = w * l
print(area)

print("Hi\t" + "sahab")
print("My name is \t" + "sahab")
print(type(w))
print(type("sahab"))

x = 60
x2 = 99
x3 = 90
avg = (x + x2 + x3) / 3
print(avg)

canVolume = 20
canVolume = canVolume + 4
print(canVolume)  # updating the value

# Constants (by convention upper-case)
BOTTLE_VOLUME = 4.0
TEXT_RATE = 2
print(BOTTLE_VOLUME)

# Six-pack volume example
CAN_VOLUME = 0.355
BOTTLE_VOLUME = 2
cans_per_pack = 6
total_volume_cans = cans_per_pack * CAN_VOLUME
print("A six-pack of 12-ounce cans contains", total_volume_cans, "liters")
total_volume_all = total_volume_cans + BOTTLE_VOLUME
print("Total volume in the cans and 2 liter bottle", total_volume_all, "liters")

# Operator precedence
x = 2 + 2 ** 4
print(x)
b = 2 * 2 ** 4
print(b)
a = 2 + 10 / 2
print(a)

# Full name concat
firstName = "Sahab"
lastName = "Al-amri"
fullName = firstName + " " + lastName
print(fullName)

# Quadratic roots for a=b=c=1 (discriminant 1-4)
a = 1
b = 1
c = 1
x1 = (-b + (b**2 - 4*a*c) ** 0.5) / (2*a)
x2 = (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)
print(x1, x2)

# Floor division and modulo
print(5 // 2)
print(8 // 3)
print(10 // 3)
print(8 % 2)

# Rials/Baises converter (simple version)
def rials_baises():
    baises = int(input("Enter number of baises: "))
    riales = baises // 1000
    baises = baises % 1000
    print("rials =", riales, "\n", "baises =", baises)
