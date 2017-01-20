#!/bin/sh

# Install pip first
if hash pip 2>/dev/null;
then
	echo "You already installed python-pip"
else
	echo "You don't install python-pip"
	echo -e "Do you want to install it? (y/n) \c"
	read
	if "$REPLY" = "y";
		then
			sudo apt-get install -y python-pip

	fi
fi

# Install necessary packages
sudo apt-get -y install python-dev libmysqlclient-dev

# Install MySQL connector for python
sudo pip install -r ./requirements.txt

if $? -eq 0
then
	echo "MySQL connector was installed successfully~"
else
	echo "Installing MySQL connector was failed~"
fi
