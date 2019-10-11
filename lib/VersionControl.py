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
import re, os

class Version:
	
	def __init__(self):
		os.chdir(os.path.expanduser("~/gausspy/lib/"))
	
	@staticmethod
	def version():
		"""
		Opens the __init__.py file to take out the version number in it.
		That number is passed down to gausspy.py an will be written to the screen every time
		the program starts.
		"""
		ver = 0

		with open("__init__.py", 'r') as rf:

			line = rf.readline()

			for nr in re.finditer("[0-9.]{1,3}", line):
				
				ver = float(nr.group(0))

		return ver

if __name__ == '__main__':
	

	v = Version()
	v.version()