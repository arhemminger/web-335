"""
============================================
; Title:  Calculator
; Author: Professor Krasso
; Date:  23 June 2019
; Modified by: Andrew Hemminger
; Description: Exercise 8.3 – Calculator
;===========================================
"""
first_name = 'Andrew'

last_name = 'Hemminger'

print(first_name + ' ' + last_name)


# Add function - 2 param. num. values
def add(num1, num2):

    return num1 + num2

# Subtract function - 2 param. num. values
def subtract(num1, num2):

    return num1 - num2

# Divide function - 2 param. num. values
def divide(num1, num2):

    return num1 / num2


# Calling math functions
print(add(1,2))

print(subtract(4,1))

print(divide(8,2))