#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    digit = number % 10
else:
    digit = ((number * -1) % 10) * -1

print("Last digit of {:d} is {:d}".format(number, digit), end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("less than 6 and not 0")
