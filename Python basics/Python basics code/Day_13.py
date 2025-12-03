# ======================================================================
# FILE I/O PRACTICE — READ, LOOP, LISTS, WRITE, SPLIT, COUNTS
# ======================================================================

# ----------------------------------------------------------------------
# Q1 — Read the first two lines (readline)
# ----------------------------------------------------------------------
print("---- Q1: first two lines ----")
with open("story.txt", "r", encoding="utf-8") as f:
    first_line = f.readline()
    second_line = f.readline()

print(first_line, end="")   # lines already include trailing '\n'
print(second_line, end="")
print()

# ----------------------------------------------------------------------
# Q2 — Read the whole file line-by-line using a while loop
# ----------------------------------------------------------------------
print("---- Q2: while + readline loop ----")
with open("story.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line != "":
        print(line, end="")  # avoid double newlines
        line = f.readline()
print()

# ----------------------------------------------------------------------
# Q3 — Read all lines into a list (correct order, no extra blank)
# ----------------------------------------------------------------------
print("---- Q3: collect lines into a list ----")
lines = []
with open("story.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line != "":
        lines.append(line.rstrip("\n"))  # store without trailing newline
        line = f.readline()
print(lines)
print()

# ----------------------------------------------------------------------
# Q4 — Read the entire file at once (read)
# ----------------------------------------------------------------------
print("---- Q4: read entire file ----")
with open("story.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)
print()

# ----------------------------------------------------------------------
# Q5 — Sum and average numbers from numbers.txt (robust to blanks)
# Assumes numbers.txt contains one number per line.
# ----------------------------------------------------------------------
print("---- Q5: total and average from numbers.txt ----")
total = 0
count = 0
with open("numbers.txt", "r", encoding="utf-8") as f:
    for raw in f:
        s = raw.strip()
        if s == "":
            continue
        total += int(s)   # change to float(...) if your file has decimals
        count += 1

if count > 0:
    average = total / count
else:
    average = 0

print("Total:", total)
print("Average:", average)
print()

# ----------------------------------------------------------------------
# Q6 — Write 5 student names to students.txt (version A: write the list)
# ----------------------------------------------------------------------
print("---- Q6A: write 5 names as one list ----")
names = []
for _ in range(5):
    sname = input("Enter student name: ")
    names.append(sname)

with open("students.txt", "w", encoding="utf-8") as f:
    f.write("students names are %s\n" % names)

print("Wrote list of names to students.txt")
print()

# ----------------------------------------------------------------------
# Q7 — Write 5 student names to students.txt (version B: one per line)
# ----------------------------------------------------------------------
print("---- Q7B: write 5 names, one per line ----")
with open("students.txt", "w", encoding="utf-8") as f:
    for _ in range(5):
        sname = input("Enter student name: ")
        f.write("student name: %s\n" % sname)

print("Wrote 5 names (one per line) to students.txt")
print()

# ----------------------------------------------------------------------
# Q8 — Split a full name into parts
# ----------------------------------------------------------------------
print("---- Q8: split full name ----")
full_name = "Fatima Said Al-Amri"
parts = full_name.split()
print(parts)
print()

# ----------------------------------------------------------------------
# Q9 — Word count in story.txt (two answers)
# A) Manual count after split
# B) len(words)
# ----------------------------------------------------------------------
print("---- Q9: word count (two ways) ----")
with open("story.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()  # split on whitespace
# A) manual loop
count_manual = 0
for _ in words:
    count_manual += 1
print("Word count (manual):", count_manual)

# B) direct length
print("Word count (len):", len(words))

# Show a few extra details (optional)
print("Preview of text:")
print(text)
print("Type of text:", type(text))
print()

# ----------------------------------------------------------------------
# NOTES
# - Using 'with open(...)' closes files automatically.
# - Use encoding="utf-8" for safer text handling.
# - When collecting lines, append before reading the next line to avoid skipping.
# - Strip newline characters when building lists unless you need them later.
# ----------------------------------------------------------------------
