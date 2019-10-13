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
import os, sys, time

from inputfile import inputfiles
from datafile import data_analysis
from VersionControl import VersionControl

#############################################################################################
#############################################################################################
"""
This is the gausspy main file.
It imports the data_analysis and inputg functions from the lib/ folder.
"""

def initialising():
	v = VersionControl()
	
	print("Welcome to gausspy; version ", v.version())
	print("This bundle of tools is meant to process files for the Gaussian quantum chemistry software.\n")

def menu():	
	
	print(
		"Menu:\n"
		"\n"
		"1. Input file manipulation\n"
		"2. Data analysis\n"
		"3. Exit\n")

def prompt():
	global pr

	pr=input('$ ')
	
def system():
	global users

	users=input('Would you like anything else? [yes/no]: ')


def mainfunc():

	prompt()

	if pr=='1':
		inputfiles()

	elif pr=='2':
		data_analysis() 

	elif pr=='3':
		print("Thank you for using gausspy.\n"
				"Have a nice day!\n")
		sys.exit(0)

	else:
		print("These are the only options that I have.")
		menu()
		mainfunc()

#############################################################################################
#############################################################################################
if __name__=='__main__':
	try:

		initialising()
		menu()
		
		while True:
			mainfunc()
			system()

			if users=='yes':
				os.system("clear")
				menu()

			else:
				print("Thank you for using gausspy.\n"
					"Have a nice day!\n")
				time.sleep(2)
				sys.exit(0)
	except KeyboardInterrupt:
		print("\nWhatever floats your boat man!\n")
