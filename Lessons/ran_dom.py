#!/usr/bin/python3

# to use random fuction you need to import the random module
# random returns random values in a range you've given it.

# randint() - generates random integer numbers
# random() - generates random float numbers, it does not take arguments.


import random

random_int = random.randint(1, 10)
random_float = random.random()
print(random_int)
print(random_float)