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

class EnergyEx:
	"""
	This class samples the energies from the *.log files into a dictionary (energy_dict).
	If the log file has errors than instead of the energy it gives as value Error.
	"""

	def __init__(self):
		"""
		Initializes the two empty lists and one empty dictionary.
		"""

		self.test_list = []
		self.scf_list = []
		self.energy_dict = {}

		print("Sampling Energies!")


	def sampler(self, file):

		try:

			name, ext = file.split('.') #split into file name and file extension

			

			if ext == "log": #if extension is log then

				with open(file, 'r+') as rf: 	#open it as rf
					lines=rf.readlines() 		#reads the whole file
							
					for SCF in lines: 			#parses the lines
						if 'SCF Done:  E'in SCF:	#if finds the words SCF Done:  E then that line 
							self.test_list.append(SCF) #is added to the self.test_list
					
					try:
						self.scf_list.append(self.test_list[-1]) #takes out only the last line

					except IndexError:
						print("No energies found in {}".format(file)) #if nothing was found then it write the message
						pass

					for y in self.scf_list: #pasrses the new list
						energy=y.split(' ') #splits the lines by spaces

						for element in energy: #parses every element in the list
							n = 0 # just a numerator variable

							try:
								
								self.energy_dict[name] = float(element) #tries to convert the element to a float
								n += 1 # numbers the successfull conversions

								if n == 1: # if it is the first conversion (that is the Energy of the system)
									break  #then breaks the loop

							except ValueError:
							 	#testing if the element can be converted to a float if not the it is a string
							 	pass


			if ext == "log" and "_ERROR" in name:
				self.energy_dict[name] = "Error"
				
		except ValueError:
			pass

		
		return self.energy_dict


if __name__ == '__main__':
	p=input('Path: ')
	os.chdir(os.path.expanduser(p))
	
	e = EnergyEx()

	for f in os.listdir():
		e.sampler(f)

	for key in sorted(e.energy_dict.keys()):
		print(key, e.energy_dict[key])

