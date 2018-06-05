#imports
import csv

from func_defs import *


def writeName1850 (c , g, config_dict):
    idn = 0
    with open(g, 'a') as the_file:
        with open(c) as csvfile:
             reader = csv.DictReader(csvfile)

             
             for row in reader:
                #print "0 @I(unique 3 digit number)@ INDI"
                 idn += 1
                 the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')

                 #Call NameWriter Function
                 __Name_Writer_No_Relation__(row, 'Name', the_file,idn)

                 #Call SexWriter Function
                 SexWriter(row,'Sex',the_file)

                 #Call YBdateWriter function
                 YBdateWriter (row,'Age','1850',the_file)

                 #call BPlaceWriter function
                 BPlaceWriter(row,'POB',the_file,idn)

                 #call CensusYearWriter function
                 CensusYearWriter(the_file, '1850')

                 #call OccupationWriter function
                 if config_dict["Occupation"] == 1:
                    OccupationWriter(row, config_dict["occupTag"], 'Occupation', the_file, '1850')

                 #call RaceWriter function
                 if config_dict["Race"] == 1:
                    RaceWriter(row,'Color', config_dict["raceTag"], the_file, '1850')

                 #call LiteracyWriter1860 function
                 if config_dict["Literacy"] == 1:
                    __Literacy_Writer_1860__ (row, 'Read-Write', 'Age', config_dict["literTag"], the_file, '1850' )

                 #call Disabled Writer 1870 function
                 if config_dict["Disability"] == 1:
                    __Disabled_Writer_1870__(row, 'Deaf-Dumb-Blind-Etc', the_file)

                 #call Property writer 1850 function
                 if config_dict["Property"] == 1:
                    __Property_Writer_1850__(row, 'Real-Estate', config_dict["propTag"], the_file , '1850')

             #call endfile function
             EndFile(the_file,g)
                 
