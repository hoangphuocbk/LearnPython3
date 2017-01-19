#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# define new dictionary
my_dict = {"server":"127.0.0.1" , "user":"root", "port":3306}

# print type and dict name
print(type(my_dict))
print(my_dict)

# print length dict
print(len(my_dict))

# get server's value
print(my_dict["server"])
print(my_dict.get("server"))
