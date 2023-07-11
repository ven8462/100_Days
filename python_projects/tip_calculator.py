#!/usr/bin/python3

print("Welcome to the tip calculator")

bill = float(input("What was the total bill? "))

percentage = float(input("What percentage tip would you like to give?"))

total_bill = float( bill * (percentage / 100) + bill)

people = int(input("How many people to split the bill? "))

ind_pay = float(total_bill / people)

print("Each person should pay: {:.2f}".format(ind_pay))
