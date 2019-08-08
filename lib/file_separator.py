#/usr/bin/python3

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