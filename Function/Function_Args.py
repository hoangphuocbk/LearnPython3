#!/usr/bin/env python3
# -*- coding: utf-8 i-*-
import getpass

def Connect ( server, user, port, password):
	password = encode(password)
	print("You connected to {0} at port {1} with user {2} and password {3}".format(server,port,user,password))

def encode(str):
	getlen = len(str)
	newstr = ''
	for i in range(0,getlen):
		if(i < getlen-3):
			newstr = newstr + '*'
		else:
			newstr = newstr + str[i]

	return newstr

if __name__ == '__main__':
	print("Connecting to mysql server!!!")
	server = input("Put server name here [default: localhost] ") or "localhost"
	try:
		port = int(input("Put server port here [default: 3306] "))
	except ValueError:
		port = 3306
		pass
	user = input("Put user name here [default: root] ") or "root"
	password = getpass.getpass("Put server password here: ")
	
	Connect(server,user,port,password)
