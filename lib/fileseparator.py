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


def fileseparator(file):
    """This function separates the files in the tmp folder into error and imag categories"""

    if os.path.isdir("imag/") and os.path.isdir("error/"): #checking if these folders are already there if not they will be created
        pass

    else:
        os.system("mkdir imag/")
        os.system("mkdir error/")

    try:
        
        name, ext = file.split('.') #splitting the file into name and extension

        if "_ERROR" in name and "_imag" in name:
            #print("Moving {} to error/".format(file))
            os.system("mv " + file + " imag/")

        elif "_imag" in name and ext == "log":
            #print("Moving {} to imag/".format(file))
            os.system("mv " + file + " imag/")

        elif "_ERROR" in name:
            os.system("mv " + file + " error/")            
        else:
            pass

    except ValueError:
        pass
        
if __name__ == "__main__":
    
    path = input("Enter path: ")
    directory = os.chdir(os.path.expanduser(path))
    
    for file in os.listdir(directory):
        FileSeparator(file)

