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
from subprocess import run

class FileSeparator:
    """
    Makes difference between files endind with error messages and files containing imaginary frequencies
    alias negative vibrations!
    """
    
    def __init__(self, imag_dict):
        """
        Initializes the imag_dict from ImagCatcher and checks if the folder error/ and imag/
        exist. If not then they will be created.
        """
       
        self.imag_dict = imag_dict
    
        if os.path.isdir("imag/") and os.path.isdir("error/"): #checking if these folders are already there if not they will be created
            pass

        else:
            os.system("mkdir imag/")
            os.system("mkdir error/")


    def file_separator(self, file):
        """This function separates the files in the tmp folder into error and imag categories"""

        try:
            
            name, ext = file.split('.') #splitting the file into name and extension

            if "_ERROR" in name and ext == "log":
                run(["mv", file, "error/"]) 


            for key in self.imag_dict.keys():

                if name in key and ext == "log":
                    run(["mv", file, "imag/"])


        except ValueError:
            pass
        
if __name__ == "__main__":
    
    path = input("Enter path: ")
    directory = os.chdir(os.path.expanduser(path))
    
    for file in os.listdir(directory):
        FileSeparator(file)

