# 1. Write a Python program to check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")



# 2. Write a program to find the largest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number =", largest)

# 3. Write a program to check whether a given number is prime

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

# 4. Write a program to print the Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

# 5. Write a program to find the factorial of a number using a loop.


num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)


# 6. Write a program to reverse a string without using [::-1].


text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed string =", reverse)


# 7. Write a program to check whether a string is a palindrome.


text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


# 8. Write a program to count the number of vowels and consonants in a string.


text = input("Enter a string: ")

vowels = 0
consonants = 0

for char in text.lower():

    if char in "aeiou":
        vowels += 1

    elif char.isalpha():
        consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)


# 9. Write a program to find the sum of all elements in a list

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

print("Sum =", total)


# 10. 10. Write a program to find the largest and smallest element in a list without using max() or min().

numbers = [25, 10, 45, 5, 30]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest =", largest)
print("Smallest =", smallest)


# 11. Write a program to remove duplicate elements from a list.

numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

for num in numbers:

    if num not in unique:
        unique.append(num)

print("List after removing duplicates =", unique)


# 12. Write a program to count how many times each element appears in a list using a dictionary.


numbers = [10, 20, 10, 30, 20, 10]

frequency = {}

for num in numbers:

    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1

print(frequency)


# 13. Write a program to find the second-largest number in a list.


numbers = [10, 50, 30, 40, 20]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:

    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("Largest =", largest)
print("Second largest =", second_largest)


# 14. Write a program to sort a list without using sort() or sorted().

numbers = [50, 20, 40, 10, 30]

n = len(numbers)

for i in range(n):

    for j in range(0, n - i - 1):

        if numbers[j] > numbers[j + 1]:

            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Sorted list =", numbers)


# 15. Write a function that accepts a list of numbers and returns a list containing only the even numbers.

def even_numbers(numbers):

    result = []

    for num in numbers:

        if num % 2 == 0:
            result.append(num)

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(even_numbers(numbers))

# 16. Write a program to find the frequency of each character in a string.

text = input("Enter a string: ")

frequency = {}

for char in text:

    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

print(frequency)


# 17. Write a program to check whether two strings are anagrams of each other.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.lower()
str2 = str2.lower()

if len(str1) != len(str2):
    print("Not anagrams")
else:

    frequency1 = {}
    frequency2 = {}

    for char in str1:
        if char in frequency1:
            frequency1[char] += 1
        else:
            frequency1[char] = 1

    for char in str2:
        if char in frequency2:
            frequency2[char] += 1
        else:
            frequency2[char] = 1

    if frequency1 == frequency2:
        print("Anagrams")
    else:
        print("Not anagrams")

# 18.Write a program to find all duplicate values in a list.

numbers = [10, 20, 10, 30, 20, 40, 50, 30]

duplicates = []

for num in numbers:

    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate values =", duplicates)



# 19. Write a program that takes a sentence and finds the longest word.


sentence = input("Enter a sentence: ")

words = sentence.split()

longest = words[0]

for word in words:

    if len(word) > len(longest):
        longest = word

print("Longest word =", longest)


# 20. Create a simple student marks program that:

# a. accepts marks for 5 subjects,
# b. calculates the total and percentage,
# c. assigns a grade,and displays whether the student passed or failed.

marks = []

for i in range(5):

    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))

    marks.append(mark)


total = 0

for mark in marks:
    total = total + mark

percentage = total / 5

if percentage >= 90:
    grade = "A+"

elif percentage >= 80:
    grade = "A"

elif percentage >= 70:
    grade = "B"

elif percentage >= 60:
    grade = "C"

elif percentage >= 50:
    grade = "D"

else:
    grade = "F"

if percentage >= 40:
    result = "Pass"
    
else:
    result = "Fail"


print("\n Student Result")
print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)
print("Result =", result)