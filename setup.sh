#!/bin/bash

#Written by xyz666

<<COMMENT
This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU General Public License
 as published by the Free Software Foundation; either version 2
 of the License, or (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY.'
COMMENT

echo "Hello '$USER!' I will setup for you the gausspy tool."
#echo "$PWD" 

cd Xvibs/

touch xvibs && echo "java -jar "$PWD/"xvibs.jar \"\$@\" " >> xvibs
chmod +x xvibs

if [ -d "/home/$USER/bin" ]
then
	echo "bin directory already exists."
else
	echo "Creating a 'bin' directory!"
	mkdir /home/$USER/bin
fi

#exiting the Xvibs folder and setting up the symbolic links
cd ..

#making gausspy executable
chmod +x lib/gausspy.py

echo "creating symbolic links for the program!"
ln -s "$PWD/lib/"gausspy.py /home/$USER/bin/gausspy
ln -s "$PWD/Xvibs/"xvibs /home/$USER/bin/xvibs
