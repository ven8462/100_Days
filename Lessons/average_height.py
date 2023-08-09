#!/usr/bin/python3

# a program that calculates the average height of students.

height_of_students = input("Enter height of students separated by a space? ")
all_heights = height_of_students.split()
sum = 0
for n in range(0, len(all_heights)):
    all_heights[n] = int(all_heights[n])
print(all_heights)
for i in all_heights:
        sum += i
print(sum)
average = sum / len(all_heights)
print(average)