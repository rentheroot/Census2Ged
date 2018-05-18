#imports
import csv

from Swedish_func_defs import *


def writeName1881_1885 (c , g):
    idn = 0
    with open(g, 'a') as the_file:
        with open(c) as csvfile:
             reader = csv.DictReader(csvfile)

             
             for row in reader:

             	#number of characters in value in the alphabet
             	alphaNumber = 0
             	row2 = list(row)

             	#check if whole row is empty
             	for i in range(len(row2)):
             		rowName = row2[i]
             		if not row[rowName]:
             			pass
             		else:
             			for char in row[rowName]:
             				if char.isalpha():
             					alphaNumber += 1

             	#if the row contains at least one letter, do the stuff
             	if alphaNumber != 0:

	                #print "0 @I(unique 3 digit number)@ INDI"
	                idn += 1
	                the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')

             #call endfile function
             #EndFile(the_file)
writeName1881_1885("Frans-Oscar-Vilhelm.csv", "test.ged")