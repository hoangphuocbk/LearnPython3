#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# r = map(func, seq)
# map() applies the function func to all elements of the sequence seq

def FahtoCel(F):
	return (F-32)*(5/9)

def CeltoFah(C):
	return C*(9/5) +32

if __name__ == '__main__':
	# list temperatures in Celsius
	temperaturesC = [12, 18, 24, 28, 32]
	# print it first
	print("Temperatures in Celsius: ")
	for temp in temperaturesC:
		print(str(temp), end = "\t")
	print()
	
	print("Temperatures in Farenheit: ")
	temperaturesF = map(CeltoFah, temperaturesC)
	
	# print temperatures are converted to Farenheit
	for temp in temperaturesF:
		print(str(temp), end = "\t")
	print()
