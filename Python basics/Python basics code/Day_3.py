# ======================================================================
# Q1 — Rectangle Area (المساحة)
# Question: Given width w and length l, compute area = w * l and print it.
# المطلوب: حساب مساحة مستطيل وطباعتها.
# ======================================================================
w = 20
l = 50
area = w * l
print("Q1 - area:", area)  # 1000


# ======================================================================
# Q2 — Strings, Tabs, and Types (الأنواع والطباعة مع tab)
# Question: Print strings with \t (tab) and show variable types.
# المطلوب: طباعة نص مع tab واستعراض نوع المتغيّر.
# ======================================================================
name = "sahab"
age = 25
print("Q2 - Hi\t" + name)
print("Q2 - My name is\t" + name)
print("Q2 - type(w):", type(w))
print("Q2 - type(name):", type(name))


# ======================================================================
# Q3 — Average of Three Scores (متوسط ثلاثة أرقام)
# Question: Compute average of x, x2, x3.
# المطلوب: حساب المتوسط لثلاث قيم.
# ======================================================================
x = 60
x2 = 99
x3 = 90
avg = (x + x2 + x3) / 3
print("Q3 - average:", avg)


# ======================================================================
# Q4 — Variable Update (تحديث قيمة متغيّر)
# Question: Start with canVolume=20, then add 4.
# المطلوب: زيادة المتغيّر 4 وطباعة الناتج.
# ======================================================================
canVolume = 20
canVolume = canVolume + 4
print("Q4 - canVolume:", canVolume)  # 24


# ======================================================================
# Q5 — Identifiers & Naming (أسماء المتغيّرات الصحيحة)
# Question: Show valid/invalid identifiers. (تعليق توضيحي فقط)
# المطلوب: أمثلة للأسماء الصحيحة/الخاطئة (لا كود).
# ملاحظات:
#   - لا يجوز البدء برقم: 5name  ✗
#   - الشرطة السفلية مسموحة في البداية: _name ✓
#   - علامة $ غير قياسية في بايثون: $name ✗
#   - camelCase أو snake_case كلاهما مقبول: canVolume / can_volume ✓
# ======================================================================


# ======================================================================
# Q6 — Constants vs Variables (ثوابت ومتغيّرات)
# Question: Use UPPER_SNAKE_CASE for constants.
# المطلوب: تعريف "ثابت" بحروف كبيرة (اتفاقية).
# ملاحظة: بايثون لا يمنع التغيير، لكن الاسم الكبير يعني "لا تغيره".
# ======================================================================
BOTTLE_VOLUME = 7      # مثال لاسم ثابت (اتفاقية)
BOTTLE_VOLUME = 4.0    # تغيير القيمة مسموح لغويًا لكن غير مفضّل للثوابت
textRate = 2           # متغيّر عادي
print("Q6 - BOTTLE_VOLUME:", BOTTLE_VOLUME)


# ======================================================================
# Q7 — Beverage Volumes (حجوم المشروبات بالليتر)
# Question: Compute liters in a six-pack of 12-oz cans, and total with a 2-L bottle.
# المطلوب: حساب حجم 6 علب (0.355 لتر لكل علبة) ثم إضافته إلى قنينة 2 لتر.
# ======================================================================
CAN_VOLUME_L = 0.355   # liters in a 12-ounce can
BOTTLE_2L   = 2.0      # liters in a two-liter bottle
cansPerPack = 6

six_pack_volume = cansPerPack * CAN_VOLUME_L
print("Q7 - six-pack liters:", six_pack_volume, "L")  # 2.13 L

total_with_bottle = six_pack_volume + BOTTLE_2L
print("Q7 - total with 2L bottle:", total_with_bottle, "L")  # 4.13 L


# ======================================================================
# Q8 — Operator Precedence (أولوية العمليات)
# Question: Show ** higher than * and +, and / higher than +.
# المطلوب: أمثلة على أولوية العمليات.
# ======================================================================
x = 2 + 2 ** 4   # ** أولاً → 2 + 16 = 18
print("Q8 - x:", x)
b = 2 * 2 ** 4   # ** أولاً → 2 * 16 = 32
print("Q8 - b:", b)
a = 2 + 10 / 2   # / أولاً → 2 + 5 = 7.0
print("Q8 - a:", a)


# ======================================================================
# Q9 — Full Name Concatenation (دمج الاسم الأول والأخير)
# Question: Concatenate first and last name with a space.
# المطلوب: دمج نصين مع مسافة.
# ======================================================================
firstName = "Sahab"
lastName = "Al-amri"
fullName = firstName + " " + lastName
print("Q9 - fullName:", fullName)


# ======================================================================
# Q10 — Quadratic Equation Roots (حل معادلة تربيعية)
# Question: Solve ax^2 + bx + c = 0 for real roots if discriminant >= 0.
# المطلوب: حساب الجذور الحقيقية فقط؛ أو رسالة إن لا توجد جذور حقيقية.
# ======================================================================
a = 1
b = 1
c = 1
discriminant = b**2 - 4*a*c
if discriminant >= 0:
    sqrt_disc = discriminant ** 0.5
    x1 = (-b + sqrt_disc) / (2 * a)
    x2 = (-b - sqrt_disc) / (2 * a)
    print("Q10 - roots:", x1, x2)
