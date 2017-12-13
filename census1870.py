#writes: name, sex, year of birth (aprox.) birthplace, cencus year, occupation, race, literacy, and disability
#missing: constitutional related things and month of birth/marriage if within the year. Also if attended school within the year

#imports
import csv

from func_defs import *


def writeName1870 (c , g):
    idn = 0
    with open(g, 'a') as the_file:
        with open(c) as csvfile:
             reader = csv.DictReader(csvfile)

             
             for row in reader:
                #print "0 @I(unique 3 digit number)@ INDI"
                 idn += 1
                 the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')

                 #Call NameWriter Function
                 __Name_Writer_No_Relation__(row, '3-Name', the_file)

                 #Call SexWriter Function
                 __Sex_Writer__(row,'5-Sex',the_file)

                 #Call YBdateWriter function
                 YBdateWriter (row,'4-Age','1870',the_file)

                 #call BPlaceWriter function
                 BPlaceWriter(row,'24-POB',the_file)

                 #call CensusYearWriter function
                 CensusYearWriter(the_file, '1870')

                 #call OccupationWriter function
                 OccupationWriter(row, '7-Occupation', the_file, '1870')

                 #call RaceWriter function
                 RaceWriter(row,'6-Color', the_file, '1870')

                 #call LiteracyWriter1880 function
                 LiteracyWriter1880(row,'16-Read','17-Write', '4-Age', the_file, '1870')

                 #call Disabled Writer 1870 function
                __Disabled_Writer_1870__(row, '18-deaf-and-dumb', the_file)

                #call property writer 1860 function
                __Property_Writer_1860__(row, '7-Real-Estate', '9-Personal-Estate', the_file , '1860')

            #call endfile function
             EndFile(the_file)
                 
