#imports
import csv
from func_defs import *


def writeName1850 (c , g, config_dict, source_dict):
     idn = 0
     with open(g, 'a') as the_file:
        with open(c) as csvfile:
             reader = csv.DictReader(csvfile)

             
             for row in reader:
                #print "0 @I(unique 3 digit number)@ INDI"
                 idn += 1
                 the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')

                 #Call NameWriter Function
                 Name_Writer_No_Relation(row, 'Name', the_file,idn)
                 try:
                    SourceWriter1870(row, the_file, source_dict, 'Dwelling-House', 'Family','Name', 'M432')
                 except:
                    pass

                 #Call SexWriter Function
                 SexWriter(row,'Sex',the_file,idn)

                 #Call YBdateWriter function
                 YBdateWriter (row,'Age','1850',the_file,idn)
                 try:
                    SourceWriter1870(row, the_file, source_dict, 'Dwelling-House', 'Family','Name', 'M432')
                 except:
                    pass
                 #call BPlaceWriter function
                 BPlaceWriter(row,'POB',the_file,idn)
                 try:
                    SourceWriter1870(row, the_file, source_dict, 'Dwelling-House', 'Family','Name', 'M432')
                 except:
                    pass
                 #call CensusYearWriter function
                 CensusYearWriter(the_file, '1850')
                 try:
                    SourceWriter1870(row, the_file, source_dict, 'Dwelling-House', 'Family','Name', 'M432')
                 except:
                    pass
                 #call OccupationWriter function
                 if config_dict["Occupation"] == 1:
                    OccupationWriter(row, config_dict["occupTag"], 'Occupation', the_file, '1850', idn)
                    try:
                        SourceWriter1870(row, the_file, source_dict, 'Dwelling-House', 'Family','Name', 'M432')
                    except:
                        pass
                 #call RaceWriter function
                 if config_dict["Race"] == 1:
                    RaceWriter(row,'Color', config_dict["raceTag"], the_file, '1850', idn)
                    try:
                        SourceWriter1870(row, the_file, source_dict, 'Dwelling-House', 'Family','Name', 'M432')
                    except:
                        pass
                 #call LiteracyWriter1860 function
                 if config_dict["Literacy"] == 1:
                    Literacy_Writer_1860 (row, 'Read-Write', 'Age', config_dict["literTag"], the_file, '1850', idn )
                    try:
                        SourceWriter1870(row, the_file, source_dict, 'Dwelling-House', 'Family','Name', 'M432')
                    except:
                        pass
                 #call Disabled Writer 1870 function
                 if config_dict["Disability"] == 1:
                    Disabled_Writer_1870(row, 'Deaf-Dumb-Blind-Etc.',config_dict["disiTag"], the_file, idn)
                    try:
                        SourceWriter1870(row, the_file, source_dict, 'Dwelling-House', 'Family','Name', 'M432')
                    except:
                        pass
                 #call Property writer 1850 function
                 if config_dict["Property"] == 1:
                    Property_Writer_1850(row, 'Real-Estate', the_file, config_dict["propTag"], '1850', idn)
                    try:
                        SourceWriter1870(row, the_file, source_dict, 'Dwelling-House', 'Family','Name', 'M432')
                    except:
                        pass             
             #write the source
             MainSourceWriter1900(row, the_file, source_dict, '1850') 
             #call endfile function
             EndFile(the_file,g,idn)
                 
