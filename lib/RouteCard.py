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

	def __init__(self, imag_dict=None, rd={}):

		self.rd = rd #route_card dictionary -> will hold the file name (key) and the routecard (value)
		self.imag_dict = imag_dict



	def route_card(self, file):
		
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
								rl.append(line)

							if "****" in line:
								sn += 1
								
								if sn == 1:
									ln -= 3
									rl.append(r[ln:])

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