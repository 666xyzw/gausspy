import os

#Written by xyz666

"""
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY.
"""


def cleaner(answer):
	"""
	This function needs a parameter. If the parameter is no, then, in the imag folder, deletes everything (*.logs, *.xyz, *.xyz- and ginp) except the new input files.
	If the parameter is yes then it will exit, doing nothing.
	"""
	if answer=='no':
		print('Cleaning up!')

		for f in os.listdir():
			fi=f.split('.')

			if 'xyz' in fi[-1] or 'xyz-' in fi[-1] or 'ginp' in fi[-1]:
				os.system('rm '+f)


	else:
		pass
