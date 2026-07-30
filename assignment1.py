# 1 check if the number is positive, negative or zero

num = int(input("Enter your number: "))

if num > 0:
    print("the number is positive")

elif num < 0:
    print("the number is negative")

else:
    print("the number is zero")


# 2 check if the number is even or odd

num = int(input("enter your number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 3 find the greatest of two number

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))

if num1 > num2:
    print("num1 is greater")
else:
    print("num2 is greater")


# 4 find the greatest of three number

num1 =int(input("Enter the number: "))
num2 =int(input("Enter the number: "))
num3 =int(input("Enter the number: "))

if num1 > num2 and num1 > num3:
    print("num1 is greater")
elif num2 > num1 and num2 > num3:
    print("num2 is greater")
elif num3 > num1 and num3 > num2:
    print("num3 is greater")
else:
    print("equal")


# 5 check if a person is eligible to vote (age>=18)

num =int(input("Enter the age of person: "))

if num>=18:
    print("The person is eligible to vote")
else:
    print("The person is not eligible")

# 6 Check whether a year is a leap year.

year = int(input("Enter a year: "))


if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

# 7 Check if a character is a vowel or consonant.

letter = input("Enter the letter: ")

if letter== "a":
    print("It is a vowel")
elif letter == "e":
    print("It is a vowel")
elif letter == "i":
    print("It is a vowel")
elif letter == "o":
    print("It is a vowel")
elif letter == "u":
    print("It is a vowel")
else:
    print("It is consonant")

# 8 Check whether a number is divisible by 5 and 11.


num =int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("the number is divisible")
else:
    print("the number is not divisible")

# 9 Check if a number is a multiple of both 3 and 7.

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("The number is a multiple of both 3 and 7.")
else:
    print("The number is not a multiple of both 3 and 7.")

# 10 Assign grades based on marks:
# 90–100: A
# 80–89: B
# 70–79: C
# 60–69: D
# Below 60: F

marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("You score grade A")
elif marks >= 80 and marks <= 89:
    print("You score grade B")
elif marks >= 70 and marks <=79:
     print("You score grade C")
elif marks >= 60 and marks <=69:
     print("You score grade D")
else:
    print("You are Fail")


# 11 Check if a character is uppercase or lowercase.

ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z':
    print("Uppercase")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase")
else:
    print("Not an alphabet")

# 12 Find whether the entered alphabet is a vowel using if-elif.

letter = input("Enter the letter: ")

if letter== "a":
    print("It is a vowel")
elif letter == "e":
    print("It is a vowel")
elif letter == "i":
    print("It is a vowel")
elif letter == "o":
    print("It is a vowel")
elif letter == "u":
    print("It is a vowel")
else:
    print("It is consonant")

# 13 Check if three sides can form a triangle.


a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and b + c > a and a + c > b:
    print("Yes, these sides can form a triangle")
else:
    print("No, these sides cannot form a triangle")


# 14 Determine the type of triangle (Equilateral, Isosceles, Scalene).

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b == c:
        print("Equilateral Triangle")
elif a == b or b == c or a == c:
        print("Isosceles Triangle")
elif( a != b or b != c or a != b):
        print("Scalene Triangle")
        
else:
    print("Not a valid triangle")


# 15 Find the largest among four numbers.

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
num4=int(input("enter num4:"))
if (num1 > num2 and num1 > num3 and num1 > num4):
    print("num1 is greater")
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print("num2 is greater")
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print("num3 is greater")
elif(num4 >num1 and num4 > num2 and num4 >num3):
    print("num4 is greater")
else:
    print("same")


# 16 Check whether a number is a three-digit number.

num=int(input("enter num:"))

if(num >= 100):
    print("the num is three digit")
else:
    print("the num is not three digit")

# 17 Calculate electricity bill using slab rates.

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = units * 2.5
else:
    bill = units * 4

print("Electricity Bill =", bill)

# 18 Calculate income tax based on income slabs.

income = int(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Income Tax =", tax)


# 19 Check if a student passes (minimum 35 marks in each subject).

sub=input("enter sub name:")
marks=int(input("enter sub marks:"))

if (marks >= 35):
    print("passed")
else:
    print("not passed")

# 20 Find whether a number is within a given range

num = int(input("Enter a number: "))
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

if num >= start and num <= end:
    print("The number is within the range.")
else:
    print("The number is outside the range.")

# 21 Build a simple calculator using if-elif-else (+, -, *, /).

a=int(input("enter a:"))
b=int(input("enter b:"))
operation=input("enter operator + - * / : ")

if operation == '+':
    print("Answer =", a + b)

elif operation == '-':
    print("Answer =", a - b)

elif operation == '*':
    print("Answer =", a * b)

elif operation == '/':
    print("Answer =", a / b)

else:
    print("not valid")


# 22. Check if a year is a century leap year.

year = int(input("Enter the year: "))

if year % 400 == 0 :
    print("Century Leap Year")
else:
    print("Not a Leap Year")


# 23.Determine the season based on the month number.

month = int(input("Enter month number (1-12): "))

if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month >= 3 and month <= 5:
    print("Summer")
elif month >= 6 and month <= 9:
    print("Monsoon")
elif month >= 10 and month <= 11:
    print("Autumn")
else:
    print("Invalid month")


# 24.Find the number of days in a month.

month=input("enter month november,december,january,februay,march,aprill,,may,june,july ,august ,september,october:")

if (month in "january,march,may,july august,october,december"):
    print("31 days")

elif(month in "aprill,june,september,november"):
    print("30 days")

elif (month in "february"):
    print("28 and 29 days")

else:
    print("not valid")
    
# 25 Check whether a password meets minimum conditions (length, digits, etc.).

password = input("Enter password: ")

if len(password) >= 8 and any(ch.isdigit() for ch in password):
    print("Strong Password")
else:
    print("Weak Password")


# 26 Determine ticket price based on age category.

age = int(input("Enter your age: "))

if age < 5:
    print("Ticket Price = Free")
elif age <= 12:
    print("Ticket Price = ₹50")
elif age <= 59:
    print("Ticket Price = ₹100")
else:
    print("Ticket Price = ₹70")


# 27 Calculate discount based on purchase amount.

amount = int(input("Enter purchase amount: "))

if amount >= 1000:
    print("Discount = 10%")
else:
    print("No Discount")


# 28.Check if a person is eligible for a driving license (age and eyesight condition).

age=int(input("enter age:"))
eyesight = input("Is your eyesight good? (yes/no): ")
if(age>=18 and eyesight == "yes"):
    print("you can drive")
else:
    print("you cannot drive")


# 29 Create a login system with username and password validation

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")


# 30.Create a menu-driven program using if-elif-else with options like:
# Addition
# Subtraction
# Multiplication
# Division
# Exit


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter choice: "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a + b)

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a - b)

elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a * b)

elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a / b)

elif choice == 5:
    print("Exit")

else:
    print("Invalid Choice")