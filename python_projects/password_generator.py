#!/usr/bin/python3

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h',  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E','F', 'J', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['~', '#', '$', '%', '*', '+']

print("Welcome to Ven's password generator")

nl = int(input("How many letters do you want?"))
nn = int(input("how many numbers do you want? "))

ns = int(input("how many symbols do you want? "))


"""Easy Level
password = ""

for char in range(1, nl + 1):
    pas = random.choice(letters)
    password += pas
for n in range(1, nn + 1):
    pas = random.choice(numbers)
    password += pas
for s in range(1, ns + 1):
    pas = random.choice(symbols)
    password += pas
print("your password is:  {}".format(password))
"""


# Hard Level

password_list = []

for char in range(1, nl + 1):
    pas = random.choice(letters)
    password_list += pas
for n in range(1, nn + 1):
    pas = random.choice(numbers)
    password_list += pas
for s in range(1, ns + 1):
    pas = random.choice(symbols)
    password_list += pas
print(password_list)

random.shuffle(password_list)
print(password_list)
#password = "".join(password_list)
"""for char in password_list:
    password += char"""
print("your password_list is:  {}".format(password))