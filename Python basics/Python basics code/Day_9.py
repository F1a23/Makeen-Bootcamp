# ======================================================================
# FOR LOOP PRACTICE + PATTERNS + USER-DEFINED FUNCTIONS
# ======================================================================

# ----------------------------------------------------------------------
# Q1 — Iterate over a string (user input)
# ----------------------------------------------------------------------
name = input("Enter your name: ")
for ch in name:
    print(ch)

# ----------------------------------------------------------------------
# Q2 — Basic range() usages
# ----------------------------------------------------------------------
for _ in range(5):
    print("Fatima")
#-----------------------------------------------------------------------
for i in range(5):
    print(i)
#-----------------------------------------------------------------------
total = 0
for item in range(5):
    print("Item", item)
    total += 10
print("running total:", total)

# ----------------------------------------------------------------------
# Q3 — Index-based iteration over a string
# ----------------------------------------------------------------------
name = input("Enter your name: ")
for i in range(len(name)):
    print(i, name[i])

# ----------------------------------------------------------------------
# Q4 — range with start/stop/step (including decreasing steps)
# ----------------------------------------------------------------------
for i in range(5, 10):
    print("Ali")  # runs 5 times

for i in range(10, 1, -1):
    print(i)

for i in range(10, 1, -2):
    print(i)

# ----------------------------------------------------------------------
# Q5 — Compound interest with for loop
# ----------------------------------------------------------------------
balance = 10000
years = 5
rate = 0.05
for year in range(1, years + 1):
    balance += balance * rate
    print(year, balance)

# ----------------------------------------------------------------------
# Q6 — print(..., end="") usage (single-line printing)
# ----------------------------------------------------------------------
for ch in "Ali":
    print(ch, end="")
print(" and my age is 20")
print("d")

# ----------------------------------------------------------------------
# Q7 — Power table (i**j) with nested loops
# ----------------------------------------------------------------------
print("Q7 — Power table (i**j):")
for i in range(1, 5):
    for j in range(1, 5):
        print(i**j)
    print()

# ----------------------------------------------------------------------
# Q8 — Pattern: Right-aligned increasing triangle
# ----------------------------------------------------------------------
print("Q8 — Right-aligned triangle:")
for i in range(4):
    # spaces then stars
    for j in range(4 - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()

# ----------------------------------------------------------------------
# Q9 — Pattern: Increasing then decreasing triangle (symmetric)
# ----------------------------------------------------------------------
print("Q9 — Increasing then decreasing triangle:")
for i in range(3):
    for j in range(i + 1):
        print("*", end="")
    print()
for i in range(3, -1, -1):
    for j in range(i + 1):
        print("*", end="")
    print()

# ----------------------------------------------------------------------
# Q10 — Pattern: Lower triangular using j <= i (fixed version)
# (The original snippet had j undefined and reused i; this is corrected.)
# ----------------------------------------------------------------------
print("Q10 — Lower triangular (j <= i):")
for i in range(4):
    for j in range(4):
        if j <= i:
            print("*", end="")
    print()

# ----------------------------------------------------------------------
# FUNCTIONS: USER-DEFINED (DEF)
# ----------------------------------------------------------------------

# Cube volume: avoid shadowing the function name with a variable
def cube_volume(length: float) -> float:
    """Return volume of a cube with given edge length."""
    return length ** 3

l = float(input("Enter the length of the cube: "))
cube_vol_result = cube_volume(l)
print("Cube volume:", cube_vol_result)

# Factorial (while-based)
def factorial_while(n: int) -> int:
    """Return n! computed with a while loop."""
    result = 1
    if n == 0:
        return 1
    while n >= 1:
        result *= n
        n -= 1
    return result

print("factorial_while(5):", factorial_while(5))

# Factorial (for-based)
def factorial_for(n: int) -> int:
    """Return n! computed with a for loop."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number for factorial: "))
print("factorial_for(num):", factorial_for(num))

# ----------------------------------------------------------------------
# Q11 — Diamond-like centered pattern using rows
# ----------------------------------------------------------------------
rows = 4
print("Q11 — Centered diamond-like pattern:")

# top (including middle line)
for i in range(rows):
    print(" " * (rows - i - 1) + "* " * (i + 1))
# bottom
for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1) + "* " * (i + 1))
