#imports
import csv
from func_defs import *


def writeName1860 (c , g, config_dict, source_dict):
     idn = 0
     with open(g, 'a') as the_file:
        with open(c) as csvfile:
             reader = csv.DictReader(csvfile)

             
             for row in reader:
                #print "0 @I(unique 3 digit number)@ INDI"
                 idn += 1
                 the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')

                 #Call NameWriter Function
                 Name_Writer_No_Relation(row, '3-name', the_file,idn)
                 try:
                    SourceWriter1870(row, the_file, source_dict, '1-Dwelling-house', '2-Family','3-name', 'M653')
                 except:
                    pass
                 #Call SexWriter Function
                 SexWriter(row,'5-Sex',the_file,idn)

                 #Call YBdateWriter function
                 YBdateWriter (row,'4-Age','1860',the_file,idn)
                 try:
                    SourceWriter1870(row, the_file, source_dict, '1-Dwelling-house', '2-Family','3-name', 'M653')
                 except:
                    pass
                 #call BPlaceWriter function
                 BPlaceWriter(row,'10-POB',the_file,idn)
                 try:
                    SourceWriter1870(row, the_file, source_dict, '1-Dwelling-house', '2-Family','3-name', 'M653')
                 except:
                    pass
                 #call CensusYearWriter function
                 CensusYearWriter(the_file, '1860')
                 try:
                    SourceWriter1870(row, the_file, source_dict, '1-Dwelling-house', '2-Family','3-name', 'M653')
                 except:
                    pass
                 #call OccupationWriter function
                 if config_dict["Occupation"] == 1:
                    OccupationWriter(row, config_dict["occupTag"], '7-Occupation', the_file, '1860', idn)
                    try:
                        SourceWriter1870(row, the_file, source_dict, '1-Dwelling-house', '2-Family','3-name', 'M653')
                    except:
                        pass
                 #call RaceWriter function
                 if config_dict["Race"] == 1:
                    RaceWriter(row,'6-Color', config_dict["raceTag"], the_file, '1860', idn)
                    try:
                        SourceWriter1870(row, the_file, source_dict, '1-Dwelling-house', '2-Family','3-name', 'M653')
                    except:
                        pass
                 #call LiteracyWriter1860 function
                 if config_dict["Literacy"] == 1:
                    Literacy_Writer_1860 (row, '13-cannot-R&W', '4-Age', config_dict["literTag"], the_file, '1860', idn )
                    try:
                        SourceWriter1870(row, the_file, source_dict, '1-Dwelling-house', '2-Family','3-name', 'M653')
                    except:
                        pass
                 #call Disabled Writer 1870 function
                 if config_dict["Disability"] == 1:
                    Disabled_Writer_1870(row, '14-Deaf', config_dict["disiTag"], the_file, idn)
                    try:
                        SourceWriter1870(row, the_file, source_dict, '1-Dwelling-house', '2-Family','3-name', 'M653')
                    except:
                        pass
                 #call property writer 1860 function
                 if config_dict["Property"] == 1:
                    Property_Writer_1860(row, '8-Real-Estate', '9-Personal-Estate', config_dict["propTag"],the_file , '1860', idn)
                    try:
                        SourceWriter1870(row, the_file, source_dict, '1-Dwelling-house', '2-Family','3-name', 'M653')
                    except:
                        pass
             #write the source
             MainSourceWriter1900(row, the_file, source_dict, '1860') 
             #call endfile function
             EndFile(the_file,g,idn)
                 
