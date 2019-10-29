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


	
def data_analysis():

	"""
	This is where the analysis is done.
	In the first step it unzips the tar/tgz files in a separate folder, and after that it`s 
	searching for error terminations and imaginary frequencies in the log files.
	The *.log files containing errors or imaginary freqs are separated from the rest.
	Also the "EnergyEx" module extracts the calculated energies and writes them into a 
	csv file with the help of the cxsvwriter module.
	Logs containig imaginary freqs are processed by the "xvibs" program.
	"""
	
	import os, sys, time

	import tmp_unrar as tu
	from ErrorCatcher import ErrorCatcher as EC
	from ImagCatcher import ImagCatcher as IC
	from RouteCard import RouteCard as RC
	from EnergyEx import EnergyEx  
	from csvwriter import csvwriter
	from fileseparator import fileseparator
	from xawker import xawker
	from ImagInput import ImagInput
	from cleaner import cleaner	
	

	global direct

	path=input('Enter the path to the directory where you have the tgz/tar folders: ')
	direct=os.chdir(os.path.expanduser(path)) #changing the directory to where I will work

	####### Checking for a tmp folder and unzipping the tar/tzgz files into tmp #######
	tu.tmp_check(direct)
	tu.unrar(direct)
	###################################################################################
	
	####### Searching for Error termination in the *.log files ########################
	er = EC()

	for file in os.listdir():
		er.e_catch(file)

	print('You have {} calculation(s) with ERROR termination!'.format(er.error_counter))
	####################################################################################
	
	####### Searching for imaginary frequencies in the *.log files #####################
	imag=IC()

	for file in os.listdir():
		imag.imag_catcher(file)
	#####################################################################################	

	########### Selecting the route cards for the files with imaginary freqs ############
	route = RC(imag.imag_dict)
	
	for file in os.listdir():
		route.route_card(file)

	#####################################################################################
	
	####### Extracting the Energies from the *.log files and saving them in energies.csv file #######
	energy=EnergyEx()

	for file in os.listdir():
		print(file)
		energy.sampler(file)


	csvwriter(energy.energy_dict)
	##################################################################################################

	####### Separating the files containig Errors from those containing imaginary frequencies ########
	for file in os.listdir():
		fileseparator(file)
	##################################################################################################

	####### Genertaing the new input files from the *.log files containing imaginary freqs #######
	if imag.imag_dict != {}:

		xawker(imag.imag_dict)

		im = ImagInput()
		
		chrg_spin=input('Please enter the molecules new charge and spin value [ex.: 0 1 ]: ')
		ext=input('Please enter the generated files extension [ex: com]: ')

		for file in os.listdir():
			im.imag_xyz_gen(file, chrg_spin, ext, route.rd)
	else:
		pass
	##################################################################################################

	################################### Cleaning up the mess #########################################

	answer = input("Do you need the old xyz/xyz-/ginp file(s)? ")

	cleaner(answer)
	##################################################################################################

	################################### Exiting the data analysis mode ###############################
	print('Data analysis terminated')
	time.sleep(1)
	##################################################################################################


if __name__ == '__main__':
	
	data_analysis()