#!/usr/bin/python3

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