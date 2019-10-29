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
import os

class VersionControl:
	
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

			ver_nr = line.split("=")
			
		return ver_nr[1]

	@staticmethod
	def version_updater():

		"""
		Updates the gausspy softwares` version number.
		"""

		new_version = input("Enter the new version of gausspy: ")

		with open("__init__.py", 'w') as  wf:
			wf.write("__version__ = " + str(new_version))

		print("The softwares` version has been updated to version number:",VersionControl.version())


if __name__ == '__main__':


	v = VersionControl()
	v.version()
	v.version_updater()