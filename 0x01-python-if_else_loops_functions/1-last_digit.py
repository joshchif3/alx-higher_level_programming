#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str2 = " and is 0"
str1 = " and is greater than 5"
str3 = " and is less than 6 and not 0"
if number < 0:
	lastnum = number % -10
else:
	lastnum = number % 10
if lastnum > 5:
	print("Last digit of {:d} is {:d} and is greater than 5".format(number, lastnum))
elif lastnum < 6 and lastnum != 0:
	print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, lastnum))
else:
	print("Last digit of {:d} is 0 and is 0".format(number))
