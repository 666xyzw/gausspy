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

def csvwriter(energy_dict):
	"""
	This function creates a csv (Comma Separated Values) type of file,
	where the data from the previous dictionary is stored for later analysis by the user.
	The csv file can be opened as an Excel sheet!
	"""

	"""
	Check if energy_dict is empty. If True then pass else create the csv file!
	"""
	if energy_dict=={}:
		print('No energies!')

	else:
		print('Creating csv file!')

		try:#look for a csv file. If found the data is appended if not a new csv file is created!

			with open ('energies.csv', 'w') as wf:
				wf.write('Name'+','+'Py-Energy'+'\n')
				for element in sorted(energy_dict.keys()):
					wf.write(element+','+str(energy_dict[element])+'\n')
					
		except ValueError:
			pass