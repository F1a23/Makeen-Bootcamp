print("----------------------------------------------------------")
print("------Q1-----")

name = input("Enter your name:")
age=int(input("Enter your age :"))
print("Hello", name + ", you are", age, "years old.")

print("----------------------------------------------------------")
print("--Q2---")
number1 = int(input(" Enter first number: "))
number2=int(input(" Enter second number : "))
result=number1+number2
print(" The sum is",result)

print("----------------------------------------------------------")
print("----Q3----")

number1 = int(input(" Enter first number:"))
number2=int(input(" Enter second number :"))
comper=number1>number2
print(" Is the first number greater?",comper)

print("----------------------------------------------------------")
print("----Q4----")

age=int(input(" Enter your age:  "))
nationality=input("Enter your nationality:  ")

if age>=18 and nationality=="Omani":
    print(" You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
print("----------------------------------------------------------")
print("----Q5----")

num = int(input("Enter number: "))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

print("----------------------------------------------------------")
print("----Q6----")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print("----------------------------------------------------------")
print("----Q7----")
marks=int(input("Enter marks:"))
if marks >=90:
    print("Excellent")
elif 70<=marks<90:
     print("Good")
elif 50<=marks<70:
     print("Pass")
else:
    print("Fail")

print("----------------------------------------------------------")
print("-----Q8----")

age = int(input("Enter your age: "))
driving_license = input("Do you have a driving license? (yes/no): ").strip().lower()

if age >= 18:
    if driving_license == "yes":
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
    print("You are too young to drive.")

print("----------------------------------------------------------")
print("----Q9--")

num=1
while num <=5:
      print(num)
      num=num+1

print("----------------------------------------------------------")
print("----Q10--")

num = int(input("Enter number: "))
count = 2
while count <= num:
    print(count)
    count += 2