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

	version={}

	def __init__(self, file):

		self.file = file

		with open(self.file, 'r') as rf:

			line = rf.readline()
		
			for nr in re.finditer("[0-9.]{1,3}", line):
				
				self.version["gausspy"] = nr.group(0)


if __name__ == '__main__':
	

	v = Version("__init__.py")

	print(v.version)