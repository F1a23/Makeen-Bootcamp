# ======================================================================
# CLEANED PRACTICE FILE — FUNCTIONS, GLOBALS, LISTS, LOOPS, UTILITIES
# ======================================================================

# ----------------------------------------------------------------------
# Section 1 — Sum of squares (0..10)
# Note: avoid shadowing built-in 'sum' -> use 'total_sum'
# ----------------------------------------------------------------------
def sum_of_squares_0_to_10():
    total_sum = 0
    last_square = None
    for i in range(11):
        square = i * i
        last_square = square
        total_sum += square
    print("[S1] last_square:", last_square, "| total_sum:", total_sum)

sum_of_squares_0_to_10()


# ----------------------------------------------------------------------
# Section 2 — Cube volume (several styles)
# Original had multiple 'main' redefinitions; here we separate them clearly.
# ----------------------------------------------------------------------
def cube_volume(side_length: float) -> float:
    return side_length * side_length * side_length

def cube_demo_style_a():
    # like: result = cubVolume(2)
    result = cube_volume(2)
    return result

def cube_demo_style_b():
    # like: pass side length via a variable
    side_length = 2
    result = cube_volume(side_length)
    return result

def cube_demo_style_c():
    # like: use an inner function with fixed sideLength=6
    def inner_cube():
        side_length = 6
        return side_length ** 3
    side_length = 2  # this value is not used by inner_cube() on purpose (to show scope)
    result = inner_cube()
    return result

def cube_demo_style_d():
    # like: return the outer 'sideLength' (shows independent scopes)
    def inner_cube():
        side_length = 6
        return side_length ** 3
    side_length = 2
    _ = inner_cube()
    return side_length  # 2

print("[S2A] cube_demo_style_a:", cube_demo_style_a())
print("[S2B] cube_demo_style_b:", cube_demo_style_b())
print("[S2C] cube_demo_style_c:", cube_demo_style_c())
print("[S2D] cube_demo_style_d:", cube_demo_style_d())

def cube_demo_with_input():
    l = float(input("[S2E] Enter the length: "))
    return cube_volume(l)

print("[S2E] cube_volume(input):", cube_demo_with_input())


# ----------------------------------------------------------------------
# Section 3 — Globals: simple bank demo (withdraw/deposit)
# ----------------------------------------------------------------------
balance = 10000.0  # global

def withdraw(amount: float):
    global balance
    if balance >= amount:
        balance -= amount

def deposit(amount: float):
    global balance
    balance += amount

def check_balance():
    global balance
    return balance

withdraw(350)
print("[S3] after withdraw 350:", balance)
deposit(500)
withdraw(200)
print("[S3] check():", check_balance())
print("[S3] after deposit 500 and withdraw 200:", balance)


# ----------------------------------------------------------------------
# Section 4 — Lists: lengths, indexing, mixed types
# ----------------------------------------------------------------------
trainees_in_ai = ["Azam", "Noor", "Muradi", "Muna"]
name = "Ali"
print("[S4] len(name):", len(name))
print("[S4] len(trainees):", len(trainees_in_ai))
print("[S4] name[0]:", name[0])
contact_numbers = ["90009999"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Ahmed", "Muna", 4, 22.44]
print("[S4] mixed:", mixed)
print("[S4] mixed last element:", mixed[-1])

# append a variable inside a list
trainees_in_ai2 = ["Azam", "Noor", "Muradi", "Muna", name]
print("[S4] len(trainees_in_ai2):", len(trainees_in_ai2))

# iterate values
print("[S4] iterate values:")
for person in trainees_in_ai2:
    print("  ", person)

# iterate by index (fixed length example)
print("[S4] iterate by fixed range (first 5):")
for i in range(5):
    print("  idx", i, "->", trainees_in_ai2[i])

# iterate by index (general)
print("[S4] iterate by len:")
n = len(trainees_in_ai2)
for i in range(n):
    print("  idx", i, "->", trainees_in_ai2[i])

# demonstrate a constant index access (as in original snippet)
print("[S4] constant index access (2) inside loop:")
for i in range(5):
    print("  i:", i, "| trainees_in_ai2[2]:", trainees_in_ai2[2])


# ----------------------------------------------------------------------
# Section 5 — Find largest / smallest in a list
# ----------------------------------------------------------------------
numbers_a = [19, 2, 3, 4, 5]
largest = numbers_a[0]
for n in numbers_a:
    if n > largest:
        largest = n
print("[S5] largest:", largest)

numbers_b = [19, 2, -1, 4, 5]
smallest = numbers_b[0]
for n in numbers_b:
    if n < smallest:
        smallest = n
print("[S5] smallest:", smallest)


# ----------------------------------------------------------------------
# Section 6 — Even/Odd report
# ----------------------------------------------------------------------
numbers_c = [3, 2, 5, 6]
for i in range(len(numbers_c)):
    if numbers_c[i] % 2 == 0:
        print(f"[S6] number {numbers_c[i]} is even")
    else:
        print(f"[S6] number {numbers_c[i]} is odd")


# ----------------------------------------------------------------------
# Section 7 — Reading numbers until 'q'
# Three versions: raw strings, ints, robust (+/- detection)
# ----------------------------------------------------------------------
# (A) as strings
def read_numbers_as_strings():
    numbers = []
    while True:
        new_no = input("[S7A] enter a value or q: ")
        if new_no == "q":
            break
        numbers.append(new_no)
    print("[S7A] list:", numbers)

# (B) as integers (no validation)
def read_numbers_as_ints():
    numbers = []
    while True:
        new_no = input("[S7B] enter a number or q: ")
        if new_no == "q":
            break
        numbers.append(int(new_no))
    print("[S7B] list:", numbers)

# (C) robust: digits, negatives, or keep as string if invalid
def read_numbers_robust():
    numbers = []
    while True:
        new_no = input("[S7C] enter a number or q: ")
        if new_no == "q":
            break
        if new_no.lstrip("-").isdigit():
            numbers.append(int(new_no))
        else:
            numbers.append(new_no)  # keep non-numeric as-is
    print("[S7C] list:", numbers)

# Uncomment any version you want to try:
# read_numbers_as_strings()
# read_numbers_as_ints()
# read_numbers_robust()


# ----------------------------------------------------------------------
# Section 8 — List operations: insert, index, remove, pop, concat, repeat
# ----------------------------------------------------------------------
newlist = ["ali", 2, "noor"]
newlist.insert(2, "4")     # insert string "4" at index 2
print("[S8] after insert:", newlist)

friends = ["Harry", "Bob", "Cari", "Emily"]
if "Emily" in friends:
    idx = friends.index("Emily")
    print("[S8] index of Emily:", idx)

friends2 = ["Harry", "Bob", "Cari", "Emily"]
if "Emily" in friends2:
    idx = friends2.index("Emily")
    print("[S8] index of Emily:", idx)
friends2.remove("Emily")
print("[S8] after remove Emily:", friends2)
friends2.pop()  # remove last
print("[S8] after pop():", friends2)

friends3 = ["Harry", "Bob", "Cari", "Emily"]
if "Emily" in friends3:
    idx = friends3.index("Emily")
    print("[S8] index of Emily:", idx)
friends3.pop(2)  # remove by index
print("[S8] after pop(2):", friends3)

myFriends = ["Fritz", "Cindy"]
yourFriends = ["Lee", "Pat", "Phuong"]
ourFriends = myFriends + yourFriends
print("[S8] concatenated:", ourFriends)

monthInQuarter = [1, 2, 3] * 4
print("[S8] monthInQuarter:", monthInQuarter)  # [1,2,3,1,2,3,1,2,3,1,2,3]
