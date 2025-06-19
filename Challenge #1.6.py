#!/bin/python3

'''
Ask the user to input a temperature in Celsius and convert it to Fahrenheit.
'''

# Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(celsius, "°C is equal to", fahrenheit, "°F.")

