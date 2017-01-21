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

mkdir ~/mysqlDir
sudo docker run --name mysql-server -p 3306:3306 -v ~/mysqlDir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=yoursecret -d mysql
