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

class AtomList:

	"""
	This class contains all the second and third row transition metals.
	The atompop function uses this library to identify if the input file contains
	such metals.
	"""

	library_of_atoms = {"Second_row_trm":{"Y":39, "Zr":40, "Nb":41, "Mo":42, "Tc":43, "Ru":44,
						"Rh":45, "Pd":46, "Ag":47, "Cd":48},
						"Third_row_trm":{"Hf":72, "Ta":73, "W":74, "Re":75, "Os":76, "Ir":77,
						"Pt":78, "Au":79, "Hg":80}}
	
	hv_atom = None #an empty variable that will contain the heavy/transitional metal atom hence the name "hv_atom"

	def atompop(self, atom_list):

		"""
		This function searches in the atom_list and if finds atoms that
		are found also in the library then that atoms is assigned to slef.hv variable
		and after that it is removed from the list.
		Also the function makes difference between atomic numbers and atomic symbols!
		"""

		for atom in atom_list[:-1]: #iterates over the atom_list
			try: 
				int_atom = int(atom) #makes an attempt to convert the atom to an integer
									 #if that throws an exception then that means that the atoms
									 #are given with symbols and not by their atomic numbers
									 
				# print("Now working whit numbers!")
				for row in AtomList.library_of_atoms:
					for atom_nr in AtomList.library_of_atoms[row]:
						if int_atom == AtomList.library_of_atoms[row][atom_nr]:
							self.hv_atom = atom
							atom_list.remove(atom)		
			
			except ValueError:
				# print("Now working whit Symbols!")
				for row in AtomList.library_of_atoms:
					for atoms in AtomList.library_of_atoms[row]:
						if atom == atoms:
							self.hv_atom = atom
							atom_list.remove(atom)

		return self.hv_atom
		return atom_list

if __name__ == '__main__':
	
	a = AtomList()
	atom_list=['C', 'B', 'Rh', 'H', '0\n']
	a.atompop(atom_list)
	print(a.hv_atom)