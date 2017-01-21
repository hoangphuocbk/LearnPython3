#!/bin/bash
  
 # Install pip first
 if [ hash pip3 2>/dev/null; ]
 then
 	echo "You already installed python3-pip"
 else
 	echo "You don't install python3-pip"
 	echo "Do you want to install it? (y/n)"
 	read input_var
 	if [ $input_var == "y" ]
 		then
 			sudo apt-get install -y python3-pip
 	fi
 fi

# Install necessary packages
sudo apt-get -y install python-dev libmysqlclient-dev
sudo pip install wheel

# Install MySQL connector for python
sudo pip3 install --egg -r ./requirements.txt

if [ $? == 0 ]
then
	echo "MySQL connector was installed successfully~"
else
	echo "Installing MySQL connector was failed~"
fi
