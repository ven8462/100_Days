#!/usr/bin/python3
# the format of if else statement is:
"""
if condition:
    do something if condition is true
else:
    do something if the previous condition was wrong.

"""

print("Welcome to the rollercoaster!")

height = int(input("What is your height? "))

if height >= 120:
    print("Eligiable");
else:
    print("Not Eligiable")