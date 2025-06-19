#!/bin/python3

'''
Ask the user to input the principal amount, rate of interest, and time period and calculate the simple interest.
'''

# Simple Interest Calculation
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))

simple_interest = (principal * rate * time) / 100
print("The simple interest is", simple_interest)
