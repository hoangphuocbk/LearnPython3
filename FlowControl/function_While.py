#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

try:
	age = int(input("Write your age: "))
except ValueError:
	print("You put the value that is not number!")
	sys.exit()

while(age<=18):
	print("Your are {0} years old ".format(age))
	print("\nOne year latter!")
	age +=1


print("Now, you are adult")
