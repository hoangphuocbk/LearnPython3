#!/bin/bash

# Check installing docker first
if [ hash docker 2>/dev/null; ]
then
	echo "You installed docker. We will run container now"
else
	echo "You dont install docker. We will install it first"
	wget -qO- https://get.docker.com/ | sh
fi

# Add user to group docker
username=$(whoami)
sudo usermod -aG docker $username 
# Run docker MySQL container

mkdir ~/mysqlDir
sudo docker run --name mysql-server -v ~/mysqlDir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=yoursecret -d mysql
