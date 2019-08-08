#!/usr/bin/python3

import os


def sampling():
	"""
	The sampling() function searches through the log files for the last SCF energy,
	which is then stored in a list named energy_list. The asociated file name is stored in
	the f_name list.
	"""
	print('Sampling the minimum energies!')
	global test_list, scf_list, energy_list, f_name, energy_dict

	test_list=[]
	scf_list=[]
	energy_list=[]
	energy_dict={}
	f_name=[]


	for f in os.listdir():
		try:
			name, ext=f.split('.')

			if ext=='csv' or ext=='com':
				pass
			elif 'ERROR' in name:
				pass
			else:
				f_name.append(name)
				
				with open(f, 'r+') as rf:
					lines=rf.readlines()
						
					for SCF in lines:
						if 'SCF Done:  E'in SCF:
							test_list.append(SCF)
			
					scf_list.append(test_list[-1])
		except ValueError:
			pass
	#u=0	
	#for x in scf_list: #for debugging just uncomment the lines!
	#	u+=1
	#	print('scf_list: ', u, x)

	for y in scf_list:
		energy=y.split(' ')
		energy_list.append(energy[7])
	
	#also for debugging	
	#for x in energy_list:
	#	print('energy_list: ', x)
	
	#for debugging too!
	#for z in f_name:
	#	print('names: ', z)

	energy_dict=dict(zip(f_name, energy_list))
	return energy_dict
	#for debugging!
	#for h in energy_dict:
	#	print('energy_dict: ', h, energy_dict[h])


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