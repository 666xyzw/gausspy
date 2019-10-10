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
from RouteCard import RouteCard

class ImagInput:

	def __init__(self, chrg="0 1", ex="com"):

		self.chrg = chrg
		self.ex = ex
		
		print('Generating the new input files!')


	def imag_xyz_gen(self, file=None, chrg_spin='', ext='', rd=''):
		
		"""
		This need to be done because the rout_card function goes back with one folder
		to take the route card from the old files, and after that
		this function has to go back to the imag folder to generate the new input files!!!
		"""

		if chrg_spin == '' and ext == '':
			chrg_spin = self.chrg
			ext = self.ex

		xf=file.split('.')

		for key in rd:

			if 'ginp' in xf[-1] and key in xf[0]:
				
				with open(file, 'r+') as rf: #opens the file and reads its content into a list

					lines=rf.readlines()

					with open(xf[0] + '.' + ext, 'w') as wf:
						
						#creates a new file with the name of the initial file and with the .com extension
						#and writes the necesarry data into it.
						
						wf.write(rd[key][0])
						wf.write('\n')
						wf.write('Title\n')
						wf.write('\n' + chrg_spin + '\n')
						for l in lines:
							wf.write(str(l))
						wf.write("\n")
								
						for m in rd[key][1:]: # --m-- variable parses through the rd (route_dictionary)
							for n in m:  # --n-- variable parses through also the rd but here --m-- is used as the 
										#key to get the value from the dictionary 
								wf.write(n) #wites the content of the dictionary into the file
						for x in range(3):
							wf.write('\n')


if __name__ == '__main__':
	
	path = input("Path: ")
	os.chdir(os.path.expanduser(path))

	r = RouteCard()

	for file in os.listdir():
		r.route_card(file)


	print(r.rd)

	ch = input("charge: ")
	ex = input("Extension: ")

	inp = ImagInput()

	for file in os.listdir():

		inp.imag_xyz_gen(file, ch, ex, r.rd)