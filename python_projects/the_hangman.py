#!/usr/bin/python3
import random

word = ["ven", "apple", "rice", "dog"]

guess_word = random.choice(word)

print(guess_word)

for i in guess_word:
    print('_', end=' ')
print()


letter = input("Enter a letter: ")
if letter in guess_word:
    index = guess_word.index(letter)
else:
    pass

for i in range(len(guess_word)):
    if i == index:
        print(letter, end=' ')
    else:
        print("_", end=' ')
print()







  

    
