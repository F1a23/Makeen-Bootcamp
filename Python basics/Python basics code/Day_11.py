# -------------------------------------------------------------------
# Question 1: Collect Positive and Negative Numbers
# Ask the user to enter integers (positive or negative) until they type "q".
# Store positive numbers in one list and negative numbers in another.
# Then print both lists.
# Example:
# Enter number or q to stop: 5
# Enter number or q to stop: -3
# Enter number or q to stop: 0
# Enter number or q to stop: q
# Positive: [5, 0]
# Negative: [-3]
# -------------------------------------------------------------------

positive_numbers = []
negative_numbers = []

while True:
    user_input = input("Enter an integer or 'q' to stop: ")

    if user_input.lower() == "q":
        break
    elif user_input.lstrip("-").isdigit():
        num = int(user_input)
        if num >= 0:
            positive_numbers.append(num)
        else:
            negative_numbers.append(num)
    else:
        print("Invalid input, please enter a number or 'q'.")

print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)


# -------------------------------------------------------------------
# Question 2: Sum of Numbers
# Keep asking the user to enter numbers until "done" is typed.
# Ignore any non-numeric input.
# At the end, print the sum of all valid numbers entered.
# Example:
# Enter number or done: 4
# Enter number or done: hello
# Enter number or done: 6
# Enter number or done: 2
# Enter number or done: done
# Sum = 12
# -------------------------------------------------------------------

numbers = []

while True:
    user_input = input("Enter number or 'done' to stop: ")

    if user_input.lower() == "done":
        break
    elif user_input.lstrip("-").isdigit():
        numbers.append(int(user_input))
    else:
        print("Invalid input, please enter a number or 'done'.")

print("Numbers entered:", numbers)
print("Sum =", sum(numbers))


# -------------------------------------------------------------------
# Extra Notes on Lists
# Sorting, Copying, and Slicing Examples
# -------------------------------------------------------------------

# Sorting lists
values = [1, 16, 9, 4]
values.sort()
print("Sorted ascending:", values)  # [1, 4, 9, 16]
values.sort(reverse=True)
print("Sorted descending:", values)  # [16, 9, 4, 1]

# Copying lists (same container vs different)
lis = [1, 2, 3, 4]
newLis = lis  # same memory
lis.append(5)
print("Same container copy:", newLis)  # [1, 2, 3, 4, 5]

lis2 = [6, 7, 8, 9]
newlis2 = list(lis2)  # different memory
lis2.append(10)
newlis2.append(11)
print("Original list:", lis2)   # [6, 7, 8, 9, 10]
print("Copied list:", newlis2)  # [6, 7, 8, 9, 11]

# List slicing
x = [21, 22, 23, 24, 25, 26]
print("Slice from index 2:", x[2:])   # [23, 24, 25, 26]
print("Slice from 0 to 2:", x[0:3])   # [21, 22, 23]


# -------------------------------------------------------------------
# Example: Loop Input with Negative Check
# Demonstrates handling both positive and negative numbers safely.
# -------------------------------------------------------------------

lis = []
while True:
    inputStr = input("Enter number or Q to stop: ")

    if inputStr.lower() == "q":
        break
    elif inputStr.lstrip("-").isdigit():
        lis.append(int(inputStr))
    else:
        print("Invalid input, please enter numbers only.")

print("Final list:", lis)
