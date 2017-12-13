#imports
import csv

from func_defs import *


def writeName1860 (c , g):
     idn = 0
     with open(g, 'a') as the_file:
        with open(c) as csvfile:
             reader = csv.DictReader(csvfile)

             
             for row in reader:
                #print "0 @I(unique 3 digit number)@ INDI"
                 idn += 1
                 the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')

                 #Call NameWriter Function
                 __Name_Writer_No_Relation__(row, '3-name', the_file)

                 #Call SexWriter Function
                 SexWriter(row,'5-Sex',the_file)

                 #Call YBdateWriter function
                 YBdateWriter (row,'4-Age','1860',the_file)

                 #call BPlaceWriter function
                 BPlaceWriter(row,'10-POB',the_file)

                 #call CensusYearWriter function
                 CensusYearWriter(the_file, '1860')

                 #call OccupationWriter function
                 OccupationWriter(row, '7-Occupation', the_file, '1860')

                 #call RaceWriter function
                 RaceWriter(row,'6-Color', the_file, '1860')

                 #call LiteracyWriter1860 function
                 __Literacy_Writer_1860__ (row, '13-cannot-R&W', '4-Age', the_file, '1860' )

                 #call Disabled Writer 1870 function
                 __Disabled_Writer_1870__(row, '14-Deaf', the_file)

                 #call property writer 1860 function
                 __Property_Writer_1860__(row, '8-Real-Estate', '9-Personal-Estate', the_file , '1860')

             #call endfile function
             EndFile(the_file)
                 
