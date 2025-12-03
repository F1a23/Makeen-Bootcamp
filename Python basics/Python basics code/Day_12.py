# =======================================================================
# 🧩 TOPIC 1: TUPLES (الـ Tuple)
# =======================================================================

# Question 1: Tuple Basics and Indexing
# Create tuples, access elements, and handle nested lists inside tuples.

t1 = (1, 2, 3)
t2 = ("a", "b", "c", "d")
t3 = (200, "A", [4, 5], 3.2)

print("Tuple t1:", t1)
print("Accessing 4 inside nested list:", t3[2][0])  # List at index 2 → element 4

# Another way to access the same value
lis0 = t3[2][0]
print(lis0)

# Nested tuple example – accessing value 4
myTuple = (200, "A", [2, 10, 5, [1, 4]], 3.2)
myTuple = myTuple[2][3][1]  # Nested list access
print("Value 4:", myTuple)

# Reverse a tuple
print("Tuple t2:", t2)
print("Tuple t3:", t3)
myTuple = (200, "A", [2, 10, 5, [1, 4]], 3.2)
print("Reversed tuple:", myTuple[::-1])

# -----------------------------------------------------------------------
# Question 2: Tuple Operations (Reverse, Add, Repeat)
# -----------------------------------------------------------------------

t1 = ("a", "b", "c")
print("Reverse tuple:", t1[::-1])  # ('c', 'b', 'a')

t2 = ("a", "b", "c")
t3 = t1 + t2  # Concatenate tuples
print("Concatenated tuple:", t3)

t3 = t3 * 4  # Repeat tuple 4 times
print("Repeated tuple:", t3)

# Print all elements in tuple
for i in t3:
    print(i, end="")
print()

# -----------------------------------------------------------------------
# Question 3: Nested Tuples – Printing Elements
# -----------------------------------------------------------------------

t = ((10, 20, 30), (1, 2))
for i in range(len(t)):
    for j in range(len(t[i])):
        print(t[i][j])

# -----------------------------------------------------------------------
# Question 4: Tuple Methods (count, index)
# -----------------------------------------------------------------------

t1 = (1, 2, 3, 1, 5, 1)
print("Count of 1:", t1.count(1))  # there are 3 ones
print("Index of 5:", t1.index(5))  # index of element 5


# =======================================================================
# 🧩 TOPIC 2: LISTS (القوائم) — Sorting and Searching
# =======================================================================

# Question 5: Sorting Function (Manual Sort)
# Demonstrate how sort() works internally using swapping.

mylist = [1, 16, 9, 4]

def sortMylist(L):
    for i in range(len(L)):
        while i > 0 and L[i-1] > L[i]:
            L[i], L[i-1] = L[i-1], L[i]
            i -= 1
    return L

print("Sorted list:", sortMylist(mylist))

# -----------------------------------------------------------------------
# Question 6: Linear Search
# Find position of a target value in a list.
# -----------------------------------------------------------------------

lis = [2, 12, 5, 3, 20, 13]
target = int(input("Enter your target: "))

position = -1
for i in range(len(lis)):
    if lis[i] == target:
        position = i

print("The target number is at position:", position)

# Second method using a function
def linearSearch(lis, num):
    for i in range(len(lis)):
        if lis[i] == num:
            return i
    return -1

lis = [1, 16, 9, 4]
num = 9
res = linearSearch(lis, num)
print("The index of number:", res)

# -----------------------------------------------------------------------
# Question 7: Find First Value Greater Than 100
# -----------------------------------------------------------------------

limit = 100
pos = 0
found = False
values = [2, 3, 1, 300, 200, 2]

while pos < len(values) and not found:
    if values[pos] > limit:
        found = True
    else:
        pos += 1

if found:
    print("Found at position:", pos)
else:
    print("Not found")


# =======================================================================
# 🧩 TOPIC 3: DICTIONARIES (القواميس)
# =======================================================================

# Question 8: Dictionary Basics
# Create, access, copy, and iterate through dictionaries.

myEmptyDic = {}
print("Empty dictionary:", myEmptyDic)

name = "Sara"
myfrinds = {"Muna": 99990000, "Noor": 9923112, name: 99736111, 2: 9999111}
print("Friends dictionary:", myfrinds)
print("Access by key 2:", myfrinds[2])

# Copy dictionary
newFrinds = dict(myfrinds)
print("Copied dictionary:", newFrinds)

# Access specific value
munaNo = myfrinds["Muna"]
print("Muna’s number:", munaNo)

# Print all key-value pairs
myfrinds = {"Muna": 99990000, "Noor": 9923112, "Sara": 99736111, "Laila": 9999111}
for i in myfrinds:
    print(i, myfrinds[i])

# Check if key exists
if "Muna" in myfrinds:
    print(myfrinds["Muna"])
else:
    print("You don’t have a friend named Muna")

# Using get() with default value
number = myfrinds.get("Muna", 0000)
print("Muna’s number (get):", number)

# Add new friend
myfrinds["Amira"] = 98989899
print("After adding Amira:", myfrinds)

# Add multiple friends using input (example shortened)
for i in range(2):
    newFrind = input("Enter new friend name: ")
    FrindNo = input("Enter new friend number: ")
    myfrinds[newFrind] = FrindNo
print("Updated dictionary:", myfrinds)

# Print only values
for value in myfrinds.values():
    print(value)

# -----------------------------------------------------------------------
# Question 9: Find Highest Score in Dictionary
# -----------------------------------------------------------------------

myStudent = {"Noor": 45, "Ali": 99, "Nada": 70}

# Manual method
maxm = 0
for i in myStudent.items():
    if i[1] > maxm:
        maxm = i[1]
print("Highest grade:", maxm)

# Using max()
maxm = max(myStudent.values())
for name, mark in myStudent.items():
    if mark == maxm:
        print("Top student:", name, mark)

# -----------------------------------------------------------------------
# Question 10: pop() Method and Sorted Keys
# -----------------------------------------------------------------------

myStudent = {"Noor": 45, "Ali": 99, "Nada": 70}

# Remove a key
if "Ali" in myStudent:
    myStudent.pop("Ali")
print("After removing Ali:", myStudent)

# Print dictionary sorted by key
print("My Contacts:")
for k in sorted(myStudent):
    print("%-10s %d" % (k, myStudent[k]))

print("Total students:", len(myStudent))

#--------------------------------------------------------------------------
        """pass by value and pass by reference"""

#pass by value
# it means not change on the value 
def changvalue(x):
    x=88 
    print("value inside the function: ",x)

z=21 # if it int,float,str,tuple it will not change
changvalue(z)
print("value outside the function: ",z)

#--------------------------------------------------------------
#pass by reference
#it means will change on the value 
def changvalue(lst):
    lst.append(88)
    print("value inside the function:", lst)

my_list = [1, 2, 3]
changvalue(my_list) # it will change if it : list,dict,set
print("value outside the function :", my_list)
