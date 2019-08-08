#/usr/bin/python3

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

def file_separator():
	"""
	Separates the logs containing imaginary frequencies from the ones containing errors, by creating
	a separate folder (imag) and moves the logs there.
	"""

	#Now the script does a double check
	#The files that are without error or imaginary frequencies will be deleted, the rest is kept.
	print('Removing files which don`t have any problem')
	for f in os.listdir():
		try:
			f_name, f_ext=f.split('.')

			if 'ERROR' in f_name:
				pass
			else:
				os.system('rm '+f)

		except ValueError:
			pass
