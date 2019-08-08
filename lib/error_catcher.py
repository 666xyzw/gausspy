import os

def error_catcher():
	"""
	Searches for error terminations in the log files, and sums up the number of theese files.
	"""
	print('Checking for errors!')
	error_counter=0

	for f in os.listdir():
		try:
			f_name, f_ext=f.split('.')

			if f_ext=='log':
				#print('Analysing {} file'.format(f))
				with open(f, 'r+') as rf:
					lines =rf.readlines()
					
					if 'Error termination' in lines[-3]:
						
						error_counter+=1

						os.rename(f_name+'.'+f_ext, f_name+'_ERROR.'+f_ext)
		except ValueError:
			pass
	print('You have {} calculation(s) with ERROR termination!'.format(error_counter))
