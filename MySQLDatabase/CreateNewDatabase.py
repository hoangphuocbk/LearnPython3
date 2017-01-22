#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql.cursors
import re

# read file MySQLConfig.txt
f = open("./install/MySQLConfig.txt","r")

mysql_user = ''
mysql_pass = ''
mysql_port = 3306

for line in f:
	clean_line = line.strip()
	line_data = line.split("=")
	if line_data[0] == "mysql_user":
		mysql_user = re.sub(r'^"|"$','',line_data[1].strip())
	elif line_data[0] == "mysql_pass":
		mysql_pass = re.sub(r'^"|"$','',line_data[1].strip())
	elif line_data[0] == "mysql_port":
		mysql_port = int(re.sub(r'^"|"$','',line_data[1].strip()))

print("mysql_user:",mysql_user )
print("mysql_pass:",mysql_pass)
print("mysql_port:",mysql_port)
