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

class ErrorCatcher:

	def __init__(self):

		print('Checking for errors!')
		self.error_counter = 0

	def e_catch(self, file):
		"""
		Searches for error terminations in the log files, and sums up the number of theese files.
		"""
		try:
			f_name, f_ext=file.split('.')

			if f_ext=='log':
				
				with open(file, 'r+') as rf:
					lines =rf.readlines()
					
					if 'Error termination' in lines[-3]:
						
						self.error_counter += 1

						os.rename(f_name+'.'+f_ext, f_name+'_ERROR.'+f_ext)
		except ValueError:
			pass
		
		return self.error_counter



if __name__ == '__main__':
	
	path = input("Path: ")

	os.chdir(os.path.expanduser(path))

	er = ErrorCatcher()

	for file in os.listdir():

		er.e_catch(file)

	print('You have {} calculation(s) with ERROR termination!'.format(er.error_counter))