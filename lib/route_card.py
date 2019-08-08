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

def route_dict():
	
	os.chdir('..')
	
	global rd
	rd={}
	

	for f in os.listdir():
		fe=f.split('.')

		if 'com' in fe:

			with open(f, 'r+') as rfe:

				r=rfe.readlines()	
				"""
				--------------------
				This is good
				don`t fuck up
				--------------------
				"""

				for line in r:
					if '#P' in line:
						rd[fe[0]]=line
		
				


	#print(rd)
	return rd
	

if __name__=="__main__":
	
	direct=os.chdir(os.path.expanduser('~/Programing/python/cosmin/sm3/tmp/imag/'))
	route_dict(direct)
