#!/bin/python3
'''
Ask the user to input a password and check if it matches a predefined password.
'''

# Simple Password Check
password = "python123"
user_input = input("Enter the password: ")

if user_input == password:
    print("Access granted.")
else:
    print("Access denied.")
