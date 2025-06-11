#!/bin/python3

#A function is a block of reusable code that performs a specific task.

def say_hello():
  print("Hello World!")

say_hello()

#Parameters are variables listed in a function definition.
#Arguments are the actual values passed when calling the function.

def greet(name):
  print("Hello, " + name + "!")

greet("Alice")

#Use return to send back a value from a function.
def square(x):
  return x * x

result = square(5)
print(result)

def area(length, width):
    return length * width  # Area = length × width

# Example
print("Area is:", area(5, 10))  # 50

#function with string
def introduce(name, age):
    print("Hi, I'm " + name + " and I'm " + str(age) + " years old.")

# Call the function
introduce("Liam", 14)
