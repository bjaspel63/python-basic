#!/bin/python3

'''
Ask the user to input their age and print if they are a minor or an adult.
'''

# Simple Age Check
age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

