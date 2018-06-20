#imports
import csv

from func_defs import *


def writeName1910 (c , g, config_dict):
    idn = 0
    with open(g, 'a') as the_file:
        with open(c) as csvfile:
            reader = csv.DictReader(csvfile)
             
            for row in reader:
                #print "0 @I(unique 3 digit number)@ INDI"
                idn += 1
                the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')