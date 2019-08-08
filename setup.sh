#!/bin/bash

#Written by xyz666

'This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU General Public License
 as published by the Free Software Foundation; either version 2
 of the License, or (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY.'


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
