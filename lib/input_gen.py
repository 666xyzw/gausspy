import os

def spinput_gen(file, fn, route, chrg_spin, header_lines, ext):
	try:
		with open(file, 'r+') as rf: #opens the file and reads its content into a list

			lines=rf.readlines()
			number_of_total_lines=0
				
			for line in lines:
				number_of_total_lines+=1
			
				if 'ENDCART' in line: #under windows it`s 'ENDCART\n'
					number_of_atoms=number_of_total_lines-4
			#in the following two lines is calculated the coordinate systems extent, which in 
			#the end will be copied in the new file.
			 	
			number_of_lines=number_of_total_lines-number_of_atoms
			coord=number_of_total_lines-number_of_lines+header_lines
		
			with open(fn+'.'+ext, 'w') as wf:
			
			#creates a new file with the name of the initial file and with the .com extension
			#and writes the necesarry data into it.
			
				wf.write(route+'\n')
				wf.write('\n')
				wf.write('Title\n')
				wf.write('\n'+chrg_spin+'\n')
				for l in lines[header_lines:coord]:
					wf.write(str(l))
				for x in range(3):
					wf.write('\n')
			
	except ValueError:
		pass


def xyz_input_gen(file, fn, route, chrg_spin, header_lines, ext):
	
	try:
		with open(file, 'r+') as rf: #opens the file and reads its content into a list

			lines=rf.readlines()
			l=lines[header_lines:]
	
		with open(fn+'.'+ext, 'w') as wf:
		
		#creates a new file with the name of the initial file and with the .com extension
		#and writes the necesarry data into it.
		
			wf.write(route+'\n')
			wf.write('\n')
			wf.write('Title\n')
			wf.write('\n'+chrg_spin+'\n')
			for l in lines[header_lines:]:
				wf.write(str(l))
			#the next line are hardcoded, they need to be removed afterwards!!!!!!!!!!!
			"""
			wf.write('\n') 
			wf.write('C B H 0\n')
			wf.write('6-31G(d)\n')
			wf.write('****\n')
			wf.write('Rh 0\n')
			wf.write('SDD\n')
			wf.write('****\n')
			wf.write('\n')
			wf.write('Rh 0\n')
			wf.write('SDD\n')
			"""
			for x in range(3):
				wf.write('\n')
							
	except ValueError:
		pass

def gjf_input_gen(file, fn, route, chrg_spin, header_lines, ext):


	try:
		with open(file, 'r+') as rf: #opens the file and reads its content into a list

			lines=rf.readlines()
								
			#in the following two lines is calculated the coordinate systems extent, which in 
			#the end will be copied in the new file.
			
			atoms=int(lines[-2])
								 	
			coord=atoms+header_lines
			
			l=lines[header_lines:coord]

		with open(fn+'.'+ext, 'w') as wf:	
			wf.write(route +'\n')
			wf.write('\n')
			wf.write('Title\n')
			wf.write('\n'+chrg_spin+'\n')
			for l in lines[header_lines:coord]:
				wf.write(str(l))
			for x in range(3):
				wf.write('\n')
				
	except ValueError:
		pass

def imag_xyz_gen(rd, chrg_spin, ext):
	print('Generating the new input files!')

	os.chdir('imag/')
	"""
	This need to be done because the rout_card function goes back with one folder
	to take the route card from the old files, and after that
	this function has to go back to the imag folder to generate the new input files!!!
	"""

	for f in os.listdir():
		xf=f.split('.')

		for key in rd:

			if 'ginp' in xf[-1] and key in xf[0]:
				with open(f, 'r+') as rf: #opens the file and reads its content into a list

					lines=rf.readlines()

					with open(xf[0]+'.'+ext, 'w') as wf:
						
						#creates a new file with the name of the initial file and with the .com extension
						#and writes the necesarry data into it.
						
						wf.write(rd[key])
						wf.write('\n')
						wf.write('Title\n')
						wf.write('\n'+chrg_spin+'\n')
						for l in lines:
							wf.write(str(l))
						
						wf.write('\n') 
						wf.write('C B H 0\n')
						wf.write('6-31G(d)\n')
						wf.write('****\n')
						wf.write('Ru 0\n')
						wf.write('SDD\n')
						wf.write('****\n')
						wf.write('\n')
						wf.write('Ru 0\n')
						wf.write('SDD\n')
						for x in range(3):
							wf.write('\n')
						
