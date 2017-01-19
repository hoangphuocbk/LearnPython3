#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# create new list 
list = [2**i for i in range(0,11,2)]
print(list)

# create new dict
newl = ["Python", "Javascript", "Golang"]
dict = {key : str(len(key)) for key in newl}

print(dict)
for item in dict:
	print(item + " ---> " + dict[item] )
