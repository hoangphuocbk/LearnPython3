#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def checkEven(num):
	if num%2 == 0:
		print(num)
		return True
	else:
		return False
# Lambda function
square = lambda num: num**2

if __name__ == '__main__':
	for i in range(1, 5):
		checkEven(i)
	print("\n###################\n")
	
	for i in range(1, 5):
		print(square(i))
