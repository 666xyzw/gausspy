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
from FileManipulator import FileManipulator

def xyz_input(file, functional, fbasis, sbasis, hva, route, chrg_spin, ext):
	
	header = 2

	try:

		fm = FileManipulator(file)

		fm.atomic_list(2, None)

		#checks if the user provided a second basis set. If not then fm.write1 will be executed
		if sbasis != '':
			
			fm.write2(fm.atom_list, functional, fbasis, sbasis, hva, route, chrg_spin, ext)
		
		else:
		
			fm.write1(functional, fbasis, route, chrg_spin, ext)

	except ValueError:
		pass



def spinput_gen(file, functional, fbasis, sbasis, hva, route, chrg_spin, ext):
	
	header = 3

	try:
		fm = FileManipulator(file)

		number_of_total_lines = 0
			
		for line in fm.lines:
			number_of_total_lines += 1
			
			if 'ENDCART' in line:
				
				number_of_atoms = number_of_total_lines - 4
			
		#in the following two lines is calculated the coordinate systems extent, which in 
		#the end will be copied in the new file.
			 	
		number_of_lines = number_of_total_lines - number_of_atoms
		footer = number_of_total_lines - number_of_lines + header

		fm.atomic_list(header, footer)

		if sbasis != '':

			fm.write2(fm.atom_list, functional, fbasis, sbasis, hva, route, chrg_spin, ext)

		else:

			fm.write1(functional, fbasis, route, chrg_spin, ext)

	except ValueError:
		pass

def gjf_input(file, functional, fbasis, sbasis, hva, route, chrg_spin, ext):

	header = 6

	try:
		fm = FileManipulator(file)
							
		#in the following two lines is calculated the coordinate systems extent, which in 
		#the end will be copied in the new file.
		
		number_of_atoms = int(fm.lines[-2])
							 	
		footer = number_of_atoms + header
		
		fm.atomic_list(header, footer)

		if sbasis != '':
			
			fm.write2(fm.atom_list, functional, fbasis, sbasis, hva, route, chrg_spin, ext)

		else:

			fm.write1(functional, fbasis, route, chrg_spin, ext)
				
	except ValueError:
		pass

	

if __name__ == '__main__':
	
	path = input("Enter path: ")
	os.chdir(os.path.expanduser(path))

	func = input("Functional: ")
	fbas = input("First basis: ")
	sbas= input("Second basis: ")
	hv = input("Heavy atoms: ")
	route = input("Provide the rest of the route card: ")
	chrg_spin = input('Enter the molecules new charge and spin value: ')
	ext = input('Enter the generated files extension: ')

	for file in os.listdir():
		try:
			fn, fe = file.split('.')

			if "xyz" in fe:
				xyz_input(file, func, fbas, sbas, hv, route, chrg_spin, ext)

			elif "spinput" in fe:

				spinput_gen(file, func, fbas, sbas, hv, route, chrg_spin, ext)

			elif "gjf" in fe:

				gjf_input(file, func, fbas, sbas, hv, route, chrg_spin, ext)

			else:

				print("No recognizable file format!")

		except ValueError:
			pass





					
