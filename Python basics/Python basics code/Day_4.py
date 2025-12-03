# ======================================================================
# Q1 — Basic Input/Output
# Question: Ask for name and age, then print a greeting with both.
# المطلوب: قراءة الاسم والعمر وطباعة رسالة ترحيب.
# ======================================================================
print("------Q1-----")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old.")


# ======================================================================
# Q2 — Sum of Two Numbers
# Question: Read two integers and print their sum.
# المطلوب: إدخال عددين صحيحين وطباعـة مجموعهما.
# ======================================================================
print("--Q2---")
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
sumv = number1 + number2
print("The sum is", sumv)


# ======================================================================
# Q3 — Compare Two Numbers
# Question: Read two integers and print whether the first is greater.
# المطلوب: مقارنة عددين وطباعة هل الأول أكبر.
# ======================================================================
print("----Q3----")
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
is_greater = number1 > number2
print("Is the first number greater?", is_greater)


# ======================================================================
# Q4 — Voting Eligibility
# Question: Read age and nationality, and check if eligible to vote.
# Rule: age >= 18 AND nationality == "Omani".
# المطلوب: التحقق من الأهلية للتصويت حسب الشرطين.
# ======================================================================
print("----Q4----")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")

if age >= 18 and nationality == "Omani":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# ======================================================================
# Q5 — Positive or Negative
# Question: Read an integer, tell if it’s positive or negative (and print the boolean check).
# المطلوب: تحديد إذا الرقم موجب أو سالب (وطباعة نتيجة الشرط).
# ملاحظة: أضفت حالة الصفر لزيادة الوضوح.
# ======================================================================
print("----Q5----")
num = int(input("Enter number: "))
positive = num > 0
print(positive)
if num > 0:
    print("number is positive")
elif num < 0:
    print("number is negative")
else:
    print("number is zero")


# ======================================================================
# Q6 — Even or Odd
# Question: Read an integer and print whether it’s even or odd.
# المطلوب: تحديد زوجي/فردي.
# ======================================================================
print("----Q6----")
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# ======================================================================
# Q7 — Grade Classification
# Question: Read marks and print the grade band:
#   >= 90: Excellent | 70–89: Good | 50–69: Pass | else: Fail
# المطلوب: تصنيف الدرجة.
# ======================================================================
print("----Q7----")
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Excellent")
elif 70 <= marks < 90:
    print("Good")
elif 50 <= marks < 70:
    print("Pass")
else:
    print("Fail")


# ======================================================================
# Q8 — Driving Eligibility
# Question: Read age and if the user has a driving license ("yes"),
# then decide if they can drive (age >= 18 and license == yes).
# المطلوب: التحقق من أهلية القيادة.
# ======================================================================
print("-----Q8----")
age = int(input("Enter your age: "))
driving_license = input("Do you have a driving license? (yes/no): ")
if age >= 18 and driving_license == "yes":
    print("You can drive.")
else:
    print("You need a license to drive.")


# ======================================================================
# Q9 — While Loop 1..5
# Question: Print numbers from 1 to 5 using a while loop.
# المطلوب: طباعة الأعداد من 1 إلى 5 بحلقة while.
# ======================================================================
print("----Q9--")
num = 1
while num <= 5:
    print(num)
    num = num + 1


# ======================================================================
# Q10 — Print Even Numbers up to N
# Question: Read N and print all even numbers from 0 to N inclusive.
# المطلوب: طباعة كل الأعداد الزوجية حتى N.
# ======================================================================
print("----Q10--")
num = int(input("Enter number: "))
count = 0
while count <= num:
    if count % 2 == 0:
        print(count)
    count = count + 1
