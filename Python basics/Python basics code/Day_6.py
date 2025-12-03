# ======================================================================
# This file covers:
# 1) if/elif/else patterns (خصومات/أدوار/مقارنات)
# 2) التعامل مع الأخطاء الشائعة (undefined vars / duplicated prints)
# 3) 
# ======================================================================

# ------------------ Example 1 ------------------
# Question: Read a price; if > 200 print 5% discount, else "no discount".
# Extra: If price <= 10, print "take it free".

price = float(input("Enter price: "))
if price > 200:
    discount = price * 0.05
    print(discount)
else:
    print("no discount")
    if price <= 10:
        print("take it free")
    else:
        print("no discount")
print("End")

print("------------------")

# ------------------ Example 2 ------------------
# Question: Why define discount before using it?
# Answer: لتفادي UnboundLocalError 
discount = 0  # initialize to avoid using undefined variable
price = float(input("Enter price: "))
if price > 200:
    discount = price * 0.05
print(discount)

print("------------------")

# ------------------ Example 3 ------------------
# Question: Map elevator floor to "actual floor" if 13 is skipped.

floor = int(input("Enter floor: "))
if floor > 13:
    actualFloor = floor - 1
else:
    actualFloor = floor
print("Actual Floor:", actualFloor)

print("------------------")

# ------------------ Example 4 ------------------
# Question: Use relational operator != to branch messages.

age = 20
compare = 20
if age != compare:
    print("you are senior")
else:
    print("you are still young")

print("------------------")

# ------------------ Example 5 ------------------
# Question: Case-insensitive username check.
# Fix: طبّق lowercase/uppercase على الطرفين بشكل متناسق.
name = "Ali".lower()
username = input("Enter username: ").lower()  # موحّد للحروف الصغيرة
print("you typed:", username)
if name == username:
    print("you can access")
else:
    print("you can't access")

print("------------------")

# ------------------ Example 6 ------------------
# Question: Compare two ages and print who is older.
myAge = 23
yourAge = int(input("Enter your Age: "))
if myAge > yourAge:
    print("I am older")
elif myAge < yourAge:
    print("you are older")
else:
    print("we are the same age")

print("------------------")

# ------------------ Example 7 ------------------
# Question: Check sqrt(2)^2 ≈ 2 within small error.
from math import sqrt
x = sqrt(2)
y = 2.0
error_rate = 0.00005
diff = x * x - y
if abs(diff) < error_rate:
    print("sqrt2 x sqrt2 equal. please proceed project")
else:
    print("you have error you cannot do this project")

print("------------------")

# ------------------ Example 8 ------------------
# Question: Is number positive/negative and divisible by 3?
x = int(input("Enter a number: "))
if x >= 0:
    print("The number is positive")
    if x % 3 == 0:
        print("and divisible by 3")
    else:
        print("but not divisible by 3")
else:
    print("The number is negative")
    if x % 3 == 0:
        print("and divisible by 3")
    else:
        print("but not divisible by 3")

print("------------------")

# ------------------ Example 9 ------------------
# Question: Is number positive/negative and even/odd?
x = int(input("Enter a number: "))
if x >= 0:
    print("The number is positive", end="")
else:
    print("The number is negative", end="")
if x % 2 == 0:
    print(", it is even")
else:
    print(", it is odd")

print("------------------")

# ------------------ Example 10 ------------------
# Question: Richter-like scale message using elif chain.

x = float(input("Enter number: "))
if x >= 8.0:
    print("Most structures fall")
elif x >= 7.0:
    print("Many buildings destroyed")
elif x >= 6.0:
    print("Many buildings damaged, some collapse")
elif x >= 4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No destruction of buildings")

print("------------------")

# ------------------ Example 11 (a) ------------------
# Question: Discount rules by age (رتّبنا الحالات لتكون واضحة وغير متداخلة).
age = int(input("Enter age: "))
if age == 25:
    print("free")
elif age > 20:
    print("you have discount 30%")
elif age == 20:
    print("you have discount 10%")
else:
    print("you dont have a discount")

print("----------------")

# ------------------ Example 11 (b) ------------------

age = int(input("Enter age: "))
if age == 25:
    print("free")
elif age > 20:
    print("you have discount 30%")
elif age == 20:
    print("you have discount 10%")
else:
    print("you dont have a discount")

print("#################################################")

# ------------------ Time Comparison — Solution 1 ------------------
# Question: Compare times HH:MM using time.strptime.
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

print("###################################################################")

# ------------------ Time Comparison — Solution 2 ------------------
# Question: Compare full times HH:MM:SS manually (no libraries).
# Fixes:
#  - لا تخلط السلاسل مع المقارنة الرقمية
#  - split من time2 وليس time1 في الثانية
#  - قارن tuples رقمية (h,m,s)
# ملاحظة: لو أدخلت HH:MM فقط، أضفنا ثانية افتراضية 00.
t1 = input("Enter first time (HH:MM or HH:MM:SS): ").strip()
t2 = input("Enter second time (HH:MM or HH:MM:SS): ").strip()

def parse_hms(ts: str):
    parts = ts.split(":")
    if len(parts) == 2:
        h, m = parts
        s = "00"
    elif len(parts) == 3:
        h, m, s = parts
    else:
        raise ValueError("Invalid time format, use HH:MM or HH:MM:SS")
    return int(h), int(m), int(s)

h1, m1, s1 = parse_hms(t1)
h2, m2, s2 = parse_hms(t2)

tup1 = (h1, m1, s1)
tup2 = (h2, m2, s2)

if tup1 < tup2:
    print("Time 1 comes before Time 2")
elif tup1 > tup2:
    print("Time 2 comes before Time 1")
else:
    print("Both times are the same")
