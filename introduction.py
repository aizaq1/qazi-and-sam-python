# Data Types

# 1. Strings - Always use quotations

# introduction = "Hello my name is Qazi"

# Primitive(simple) Data Types

# 2. Variables
# greeting = "Hello everyone"
# The string "Hello everyone" is ASSIGNED to the variable: greeting

# print(greeting)

# 3. Integers
# age = 13
# The integer 13 is ASSIGNED to the variable: age
# print(age)

# print("4"*100) # prints "4" one hundred times

# Arithmetic
# print(age + 5)  # Addition
# print(age - 2)  # Subtraction
# print(age * 2)  # Multiplication [Located above 8 on the keyboard]
# print(age / 2)  # Division [Located below the question mark on the keyboard]

# 4. Floating Point Numbers or Floats (Decimals)
#    Doubles (Also Decimals)

# print(13.3)
# print(-0.353345)

# 5. Booleans (True / False)
# Camel Case - first word is lowercase and every other word is capitilized.
# isCold = False
# if isCold:
#     print("It is cold outside.")

# print(True)

# AVOID THIS: (BOOLEAN AS THE VARIABLE NAME)
# true = "John"
# print(true)

# age = 13

# age = 30
# name = "John"
# employeeRating = 9.8

# print(age * 2)

# ageString = "30"

# print(ageString * 2)

# In Java, the boolean True is actually true (spelled lowercase). So we probably don't want to use this kind of variable name.

# Keywords: do not use as variable names
# for
# in
# this
# while
# if
# else

# Why do we use different data types?

# print("Hello world\n" * 100)
# Escape sequence: BACKSLASH (\) + A LETTER
# \b - backspace
# \t - tab
# \n - new line
# \\ - new backslash

# print("/\\")

# Methods - A method is basically an operation on a data type or a variable

# greeting = "Hello EVERYONE MY NAME IS JOHN"

# To call a method, use a DOT (.) followed by the method name, and then by open and closed parentheses (). Methods must be called on objects.
# if you want to see the changes, reassign to the variable
# greeting = greeting.upper()
# greeting.lower()

# print(greeting.lower())
# print(greeting)

# greeting = greeting.lower()
# print(greeting)

# print(greeting.split())  # Returns an Array/List
# The default split location or "splitter" is the SPACE

# addresses = "5630 27th Avenue | 7930 87th Street | 3530 90th Road | 2323 65th Drive"
# print(addresses.split(" | "))  # A parameter

# greeting = "Hello EVERYONE MY NAME IS JOHN"

# print(greeting.startswith(" He"))  # Prints False
# print(greeting.endswith("John"))  # Prints False

# .count() to count the number of occurrences

# print(greeting.count("E"))

# name = "John Smith"
# len() for checking the length of the string - number of characters
# print(len(name) - 1)

# firstInitial = "J"
# lastInitial = "3"
# print(firstInitial.isalpha())  # Is it part of an alphabet?
# print(lastInitial.isalpha())

# age = "15"
# print(age.isnumeric())  # Is it a number?

# greeting = "Hello world hello everyone hello humanity"
# replace all (lowercase) "h" with (uppercase) "X"
# print(greeting.replace("h", "X"))

# print(greeting.isascii())
# ASCII We will look at this a little more later on through some examples
