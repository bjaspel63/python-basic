#!/bin/python3

'''
Ask the user to input a number and determine if it is positive, negative, or zero.
'''

number = float(input("Enter a number: "))

if number > 0:
  print(number," is positive.")
  
elif number < 0:
  print(number," is negative.")
  
else:
  print(number," is zero.")
