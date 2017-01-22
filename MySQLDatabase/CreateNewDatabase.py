#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql.cursors
import re

# read file MySQLConfig.txt
def readConfig(path):
	#f = open("./install/MySQLConfig.txt","r")
	f = open(path , "r")

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
	
	dict = {"user":mysql_user , "passwd":mysql_pass , "port":mysql_port}
	return dict

if __name__ == '__main__':
	configs = readConfig("./install/MySQLConfig.txt")
	# connect to the database
	connection = pymysql.connect(host = 'localhost',
								user = configs['user'],
								password = configs['passwd'])

	try:
		with connection.cursor() as cursor:
			sql = "CREATE DATABASE IF NOT EXISTS myDatabase;"
			cursor.execute(sql)
			sql = "use myDatabase;"
			cursor.execute(sql)
			# create table users
			sql = '''CREATE TABLE users (
			    id int(11) NOT NULL AUTO_INCREMENT,
			    email varchar(255) COLLATE utf8_bin NOT NULL,
			    password varchar(255) COLLATE utf8_bin NOT NULL,
			    PRIMARY KEY (id)
				) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
				AUTO_INCREMENT=1 ;
			'''
			cursor.execute(sql)

		connection.commit()
	finally:
		connection.close()
