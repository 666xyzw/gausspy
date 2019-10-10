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



class FileManipulator:
	""" This class contains all the file opening, reading, writing operations
		from the inputgenerators file, to reduce duplicate code to the minimum.
	"""
	def __init__(self, file):
		
		"""
		The file is split into name (f_name) and extension (f_ext).
		After this it will be opened and its content will be put into
		self.lines variable which will be used in the other methods.
		"""

		self.file = file
		
		try:
			self.f_name, self.f_ext = self.file.split('.')

			with open(self.file, "r+") as rf:

				self.lines = rf.readlines()

		except ValueError:
			pass


	def atomic_list(self, header=None, footer=None):

		"""
		Creates a list of the atoms found in the coordinate system.
		The list will contain only ONE of each atom. This is needed
		in the input file where we have two basis sets.
		"""

		self.matrix = self.lines[header:footer] #the coordinate system

		temp = [] #temporary list
		self.atom_list=[] #list that will contain the atoms

		for ch in self.matrix: #parsing through the coordinate system
			if ch[0:2] not in temp: #selecting the first two characters 
				temp.append(ch[0:2]) # adding those characters to a list
	

		for atom in temp: #parsing through the temp list
			if atom not in self.atom_list: #if the atom (character) is not already in the atom_list
				self.atom_list.append(atom.strip()) #then it will be put there

		self.atom_list.append('0\n') #in the end of the list there must be a 0\n otherwise the Gaussian program
								#will throw in an error!

		
	
	def write1(self, functional, fbasis, route, chrg_spin, ext):
		"""This method is called only when the user doesn`t supply a second 
		basis set which is required by second or higher row transitional metal atoms!
		"""
		try:
		
			with open(self.f_name + '.' + ext, 'w') as wf:

				wf.write("#P " + functional + '/' + fbasis + ' ' + route+'\n')
				wf.write('\n')
				wf.write('Title\n')
				wf.write('\n'+chrg_spin+'\n')
				
				for l in self.matrix:
					wf.write(str(l))
			
				for x in range(3):
					wf.write('\n')

		except ValueError:
			pass

	def write2(self, atom_list, functional, fbasis, sbasis, hv, route, chrg_spin, ext):
		"""
		This method is called when a second basis set is supplied by the user.
		"""
		
		try:

			with open(self.f_name+ '.' + ext, 'w') as wf:

				wf.write("#P " + functional + '/gen Pseudo=read ' + route+'\n')
				wf.write('\n')
				wf.write('Title\n')
				wf.write('\n'+chrg_spin+'\n')

				for l in self.matrix:
					wf.write(str(l))
					
				wf.write('\n')
				wf.write(' '.join(atom_list))
				wf.write(fbasis + "\n")
				wf.write("****\n")
				wf.write(hv + " 0\n")
				wf.write(sbasis +"\n")
				wf.write("\n")
				wf.write("****\n")
				wf.write(hv + " 0\n")
				wf.write(sbasis + "\n")

				for x in range(3):
					wf.write('\n')	


		except ValueError:
			pass


	

if __name__ == '__main__':
	
	import os

	path = input("Enter path: ")

	os.chdir(os.path.expanduser(path))

	functional = input("Enter the functional: ")
	fbasis = input("Enter the first basis set: ")
	sbas= input("Second basis: ")
	hv = input("Heavy atoms: ")
	route = input('Enter the rest of the route section: ')
	chrg_spin=input('Enter the molecules new charge and spin value: ')
	ext=input('Enter the generated files extension: ')

	atom_list=['C', 'B', 'H', '0\n'] #this is a dummy list

	for file in os.listdir():
	
		f = FileManipulator(file)
		
		if sbas == '':
			f.write1(functional, fbasis, route, chrg_spin, ext)
		elif sbas != '':
			f.write2(atom_list, functional, fbasis, sbas, hv, route, chrg_spin, ext)