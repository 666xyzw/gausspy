import os

def cleaner(answer):
	"""
	This function needs a parameter. If the parameter is no, then, in the imag folder, deletes everything (*.logs, *.xyz, *.xyz- and ginp) except the new input files.
	If the parameter is yes then it will exit, doing nothing.
	"""
	if answer=='no':
		print('Cleaning up!')

		for f in os.listdir():
			fi=f.split('.')

			if 'xyz' in fi[-1] or 'log' in fi[-1] or 'xyz-' in fi[-1] or 'ginp' in fi[-1]:
				os.system('rm '+f)


		os.chdir('..')

		try:
			for f in os.listdir():
				fi=f.split('.')

				if 'com' in fi:
					os.system('rm '+f)
		except ValueError:
			pass
	else:
		pass