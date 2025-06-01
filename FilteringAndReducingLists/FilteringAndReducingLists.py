# Purpose: Demonstrate filtering and reducing lists in Python.
numlist = [1, 2, 3, 4, 5, 6]

# How to use map and list functions
def square(n):
    return n * n

squares = map(square, numlist)
squares = list(squares)
print("Results: ", squares)

# Filtering: using filter function
def is_even(n):
    return n % 2 == 0

evens = filter(is_even, numlist)
evens = list(evens)
print("Even numbers: ", evens)

# Reducing: using reduce function
import functools
def add_square(total, current):
    return total + (current * current)

total = functools.reduce(add_square, numlist)
total = functools.reduce(add_square, numlist, 10)
# total = functools.reduce(add_square, numlist, start=10) #Type Error because of Python 3 syntax
# Doesnt allow you to pass the optional start value as a keyword argument

print("Total of squares: ", total)

# How to work with list comprehensions and creating a new list from an existing
# This could be more about Project 2
# newlist = [expression for item in list [if condition]]

# A list of numbers 
numbers = [1, 2, 3, 4, 5, 6]

# A loop that creates a list of the squares of the number
squares = []
for n in numbers:
    squares.append(n * n)

# A list comprehension thgat creates a list of the squares of the numbers
squares = [n * n for n in numbers]

# A list comprehension that uses a conditional expression for filtering
even_squares = [n * n for n in numbers if n % 2 == 0]
print("Even squares: ", even_squares)

# A list of comprehension that calls functions
def square(n):
    return n * n
def is_even(n):
    return n % 2 == 0

even_squares = [square(n) for n in numbers if is_even(n)]
print("Results: ", even_squares)

# A list comprehension that uses assignment expressions and works with a function to return value
import random

def get_number():
    return random.randrange(1, 10)

squares = [square(num) for n in range(10) if (num := get_number()) <= 6]
print("Result: ", squares)

