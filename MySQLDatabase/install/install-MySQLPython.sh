#!/bin/bash

# Install python-mysql-connector
wget https://cdn.mysql.com//Downloads/Connector-Python/mysql-connector-python-py3_2.1.5-1ubuntu14.04_all.deb

sudo dpkg -i PACKAGE.deb

rm mysql-connector-python-py3_2.1.5-1ubuntu14.04_all.deb	# delete file

# Install mysql-client
sudo apt-get install -y mysql-client
