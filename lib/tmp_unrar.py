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


def tmp_check(directory):
	"""
	First it checks if a folder named tmp is already existing. If it doesen`t exist then it`s creating one
	"""
	
	for f in os.listdir(directory):
		if os.path.isdir('tmp') == False:
			os.system('mkdir tmp')

def unrar(directory):
	"""
	Unzips the tar/tgz files in the tmp folder.
	"""
	print('Decompressing the tar/tgz files')
	for f in os.listdir(directory):
		try:
			f_name, f_ext=f.split('.')
			"""
			if  f_ext=='tgz':
				#print('Decompressing {}'.format(f))
				os.system('tar xzpf '+ f +' -C tmp ')
			else:
				#print('Decompressing {}'.format(f))
				os.system('tar xpf '+ f +' -C tmp ')
			"""
			if 'error' in f_name and f_ext=='tgz':
				pass

			elif 'error' not in f_name and f_ext=='tgz':	
				#print('Decompressing {}'.format(f))
				os.system('tar xzpf '+ f +' -C tmp ')

			elif 'error' in f_name and f_ext=='tar':
				pass

			elif 'error' not in f_name and f_ext=='tar':
				#print('Decompressing {}'.format(f))
				os.system('tar xpf '+ f +' -C tmp ')

			else:
				pass
				
		except ValueError:
			pass
	
	os.chdir('tmp/')

