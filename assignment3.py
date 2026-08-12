# DATA TYPES:

# 1. Find the data type of every value in a mixed list

my_list = [10, 3.14, "Hello", True, [1, 2], (3, 4)]
for value in my_list:
    print(value , type(value))

# 2. Convert a nested list into a tuple of tuples

my_list = [[1, 2], [3, 4], [5, 6]]
result = tuple(tuple(x) for x in my_list)
print(result)

# 3. Remove duplicate values while preserving original order

list1 = [10, 20, 10, 30, 20, 40, 30]
list2 = []
for value in list1:
    if value not in list2:
        list2.append(value)
print(list2)


# OPERATORS:

# 4. Check whether a number is a power of 2 using operators.

num = int(input("Enter a number: "))
if num > 0 and (num & (num - 1)) == 0:
    print("Power of 2")
else:
    print("Not a power of 2")

# 5. Swap two numbers using bitwise XOR.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping:")
print("a =", a)
print("b =", b)

# 6. Check whether a number is divisible by both 4 and 6

num = int(input("Enter a number: "))
if num % 4 == 0 and num % 6 == 0:
    print("number is divisible by both 4 and 6")
else:
    print("number is not divisible")

# 7. Calculate the total electricity bill using different unit rates.

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7

else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Electricity Bill =", bill)


# CONDITIONAL STATEMENTS:

# 8. Check whether three sides can form a triangle.

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b > c and b + c > a and a + c > b:
    print("These sides can form a triangle")
else:
    print("These sides cannot form a triangle")

# 9. Determine the type of triangle (Equilateral, Isosceles, Scalene)

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b > c and b + c > a and a + c > b:

    if a == b == c:
        print("Equilateral Triangle")

    elif a == b or b == c or a == c:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

else:
    print("Not a valid triangle")

# 10. Create a simple ATM menu (Withdraw, Deposit, Balance)

balance = 10000

print("1. Withdraw")
print("2. Deposit")
print("3. Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance = balance - amount
        print("Please collect your cash")
        print("Remaining balance =", balance)
    else:
        print("Insufficient balance")

elif choice == 2:
    amount = int(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Amount deposited")
    print("New balance =", balance)

elif choice == 3:
    print("Your balance =", balance)

else:
    print("Invalid choice")

# 11. Calculate income tax based on different tax slabs

income = float(input("Enter your annual income: "))

if income <= 250000:
    tax = 0

elif income <= 500000:
    tax = (income - 250000) * 0.05

elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20

else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

print("Income Tax =", tax)

# 12. Create a menu-driven calculator using if-elif.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result =", a + b)

elif choice == 2:
    print("Result =", a - b)

elif choice == 3:
    print("Result =", a * b)

elif choice == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")


# LOOPS:

# 13. Print all prime numbers between 1 and n.

n = int(input("Enter n: "))

for num in range(2, n + 1):

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)

# 14. Find the factorial of a number using a loop.

num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)


# 15. Print Fibonacci series up to n terms

n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

# 16. Check whether a number is an Armstrong number

num = int(input("Enter a number: "))

original = num
digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# 17. Reverse a number and check if it is a palindrome.

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse =", reverse)

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

# 18. Find the Greatest Common Divisor (GCD) of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    remainder = a % b
    a = b
    b = remainder
print("GCD =", a)


# FUNCTIONS:

# 19. Write a function to check if a string is a palindrome.

def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False
word = input("Enter a string: ")

if palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")

# 20. Write a function to count vowels and consonants in a string.

def count_vowels_consonants(text):

    vowels = 0
    consonants = 0

    for ch in text.lower():

        if ch in "aeiou":
            vowels += 1

        elif ch.isalpha():
            consonants += 1

    return vowels, consonants


text = input("Enter a string: ")

v, c = count_vowels_consonants(text)

print("Vowels =", v)
print("Consonants =", c)

