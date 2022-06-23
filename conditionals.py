# The datatype that is important for conditionals is the boolean.

# Boolean : True / False
# Syntax (the way we write the code)

# if - else constructions
# isCold = False
# if isCold:
#     print("It is cold outside.")
# else:
#     print("It is very hot outside.")
#     print("It is hot outside.")

# Regular operators: + - / *
# Comparison operators: < (less than), > (greater than), == (equal to), <= (less than or equal to), >= (greater than or equal to)
# print(3 > 4) # The comparison operators return a BOOLEAN
# print(3 == 4)
# print("3" == 3)

# age = 17  # assignment

# if (age > 17):
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# if (age < 18):
#     print("You are a minor.")
# else:
#     print("You are an adult.")

# if (age == 17):
#     print("You can go on the ride!")
# else:
#     print("You are not allowed on the ride.")

# temperature = 10
# if (temperature > 80):
#     print("It is VERY hot outside.")
# else:
#     if (temperature > 50 and temperature < 80):
#         print("It is fair outside.")
#     else:
#         print("It is cold outside.")

# Conditional operators
# and: BOTH have to be true
# or: Either one has to be true

# Tests for the "and" operator
# "and" is true when BOTH are true
# print(True and True)  # True
# print(True and False)  # False
# print(False and True)  # False
# print(False and False)  # False

# Tests for the "or" operator
# "or" is true when EITHER are true
# print(True or True)  # True
# print(True or False)  # True
# print(False or True)  # True
# print(False or False)  # False

# input()
# age = input("Enter your age: ") # the input method stores a String
# print(age * 2) # age is a String here, here the String gets duplicated instead of multiplying the age by 2

# MENTION SHORT-CIRCUITING

# print((False and True) or (True and True))
# print(False or True)
# print(True)

# print(False and True)  # Short-circuiting : skips the "True"
# print(True or False)  # Short-circuiting: skips the "False"

# age = 13
# height = 70.5
# name = "John"
# String concatenation - adding strings together
# print("You are " + age + " years old")

# Formatted string
# print(f"You are {age} {height} {name} years old")

# Sample program
# Rules:
# You have to be at least 12 years old to play the game.
# You are allowed to play if you are older than 12:
# If you make the toss within 3 tries, then you win
# Otherwise, you have to walk across the pool
# If you make it across the pool, you win $500,000
# Otherwise you go home.

# Greater than or equal to: >= (AT LEAST/MINIMUM)
# Less than or equal to: <= (AT MOST/MAXIMUM)

# Type-casting into an integer, because input() returns a String
# age = int(input("How old are you? "))  # age is now an Integer, not a String
# if (age >= 12):
#     print("You can play the game!")
#     print("Welcome to the Ring Game!")
#     # tosses is now an Integer
#     tosses = int(input("How many tosses did it take you? "))
#     if (tosses <= 3):
#         print("You won!")
#     else:
#         print("You have to walk across the pool. :(")
#         madeItAcross = input("Did you make it across the pool? ")
#         # checks to see if the inputted String in all CAPITAL is "YES"
#         if (madeItAcross.upper() == "YES"):  # yES yEs allowed
#             print("You won $500,000!")
#         else:
#             print("Go home!")
# else:
#     print("You cannot play.")

# The "not" operator - negate (make it opposite) a boolean
# isYoung = False
# if not isYoung:
#     print("You are not young.")
# else:
#     print("You are young.")


# != operator(Not equal)
# age = 3
# if age != 18:
#     print("You cannot play.")
# else:
#     print("You can play!")

# Same as below:
# if age == 18:
#     print("You can play!")
# else:
#     print("You cannot play.")
