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
from ImagCatcher import ImagCatcher

class RouteCard:

	"""
	The RouteCard class extracts the route card of the old input files and passes it
	to ImagInput and by this the user doesn`t have to retype every time the
	route card for every new input file.
	"""

	def __init__(self, imag_dict=None, rd={}):

		self.rd = rd #route_card dictionary -> will hold the file name (key) and the routecard (value)
		self.imag_dict = imag_dict



	def route_card(self, file):
		"""
		Opens the com file and takes out the first line and if the input file contains
		a secondary basis set then it takes out that too, and saves them into a dictionary.
		"""
		
		try:
			fn, fe = file.split('.')

			for imag_name in self.imag_dict:

				if fn in imag_name and fe == "com":

					with open(file, 'r+') as rfe:
						
						ln = 0 #variable for numbering the lines
						sn = 0 #variable that keeps the count of the line with stars
						rl = [] #route list -> will hold everything that is connected to the files` route card
						
						r=rfe.readlines()	
						
						for line in r:
							ln += 1
							
							if "#P " in line:
								rl.append(line) #this is the first line of the file

							if "****" in line: #searches for the "****" line
								sn += 1
								
								if sn == 1: #if that line is found then
									ln -= 3 #from the total line number (which was counted until then) is substracted 3
									rl.append(r[ln:]) #and from that line number everything till EOF is stored in self.rd dictionary

							self.rd[fn]=rl
		
		except ValueError:
			pass

		return self.rd
	

if __name__=="__main__":
	path=input("Path: ")
	os.chdir(os.path.expanduser(path))

	im = ImagCatcher()

	for file in os.listdir():
		im.imag_catcher(file)

	route = RouteCard(im.imag_dict)
	
	
	for file in os.listdir():
		print("Working on: ", file)
		route.route_card(file)


	print(route.rd)

	num=0
	for key in route.rd:
		num +=1
		print(num, key)