#imports
import csv

from func_defs import *


def writeName1850 (c , g):
    idn = 0
    with open(g, 'a') as the_file:
        with open(c) as csvfile:
             reader = csv.DictReader(csvfile)

             
             for row in reader:
                #print "0 @I(unique 3 digit number)@ INDI"
                 idn += 1
                 the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')

                 #Call NameWriter Function
                 __Name_Writer_No_Relation__(row, 'Name', the_file)

                 #Call SexWriter Function
                 SexWriter(row,'Sex',the_file)

                 #Call YBdateWriter function
                 YBdateWriter (row,'Age','1850',the_file)

                 #call BPlaceWriter function
                 BPlaceWriter(row,'POB',the_file)

                 #call CensusYearWriter function
                 CensusYearWriter(the_file, '1850')

                 #call OccupationWriter function
                 OccupationWriter(row, 'Occupation', the_file, '1850')

                 #call RaceWriter function
                 RaceWriter(row,'Color', the_file, '1850')

                 #call LiteracyWriter1860 function
                 __Literacy_Writer_1860__ (row, 'Read-Write', 'Age', the_file, '1850' )

                 #call Disabled Writer 1870 function
                 __Disabled_Writer_1870__(row, 'Deaf-Dumb-Blind-Etc', the_file)

                 #call Property writer 1850 function
                 __Property_Writer_1850__(row, 'Real-Estate', the_file , '1850')

             #call endfile function
             EndFile(the_file)
                 