# 21. Create a function to calculate simple and compound interest.

def interest(p, r, t):

    simple_interest = (p * r * t) / 100

    compound_interest = p * (1 + r / 100) ** t - p

    return simple_interest, compound_interest


p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si, ci = interest(p, r, t)

print("Simple Interest =", si)
print("Compound Interest =", ci)

# 22. Write a function to return all factors of a number.

def factors(num):

    result = []

    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)

    return result


num = int(input("Enter a number: "))

print("Factors =", factors(num))

# 23. Write a function to find the second-largest number in a list.

def second_largest(numbers):

    numbers = list(set(numbers))
    numbers.sort()

    return numbers[-2]

my_list = [10, 20, 30, 40, 50]

print("Second largest =", second_largest(my_list))


# LISTS:

# 24. Merge two lists without duplicates.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = []

for value in list1 + list2:
    if value not in result:
        result.append(value)

print(result)

# 25. Find the second-largest and second-smallest elements.

numbers = [10, 20, 5, 40, 30]

numbers = list(set(numbers))
numbers.sort()

print("Second smallest =", numbers[1])
print("Second largest =", numbers[-2])

# 26. Rotate a list to the left by k positions

numbers = [1, 2, 3, 4, 5]

k = int(input("Enter k: "))

k = k % len(numbers)

result = numbers[k:] + numbers[:k]

print("Rotated list =", result)

# 27. Separate even and odd numbers into two lists.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = []
odd = []

for num in numbers:

    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers =", even)
print("Odd numbers =", odd)

# 28. Find the common elements between two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for value in list1:
    if value in list2:
        common.append(value)

print("Common elements =", common)


# TUPLES & SETS:

# 29. Count the frequency of each element in a tuple.

my_tuple = (1, 2, 2, 3, 3, 3, 4)

frequency = {}

for value in my_tuple:

    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

print(frequency)

# 30. Find the union, intersection, and difference of two sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union =", set1 | set2)
print("Intersection =", set1 & set2)
print("Difference =", set1 - set2)

# 31. Check whether one set is a subset of another.

set1 = {1, 2}
set2 = {1, 2, 3, 4}

if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")


# DICTIONARIES:

# 32. Count the frequency of words in a sentence.

sentence = input("Enter a sentence: ")

words = sentence.lower().split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)

# 33. Create a dictionary from two lists (keys and values).

keys = ["name", "age", "city"]
values = ["Sam", 21, "Nashik"]

my_dict = dict(zip(keys, values))

print(my_dict)

# 34. Sort a dictionary by its values.

my_dict = {"A": 50, "B": 20, "C": 40, "D": 10}

sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

print(sorted_dict)


# FILE HANDLING:

# 35. Read a text file and count the number of lines, words, and characters.

file = open("sample.txt", "r")

lines = file.readlines()

line_count = len(lines)
word_count = 0
character_count = 0

for line in lines:
    word_count += len(line.split())
    character_count += len(line)

file.close()

print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Number of characters:", character_count)

# 36. Copy only the even-numbered lines from one file to another.

file1 = open("source.txt", "r")
file2 = open("even_lines.txt", "w")

lines = file1.readlines()

for i in range(len(lines)):

    if (i + 1) % 2 == 0:
        file2.write(lines[i])

file1.close()
file2.close()

print("Even-numbered lines copied")


# EXCEPTION HANDLING:

# 38. Handle file-not-found error

try:

    file = open("sample.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File not found!")


# MODULES:

# 39. Random password generator

import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your password is:", password)


# 40. Calculate number of days between two dates

from datetime import datetime

date1 = input("Enter first date (DD-MM-YYYY): ")
date2 = input("Enter second date (DD-MM-YYYY): ")

date1 = datetime.strptime(date1, "%d-%m-%Y")
date2 = datetime.strptime(date2, "%d-%m-%Y")

difference = date2 - date1

print("Number of days =", abs(difference.days))