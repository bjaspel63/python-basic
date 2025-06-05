#!/bin/python3

#create a lists

# List of fruits
fruits = ["apple", "banana", "cherry"]

# Empty list
empty = []

# List of numbers
numbers = [5, 10, 15, 20]

# Mixed types
mixed = ["text", 123, True]

#print(",".join(fruits))

#accessing items
fruits = ["apple", "banana", "cherry"]

print(fruits[0])     # apple (first item)
print(fruits[1])     # banana
print(fruits[-1])    # cherry (last item)

#adding item on a lists
# Add to the end
fruits.append("tomato")

# Insert at a specific index
fruits.insert(1, "grapes")  # at index 1
print(",".join(fruits))

#removing items
# Remove by value
fruits.remove("grapes")

# Remove by index
fruits.pop(0)     # removes the first item

# Delete by index
del fruits[1]
print(", ".join(fruits))


#looping
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like ",fruit)
    
#checking
if "apple" in fruits:
    print("Apple is in the list!")

#input
# Ask the user for 3 favorite fruits
fruit1 = input("Enter a fruit: ")
fruit2 = input("Enter another fruit: ")
fruit3 = input("Enter one more fruit: ")

# Store in a list
fruits = [fruit1, fruit2, fruit3]

print("Your fruit list:", ", ".join(fruits))
