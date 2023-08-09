#!/usr/bin/python3

# spilt() - is used to split a string into a list.

import random

all_names = input("Enter names separated by commas: ")
names = all_names.split(", ")

# print(names)
#list = len(names)

#person = random.randint(0, list -1)

#print(f"{names[person]}, is gonna pay the bill")


name = random.choice(names)
print(name)