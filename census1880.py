#imports
import csv

from func_defs import *


def writeName1910 (c , g):
    idn = 0
    with open(g, 'a') as the_file:
        with open(c) as csvfile:
             reader = csv.DictReader(csvfile)

             
             for row in reader:
                #print "0 @I(unique 3 digit number)@ INDI"
                 idn += 1
                 the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')

                 #Call NameWriter Function
                 NameWriter(row,'3-Name','8-Relationship', the_file)

                 #Call SexWriter Function
                 SexWriter(row,'5-Sex',the_file)

                 #Call YBdateWriter function
                 YBdateWriter (row,'6-Age','1880',the_file)

                 #call BPlaceWriter function
                 BPlaceWriter(row,'24-POB',the_file)

                 #call CensusYearWriter function
                 CensusYearWriter(the_file, '1880')

                 #call OccupationWriter function
                 OccupationWriter(row, '13-Occupation', the_file, '1880')

                 #call RaceWriter function
                 RaceWriter(row,'4-Color', the_file, '1880')

                 #call LiteracyWriter1880 function
                 LiteracyWriter1880(row,'22-Cannot read','23-Cannot write', '6-Age', the_file, '1880')
