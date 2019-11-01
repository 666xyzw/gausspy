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

import subprocess

class PathEngine:

	"""
	The "PathEngine" uses the subprocess to search for itslef in the filesystem.
	After it found itself teconstructs the path, removes itself from the list.
	That list is then passed on tho the PathConstructor class.
	"""

	def __init__(self):

		path_search = subprocess.run("readlink ~/bin/gausspy", shell=True, stdout=subprocess.PIPE)
		self.path_variables = path_search.stdout.decode().split('/')
		
		for x in self.path_variables:
			
			if "gausspy.py\n" in x:
				self.path_variables.remove(x)

class PathConstructor(PathEngine):
	"""
	The "PathConstructor" inherits the path_variables from the PathEngine
	and reconstructs the paths for gausspy, for the README file and LICENSE file.
	"""
	def __init__(self):
		PathEngine.__init__(self)
		self.new_path = '/'.join(self.path_variables)

	def gauss_py(self):
		#the new_path is the same as the gausspy.pys` path
		gauss_path = self.new_path

		return gauss_path

	def lic_read_path(self):
		"""
		From the self.path_variables the "lib" folder is removed and by this
		the program moved up in the directory tree from where it can easily access
		the README and LICENSE files.
		"""
		self.path_variables.pop(-1)
		
		self.lr_path = '/'.join(self.path_variables)

		return self.lr_path

if __name__ == '__main__':
	print("path variables: ", PathEngine().path_variables)
	
	pc = PathConstructor()
	print("new path: ", pc) 
	print("gauss_py: ",pc.gauss_py())
	print("lic_read_path: ", pc.lic_read_path())