else:
    print("Q10 - no real roots (discriminant < 0)")


# ======================================================================
# Q11 — Integer Division // and Modulo % (القسمة الصحيحة والباقي)
# Question: Show // for floor division and % for remainder. Check even/odd.
# المطلوب: أمثلة على // و % ومعرفة زوجي/فردي.
# ======================================================================
x = 5 // 2      # 2
print("Q11 - 5//2:", x)
a = 8 // 3      # 2
print("Q11 - 8//3:", a)
a1 = 10 // 3    # 3
print("Q11 - 10//3:", a1)

a = 8
b = a % 2       # 0 → even
print("Q11 - a%2 (0=even,1=odd):", b)


# ======================================================================
# Q12 — Currency: Baises to Rials (تحويل بيسة إلى ريال)
# Question A: Read total baises and print rials and remaining baises.
# المطلوب: تحويل البيسة إلى ريال وباقي البيسات (1000 بيسة = 1 ريال).
# ======================================================================
baises = int(input("Q12A - Enter amount in baises: "))
riales = baises // 1000       # عدد الريالات
baises = baises % 1000        # المتبقي بالبيسة
print("Q12A - rials =", riales, "\nQ12A - baises =", baises)

# Question B: Same, but only if input > 1000; otherwise print Error.
# المطلوب: تنفيذ التحويل بشرط أن المبلغ أكبر من 1000، وإلا خطأ.
baises2 = int(input("Q12B - Enter amount in baises (> 1000): "))
if baises2 > 1000:
    riales2 = baises2 // 1000
    baises_rem = baises2 % 1000
    print("Q12B - rials:", riales2)
    print("Q12B - baises:", baises_rem)
else:
    print("Q12B - Error: amount must be > 1000")


# ======================================================================
# Q13 — String length & concatenation
# Question: Given a string and a count, print the string length,
# then concatenate the string with the count (after converting to str).
# المطلوب: احسب length وادمج النص مع العدد بعد تحويله لسلسلة.
# ======================================================================
word = "Hi I am Fatima #"
count = 5
word_length = len(word)
count_str = str(count)
print("Q13 - length:", word_length)
print("Q13 - concat:", word + count_str)


# ======================================================================
# Q14 — Indexing in strings and lists
# Question: Print the last char of a name, and specific indices from name/list.
# المطلوب: فهرسة آخر حرف وبعض العناصر.
# ======================================================================
name = "fatima"
number = [1, 2, 3, 4]
n = len(name)
print("Q14 - last char:", name[n - 1])            # same as name[-1]
print("Q14 - name[2:5]:", name[2], name[3], name[4])  # t i m
print("Q14 - number[2], number[3]:", number[2], number[3])  # 3 4


# ======================================================================
# Q15 — String concatenation with numbers
# Question: Build "Python" from "Py" and print with text and age.
# المطلوب: دمج نص + رقم (مع str عند الحاجة).
# ======================================================================
string = "Py"
age = 20
string = string + "thon"                  # "Python"
print("Q15 - with commas:", string, "hi", age)      # auto space & cast
print("Q15 - with '+':", string + " hi " + str(age))  # need str() for numbers


# ======================================================================
# Q16 — Escape sequences
# Question: Demonstrate newline '\n'.
# المطلوب: استخدام \n لسطر جديد.
# ======================================================================
print("Q16 - Hi//world \n")
print("Q16 - F")  # on a new line because of previous \n


# ======================================================================
# Q17 — Basic arithmetic from user input (multiplication only)
# Question: Ask for two floats and print their product.
# المطلوب: قراءة عددين (float) وطباعـة حاصل الضرب.
# ======================================================================
x = float(input("Q17 - Enter x : "))
y = float(input("Q17 - Enter y : "))
z = x * y
print("Q17 - product:", z)


# ======================================================================
# Q18 — Simple Calculator (Two Approaches)
# Task: Read numbers and print result.
# 1) Compute all operations (+, -, *, /)
# 2) User chooses operator (+, -, *, /) with zero-division check
# المطلوب: آلتان حاسبتان مبسّطتان (طريقتان).
# ======================================================================

# Approach 1: compute all operations at once
num1 = float(input("Q18-1 - Enter first number : "))
num2 = float(input("Q18-1 - Enter second number : "))
print("Addition (+):        ", num1 + num2)
print("Subtraction (-):     ", num1 - num2)
print("Multiplication (*):  ", num1 * num2)
print("Division (/):        ", num1 / num2)

print("\n")  # spacer

# Approach 2: user selects the operator
num1 = float(input("Q18-2 - Enter first number: "))
operator = input("Q18-2 - Enter operator (+, -, *, /): ")
num2 = float(input("Q18-2 - Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operator")

