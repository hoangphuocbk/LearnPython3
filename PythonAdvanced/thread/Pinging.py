#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from threading import Thread

class ip_check(Thread):
	
	received_packages = re.compile(r"(\d) received")
	def __init__(self, ip):
		Thread.__init__(self)
		self.ip = ip
		self.__successful_pings = -1

	def run(self):
		ping_out = os.popen("ping -q -c2 " + self.ip, "r")
		while True:
			line = ping_out.readline()
			if not line:
				break
			n_received = re.findall(ip_check.received_packages, line)
			if n_received:
				self.__successful_pings = int(n_received[0])
	def status(self):
		if self.__successful_pings == 0:
			return "no response"
		elif self.__successful_pings == 1:
			return "alive, but 50 % package loss"
		elif self.__successful_pings == 2:
			return "alive"

check_results = []
for suffix in range (15,17):
	ip = "10.0.2." + str(suffix)

	current = ip_check(ip)
	check_results.append(current)
	current.start()

for i in check_results:
	# the operation will block util the thread terminates
	i.join()
	print("Status from {0} is {1}.".format(i.ip, i.status()))
