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

sys.path.insert(0, 'lib/')

#############################################################################################
#############################################################################################
"""
This is the first part of the script!
It has three functions that can generate input files from spinput, xyz and gjf files.
The fourth function imag_xyz_gen is used to automate the process of making new input files from the old ones if they have imaginary frequencies.
"""
def inputg():
	from lib import input_gen as ig
	global direct, file, f_long, f_short, route_section, chrg_spin, ext

	path=input('Enter the full path to the directory where you have the files: ')
	direct = os.chdir(os.path.expanduser(path)) #changing the directory to where you will work

	route_section=input('Please enter the route section of the new input file(s): ')
	chrg_spin=input('Please enter the molecules new charge and spin value [ex.: 0 1 ]: ')
	ext=input('Please enter the generated files extension [ex: com]: ')

	for f in os.listdir(direct): #listing the files in the directory
		try:
			f_long, f_short=f.split(".")

			if f_short=='spinput':
				header_lines=3
				ig.spinput_gen(f, f_long, route_section, chrg_spin, header_lines, ext)
				
			elif f_short=='xyz':
				header_lines=2
				ig.xyz_input_gen(f, f_long, route_section, chrg_spin, header_lines, ext)
				
			else:
				header_lines=6
				ig.gjf_input_gen(f, f_long, route_section, chrg_spin, header_lines, ext)
	
		except ValueError:
			pass
	print('Input file generation terminated')
	time.sleep(1)
#############################################################################################
#############################################################################################
"""
Second part of the script!
Practicly this is where the analysis is done.
In the first step it unzips the tar/tgz files in a separate folder, and after that it`s searching for error terminations and imaginary frequencies in the log files.
"""
def data_analysis():
	from lib import tmp_unrar as tu
	from lib import error_catcher as ec, cleaner 
	from lib import energy_ex as eex
	from lib import imag_catcher as ic
	from lib import route_card as rc
	from lib.input_gen import imag_xyz_gen

	global direct

	path=input('Enter the path to the directory where you have the tgz/tar folders: ')
	direct=os.chdir(os.path.expanduser(path)) #changing the directory to where I will work
	
	tu.tmp_check(direct)
	tu.unrar(direct)
	ec.error_catcher()
	eex.csv_writer(eex.sampling())
	
	if ic.imag_catcher() == 0:
		"""
		If this part is true, then the script skips the part with the imaginary freqs
		and removes the imag directory that has been created!
		"""
		os.system('rmdir imag/')
		pass

	else:
		"""
		if the above statement isn`t true then the script continues to work
		with the imaginary freqs!
		"""
		ic.xawker()
	
		chrg_spin=input('Please enter the molecules charge and spin [ex.: 0 1 ]: ')
		ext=input('Please enter the genereated files extension [ex: com]: ')

		imag_xyz_gen(rc.route_dict(), chrg_spin, ext)

		answer=input('Do you need the *.log and the old *.xyz files? [yes/no]: ')
		cleaner.cleaner(answer)
	
	print('Data analysis terminated')
	time.sleep(1)
#############################################################################################
#############################################################################################
def initialising():
	print("Welcome to gausspy.\n"
		"This bundle of tools is meant to process files for the Gaussian quantum chemistry software.\n")

def menu():	
	print("Menu: ")
	print("1. Input file manipulation\n"
		"2. Data analysis\n"
		"3. Readme\n"
		"4. License\n"
		"5. Exit\n")

def prompt():
	global pr

	pr=input('$ ')
	
def system():
	global users

	users=input('Would you like anything else?[yes/no]: ')


def mainfunc():

	prompt()

	if pr=='1':
		inputg()

	elif pr=='2':
		data_analysis() 

	elif pr=='3':
		with open('README', 'r') as rf:
			file=rf.read()
		print(file)

	elif pr=='4':
		with open('LICENSE', 'r') as rf:
			l=rf.read()
		print(l)

	elif pr=='5':
		print('Terminating software.')
		sys.exit(0)

	else:
		print("These are the only options that I have.")
		menu()
		mainfunc()

#############################################################################################
#############################################################################################
if __name__=='__main__':

	initialising()
	menu()
	
	while True:
		mainfunc()
		system()

		if users=='yes':
			menu()

		else:
			print('System going back offline')
			time.sleep(2)
			sys.exit(0)
