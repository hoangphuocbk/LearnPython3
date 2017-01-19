#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print("############################################")
print()

# get python version
pythonVer = sys.version_info.major

if(pythonVer == 2):
	print("You are using Python version 2.x")
elif(pythonVer == 3):
	print("You are using Python version 3.x")
else:
	print("I don't know your Python version!")

print()
print("############################################")

### new test 
yournum = 0
try:
	yournum = int(input("Enter your number: "))
except ValueError:
	print("It's not a number")

if(yournum == 7):
	print("We have the same thought!")
else:
	print("We don't match each other!")

print("done")
print("############################################")
