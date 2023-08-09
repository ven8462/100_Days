#!/usr/bin/python3

#calculates the sum of nums even between 1 to 100

sum = 0

for num in range(1, 101):
    #print(num)
    if num % 2 == 0:
        sum += num
    else:
        pass
print(sum)

