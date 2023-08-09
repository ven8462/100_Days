#!/usr/bin/python3

print("Welcome to Ven's Pizza Deliveries!")
print()
size = input("What size pizza do you want? S, M, L :")
print()
add_pepperoni = input("Do you want pepperoni? Y or N :  ")
print()
extra_cheese = input("Do you want extra cheese? Y or N : ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "N":
    bill += 1

print()
print(f"your final bill is {bill}")


