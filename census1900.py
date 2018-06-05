#imports
import csv
from func_defs import *

def writeName1900 (c , g, config_dict):
    idn = 0
    
    with open(g, 'a') as the_file:
        with open(c) as csvfile:
             reader = csv.DictReader(csvfile)

             
             for row in reader:
                #print "0 @I(unique 3 digit number)@ INDI"
                 idn += 1
                 the_file.write('0 ' + '@I' + "{0:0=3d}".format(idn) + '@' + ' INDI\n')

                 #Call NameWriter Function
                 NameWriter(row,"3 NAME",'4 Relationship of each person to the head of the family.', the_file,idn)

                 #Call SexWriter Function
                 sex = SexWriter(row,"6 Sex",the_file,idn)

                 #call YMBdateWriter function
                 YMBdateWriter(row,"7 Year","7 Month",the_file,idn)

                 #call BPlaceWriter function
                 BPlaceWriter(row,"13 POB",the_file,idn)

                 #call CensusYearWriter function
                 CensusYearWriter(the_file, '1900')

                 #call ImmigYearWriter function
                 if config_dict["Immigration"] == 1:
                    ImmigYearWriter(row,"16 Year of immigration to the United States.",config_dict["immigTag"],the_file)

                 #call OccupationWriter function
                 if config_dict["Occupation"] == 1:
                    OccupationWriter(row, config_dict["occupTag"], "19 Occupation", the_file, '1900')

                 #call RaceWriter function
                 if config_dict["Race"] == 1:
                    RaceWriter(row,'5 Color or race',config_dict["raceTag"], the_file, '1900')

                 #call NaturalizedWriter function
                 if config_dict["Naturalize"] == 1:
                    NaturalizedWriter(row, the_file,config_dict["natuTag"],'18 Naturalization.', '1900' )

                 #call LiteracyWriter function
                 if config_dict["Literacy"] == 1:
                    LiteracyWriter(row,'22 Can read','23 Can write', config_dict["literTag"], the_file, '1900')

                 #call ChildNoWriter function
                 if config_dict["Children Born"] == 1:
                    ChildNoWriter(row,'11 Mother of how many children.','12 Number living.', config_dict["chilTag"],the_file, '1900')

                 #call SpeakEnglishWriter function
                 if config_dict["Language"] == 1:
                    SpeakEnglishWriter(row,'24 Can speak English', config_dict["langTag"], the_file, '1900')

                 #call PropertyWriter function
                 if config_dict["Property"] == 1:
                    PropertyWriter(row,'25 Owned or rented', '26 Owned free or mortgaged.','27 Farm or home','28 Number of farm schedule.', config_dict["propTag"],the_file, '1900' )

                 #call FamilyWriter1900 function
                 FamilyWriter1900(row, '4 Relationship of each person to the head of the family.','10 Years married.', the_file,idn, '1900',sex)
                   
             #call EndFile function
             EndFile(the_file,g,idn)
        
