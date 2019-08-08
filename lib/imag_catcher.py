#Written by xyz666

"""
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY.
"""



import os, sys, re

#sys.path.insert(0, 'Xvibs/')

def imag_catcher():
	"""
	Searches for imaginary frequencies in the log files.
	If finds anny, then it takes that number of frequencies and renames the file adding '_imag_number-of-imaginary frequencies'.
	"""
	print("Checking for imaginary frequency(ies)!")
	global imag_dict, imag_counter
	

	imag_dict={}

	imag_counter=0 #it just counts how manny calculations have imaginary freqs
	
	for f in os.listdir():
		if os.path.isdir('imag')==False:
			os.system('mkdir imag')


	for f in os.listdir():
		try:		
			f_name, f_ext=f.split('.')
			
			if f_ext=='log':
				#print('Analysing {} file'.format(f))
				with open(f, 'r+') as rf:
					lines=rf.readlines()
					
					for line in lines: #iterates over the *.log file
						if ' imaginary frequencies (negative Signs)' in line: #if the line contains that text then it`s a match
							
							imag_counter+=1
							
							for m in re.finditer('[0-9]{1,3}', line):#with regex searches from 1 to 3  digit numbers in the line found earlier
								
								imag_dict[f_name]=m.group(0) #if the number is found then that number is assigned to the files name in a dictionary
								

							print('The {} file contains {} Imaginary Frequency(ies)!'.format(f,imag_dict[f_name])) #prints out the number of imaginary frequencies in the file found with regex
							os.system('mv ' + f + ' imag/') #moves the imaginary files to the imag folder

		except (ValueError, OSError):
			pass

	return imag_counter #it is returned because it needs to be evaluated in the main script
	#if it`s 0 then the script skips the part with the imaginary freqs!
	print('You have a total of {} calculation(s) with Imaginary Frequency(ies)!'.format(imag_counter))


def xawker():
	"""
	Here the script combines two other programs, namely xvibs and awk.
	In the first step it changes the current directory to the imag directory.
	Then it begins to process the files, with xvibs creating *.xyz files containing xyz coordinates
	from whitch, with awk, it takes out the first four collumns and creating a new *.xyz- file, which will be processed by
	the imag_xyz_gen function.
	"""

	os.chdir('imag')
	
	#print('Generating xyz file(s)')
	for f in os.listdir():
		try:

			f_n, f_ext=f.split('.')

			if f_n in imag_dict:
				for idc in imag_dict:
					idc=imag_dict[f_n]
					im=1

				print('Generating xyz file from {} file'.format(f))
				while im<=int(idc):
					
					os.system('xvibs '+ f +' '+str(im))
					im+=1
		except ValueError:
			pass


	print('Generating xyz- file(s)')
	for f in os.listdir():
		
		if 'xyz' in f:
			
			os.system("awk '{print $1, $2, $3, $4}' "+ f +" "+"> "+f+"-")

	print('Generating ginp file(s)')

	for f in os.listdir():
		fi=f.split('.')
		
		if fi[-1]=='xyz-':
			with open(f, 'r+') as rf:
				text=rf.readlines()

				h1=int(text[0]) #first line in the xyz- file -> gives the total number of atoms 
				h2=text[1].split(' ') #second line in the xyz- file, is split into a list
				x=h2[-1].split('.') #the freq number is take out of the second line
				i=x[0] #'i' is asociated with the freq number
				#fs_name=fi[0].split('_') #the files name is split by '_'
									
				n1=0 #line number
				n2=0 #numbering the lines which contain the 'Energy' word

				for line in text:
					n1+=1	
					if 'Energy' in line:
						n2+=1
						if n2==6:
							begin=n1
							end=n1+h1
							
							with open(fi[0]+'_r' + str(i)+ '.ginp', 'w') as wf:
								for l in text[begin:end]:
									wf.write(str(l))						
								#for x in range(3):
								#	wf.write('\n')

if __name__ == '__main__':
	imag_catcher()
	xawker()
