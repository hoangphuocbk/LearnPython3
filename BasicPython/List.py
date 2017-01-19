#!/usr/bin/env python3
# -*- coding: utf-8 -*-

listChars = ["A","B","C"]
# print list
print(listChars)

# print type list
print(type(listChars))

# print first element
print(listChars[0])

# append new character
listChars.append("D")
print(listChars)

# insert new character at index 2
listChars.insert(2,"M")
print(listChars)

# extend list 
listChars.extend(["hit","run"])
print(listChars)

# get last element
last = listChars.pop()
print(last)

# remove element
listChars.remove("hit")
del listChars[0]
print(listChars)

# print index of character
print(listChars.index("B"))
