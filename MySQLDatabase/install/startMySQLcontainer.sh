#!/bin/bash

# Check installing docker first
sudo docker -v 2>/dev/null
if [ $? == 0 ]
then
	echo "You installed docker. We will run container now"
else
	echo "You dont install docker. We will install it first"
	wget -qO- https://get.docker.com/ | sh

	# Add user to group docker
	username=$(whoami)
	sudo usermod -aG docker $username
fi

# Run docker MySQL container
# Read MySQL configuration
source ./MySQLConfig.txt

mkdir ~/mysqlDir
sudo docker run --name mysql-server -p $mysql_port:3306 -v ~/mysqlDir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=$mysql_pass -e MYSQL_USER=$mysql_user -d mysql
