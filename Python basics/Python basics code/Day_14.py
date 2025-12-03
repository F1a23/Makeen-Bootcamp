# ======================================================================
# 2D LIST (MATRIX) — INDEXING & NESTED LOOPS
# ======================================================================
matrix = [
    [0, 3, 0],
    [0, 0, 1],
    [1, 0, 0]
]

row0 = matrix[0]
print(row0)               # [0, 3, 0]
val_1_2 = matrix[1][2]
print(val_1_2)            # 1
print(matrix[0][1])       # 3

for i in range(len(matrix)):
    print(matrix[i])
    for j in range(len(matrix[i])):
        print(matrix[i][j])

# ======================================================================
# WRITE A FILE (hello.txt)
# ======================================================================
with open("hello.txt", "w", encoding="utf-8") as outfile:
    print("Hello world!\n", file=outfile)

# ======================================================================
# STRING STRIP / LSTRIP / RSTRIP
# ======================================================================
name = "!#Fatima!"
print(name.strip())  # removes leading/trailing whitespace by default

name = "!#Fatima!!@@@!?"
print(name.rstrip("@!?"))   # strip these chars from the RIGHT

name = "!#Fatima!!@@@!?"
print(name.lstrip("@!#?"))  # strip these chars from the LEFT

# ======================================================================
# READ LINES WITH readlines(), STRIP NEWLINES (CORRECTED)
# ======================================================================
# Example A: fix typos: range(), "\n" not "/n"
with open("story.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].rstrip("\n")  # remove trailing newline safely

# Example B: build a new list with stripped lines
with open("story.txt", "r", encoding="utf-8") as infile:
    lines_raw = infile.readlines()

newlist1 = []
for i in range(len(lines_raw)):
    newlist1.append(lines_raw[i].rstrip("\n"))

print(lines_raw)   # original with newlines
print("------------------------------------------------")
print(newlist1)    # cleaned list

# ======================================================================
# READ THE ENTIRE FILE AT ONCE
# ======================================================================
with open("story.txt", "r", encoding="utf-8") as infile:
    all_text = infile.read()
print(all_text)

# ======================================================================
# SPLIT / RSPLIT EXAMPLES
# ======================================================================
fullname = "Fatima Said Al Amri"
print("using split: ", fullname.split(" ", 1))   # split once from LEFT
print("using rsplit:", fullname.rsplit(" ", 1))  # split once from RIGHT

s = "a,bc,d"
print(s.split(","))   # ['a', 'bc', 'd']

print("-------------------------------")
s = "a b  c"
print(s.split())      # ['a', 'b', 'c'] (collapses multiple spaces)

print("-------------------------------")
s = "a b  c"
print(s.split(" "))   # ['a', 'b', '', 'c'] (keeps empty splits)

print("-------------------------------")
s = "a:bc:d"
print(s.split(":", 1))   # ['a', 'bc:d'] (first ':' from left)

print("-------------------------------")
s = "a:bc:d"
print(s.rsplit(":", 1))  # ['a:bc', 'd'] (first ':' from right)

# ======================================================================
# TRY / EXCEPT — FILE ERRORS & GENERAL EXCEPTIONS
# ======================================================================
try:
    with open("x.txt", "r", encoding="utf-8") as infile:  # file likely missing
        pass
except IOError:
    print("the file does not exist")

try:
    with open("story.txt", "r", encoding="utf-8") as infile:
        avg = 10 / 0  # force ZeroDivisionError
except IOError:
    print("the file does not exist")
except Exception as exceptObj:
    print("Sorry you got error:", str(exceptObj))

# with finally (ensures closure even on error)
try:
    infile = open("story.txt", "r", encoding="utf-8")
    avg = 10 / 0
except IOError:
    print("the file does not exist")
except Exception as exceptObj:
    print("the Error is:", str(exceptObj))
finally:
    infile.close()
    print("This file is closed")

# ======================================================================
# INPUT VALIDATION WITH TRY/EXCEPT (SINGLE VALUE)
# ======================================================================
input_ok = False
while not input_ok:
    try:
        num = input("Enter a number: ")
        num = float(num)
        input_ok = True
    except ValueError:
        print("Non-numeric value entered: '%s'" % num)
num = num * 2
print(num)

# ======================================================================
# INPUT VALIDATION WITH TRY/EXCEPT (APPEND TO LIST)
# ======================================================================
input_ok = False
nums = []
while not input_ok:
    try:
        num = input("Enter a number: ")
        num = float(num)
        nums.append(num)
        input_ok = True
    except ValueError:
        print("Non-numeric value entered: '%s'" % num)
num = num * 2
print(nums)
