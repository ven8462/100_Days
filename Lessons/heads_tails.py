#!/usr/bin/python3

# Write a program that tells a user Heads or Tails Depending on What the choose

import random

choice = random.randint(0, 1)

if choice == 0:
    print("Heads")
else:
    print("Tails")