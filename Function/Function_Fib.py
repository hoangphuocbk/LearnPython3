#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if(len(sys.argv) < 2):
	print("You should add 1 number as argument!")
	sys.exit()

try:
	n = int(sys.argv[1])
except ValueError:
	print("Please put number not the other")
	sys.exit()

# print up to nth number of Fibonaci
def Fib(n):
	iLast = 1
	iSecondLast = 0
	list = [0,1]

	for i in range(2,n):
		new_element = iLast + iSecondLast
		list.append(new_element)
		iSecondLast = iLast
		iLast = new_element

	return list

list = Fib(n)

print(list)
