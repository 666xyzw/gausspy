#!/bin/bash


echo "Hello '$USER!' I will setup for you the gausspy tool."
#echo "$PWD" 

cd Xvibs/

touch xvibs && echo "java -jar "$PWD/"xvibs.jar \"\$@\" " >> xvibs
chmod +11 xvibs

if [ -d "/home/$USER/bin" ]
then
	echo "bin directory already exists."
else
	echo "Creating a 'bin' directory!"
fi

#exiting the Xvibs folder and setting up the symbolic links
cd ..


echo "creating symbolic links for the program!"
ln -s "$PWD/"gausspy.py /home/$USER/bin/gausspy
ln -s "$PWD/Xvibs/"xvibs /home/$USER/bin/xvibs
