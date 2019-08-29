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


def sampling():
	"""
	The sampling() function searches through the log files for the last SCF energy,
	which is then stored in a list named energy_list. The asociated file name is stored in
	the f_name list.
	"""
	print('Sampling the minimum energies!')
	global test_list, scf_list, f_name, energy_dict

	test_list=[]
	scf_list=[]
	energy_dict={}
	f_name=[]


	for f in os.listdir():
		try:
			name, ext=f.split('.')

			if ext=='csv' or ext=='com':
				pass
			elif 'ERROR' in name:
				
				energy_dict[name]='ERROR'
			else:
								
				with open(f, 'r+') as rf:
					lines=rf.readlines()
						
					for SCF in lines:
						if 'SCF Done:  E'in SCF:
							test_list.append(SCF)
			
					scf_list.append(test_list[-1])

					for y in scf_list:
						energy=y.split(' ')
						energy_dict[name]=energy[7]
		except ValueError:
			pass

	#print(energy_dict)
	return energy_dict


def csv_writer(energy_dict):
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

			if os.path.isfile('energies.csv')==True:
				with open('energies.csv', 'a') as af:
					for element in energy_dict:
						af.write(element+','+energy_dict[element]+'\n')
			else:
				
				with open ('energies.csv', 'w') as wf:
					wf.write('Name'+','+'Py-Energy'+'\n')
					for element in energy_dict:
						wf.write(element+','+energy_dict[element]+'\n')
		except ValueError:
			pass
		
if __name__ == '__main__':
	p=input('Path: ')
	os.chdir(os.path.expanduser(p))
	sampling()
	csv_writer(energy_dict)
