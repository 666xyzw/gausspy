# gausspy

**written by xyz666**

This program can generate gaussian input files from spinput, xyz, and gjf files,
and can analyze the tar/tgz files from the calculations, by searching for error termination, 
imaginary frequencies and samples the optimization energies to a separate file named 'enrgies.csv'.
It does not have fancy graphical user interface so you can run it on a server too ;).

The script uses the Xvibs software written by Bradly A. Smith and modified by Kun Attila-Zsolt.
The src/ folder contains the source files for the Xvibs software.

The program comes with **NO WARRANTY!**

How to use the program? 

Well...:

## On GNU/Linux system(s)

1. Open a terminal (usually Ctrl + Alt + T)

2. Download gausspy either as a zip file and then unpack it, or enter in the terminal the following: git clone git_address (this can be copied from abode the download button ;)

3. Go in to the gausspy folder and make the setup.py executable: chmod +x setup.py

4. Run setup.sh (ex.: ./setup.sh)

	1. this script creates the symbolic links needed for the gausspy tool.
	2. if the setup prints a message like "mkdir: cannot create directory 'bin/': File exists." it means
	that you already have a bin folder and it didn`t overwrite it; 
	3. if the setup prints a message like "ln: failed to create symbolic link '/home/username/bin/xvibs(gausspy)': File
	exists" it means that the files are already present in the bin folder. If you want to update those files first 
	delete them and run the script again.

5. Type in gausspy (it will display some messages...don`t worry about them...)

6. A Menu with 5 choices will appear

	**1. Input file manipualtion**
	
	This gets you to the part where you can generate inputfile from xyz/spinput/gjf files created with Jmol, Spartan, GaussView...etc.
		
	- The first thing you have to give to the program is the path to the directory where the xyz/spinput/gjf files are located; ex.: /path/to/Programing/python/test/	
> The source files extension is handled automatically by gausspy.
		
	- Second request is to enter the functional that will be used in the  calculations, ex.: B3LYP
> In a gaussian input file the first line is the route section where you can specify
the functionals/basis sets, optimization, frequency calculation...and so on...
		
	- Third request is to give the first basis set for the calculation, ex.: 6-31G(d)
> I named it first basis set because the program takes two basis sets.
This will be used in every calculation!

	- [OPTIONAL] Fourth request is to give the second basis set, ex.: SDD
> Now this part is optional as the fifth request! You ONLY have to enter
a second basis set if the molecule contains second row transition metal(s)!

	- Fifth request is to specify the molecules charge and multiplicity, ex.: 0 1

       - Sixth request is to give the new file(s) extension, ex.: com
		
	**2. Data analysis** 
	In this part you have to give the /path/to/the/tgz files; ex.: ~/Programing/python/test/
	
	- When you get promted to enter the route section, charge and spin, extension then basically you must do the same thing as above at the input file generation section :) . These request pop up only when the program has found imaginary frequency(ies) and needs to generate a new set of coordinates.

	 **3. README**
	 Opens the README file and ask the user if it wants to do anything else; if the answer is yes then it goes bakc in to the menu if no then exits the program.
	 
	 **4. LICENSE**
	 Same operations as in the REAMDE file, but here the LICENSE file is displayed.
	 
	 **5. Exit**
	 Terminates the software.
	 
## On Windows 10 system(s) 

The program is not fully compatible with Windows OS. BUT if you have Windows 10 then you should look up this 
  link: [How to install linux bash shell on Windows 10]( https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/) where it is explained how to install Bash under Windows and from there on you can run this script within that linux environment and it will work!
 
## For Developers

For those who want to contribute to this little and humble project :)
    
 first of all: feel free to modify/add to the project :)

 every file that does something (functions, classes) goes into lib/ folder

 file names that contain only functions are written in lowerCamelCase style, and are named after the main function, ex.: xawker.py

 file names that contain classes are written in UpperCamelCase (like the class it self) style, ex.: ImagCatcher.py

 if you write something in another language that is compiled and not interpreted (C, C++, Java...etc.) then the source
 code goes in to the src/ folder. This is because of the GPL-2.0 license.

 the tests/ folder holds some files that can be analyzed and some files to generate input files; both type of files are held in different folders, namely tests/analysis/ and tests/input/.

 the tests/input/ folder also holds 2 sets of files:
> 1. inputs_with_first_row_transitional_metals/ -> stores files that don`t contain second row transition metals
> 2. inputs_with_second_row_transitional_metals/ -> stores files that contain second row transition metals