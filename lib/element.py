#!/usr/bin/python3

import os

"""
Element_dict={'H':1, 'He':2, 'Li':3, 'Be':4, 'B':5, 'C':6, 'N':7, 'O':8, 'F':9, 'Ne':10
				'Na':11, 'Mg':12, 'Al':13, 'Si':14, 'P':15, 'S':16, 'Cl':17, 'Ar':18
				'K':19, 'Ca':20, 'Sc':21, 'Ti':22, 'V':23, 'Cr':24, 'Mn':25, 'Fe':26, 'Co':27,
				'Ni':28, 'Cu':29, 'Zn':30, 'Ga':31, 'Ge':32, 'As':33, 'Se':34, 'Br':35, 'Kr':36
				'Rb':37, 'Sr':38, 'Y':39, 'Zr':40, 'Nb':41, 'Mo':42, 'Tc':43, 'Ru':44, 'Rh':45}
"""
def element():
	
	for f in os.listdir():
		try:
			f_name, f_ext = f.split('.')

			if 'com' in f_ext:

				with open(f, 'r+') as rf:
					lnr=0
					lines=rf.readlines()
					
					#print(lines)
					for line in lines:
						lnr+=1	
						

					for line in lines:		
						if '%nproc' and '%mem' in line:
							lnr-=1
							#print(lnr, line)
						if '%mem' in line:
							lnr-=1
							#print(lnr, line)
					
					for line in lines[5:]:
						print(line)


		except ValueError:
			pass

if __name__ == '__main__':

	os.chdir(os.path.expanduser('~/Programing/python/test/analysis/tmp/'))
	element()