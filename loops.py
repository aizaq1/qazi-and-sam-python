# A loop is a way for us to do something many times (as many times as we want or infinitely many times)

# The "while" loop - constantly checking a condition
# while True:
#     print("Hello")

# Keyboard Interrupt – CONTROL + C

# import time

# count = 2
# while True:
#     print(count)
#     # count = count + 1  # Increase the variable by 1
#     time.sleep(1)  # Wait one second
#     count *= 2  # Same as above

# Simple Program:
# Guessing game

# from random import Random
# import random  # Assume for now that this imports a library that we need

# Get a random integer from 1 to the maximum (chosen by the user) and set it equal to the variable number
# maximum = int(input("Enter a maximum value: "))
# targetAnswer = random.randint(1, maximum)  # random integer

# Ask the user for a guess
# guess = int(input(f"Guess a number from 1 to {maximum}: "))

# while guess != targetAnswer:
#     # asks the user for a new guess
# if (abs(guess - targetAnswer) <= 10):
#         guess = int(
#             input(f"Within 10. Guess a number from 1 to {maximum}: "))
#     else:
#         if (abs(guess - targetAnswer) <= 20):
#             guess = int(
#                 input(f"Within 20. Guess a number from 1 to {maximum}: "))
#         else:
#             if (abs(guess - targetAnswer) <= 30):
#                 guess = int(
#                     input(f"Within 30. Guess a number from 1 to {maximum}: "))
#             else:
#                 if (abs(guess - targetAnswer) <= 40):
#                     guess = int(
#                         input(f"Within 40. Guess a number from 1 to {maximum}: "))
#                 else:
#                     guess = int(
#                         input(f"Over 50. Guess a number from 1 to {maximum}: "))
# # the while loop exits when the user guesses correctly
# print(f"You guessed it! The number was {targetAnswer}.")

# For loops
# number = "123456789"
# # for [a reference variable] in [variable name of the data structure]:
# # [Tell it what to do]
# for num in number:  # "Iteration"/"iterate"
#     print(num)

# List/Array - another data structure that we will go more in depth with later on
# numbers = [3, 4, 1, 8, 9, 10, 6, 7, 9]  # an example of a list of integers
# for number in numbers:
#     print(number)

# The range() method

# Range() with one parameter
# range(5) : generates 0, 1, 2, 3, 4
# range(10): generates 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# Range() with two parameters
# range(1, 5): generates 1, 2, 3, 4
# range(2, 10): generates 2, 3, 4, 5, 6, 7, 8, 9

# Range() with three parameters
# range(1, 10, 2): 1, 3, 5, 7, 9
# range(2, 15, 3): 2, 5, 8, 11, 14

# Using a for-loop with range
# for variable in range(something):

# for number in range(2, 15, 3):
#     print(number)
