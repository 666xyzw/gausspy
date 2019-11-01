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
import os, sys, time, subprocess

from inputfile import inputfiles
from datafile import data_analysis
from VersionControl import VersionControl
from PathEngine import PathConstructor as PC

#############################################################################################
#############################################################################################
"""
This is the gausspy main file.
It imports the data_analysis and inputg functions from the lib/ folder.
"""

def initialising():
	"""
	Initializes the path and version of the program.
	Also display a welcome message with the version of the program and a description of the program.
	"""

	global path, v

	path = PC()
	path.lic_read_path()
	
	os.chdir(path.gauss_py())

	v = VersionControl()

	print("Welcome to gausspy; version ", v.version())
	print("This bundle of tools is meant to process files for the Gaussian quantum chemistry software.\n")
	
def menu():
	"""
	The function displays the menu.
	"""	
	
	print(
		"Menu:\n"
		"\n"
		"1. Input file manipulation\n"
		"2. Data analysis\n"
		"3. README\n"
		"4. License\n"
		"5. Exit\n")

def prompt():
	#prompts the user with the input interface.
	global pr

	pr=input('$ ')
	
def system():
	"""
	ist`s called system but id does only one thing: asks the user if it
	wants something else after one operation is completed.
	"""
	global answer
	
	answer=input('Would you like anything else? [yes/no]: ')
	
	if answer == 'yes':
		subprocess.run("clear")
		pass #it has to be passed so the program jumps back to the beggining
		#of the while loop!


	elif answer == 'no':

		print("Thank you for using gausspy.\n"
			"Have a nice day!\n")
		time.sleep(2)
		sys.exit(0)
	
	else:
		print("Please give a 'yes' or 'no' answer!")
		system()

	
def mainfunc():
	"""
	Main function of the program.
	"""
	prompt()

	if pr == '1':
		inputfiles()
		os.chdir(path.gauss_py())

	elif pr == '2':
		data_analysis()
		os.chdir(path.gauss_py())

	elif pr == '3' or pr == '4':
		os.chdir(path.lr_path)
		
		if pr == '3':
			with open("README", 'r') as rf:
				file = rf.read()

			print(file)
			os.chdir(path.gauss_py()) 

		if pr == '4':
			with open("LICENSE", 'r') as rf:
				file = rf.read()

			print(file)		
			os.chdir(path.gauss_py())
			
	elif pr == '5':
		print("Thank you for using gausspy.\n"
				"Have a nice day!\n")
		sys.exit(0)

	else:
		subprocess.run("clear")
		print("These are the only options that I have.")
		menu()
		mainfunc()

#############################################################################################
#############################################################################################
if __name__=='__main__':
	try:

		initialising()
		
		
		while True:

			menu()
			mainfunc()
			system()
			
		
	except KeyboardInterrupt:
		print("\nWhatever floats your boat man!\n")
