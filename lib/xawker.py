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

def xawker(imag_dict):
	"""
	Here the script combines two other programs, namely xvibs and awk.
	In the first step it changes the current directory to the imag directory.
	Then it begins to process the files, with xvibs creating *.xyz files containing xyz coordinates
	from whitch, with awk, it takes out the first four collumns and creating a new *.xyz- file, which will be processed by
	the imag_xyz_gen function.
	"""

	os.chdir('imag/')
	
	for f in os.listdir():
		try:

			f_n, f_ext=f.split('.')
		
			for key in imag_dict: #iterates over the dictionary extracting only the key
				if key in f_n: #tests if the key is also found in the fn (files name); if yes then
					idc=imag_dict[key] #saves the keys value in idc
					im=1 #sets im to 1

					print('Generating xyz file from {} file'.format(f))
					while im <= int(idc): #until im is not equal to the extracted value
						
						os.system('xvibs '+ f +' '+str(im)) #generates xyz files with xvibs
						im+=1

		except ValueError:
			pass


	print('Generating xyz- file(s)')
	for f in os.listdir():
		
		if 'xyz' in f:
			
			os.system("awk '{print $1, $2, $3, $4}' "+ f +" "+"> "+f+"-")

	print('Generating ginp file(s)')
	
	for f in os.listdir():
		
		fi = f.split('.')

		if fi[-1] == "xyz-":
		
			with open(f, 'r+') as rf:
		
				text=rf.readlines()

				h1=int(text[0]) #first line in the xyz- file -> gives the total number of atoms 
				h2=text[1].split(' ') #second line in the xyz- file, is split into a list
													
				n1=0 #line number
				n2=0 #numbering the lines which contain the 'Energy' word

				for line in text:
					n1+=1	
					if 'Energy' in line:
						n2+=1
						if n2==6:
							begin=n1
							end=n1+h1
							
							with open(fi[0]+'_r-' + str(fi[1])+ '.ginp', 'w') as wf:
								#fi[1] is the imag files number; it`s more practical to number the files
								#like this than to every time search and round up the actual freq(s)
								#to prevent overwriting in case if there are two very close freqs
								for l in text[begin:end]:
									wf.write(str(l))
