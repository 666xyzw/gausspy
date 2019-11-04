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



import os, re

class ImagCatcher:

	"""
	The ImagCatcher class searches through the given file for imaginary frequency(ies).
	"""

	def __init__(self):
		"""
		Initializes the imag_dict dictionary and imag_counter variable
		"""
		print("Checking for imaginary frequency(ies)!")
		self.imag_dict = {} #stores the imaginary freqs in file_name:imaginary number format
		self.imag_counter = 0 #counts how manny calculations have imaginary freqs


	def imag_catcher(self, file):
		"""
		Searches for imaginary frequencies in the log files.
		If it finds any, then it takes that number of frequencies and renames the file adding '_imag_number-of-imaginary frequencies'.
		"""

		try:		
			f_name, f_ext=file.split('.')
			
			if f_ext=='log':
				#print('Analysing {} file'.format(f))
				with open(file, 'r+') as rf:
					lines=rf.readlines()
					
					for line in lines: #iterates over the *.log file
						if ' imaginary frequencies (negative Signs)' in line: #if the line contains that text then it`s a match
							
							self.imag_counter+=1
							
							for m in re.finditer('[0-9]{1,3}', line):#with regex searches from 1 to 3  digit numbers in the line found earlier
								
								self.imag_dict[f_name]=m.group(0) #if the number is found then that number is assigned to the files name in a dictionary
								

							print('The {} file contains {} Imaginary Frequency(ies)!'.format(file, self.imag_dict[f_name])) #prints out the number of imaginary frequencies in the file found with regex
														
		except (ValueError, OSError):
			pass

		return self.imag_counter #it is returned because it needs to be evaluated in the main script
		#if it`s 0 then the script skips the part with the imaginary freq(s)!
		return self.imag_dict
		print('You have a total of {} calculation(s) with Imaginary Frequency(ies)!'.format(self.imag_counter))


if __name__ == '__main__':
	
    path=input("Enter path: ")

    os.chdir(os.path.expanduser(path))
    
    im = ImagCatcher()

    for file in os.listdir():
    	im.imag_catcher(file)

    print("imag_dict: ",im.imag_dict)
    print("imag_counter: ", im.imag_counter)
