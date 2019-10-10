#!/usr/bin/python3

#Written by xyz666

"""
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY.
"""
import re

class Version:
	"""
	Open the __init__.py file to take out the version number in it.
	That number is passed down to gausspy.py an will be written to the screen every time
	the program starts.
	"""

	def __init__(self):

		with open("__init__.py", 'r') as rf:

			line = rf.readline()
		
			for nr in re.finditer("[0-9.]{1,3}", line):
				
				self.version = float(nr.group(0))


if __name__ == '__main__':
	

	v = Version()

	print(v.version)