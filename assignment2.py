# 1.Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd"

def Evenodd(num):
    if num %2 ==0:
        return f"This is even number"
    else:
        return f"This is odd number"
    
print(Evenodd(24))


# 2.write a function largest(a,b) that returns the larger number

def large(a,b):
    if a > b:
        return "a is greater"
    else:
        return "b is greater"
    
print(large(50,70))


# 3.wite a function print_numbers(n) that prints numbers from 1 to n using a loop

def print_numbers(n):
    for i in range(1, n+1):
        print(i)

print_numbers(20)


# 4.write a function sum_n(n) that returns the sum of numbers from 1 to n 

def sum_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

print(sum_n(6))


# 5.Write a function table(n) that prints the multiplication table of n from 1 to 10.

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

table(5)


# 6.Write a function that takes a list and returns how many even numbers it contains.

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

nums = [2, 5, 8, 11, 14, 17, 20, 22]
print("Number of even numbers:", count_even(nums))


# 7.Without using max(), write a function that returns the largest number in a list

def largest(list):
    largest = list[0]
    for num in list:
        if num > largest:
            largest = num
    return largest

print(largest([5, 8, 2, 10, 3, 40]))


# 8.FizzBuzz
# Write a function that prints numbers from 1 to 100.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".

def FizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

FizzBuzz()

# 9.Write a function that returns True if a string is a palindrome.

def palindrome(s):
    return s == s[::-1]

print(palindrome("madam"))
print(palindrome("hello"))

# 10.Write a function that counts the vowels in a string.

def count_vowels(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count += 1
    return count

print(count_vowels("Hello"))

# 11.Write a function that returns the second largest number in a list without using sort().

def second_largest(list):
    largest = max(list)
    list.remove(largest)
    return max(list)

print(second_largest([10, 20, 5, 15, 18]))

# 12.Guessing Game
# Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions.

def guess_game():
    number = 5

    while True:
        guess = int(input("Guess a number (1-10): "))

        if guess == number:
            print("Correct!")
            break
        else:
            print("Try Again!")

guess_game()

# 13.Write a function grade(marks) that:
# Returns "A" for marks ≥ 90
# Returns "B" for marks ≥ 80
# Returns "C" for marks ≥ 70
# Returns "D" for marks ≥ 60
# Otherwise returns "F"

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print(grade(95))
print(grade(82))
print(grade(75))
print(grade(65))
print(grade(50))