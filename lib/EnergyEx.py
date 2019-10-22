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

			name, ext = file.split('.')

			if ext == "log":

				with open(file, 'r+') as rf:
					lines=rf.readlines()
							
					for SCF in lines:
						if 'SCF Done:  E'in SCF:
							self.test_list.append(SCF)
				
					self.scf_list.append(self.test_list[-1])

					for y in self.scf_list:
						energy=y.split(' ')
						self.energy_dict[name]=energy[7]


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

