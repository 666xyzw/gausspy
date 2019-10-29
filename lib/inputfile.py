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

def inputfiles():

	"""
	This part of the script has three functions that can generate input files from spinput, 
	xyz and gjf files. The files are split inot names and extensions and each extension is
	verified. If the extension matches one of the provided extension (xyz, spinput or gjf)
	the respective function will be called on the file.
	"""

	import os, sys, time
	from inputgenerators import xyz_input, spinput_gen, gjf_input
	
	################################### Asking for the path #####################################
	path=input('Enter the full path to the directory where you have the files: ')
	direct = os.chdir(os.path.expanduser(path)) #changing the directory to where you will work
	#############################################################################################

	######################### Asking for the details of the input file############################
	functional = input("Enter the functional: ")
	fbasis = input("Enter the first basis set: ")
	sbasis = input("Enter the second basis (optional): ")
	route = input('Enter the rest of the route section: ')
	chrg_spin = input('Enter the molecules new charge and spin value: ')
	ext = input('Enter the generated files extension: ')
	#############################################################################################
	
	##############################Generating the new input files#################################
	print("Generating new input files!")

	for file in os.listdir(direct): #listing the files in the directory
		try:
			fe = file.split('.') #splits the file into name and extension in a single variable

			if "xyz" in fe:
				
				xyz_input(file, functional, fbasis, sbasis, route,  chrg_spin, ext)
			
			elif 'spinput' in fe:
				
				spinput_gen(file, functional, fbasis, sbasis, route, chrg_spin, ext)
			
			elif "gjf" in fe:
				
				gjf_input(file, functional, fbasis, sbasis, route, chrg_spin, ext)
		
		except ValueError:
			pass #if "file" is a folder then it just skips the folder

	print('Input file generation terminated')
	time.sleep(1)
	#############################################################################################

if __name__ == '__main__':
	
	inputfiles()