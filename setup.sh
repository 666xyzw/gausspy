#!/bin/bash


echo "Hello '$USER!' I will setup for you the gausspy tool."
echo "$PWD" 

echo Downloading software!
wget -q https://sourceforge.net/projects/xvibs/files/xvibs/17/xvibs.jar

if [ -e "xvibs.jar" ]
then
	echo "Download complete!"
	chmod +7 "xvibs.jar"
else
	echo "Could not download the file!"
fi

touch xvibs | echo 'java -jar "$PWD/"xvibs.jar "$@"'
chmod +11 xvibs

if [ -d "/home/$USER/bin" ]
then
	echo "bin directory already exists."
else
	echo "Creating a 'bin' directory!"
fi

#echo "$PWD"
echo "creating symbolic links for the program!"
ln -s "$PWD/"gausspy.py /home/$USER/bin/gausspy
ln -s "$PWD/"xvibs.jar /home/$USER/bin/xvibs