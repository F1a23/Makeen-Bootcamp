# ======================================================================
# This file demonstrates:
# 1) Old-style string formatting with % (width, precision, alignment, % sign)
# 2) Common string methods (upper/lower/title/center/replace/find/count/…)
# 3) Simple if/else examples (floor mapping, discount)
# ======================================================================

# ----------------------------------------------------------------------
# (Optional) Example 1 — Intentional error demo
# Question: Why does input(1) raise an error?
# Answer: input() expects a prompt string, not an integer.

# ----------------------------------------------------------------------
"""
print("-------Example 1--------")
message = "Fatima"
number = input(1)  # ❌ TypeError: prompt must be str, not int
print("-------------------------")
"""

# ----------------------------------------------------------------------
# Example 2 — Old-style % formatting (float precision, width, alignment)
# Question: Format floats with precision and width; format ints; left/right align.

# ----------------------------------------------------------------------
print("-------Example 2--------")

# %.4f → 4 digits after decimal; %10.2f → width 10, 2 decimals (right-aligned)
price = 1.2199967
discount = 588

print("The price is %.4f" % (price,))
print("The price is: %10.2f" % (price,))   # field width 10 (right)
print("The price is:%10.2f" % (price,))    # same, just no space before %
print("The price is %.4f And the discount is %d" % (price, discount))      # %d for int
print("The price is %.4f And the discount is %10d" % (price, discount))    # int width 10 (right)
print("The price is %.4f And the discount is %-10d" % (price, discount))   # int width 10 (left)

print("-------------------------")
price2 = 3.989889
print("The price is %.4f" % (price2,))
print("price:       %.4f" % (price2,))   # just spacing in the label for nicer output

print("-------------------------")
# Strings with width; printing literal % with %%
greet = "Hello"
greet2 = "Good morning"
num = 4
print("%-10s %10s" % (greet, greet2))  # left-align greet, right-align greet2
print("%%%20d" % (num,))                # '%%' → literal '%', then a right-aligned int
print("%20d%%" % (num,))                # right-aligned int, then a literal '%'

# ----------------------------------------------------------------------
# String Methods — upper/lower/title/center/isidentifier/replace/find/rfind/count
# Question: Demonstrate common and useful string methods.

# ----------------------------------------------------------------------
print("-------------------------")
print("--------- Methods --------")
print("\n")

title = "Python For everyone python for everyone"

print(title.upper())                # ALL CAPS
print(title.lower())                # all lowercase
print('Python'.center(10, '-'))     # center with fill char '-'
print(title.title())                # Title Case
print(title.isidentifier())         # valid Python identifier? (false here)
print(title.replace("everyone", "program"))       # replace all
print(title.replace("everyone", "program", 1))    # replace first occurrence only
print(title.find("y"))              # first index of 'y' (or -1 if not found)
print(title.find("y", 4, 18))       # search between indices [4, 18)
print(title.rfind("y"))             # last index of 'y'
print(title.count("y"))             # count all 'y'
print(title.count("y", 4))          # count 'y' starting at index 4

# ----------------------------------------------------------------------
# Floor Mapping (skip floor 13) — kept commented as in your code
# Question: Map “displayed elevator floor” to “actual floor” (13 is skipped).
# ----------------------------------------------------------------------
print("-------------------------")
"""
floor = int(input("Enter the floor number: "))

if floor == 13:
    print("Invalid input please enter floor again")

if floor > 13:
    actualFloor = floor - 1
    print(actualFloor)
else:
    actualFloor = floor

print("the actual Floor is: ", actualFloor)
"""

# ----------------------------------------------------------------------
# If/Else — Discount example
# Question: If price > 200, apply 5% discount; else print original price.
# ----------------------------------------------------------------------
print("-------------------------")
print("--------- if else condition ----\n")
price = float(input("Enter the price: "))

if price > 200:
    d = price * 0.05
    finpric = price - d
    print("The price after discount is:", finpric)
    print("the discount is", d)
else:
    print("the price without discount is", price)
